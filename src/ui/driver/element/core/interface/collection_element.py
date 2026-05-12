from abc import ABC, abstractmethod
from typing import Any, TYPE_CHECKING, List, Union
from playwright.sync_api import Locator as PlaywrightElement
from selenium.webdriver.remote.webelement import WebElement as SeleniumElement

if TYPE_CHECKING:
    from .element import Element


# ###############################################################################################################
# #########   Collection element ################################################################################
# ###############################################################################################################

class CollectionElement(ABC):

    # Builders
    # #####################################################################
    @abstractmethod
    def from_css(self, locator: str) -> "CollectionElement":
        ...

    @abstractmethod
    def from_wrapped(self, elements: Union[List[SeleniumElement], List[PlaywrightElement]]):
        ...

    @abstractmethod
    def build(self) -> "CollectionElement":
        ...
    # #####################################################################

    @abstractmethod
    def get_parameter(self, field_: str):
        ...

    @abstractmethod
    def get_underlying_collection(self) -> Any:
        ...

    @abstractmethod
    def should_(self) -> "CollectionElmntShould":
        ...

    @abstractmethod
    def filter(self) -> "CollectionElmntFilter":
        ...

    @abstractmethod
    def action(self) -> "CollectionElmntAction":
        ...


# ###############################################################################################################
# #########   Collection action #######################################3#########################################
# ###############################################################################################################


class CollectionElmntAction(ABC):

    @abstractmethod
    def should_(self) -> "CollectionElmntShould":
        ...

    @abstractmethod
    def filter(self) -> "CollectionElmntFilter":
        ...

    @abstractmethod
    def get_elements(self) -> list["Element"]:
        ...

# ###############################################################################################################
# #########   Collection filter #################################################################################
# ###############################################################################################################


class CollectionElmntFilter(ABC):

    @abstractmethod
    def should_(self) -> "CollectionElmntShould":
        ...

    @abstractmethod
    def action(self) -> "CollectionElmntAction":
        ...

    @abstractmethod
    def by_text(self, text: str) -> "CollectionElmntFilter":
        ...

    @abstractmethod
    def by_exact_text(self, text: str) -> "CollectionElmntFilter":
        ...

    @abstractmethod
    def by_attribute(self, attribute: tuple[str, str]) -> "CollectionElmntFilter":
        ...

    @abstractmethod
    def nth(self, index: int) -> "Element":
        ...

    @abstractmethod
    def first(self) -> "Element":
        ...

    @abstractmethod
    def second(self) -> "Element":
        ...

    @abstractmethod
    def by_first_match(self, text: str) -> "Element":
        ...

# ###############################################################################################################
# #########   Collection should #################################################################################
# ###############################################################################################################


class CollectionElmntShould(ABC):

    @abstractmethod
    def filter(self) -> "CollectionElmntFilter":
        ...

    @abstractmethod
    def action(self) -> "CollectionElmntAction":
        ...

    @abstractmethod
    def have_size(self, comparator, amount) -> "CollectionElmntShould":
        ...
