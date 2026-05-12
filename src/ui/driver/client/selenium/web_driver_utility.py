import logging
import os
import subprocess
import time
from typing import List, Tuple, Dict

from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver

from conf.ui.resources import Resources
from src.util.timeout import ThreadingTimeout as Timeout

from src.conf.property import Property
from src.util.file import FileUtils
from ..base_web_driver_utility import WebDriverUtility
from ..itf_api_interceptor import IApiInterceptor
from ..itf_client import IWebDriverClient
from ..itf_web_driver_utility import IWebDriverUtilityStrategy


class SeleniumWebDriverUtility(WebDriverUtility, IWebDriverUtilityStrategy):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)
        self._video_process = None

    def api_interceptor(self) -> IApiInterceptor:
        raise NotImplementedError("API interception is not supported in Selenium driver")

    def add_local_storage(self, variables: Dict[str, str]):
        for key, value in variables.items():
            self.get_underlying_driver().execute_script(f'window.localStorage.setItem("{key}", `{value}`);')

    def add_cookies(self, cookies: List[Tuple[str, str]]):
        for cookie in cookies:
            self.get_underlying_driver().add_cookie({"name": cookie[0], "value": cookie[1]})

    def delete_cookie(self, name):
        self.get_underlying_driver().delete_cookie(name)

    def navigate(self, url: str):
        self.get_underlying_driver().get(url)

    def url(self) -> str:
        return self.get_underlying_driver().current_url

    def wait_for_url_to_be(self, expected_url):
        current_url = self.url().rstrip("/")
        expected_url = expected_url.rstrip("/")
        with Timeout(60) as timeout_ctx:
            while current_url != expected_url:
                logging.info(f"Expected URL {expected_url}, but got {self.url()}")
                logging.info("Waiting 3 seconds before try again")
                time.sleep(3)
                current_url = self.url().rstrip("/")

        if timeout_ctx.state == timeout_ctx.TIMED_OUT:
            raise TimeoutError(f"Current URL is not the expected")

    def refresh(self):
        self.get_underlying_driver().refresh()

    def wait_for_page_to_load(self, timeout: int = 10):
        import time
        start_time = time.time()
        while time.time() - start_time < timeout:
            state = self.execute_js("return document.readyState")
            if state == "complete":
                return True
            time.sleep(0.5)
        raise TimeoutError("Page load timed")

    def wait_for_ajax_to_complete(self, timeout: int = 10):
        import time
        start_time = time.time()
        while time.time() - start_time < timeout:
            active_ajax_calls = self.execute_js("return window.XMLHttpRequest && XMLHttpRequest.active || 0;")
            if active_ajax_calls == 0:
                return True
            time.sleep(0.5)
        raise TimeoutError("Ajax request load timed")

    def execute_js(self, js: str):
        return self.get_underlying_driver().execute_script(js)

    def save_screenshot(self, screenshot_name):
        self.get_underlying_driver().save_screenshot(screenshot_name)

    def switch_to_tab(self, index: int, new_tab: bool = True):
        """
        Switch to a browser tab by its index.
        Args:
            index: The index of the tab to switch to (0-based)
            new_tab: If True, waits for a new tab to appear at the given index
        Raises:
            TimeoutException: If waiting for a new tab times out
            IndexError: If the tab index is invalid
        """
        driver = self.get_underlying_driver()
        timeout = 10.0  # Default timeout for waiting
        poll_interval = 0.1  # Check every 100ms

        if new_tab:
            # Wait for the new tab to appear at the specified index
            start_time = time.time()
            expected_count = index + 1  # We need at least index+1 tabs

            while len(driver.window_handles) < expected_count:
                elapsed = time.time() - start_time
                if elapsed > timeout:
                    current_count = len(driver.window_handles)
                    raise TimeoutException(
                        f"Timed out after {timeout}s waiting for tab at index {index}. "
                        f"Current tab count: {current_count}, Expected: at least {expected_count}"
                    )
                time.sleep(poll_interval)

        # Get current window handles
        handles = driver.window_handles
        # Validate index
        if index < 0:
            raise IndexError(f"Tab index cannot be negative: {index}")
        if index >= len(handles):
            raise IndexError(
                f"Tab index {index} out of range. Available tabs: {len(handles)} (indices 0-{len(handles)-1})"
            )
        # Switch to the tab
        target_handle = handles[index]
        driver.switch_to.window(target_handle)

    def close_tab(self, index: int):
        raise NotImplementedError

    def close_page(self):
        raise NotImplementedError

    def set_current_tab_as_active(self):
        raise NotImplementedError

    def get_underlying_driver(self) -> WebDriver:
        return self._driver._browser

    def start_recording(self, scenario_name: str):
        if super().start_recording(scenario_name):
            video_name = f"{self._scenario_name}.mp4"
            video_path = os.path.join(self._video_path, video_name)
            logging.info(f"Video path: {video_path}")

            ffmpeg_command = Resources.get_ffmepg_config()
            if ffmpeg_command is None:
                raise NotImplementedError("Record video only supported for linux version")
            ffmpeg_command.append(video_path)
            logging.info(f"Starting ffmpeg with command: {' '.join(ffmpeg_command)}")  # Print the command

            # Create logs directory if it doesn't exist
            logs_dir = FileUtils.get_file_path("videos", "logs")
            if not os.path.exists(logs_dir):
                os.makedirs(logs_dir)

            # Save FFmpeg log in videos/logs directory
            log_file_path = os.path.join(logs_dir, f"{self._scenario_name}_ffmpeg.log")
            log_file = open(log_file_path, "w")
            self._video_process = subprocess.Popen(ffmpeg_command, stdout=log_file, stderr=subprocess.STDOUT)
            logging.info(f"Ffmpeg process started with PID: {self._video_process.pid}, log: {log_file_path}")

    def stop_recording(self):
        if Property.record_video_should_be_disabled():
            return None
        logging.info(f"Finalizing video recording for scenario: {self._scenario_name}")
        if self._video_process:
            try:
                self._video_process.terminate()
                self._video_process.wait(timeout=5)
                logging.info(f"Ffmpeg process (id={self._video_process.pid}) terminated for scenario: {self._scenario_name}")
            except subprocess.TimeoutExpired:
                logging.info(f"Ffmpeg process did not terminate for scenario: {self._scenario_name}")
                self._video_process.kill()
            except Exception as e:
                logging.info(f"Error while terminating Ffmpeg process: {e}")
        return super().stop_recording()
