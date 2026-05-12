import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

from src.util.directory import DirectoryUtils

from conf.property import Property
from conf.ui.resources import Resources
from src.ui.driver.client.selenium.web_driver_utility import SeleniumWebDriverUtility
from src.ui.driver.client.base_client import WebDriverClient
from src.ui.driver.element.core.interface import (
    Button, Checkbox, CollectionElement, Error, Warn, FileUpload, Image, Info,
    Input, Datepicker, TextArea, CodeEditor, Link, Select, SelectHtml, MultiSelect, Tab, Element
)
from src.ui.driver.client.itf_client import IWebDriverClient



class SeleniumChromeWebDriverClient(WebDriverClient, IWebDriverClient):

    def __init__(self, url: str):
        super().__init__(url)
        self._x11_process = None
        self._browser: WebDriver = webdriver.Chrome(
            options=Resources.get_chrome_options(),
            service=Service(
                log_output=Resources.get_chrome_driver_log(),
                executable_path=Resources.get_chrome_driver_path(),
                service_args=["--verbose"]
            )
        )
        self._utility = SeleniumWebDriverUtility(self)

    def init(self):
        Property.show_env_vars()
        self._x11_process = Resources.starts_x11_server()
        DirectoryUtils.create_log_directory()
        self._browser.implicitly_wait(5)
        self._browser.set_page_load_timeout(30)
        self._session_started = True

    def start(self):
        if not self.is_active():
            self.init()
            self._session_started = True

        self._browser.get(self._url)
        logging.info(f"session_id={getattr(self._browser.session_id, 'session_id', None)}")
        logging.info(f"capabilities={self._browser.capabilities.get('goog:chromeOptions')}")


    def stop(self):
        if self.is_active():
            self._browser.quit()
            Resources.finish_x11_server(self._x11_process)
            self._session_started = False

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
