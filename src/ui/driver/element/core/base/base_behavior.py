from abc import ABC, abstractmethod
from typing import Optional, Union

from playwright.sync_api import Locator as PlaywrightElement
from selenium.webdriver.remote.webelement import WebElement as SeleniumElement


class BaseBehavior(ABC):

    def __init__(self):
        # This is the underlying element of behavior main element.
        # The only reason to use in this way is to expose Selene/Playwright functionalities.
        # It's populated by post_build method, called at the end of build method of main element
        self._encapsulated_element: Optional[Union[SeleniumElement, PlaywrightElement]] = None
        self._timeout = 5 * 1000

    @abstractmethod
    def post_build(self):
        ...

    def with_timeout(self, second: int):
        self._timeout = second * 1000
        return self

    def get_timeout(self):
        return self._timeout

    def _after_method(self):
        self._timeout = 5 * 1000
