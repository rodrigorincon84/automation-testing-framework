from typing import Optional, List, Union
from playwright.sync_api import Locator as PlaywrightElement
from selenium.webdriver.remote.webelement import WebElement as SeleniumElement

from .behavior.action.ui_collection_element import CollectionElementAction
from .behavior.filter.ui_collection_element import CollectionElementFilter
from .behavior.should.ui_collection_element import CollectionElementShould
from core.interface.collection_element import (
    CollectionElement as ICollectionElement, CollectionElmntShould, CollectionElmntAction,CollectionElmntFilter
)
from ui.driver.client.itf_client import IWebDriverClient


class CollectionElement(ICollectionElement):

    def __init__(self, driver: IWebDriverClient):
        self._locator: Optional[str] = None
        self._driver: IWebDriverClient = driver
        self._underlying_collection: Optional[List[PlaywrightElement]] = None
        self._should: CollectionElmntShould = CollectionElementShould(self)
        self._action: CollectionElmntAction = CollectionElementAction(self)
        self._filter: CollectionElmntFilter = CollectionElementFilter(self)

    def from_css(self, locator: str) -> ICollectionElement:
        self._locator = locator
        return self

    def from_wrapped(self, elements: Union[List[SeleniumElement], List[PlaywrightElement]]):
        self._underlying_collection = elements
        return self

    def build(self) -> ICollectionElement:
        if self._underlying_collection is None:
            self._underlying_collection = self._driver.utilities().get_underlying_driver().locator(self._locator).all()
        return self

    def get_parameter(self, field_: str):
        attr_name = f"_{field_}"
        if hasattr(self, attr_name):
            return getattr(self, attr_name)
        raise AttributeError(f"{self.__class__.__name__} has no attribute '{attr_name}'")

    def get_underlying_collection(self) -> List[PlaywrightElement]:
        return self._underlying_collection

    def should_(self) -> CollectionElmntShould:
        return self._should

    def filter(self) -> CollectionElmntFilter:
        return self._filter

    def action(self) -> CollectionElmntAction:
        return self._action
