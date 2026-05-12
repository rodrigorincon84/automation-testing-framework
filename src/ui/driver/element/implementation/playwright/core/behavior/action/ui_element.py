from typing import Generic
from playwright.sync_api import Locator

from core.base.base_behavior import BaseBehavior
from core.interface.error import Error
from core.interface.element import UIAction, UIQuestion, UIShould
from core.types.generic_types import TElement


class Action(Generic[TElement], BaseBehavior, UIAction):

    def __init__(self, element: TElement):
        super().__init__()
        self._element: TElement = element

    def should_(self) -> UIShould:
        return self._element.should_()

    def question(self) -> UIQuestion:
        return self._element.question()

    def post_build(self):
        self._encapsulated_element: Locator = self._element.get_underlying_element()

    def get_parent(self) -> TElement:
        return self._element.action().get_element("..")

    def go_to(self) -> UIAction:
        self._encapsulated_element.scroll_into_view_if_needed()
        return self

    def get_attributes(self):
        raise NotImplementedError

    def verify_tooltip(self):
        raise NotImplementedError

    def get_attribute(self, attribute) -> str:
        return self._encapsulated_element.get_attribute(attribute)

    def get_element_with_text(self, text):
        raise NotImplementedError

    def get_element(self, sub_locator: str, text_value=None) -> TElement:
        sub_element = self._encapsulated_element.locator(sub_locator).first
        return self._element.get_parameter("driver").Element().from_wrapped(sub_element).with_value(text_value).build()

    def get_elements(self, sub_locator):
        sub_elements = self._encapsulated_element.locator(sub_locator).all()
        return self._element.get_parameter("driver").CollectionElement().from_wrapped(sub_elements).build()

    def go_to_center(self):
        raise NotImplementedError

    def click(self):
        self._encapsulated_element.click()
        return self

    def force_click(self):
        raise NotImplementedError

    def focus(self):
        raise NotImplementedError

    def scroll_into_view(self):
        raise NotImplementedError

    def get_text(self):
        return self._encapsulated_element.inner_text()

    def set_value(self, value):
        raise NotImplementedError

    def get_value(self):
        raise NotImplementedError

    def page_down(self):
        raise NotImplementedError

    def add_error(self, error_key, error: Error):
        self._element.get_parameter("associated_errors")[error_key] = error
        return self

    def get_error(self, error_key) -> Error:
        return self._element.get_parameter("associated_errors")[error_key]

    def scroll_to_top(self):
        raise NotImplementedError
