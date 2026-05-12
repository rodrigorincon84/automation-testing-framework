import logging
from pathlib import Path
from typing import Optional
from playwright.sync_api import sync_playwright, BrowserContext, Page, Browser

from src.util.string import StringUtils
from src.ui.driver.client.playwright.api_interceptor import PlaywrightApiInterceptor
from src.ui.driver.client.playwright.web_driver_utility import PlaywrightWebDriverUtility
from src.ui.driver.client.base_client import WebDriverClient
from src.ui.driver.client.itf_web_driver_utility import IWebDriverUtilityStrategy
from src.ui.driver.element.core.interface import (
    Button, Checkbox, CollectionElement, Error, Warn, FileUpload, Image, Info,
    Input, Datepicker, TextArea, CodeEditor, Link, Select, SelectHtml, MultiSelect, Tab, Element
)
from src.ui.driver.client.itf_client import IWebDriverClient
from src.conf.property import Property
from conf.ui.resources import Resources


class PlaywrightChromeWebDriverClient(WebDriverClient, IWebDriverClient):

    def __init__(self, url: str):
        super().__init__(url)
        self._playwright = None
        self._browser: Optional[Browser] = None
        self._context: Optional[BrowserContext] = None
        self._page: Optional[Page] = None
        self._utility: Optional[IWebDriverUtilityStrategy] = None
        self._browser_args: Optional[dict] = None
        self._context_args: Optional[dict] = None

    def init(self):
        logging.debug("[INIT] Configuring browser arguments")
        # Configure Chrome binary
        chrome_path = Resources.get_browser_path()

        # Build args for Chrome
        chrome_args = [
            "--disable-notifications",
            "--disable-extensions",
            "--disable-infobars",
        ]
        if Property.dev_mode_enabled():
            # Local mode: maximize window
            # chrome_args.append("--start-maximized")
            ...
        else:
            # CI mode: headless with fixed size
            chrome_args += [
                "--headless",
                "--no-sandbox",
                "--disable-gpu",
                "--disable-dev-shm-usage",
                "--disable-setuid-sandbox",
            ]
        self._browser_args = {
            "executable_path": chrome_path,
            "args": chrome_args,
            "headless": not Property.dev_mode_enabled(),
        }

        self._context_args = {
            "ignore_https_errors": True,
            # "viewport": None if Property.dev_mode_enabled() else {"width": 1920, "height": 1080},
            "viewport": {"width": 1800, "height": 960},
            "base_url": self._url,
        }
        if not Property.record_video_should_be_disabled():
            self._context_args.update({
                "record_video_dir": "reports/videos",
                "record_video_size": {"width": 1800, "height": 960},
            })

        auth_path = Path("/tmp/auth.json")
        if auth_path.exists():
            logging.debug("File /tmp/auth.json exists, which means, login already performed and state saved")
            self._context_args['storage_state'] = auth_path

        # Initialize utilities early so set_video_directory() can be called before start()
        self._utility = PlaywrightWebDriverUtility(self)

        logging.debug("[INIT] Finish browser arguments configuration")

    def start(self):
        if not self.is_active():
            logging.debug("[START] Web driver is not active")
            Property.show_env_vars()

            # Initialize Playwright
            self._playwright = sync_playwright().start()
            chromium = self._playwright.chromium

            self._browser = chromium.launch(**self._browser_args)

            self._context = self._browser.new_context(**self._context_args)
            self._context.set_default_timeout(5 * 1000)
            self._context.set_default_navigation_timeout(10 * 1000)
            self._context.tracing.start(screenshots=True, snapshots=True, sources=True)
            self._session_started = True

        # Use the first page and navigate to root
        try:
            self._page = self._context.new_page()
        except Exception as ex:
            logging.error(ex)
            self.stop()
            return

        # Initialize API interceptor now that _page is ready
        self._utility._api_interceptor = PlaywrightApiInterceptor(self)

        self.utilities().navigate("/")
        logging.debug("[START] Web driver is active")

    def stop(self):
        if self.is_active():
            trace_file = None
            logging.debug("[STOP] Web driver is active")
            if self._page and not self._page.is_closed():
                # Clean when finish
                trace_file = f"reports/traces/trace_{StringUtils.now_as_str()}.zip"
                logging.info(f"[STOP] Trace file will be saved to {trace_file}")
                self._context.tracing.stop(path=trace_file)
                self._page.evaluate("() => localStorage.clear()")
                self._page.close()
                logging.debug("[STOP] Playwright page closed")
            self._clear_all()
            self._session_started = False
            return trace_file
        else:
            logging.debug("[STOP] Web driver is not active")
            return None

    def _clear_all(self):
        if self._context and not self._context.is_closed():
            # Closing the context, automatically closes the page or pages
            self._context.close()
            logging.debug("[STOP] Playwright context closed")
        if self._browser and self._browser.is_connected():
            self._browser.close()
            logging.debug("[STOP] Playwright browser closed")
        if self._playwright:
            self._playwright.stop()
            self._playwright = None
            logging.debug("[STOP] Playwright client closed")

    # Web elements from strategy: delegate element creation to the strategy
    # #################################################################################
    def Element(self) -> Element:
        return self._elements.Element(self)

    def CollectionElement(self) -> CollectionElement:
        return self._elements.CollectionElement(self)

    def Input(self) -> Input:
        return self._elements.Input(self)

    def TextArea(self) -> TextArea:
        return self._elements.TextArea(self)

    def CodeEditor(self) -> CodeEditor:
        return self._elements.CodeEditor(self)

    def Datepicker(self) -> Datepicker:
        return self._elements.Datepicker(self)

    def Button(self) -> Button:
        return self._elements.Button(self)

    def Tab(self) -> Tab:
        return self._elements.Tab(self)

    def Link(self) -> Link:
        return self._elements.Link(self)

    def Image(self) -> Image:
        return self._elements.Image(self)

    def Select(self) -> Select:
        return self._elements.Select(self)

    def SelectHtml(self) -> SelectHtml:
        return self._elements.SelectHtml(self)

    def MultiSelect(self) -> MultiSelect:
        return self._elements.MultiSelect(self)

    def Info(self) -> Info:
        return self._elements.Info(self)

    def FileUpload(self) -> FileUpload:
        return self._elements.FileUpload(self)

    def Error(self) -> Error:
        return self._elements.Error(self)

    def Warning(self) -> Warn:
        return self._elements.Warning(self)

    def Checkbox(self) -> Checkbox:
        return self._elements.Checkbox(self)
