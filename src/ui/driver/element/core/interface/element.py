from abc import ABC, abstractmethod
from typing import Any, Union
from playwright.sync_api import Locator as PlaywrightElement
from selenium.webdriver.remote.webelement import WebElement as SeleniumElement
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .error import Error
    from .collection_element import CollectionElement


class Element(ABC):

    # Builders
    # # #####################################################################
    @abstractmethod
    def from_css(self, locator: str) -> "Element":
        ...

    @abstractmethod
    def from_text(self, text: str) -> "Element":
        ...

    @abstractmethod
    def from_wrapped(self, element: Union[SeleniumElement, PlaywrightElement]) -> "Element":
        ...

    @abstractmethod
    def with_label(self, label: str) -> "Element":
        ...

    @abstractmethod
    def with_value(self, value: str) -> "Element":
        ...

    @abstractmethod
    def with_regexp_value(self, value: str) -> "Element":
        ...

    @abstractmethod
    def with_source(self, source: str) -> "Element":
        ...

    @abstractmethod
    def with_tooltip(self, tooltip: str) -> "Element":
        ...

    @abstractmethod
    def build(self) -> "Element":
        ...

    @abstractmethod
    def get_parameter(self, field_: str):
        ...

    @abstractmethod
    def set_parameter(self, field_: str, value):
        ...

    @abstractmethod
    def get_underlying_element(self) -> Any:
        ...

    @abstractmethod
    def should_(self) -> "UIShould":
        ...

    @abstractmethod
    def question(self) -> "UIQuestion":
        ...

    @abstractmethod
    def action(self) -> "UIAction":
        ...

# ###############################################################################################################
# #########   Element action ##############@###################################################################
# ###############################################################################################################


class UIAction(ABC):

    @abstractmethod
    def should_(self) -> "UIShould":
        ...

    @abstractmethod
    def question(self) -> "UIQuestion":
        ...

    @abstractmethod
    def get_attributes(self):
        ...

    @abstractmethod
    def with_timeout(self, second: int) -> "UIAction":
        ...

    @abstractmethod
    def verify_tooltip(self):
        ...

    @abstractmethod
    def get_attribute(self, attribute) -> str:
        ...

    @abstractmethod
    def get_element_with_text(self, text):
        ...

    @abstractmethod
    def get_element(self, sub_locator: str, text_value=None) -> "Element":
        ...

    @abstractmethod
    def get_elements(self, sub_locator) -> "CollectionElement":
        ...

    @abstractmethod
    def get_parent(self) -> "Element":
        ...

    @abstractmethod
    def go_to(self) -> "UIAction":
        ...

    @abstractmethod
    def go_to_center(self):
        ...

    @abstractmethod
    def click(self):
        ...

    @abstractmethod
    def force_click(self):
        ...

    @abstractmethod
    def focus(self):
        ...

    @abstractmethod
    def scroll_into_view(self):
        ...

    @abstractmethod
    def get_text(self):
        ...

    @abstractmethod
    def set_value(self, value):
        ...

    @abstractmethod
    def get_value(self):
        ...

    @abstractmethod
    def page_down(self):
        ...

    @abstractmethod
    def add_error(self, error_key, error: "Error"):
        ...

    @abstractmethod
    def get_error(self, error_key) -> "Error":
        ...

    # If a html element has an overflow, this method allows to move the vertical bar to the top of the element
    @abstractmethod
    def scroll_to_top(self):
        ...

# ###############################################################################################################
# #########   Element question ################@###############################################################
# ###############################################################################################################


class UIQuestion(ABC):

    @abstractmethod
    def should_(self) -> "UIShould":
        ...

    @abstractmethod
    def action(self) -> "UIAction":
        ...

    @abstractmethod
    def with_timeout(self, second: int) -> "UIQuestion":
        ...

    @abstractmethod
    def is_overlapped(self):
        ...

    # displayed means that the element is on the page DOM and does not have a hidden property (display: none or
    # visibility: hidden), does not matter if is outside the browser viewport
    @abstractmethod
    def is_displayed(self) -> bool:
        ...

    # present means that the element is on the page DOM, does matter its visibility, if is on the DOM then is present
    @abstractmethod
    def is_present(self) -> bool:
        ...

    # visible means that the element is on the page DOM, and is in the browser viewport
    def is_visible(self) -> bool:
        ...

    @abstractmethod
    def has_css_class(self, class_name) -> bool:
        ...

    @abstractmethod
    def is_selected(self) -> bool:
        ...

    @abstractmethod
    def is_enabled(self) -> bool:
        ...

    @abstractmethod
    def is_disabled(self) -> bool:
        ...

    @abstractmethod
    def has_text(self, text) -> bool:
        ...

# ###############################################################################################################
# #########   Element should #################@################################################################
# ###############################################################################################################


class UIShould(ABC):

    @abstractmethod
    def question(self) -> "UIQuestion":
        ...

    @abstractmethod
    def action(self) -> "UIAction":
        ...

    @abstractmethod
    def be_on_page(self) -> "UIShould":
        ...

    @abstractmethod
    def with_timeout(self, second: int) -> "UIShould":
        ...

    # visible means that the element is on the page DOM, is not hidden, and is on the browser viewport
    # if the element is on the DOM, does not have a hidden property but is outside the browser viewport the is not
    # considered as visible, it must be on the visible area of the browser viewport
    @abstractmethod
    def be_visible(self) -> "UIShould":
        ...

    @abstractmethod
    def be_disabled(self) -> "UIShould":
        ...

    @abstractmethod
    def be_enabled(self) -> "UIShould":
        ...

    @abstractmethod
    def be_displayed(self) -> "UIShould":
        ...

    @abstractmethod
    def be_not_present(self) -> "UIShould":
        ...

    @abstractmethod
    def be_present(self) -> "UIShould":
        ...

    @abstractmethod
    def be_not_visible(self) -> "UIShould":
        ...

    @abstractmethod
    def have_text(self, text=None) -> "UIShould":
        ...
    is_filled = have_text  # Alias

    @abstractmethod
    def have_no_text(self, text=None) -> "UIShould":
        ...

    @abstractmethod
    def contain_text(self, text, normalize_text=False) -> "UIShould":
        ...

    @abstractmethod
    def match_text(self, text_expression=None) -> "UIShould":
        ...

    @abstractmethod
    def have_value(self, text) -> "UIShould":
        ...

    @abstractmethod
    def have_css_class(self, css) -> "UIShould":
        ...

    @abstractmethod
    def no_have_css_class(self, css) -> "UIShould":
        ...

    @abstractmethod
    def contain_css_class(self, css) -> "UIShould":
        ...

    @abstractmethod
    def no_contain_css_class(self, css) -> "UIShould":
        ...

    @abstractmethod
    def contain_css_class_or_fail_on(self, expected_class: str, failure_class: str) -> "UIShould": ...

    @abstractmethod
    def have_text_label(self, text) -> "UIShould":
        ...

    @abstractmethod
    def have_label(self) -> "UIShould":
        ...

    @abstractmethod
    def have_data_tip_attribute_empty(self) -> "UIShould":
        ...

    @abstractmethod
    def have_attribute(self, attribute, value=None) -> "UIShould":
        ...

    @abstractmethod
    def no_have_attribute(self, attribute) -> "UIShould":
        ...

    @abstractmethod
    def be_empty(self) -> "UIShould":
        ...

    @abstractmethod
    def have_css_property(self, attribute, value) -> "UIShould":
        ...

    @abstractmethod
    def have_error(self) -> "UIShould":
        ...
