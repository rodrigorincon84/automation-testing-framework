from abc import ABC, abstractmethod
from typing import Tuple, List, Any, Dict
from .itf_api_interceptor import IApiInterceptor


class IWebDriverUtilityStrategy(ABC):

    @abstractmethod
    def add_local_storage(self, variables: Dict[str, str]): ...

    # TODO
    #Add abstract function to remove local storage

    @abstractmethod
    def add_cookies(self, cookies: List[Tuple[str, str]]): ...

    @abstractmethod
    def delete_cookie(self, name): ...

    @abstractmethod
    def navigate(self, url: str): ...

    @abstractmethod
    def url(self) -> str: ...

    @abstractmethod
    def wait_for_url_to_be(self, expected_url): ...

    @abstractmethod
    def refresh(self): ...

    @abstractmethod
    def wait_for_page_to_load(self, timeout: int = 10): ...

    @abstractmethod
    def wait_for_ajax_to_complete(self, timeout: int = 10): ...

    @abstractmethod
    def execute_js(self, js: str): ...

    @abstractmethod
    def save_screenshot(self, screenshot_name): ...

    @abstractmethod
    def switch_to_tab(self, index: int, new_tab: bool = True): ...

    @abstractmethod
    def close_tab(self, index: int): ...

    @abstractmethod
    def close_page(self): ...

    @abstractmethod
    def set_current_tab_as_active(self): ...

    @abstractmethod
    def get_underlying_driver(self) -> Any: ...

    @abstractmethod
    def set_video_directory(self, directory: str): ...

    @abstractmethod
    def start_recording(self, scenario_name: str): ...

    @abstractmethod
    def stop_recording(self): ...

    @abstractmethod
    def api_interceptor(self) -> IApiInterceptor: ...
