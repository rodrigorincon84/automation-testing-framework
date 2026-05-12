from typing import Generic

from .ui_element import Question
from core.interface.input import (
    Datepicker, TextArea, CodeEditor,
    InptAction, TxtAreaAction, CodeEdtrAction, DatepckrAction,
    DatepckrQuestion, InptQuestion, TxtAreaQuestion, CodeEdtrQuestion,
    InptShould, TxtAreaShould, CodeEdtrShould, DatepckrShould
)
from core.types.generic_types import TInput


class InputQuestion(Question[TInput], InptQuestion, Generic[TInput]):

    def __init__(self, element: TInput):
        super().__init__(element)

    def should_(self) -> InptShould:
        return self._element.should_()

    def action(self) -> InptAction:
        return self._element.action()


# ###############################################################################################################
# ###############################################################################################################

class TextAreaQuestion(InputQuestion[TextArea], TxtAreaQuestion):

    def __init__(self, element: TextArea):
        super().__init__(element)

    def should_(self) -> TxtAreaShould:
        return self._element.should_()

    def action(self) -> TxtAreaAction:
        return self._element.action()

# ###############################################################################################################
# ###############################################################################################################


class CodeEditorQuestion(InputQuestion[CodeEditor], CodeEdtrQuestion):

    def __init__(self, element: CodeEditor):
        super().__init__(element)

    def should_(self) -> CodeEdtrShould:
        return self._element.should_()

    def action(self) -> CodeEdtrAction:
        return self._element.action()


# ###############################################################################################################
# ###############################################################################################################


class DatepickerQuestion(InputQuestion[Datepicker], DatepckrQuestion):

    def __init__(self, element: Datepicker):
        super().__init__(element)

    def should_(self) -> DatepckrShould:
        return self._element.should_()

    def action(self) -> DatepckrAction:
        return self._element.action()

    def is_calendar_open(self) -> bool:
        raise NotImplementedError

    def has_a_date_selected(self) -> bool:
        raise NotImplementedError
