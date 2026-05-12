from typing import Generic
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError, Locator

from core.base.base_behavior import BaseBehavior
from core.interface.element import UIAction, UIQuestion, UIShould
from core.types.generic_types import TElement


class Question(Generic[TElement], BaseBehavior, UIQuestion):

    def __init__(self, element: TElement):
        super().__init__()
        self._element: TElement = element

    def should_(self) -> UIShould:
        return self._element.should_()

    def action(self) -> UIAction:
        return self._element.action()

    def post_build(self):
        self._encapsulated_element: Locator = self._element.get_underlying_element()

    # displayed means that the element is on the page DOM and does not have a hidden property (display: none or
    # visibility: hidden), does not matter if is outside the browser viewport
    def is_displayed(self) -> bool:
        displayed = True
        try:
            # visible implies present + display != none + in viewport
            self._encapsulated_element.wait_for(state="visible", timeout=self._timeout)
        except PlaywrightTimeoutError:
            displayed = False
        self._after_method()
        return displayed

    def is_overlapped(self):
        raise NotImplementedError

    # present means that the element is on the page DOM, does matter its visibility, if is on the DOM then is present
    def is_present(self) -> bool:
        # present = self._encapsulated_element.count() >= 1
        try:
            self._encapsulated_element.wait_for(state="attached", timeout=self.get_timeout())
            present = True
        except PlaywrightTimeoutError:
            present = False
        self._after_method()
        return present

    # visible means that the element is on the page DOM, and is in the browser viewport
    def is_visible(self) -> bool:
        try:
            box = self._encapsulated_element.bounding_box(timeout=self.get_timeout())
        except Exception:
            box = None
        self._after_method()
        return False if not box else True

    def is_selected(self) -> bool:
        raise NotImplementedError

    def is_enabled(self) -> bool:
        return self._encapsulated_element.is_enabled()

    def is_disabled(self) -> bool:
        return self._encapsulated_element.is_disabled()

    def has_css_class(self, class_name) -> bool:
        class_attr = self._encapsulated_element.get_attribute("class", timeout=self.get_timeout())
        result = class_name in class_attr.split() if class_attr else False
        self._after_method()
        return result

    def has_text(self, text) -> bool:
        try:
            element_text = self._encapsulated_element.text_content(timeout=self.get_timeout())
            result = text in element_text if element_text else False
        except PlaywrightTimeoutError:
            result = False
        self._after_method()
        return result
