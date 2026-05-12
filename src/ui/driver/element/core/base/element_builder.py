from abc import ABC, abstractmethod
from typing import Optional, Union
from playwright.sync_api import Locator as PlaywrightElement
from selenium.webdriver.remote.webelement import WebElement as SeleniumElement

from ....client.itf_client import IWebDriverClient


class ElementBuilder(ABC):
    _driver: IWebDriverClient
    _locator: Optional[str]
    _label: Optional[str]
    _value: Optional[str]
    _regexp_value: Optional[str]
    _source: Optional[str]
    _tooltip: Optional[str]
    _built: bool
    _underlying_element: Optional[Union[SeleniumElement, PlaywrightElement]]

    def __init_mixin__(self, driver: IWebDriverClient):
        self._driver = driver
        self._locator = None
        self._label = None
        self._value = None
        self._regexp_value = None
        self._source = None
        self._tooltip = None
        self._built = False
        self._underlying_element = None

    def from_css(self, locator: str):
        self._locator = locator
        return self

    @abstractmethod
    def from_text(self, text: str):
        ...

    def from_wrapped(self, element: Union[SeleniumElement, PlaywrightElement]):
        self._underlying_element = element
        return self

    def with_label(self, label: str):
        self._label = label
        return self

    def with_source(self, source: str):
        self._source = source
        return self

    def with_value(self, value: str):
        self._value = value
        return self

    def with_regexp_value(self, value: str):
        self._regexp_value = value
        return self

    def with_tooltip(self, tooltip: str):
        self._tooltip = tooltip
        return self

    def build(self):
        if not self._built:
            self._set_underlying_element()
            self._built = True
        return self

    def get_underlying_element(self):
        return self._underlying_element

    @abstractmethod
    def _set_underlying_element(self):
        ...
