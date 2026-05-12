import logging
from typing import List, Tuple, Dict

from playwright.sync_api import Page

from src.util.file import FileUtils
from src.ui.driver.client.base_web_driver_utility import WebDriverUtility
from src.ui.driver.client.itf_api_interceptor import IApiInterceptor
from src.ui.driver.client.itf_client import IWebDriverClient
from src.ui.driver.client.itf_web_driver_utility import IWebDriverUtilityStrategy


class PlaywrightWebDriverUtility(WebDriverUtility, IWebDriverUtilityStrategy):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)
        self._api_interceptor = None

    def api_interceptor(self) -> IApiInterceptor:
        return self._api_interceptor

    def add_local_storage(self, variables: Dict[str, str]):
        page = self.get_underlying_driver()
        for key, value in variables.items():
            page.evaluate(f"""() => {{
                localStorage.setItem("{key}", `{value}`);
            }}""")

    # TODO
    #Add remove local storage function

    def add_cookies(self, cookies: List[Tuple[str, str]]):
        dict_cookies = [{cookie[0]: cookie[1]} for cookie in cookies]
        self.get_underlying_driver().context.add_cookies(dict_cookies)

    def delete_cookie(self, name):
        self.get_underlying_driver().context.clear_cookies(name=name)

    def navigate(self, url: str):
        self.get_underlying_driver().goto(url)

    def url(self) -> str:
        return self.get_underlying_driver().url

    def wait_for_url_to_be(self, expected_url):
        raise NotImplementedError()

    def refresh(self):
        self.get_underlying_driver().reload()

    def wait_for_page_to_load(self, timeout: int = 10):
        self.get_underlying_driver().wait_for_load_state("load", timeout=timeout * 1000)
        self.get_underlying_driver().wait_for_load_state("domcontentloaded", timeout=timeout * 1000)

    def wait_for_ajax_to_complete(self, timeout: int = 10):
        raise NotImplementedError()
        # self._page.wait_for_load_state("networkidle", timeout=self._timeout * 1000)

    def execute_js(self, js: str):
        self._driver._context.pages[0].evaluate(js)

    def save_screenshot(self, screenshot_name):
        self.get_underlying_driver().screenshot(path=screenshot_name)

    def switch_to_tab(self, index: int, new_tab: bool = True):
        if new_tab:
            self.get_underlying_driver().context.wait_for_event("page", timeout=10 * 1000)
        pages = self._driver._context.pages
        if index < 0 or index >= len(pages):
            raise IndexError(f"Page index {index} out of range (0..{len(pages)-1})")

        target_page = pages[index]
        if target_page.is_closed():
            raise RuntimeError(f"Target page {target_page} is closed")
        self._driver._page = target_page

    def close_tab(self, index: int):
        pages = self._driver._context.pages
        if index < 0 or index >= len(pages):
            raise IndexError(f"Page index {index} out of range (0..{len(pages)-1})")
        if len(pages) == 1:
            logging.warning("Cannot close the last remaining tab")
            return
        current_page = pages[index]
        if current_page.video:
            current_page.close()
            logging.debug(f"Page at position {index} was closed. Video saved in {current_page.video.path()}")
        else:
            current_page.close()
            logging.debug(f"Page at position {index} was closed")

    def close_page(self):
        logging.debug("Closing page")
        if not self.get_underlying_driver().is_closed():
            self.get_underlying_driver().close()
            logging.debug("Page closed")
        else:
            logging.debug("Page already closed")

    def set_current_tab_as_active(self):
        self.get_underlying_driver().bring_to_front()

    def get_underlying_driver(self) -> Page:
        return self._driver._page

    def set_video_directory(self, directory: str):
        default_video_dir = "videos"
        self._video_path = FileUtils.get_file_path(default_video_dir, directory)
        self._driver._context_args['record_video_dir'] = self._video_path
