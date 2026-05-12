from .behavior.action.input import InputAction, TextAreaAction, CodeEditorAction, DatepickerAction
from .behavior.question.input import InputQuestion, TextAreaQuestion, CodeEditorQuestion, DatepickerQuestion
from .behavior.should.input import InputShould, TextAreaShould, CodeEditorShould, DatepickerShould
from .element import Element
from core.interface.input import (
    Input as IInput, TextArea as ITextArea, CodeEditor as ICodeEditor, Datepicker as IDatepicker
)
from ui.driver.client.itf_client import IWebDriverClient


class InputType:
    INPUT = "input"
    TEXTAREA = "textarea"


class Input(Element, IInput):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)

    def _init_behaviors(self):
        self._should = InputShould(self)
        self._question = InputQuestion(self)
        self._action = InputAction(self)

    def from_label(self, label_locator: str) -> IInput:
        raise NotImplementedError

    def of_type(self, input_type: str) -> IInput:
        return self

    def build(self) -> IInput:
        super().build()
        return self

# **********************************************************************************************************************
# **********************************************************************************************************************


class TextArea(Input, ITextArea):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)
        self.of_type(InputType.TEXTAREA)

    def _init_behaviors(self):
        self._should = TextAreaShould(self)
        self._question = TextAreaQuestion(self)
        self._action = TextAreaAction(self)

    def build(self) -> ITextArea:
        super().build()
        return self

# **********************************************************************************************************************
# **********************************************************************************************************************


class CodeEditor(Input, ICodeEditor):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)

    def _init_behaviors(self):
        self._should = CodeEditorShould(self)
        self._question = CodeEditorQuestion(self)
        self._action = CodeEditorAction(self)

    def associated_label(self, locator, text) -> ICodeEditor:
        return self

    def build(self) -> ICodeEditor:
        super().build()
        return self


# **********************************************************************************************************************
# **********************************************************************************************************************


class Datepicker(Input, IDatepicker):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)

    def _init_behaviors(self):
        self._should = DatepickerShould(self)
        self._question = DatepickerQuestion(self)
        self._action = DatepickerAction(self)

    def build(self) -> IDatepicker:
        super().build()
        return self
