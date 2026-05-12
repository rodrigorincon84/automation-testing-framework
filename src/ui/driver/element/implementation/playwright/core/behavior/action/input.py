from typing import Generic

from .ui_element import Action
from core.interface.input import (
    Datepicker, CodeEditor, TextArea,
    InptAction, DatepckrAction, CodeEdtrAction, TxtAreaAction,
    InptQuestion, TxtAreaQuestion, CodeEdtrQuestion, DatepckrQuestion,
    InptShould, TxtAreaShould, CodeEdtrShould, DatepckrShould
)
from core.types.generic_types import TInput


class InputAction(Action[TInput], InptAction, Generic[TInput]):

    def __init__(self, element: TInput):
        super().__init__(element)

    def should_(self) -> InptShould:
        return self._element.should_()

    def question(self) -> InptQuestion:
        return self._element.question()

    def clear(self):
        self._encapsulated_element.fill("")

    # This method allows to write a text on an input that is accessed through the label
    def type(self, text, clean_field_before_type=True, delay=0):
        if clean_field_before_type:
            self.clear()
        if delay > 0:
            self._encapsulated_element.type(text, delay=delay)
        else:
            self._encapsulated_element.fill(text)
    write = type  # Alias

    def _perform_type(self, text, delay):
        raise NotImplementedError


# ###############################################################################################################
# ###############################################################################################################


class TextAreaAction(InputAction[TextArea], TxtAreaAction):

    def __init__(self, element: TextArea):
        super().__init__(element)

    def should_(self) -> TxtAreaShould:
        return self._element.should_()

    def question(self) -> TxtAreaQuestion:
        return self._element.question()

# ###############################################################################################################
# ###############################################################################################################


class CodeEditorAction(InputAction[CodeEditor], CodeEdtrAction):

    def __init__(self, element: CodeEditor):
        super().__init__(element)

    def should_(self) -> CodeEdtrShould:
        return self._element.should_()

    def question(self) -> CodeEdtrQuestion:
        return self._element.question()

    def clear(self):
        raise NotImplementedError

    def _perform_type(self, text, delay):
        raise NotImplementedError

# ###############################################################################################################
# ###############################################################################################################


class DatepickerAction(InputAction[Datepicker], DatepckrAction):

    def __init__(self, element: Datepicker):
        super().__init__(element)

    def should_(self) -> DatepckrShould:
        return self._element.should_()

    def question(self) -> DatepckrQuestion:
        return self._element.question()

    def set_date(self, date_: str):
        raise NotImplementedError

    def pick_first_selectable_date(self):
        raise NotImplementedError
