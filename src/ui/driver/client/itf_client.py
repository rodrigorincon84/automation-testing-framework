from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..element.strategy.itf_strategy_element import IElementStrategy

from .itf_web_driver_utility import IWebDriverUtilityStrategy
from ..element.core.interface import (
    Button, Checkbox, CollectionElement, Error, Warn, FileUpload, Image, Info,
    Input, Datepicker, TextArea, CodeEditor, Link, Select, SelectHtml, MultiSelect, Tab, Element
)


class IWebDriverClient(ABC):

    @abstractmethod
    def init(self):
        ...

    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def stop(self):
        ...

    @abstractmethod
    def is_active(self) -> bool: ...

    @abstractmethod
    def set_elements(self, element_strategy: "IElementStrategy"):
        ...

    @abstractmethod
    def utilities(self) -> IWebDriverUtilityStrategy:
        ...

    @abstractmethod
    def Element(self) -> Element:
        ...

    @abstractmethod
    def CollectionElement(self) -> CollectionElement:
        ...

    @abstractmethod
    def Input(self) -> Input:
        ...

    @abstractmethod
    def TextArea(self) -> TextArea:
        ...

    @abstractmethod
    def CodeEditor(self) -> CodeEditor:
        ...

    @abstractmethod
    def Datepicker(self) -> Datepicker:
        ...

    @abstractmethod
    def Button(self) -> Button:
        ...

    @abstractmethod
    def Tab(self) -> Tab:
        ...

    @abstractmethod
    def Link(self) -> Link:
        ...

    @abstractmethod
    def Image(self) -> Image:
        ...

    @abstractmethod
    def Select(self) -> Select:
        ...

    @abstractmethod
    def SelectHtml(self) -> SelectHtml:
        ...

    @abstractmethod
    def MultiSelect(self) -> MultiSelect:
        ...

    @abstractmethod
    def Info(self) -> Info:
        ...

    @abstractmethod
    def FileUpload(self) -> FileUpload:
        ...

    @abstractmethod
    def Error(self) -> Error:
        ...

    @abstractmethod
    def Warning(self) -> Warn:
        ...

    @abstractmethod
    def Checkbox(self) -> Checkbox:
        ...