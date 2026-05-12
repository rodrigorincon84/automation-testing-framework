from typing import Optional
from playwright.sync_api import Locator as PlaywrightElement

from .behavior.action.ui_element import Action
from .behavior.question.ui_element import Question
from .behavior.should.ui_element import Should
from src.ui.driver.element.core.base.base_element import BaseElement
from src.ui.driver.element.core.interface.element import Element as IElement
from src.ui.driver.client.itf_client import IWebDriverClient


class Element(BaseElement):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)
        self._underlying_element: Optional[PlaywrightElement] = None

    def _init_behaviors(self):
        self._should = Should(self)
        self._action = Action(self)
        self._question = Question(self)

    def from_text(self, text: str):
        self._underlying_element = self._driver.utilities().get_underlying_driver().get_by_text(text, exact=True)
        return self

    def build(self) -> IElement:
        super().build()
        self._should.post_build()
        self._question.post_build()
        self._action.post_build()
        return self

    def _set_underlying_element(self):
        # _underlying_element can be populated by from_text or from_wrapped method
        if self._underlying_element is None:
            self._underlying_element = self._driver.utilities().get_underlying_driver().locator(self._locator)

    def get_underlying_element(self) -> PlaywrightElement:
        return self._underlying_element
