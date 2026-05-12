from .itf_strategy_element import IElementStrategy
from ..core.interface import (
    Button, Checkbox, CollectionElement, Error, Warn, FileUpload, Image, Info, Input, TextArea, CodeEditor, Datepicker,
    Link, Select, SelectHtml, MultiSelect, Tab, Element
)
from ..implementation.playwright.core import (
    CoreCheckbox, CoreError, CoreWarn, CoreFileUpload, CoreImage, CoreInfo, CoreCodeEditor, CoreDatepicker, CoreInput,
    CoreTextArea, CoreLink, CoreSelect, CoreSelectHtml, CoreMultiSelect, CoreTab, CoreButton, CoreCollectionElement,
    CoreElement
)
from ...client.itf_client import IWebDriverClient


class PlaywrightElementStrategy(IElementStrategy):

    def Element(self, driver: IWebDriverClient) -> Element:
        return CoreElement(driver)

    def CollectionElement(self, driver: IWebDriverClient) -> CollectionElement:
        return CoreCollectionElement(driver)

    def Input(self, driver: IWebDriverClient) -> Input:
        return CoreInput(driver)

    def TextArea(self, driver: IWebDriverClient) -> TextArea:
        return CoreTextArea(driver)

    def CodeEditor(self, driver: IWebDriverClient) -> CodeEditor:
        return CoreCodeEditor(driver)

    def Datepicker(self, driver: IWebDriverClient) -> Datepicker:
        return CoreDatepicker(driver)

    def Button(self, driver: IWebDriverClient) -> Button:
        return CoreButton(driver)

    def Tab(self, driver: IWebDriverClient) -> Tab:
        return CoreTab(driver)

    def Link(self, driver) -> Link:
        return CoreLink(driver)

    def Image(self, driver: IWebDriverClient) -> Image:
        return CoreImage(driver)

    def Select(self, driver: IWebDriverClient) -> Select:
        return CoreSelect(driver)

    def SelectHtml(self, driver: IWebDriverClient) -> SelectHtml:
        return CoreSelectHtml(driver)

    def MultiSelect(self, driver: IWebDriverClient) -> MultiSelect:
        return CoreMultiSelect(driver)

    def Info(self, driver: IWebDriverClient) -> Info:
        return CoreInfo(driver)

    def FileUpload(self, driver: IWebDriverClient) -> FileUpload:
        return CoreFileUpload(driver)

    def Error(self, driver: IWebDriverClient) -> Error:
        return CoreError(driver)

    def Warning(self, driver: IWebDriverClient) -> Warn:
        return CoreWarn(driver)

    def Checkbox(self, driver: IWebDriverClient) -> Checkbox:
        return CoreCheckbox(driver)
