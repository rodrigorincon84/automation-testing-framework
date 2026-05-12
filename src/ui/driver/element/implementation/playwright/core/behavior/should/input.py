from typing import Generic

from playwright.sync_api import expect

from .ui_element import Should
from core.types.generic_types import TInput
from core.interface.input import (
    CodeEditor, Datepicker, TextArea,
    InptAction, TxtAreaAction, CodeEdtrAction, DatepckrAction,
    InptQuestion, TxtAreaQuestion, CodeEdtrQuestion, DatepckrQuestion,
    DatepckrShould, CodeEdtrShould, InptShould, TxtAreaShould
)


class InputShould(Should[TInput], InptShould, Generic[TInput]):

    def __init__(self, element: TInput):
        super().__init__(element)

    def question(self) -> InptQuestion:
        return self._element.question()

    def action(self) -> InptAction:
        return self._element.action()

    def have_text(self, text=None):
        self.have_value(text)

    def contain_value(self, text):
        raise NotImplementedError
        return self

    def have_error(self):
        self.action().should_().have_css_class('InputField InputFieldError')
        return self

    def be_empty(self):
        expect(self._encapsulated_element).to_have_value('', timeout=self.get_timeout())
        self._after_method()
        return self


# ###############################################################################################################
# ###############################################################################################################

class TextAreaShould(InputShould[TextArea], TxtAreaShould):

    def __init__(self, element: TextArea):
        super().__init__(element)

    def question(self) -> TxtAreaQuestion:
        return self._element.question()

    def action(self) -> TxtAreaAction:
        return self._element.action()


# ###############################################################################################################
# ###############################################################################################################

class CodeEditorShould(InputShould[CodeEditor], CodeEdtrShould):

    def __init__(self, element: CodeEditor):
        super().__init__(element)

    def question(self) -> CodeEdtrQuestion:
        return self._element.question()

    def action(self) -> CodeEdtrAction:
        return self._element.action()

    def have_text(self, text=None):
        raise NotImplementedError
        return self

    def contain_text(self, text, normalize_text=False):
        raise NotImplementedError
        return self

    def be_empty(self):
        raise NotImplementedError
        return self

    def be_not_empty(self):
        raise NotImplementedError
        return self

    def have_error(self):
        raise NotImplementedError
        return self

    def be_on_page(self):
        raise NotImplementedError


# ###############################################################################################################
# ###############################################################################################################

class DatepickerShould(InputShould[Datepicker], DatepckrShould):

    def __init__(self, element: Datepicker):
        super().__init__(element)

    def question(self) -> DatepckrQuestion:
        return self._element.question()

    def action(self) -> DatepckrAction:
        return self._element.action()

    def have_a_configured_date(self):
        raise NotImplementedError
        return self
