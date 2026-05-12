from typing import Generic

from .ui_element import Question
from core.interface.error import Warn, ErrAction, WrnAction, WrnQuestion, ErrQuestion, ErrShould, WrnShould
from core.types.generic_types import TError


class ErrorQuestion(Question[TError], ErrQuestion, Generic[TError]):

    def __init__(self, element: TError):
        super().__init__(element)

    def should_(self) -> ErrShould:
        return self._element.should_()

    def action(self) -> ErrAction:
        return self._element.action()


class WarnQuestion(ErrorQuestion[Warn], WrnQuestion):

    def __init__(self, element: Warn):
        super().__init__(element)

    def should_(self) -> WrnShould:
        return self._element.should_()

    def action(self) -> WrnAction:
        return self._element.action()
