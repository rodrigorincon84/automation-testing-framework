from abc import abstractmethod, ABC
from typing import Optional, Any

from ..interface.error import Error
from ....client.itf_client import IWebDriverClient
from .element_builder import ElementBuilder
from ..interface.element import UIShould, UIAction, UIQuestion, Element


class BaseElement(ElementBuilder, Element, ABC):

    def __init__(self, driver: IWebDriverClient):
        self.__init_mixin__(driver)
        self._associated_errors: dict[str, Error] = {}
        self._should: Optional[UIShould] = None
        self._action: Optional[UIAction] = None
        self._question: Optional[UIQuestion] = None
        self._init_behaviors()

    def get_parameter(self, field_: str):
        attr_name = f"_{field_}"
        if hasattr(self, attr_name):
            return getattr(self, attr_name)
        raise AttributeError(f"{self.__class__.__name__} has no attribute '{attr_name}'")

    def set_parameter(self, field_: str, value: Any):
        attr_name = f"_{field_}"
        if hasattr(self, attr_name):
            setattr(self, attr_name, value)
        else:
            raise AttributeError(f"{self.__class__.__name__} has no attribute '{attr_name}'")

    @abstractmethod
    def _set_underlying_element(self):
        ...

    @abstractmethod
    def _init_behaviors(self):
        ...

    def should_(self) -> UIShould:
        return self._should

    def action(self) -> UIAction:
        return self._action

    def question(self) -> UIQuestion:
        return self._question
