from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....driver.client.itf_client import IWebDriverClient
from ..core.interface.button import Button
from ..core.interface.checkbox import Checkbox
from ..core.interface.collection_element import CollectionElement
from ..core.interface.error import Error, Warn
from ..core.interface.file_upload import FileUpload
from ..core.interface.image import Image
from ..core.interface.info import Info
from ..core.interface.input import Input, TextArea, CodeEditor, Datepicker
from ..core.interface.link import Link
from ..core.interface.select import Select, SelectHtml, MultiSelect
from ..core.interface.tab import Tab
from ..core.interface.element import Element


class IElementStrategy(ABC):

    @abstractmethod
    def Element(self, driver: "IWebDriverClient") -> Element:
        ...

    @abstractmethod
    def CollectionElement(self, driver: "IWebDriverClient") -> CollectionElement:
        ...

    @abstractmethod
    def Input(self, driver: "IWebDriverClient") -> Input:
        ...

    @abstractmethod
    def TextArea(self, driver: "IWebDriverClient") -> TextArea:
        ...

    @abstractmethod
    def CodeEditor(self, driver: "IWebDriverClient") -> CodeEditor:
        ...

    @abstractmethod
    def Datepicker(self, driver: "IWebDriverClient") -> Datepicker:
        ...

    @abstractmethod
    def Button(self, driver: "IWebDriverClient") -> Button:
        ...

    @abstractmethod
    def Tab(self, driver: "IWebDriverClient") -> Tab:
        ...

    @abstractmethod
    def Link(self, driver: "IWebDriverClient") -> Link:
        ...

    @abstractmethod
    def Image(self, driver: "IWebDriverClient") -> Image:
        ...

    @abstractmethod
    def Select(self, driver: "IWebDriverClient") -> Select:
        ...

    @abstractmethod
    def SelectHtml(self, driver: "IWebDriverClient") -> SelectHtml:
        ...

    @abstractmethod
    def MultiSelect(self, driver: "IWebDriverClient") -> MultiSelect:
        ...

    @abstractmethod
    def Info(self, driver: "IWebDriverClient") -> Info:
        ...

    @abstractmethod
    def FileUpload(self, driver: "IWebDriverClient") -> FileUpload:
        ...

    @abstractmethod
    def Error(self, driver: "IWebDriverClient") -> Error:
        ...

    @abstractmethod
    def Warning(self, driver: "IWebDriverClient") -> Warn:
        ...

    @abstractmethod
    def Checkbox(self, driver: "IWebDriverClient") -> Checkbox:
        ...
