from typing import Generic

from .ui_element import Action
from core.interface.error import Warn, ErrAction, WrnAction, ErrQuestion, WrnQuestion, ErrShould, WrnShould
from core.types.generic_types import TError


class ErrorAction(Action[TError], ErrAction, Generic[TError]):

    def __init__(self, element: TError):
        super().__init__(element)

    def should_(self) -> ErrShould:
        return self._element.should_()

    def question_(self) -> ErrQuestion:
        return self._element.question()


class WarnAction(ErrorAction[Warn], WrnAction):

    def __init__(self, element: Warn):
        super().__init__(element)

    def should_(self) -> WrnShould:
        return self._element.should_()

    def question_(self) -> WrnQuestion:
        return self._element.question()
