from typing import Generic

from .ui_element import Should
from core.types.generic_types import TError
from core.interface.error import Warn, WrnAction, ErrAction, WrnQuestion, ErrQuestion, ErrShould, WrnShould


class ErrorShould(Should[TError], ErrShould, Generic[TError]):

    def __init__(self, element: TError):
        super().__init__(element)

    def question_(self) -> ErrQuestion:
        return self._element.question()

    def action(self) -> ErrAction:
        return self._element.action()

    def error_be_present(self):
        self._element.action().go_to()
        self._element.should_().with_timeout(self.get_timeout()).be_visible().have_text(self._element.get_parameter("value"))
        self._element.should_().have_attribute("data-accent-color", "red")

    def error_be_not_present(self):
        raise NotImplementedError


class WarnShould(ErrorShould[Warn], WrnShould):

    def __init__(self, element: Warn):
        super().__init__(element)

    def question_(self) -> WrnQuestion:
        return self._element.question()

    def action(self) -> WrnAction:
        return self._element.action()

    def error_be_present(self):
        self._element.action().go_to()
        self._element.should_().with_timeout(self.get_timeout()).be_visible().have_text(self._element.get_parameter("value"))
        parent = self._element.action().get_parent()
        parent.should_().have_css_property('background-color', 'rgba(255, 222, 0, 0.24)')
        parent.action().get_elements('svg').action().filter().first().should_().be_visible()
        return self
