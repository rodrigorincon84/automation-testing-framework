from typing import Generic

from core.interface.select import (
    MultiSelect, SelectHtml,
    SlctAction, MultiSlctAction, SlctHtmlAction,
    SlctQuestion, MultiSlctQuestion, SlctHtmlQuestion,
    SlctShould, MultiSlctShould, SlctHtmlShould
)
from .ui_element import Action
from core.types.generic_types import TSelect


class SelectAction(Action[TSelect], SlctAction, Generic[TSelect]):

    def __init__(self, element: TSelect):
        super().__init__(element)

    def should_(self) -> SlctShould:
        return self._element.should_()

    def question(self) -> SlctQuestion:
        return self._element.question()

    def _select(self, option):
        raise NotImplementedError("_select method should be implemented in specific subclass")

    def select(self, option):
        if self._element.question().is_value_already_selected(option):
            return self
        self.show_options()
        if option is not None:
            self._select(option)
            self._element.should_().have_an_option_selected(option)
        return self

    def show_options(self):
        if not self._element.question().are_options_displayed():
            self.click()
        return self

    def hide_options(self):
        if self._element.question().are_options_displayed():
            self.click()
        return self

    def remove_option(self, option=None):
        raise NotImplementedError

    def get_options(self):
        raise NotImplementedError

    def get_options_as_list(self):
        raise NotImplementedError


class MultiSelectAction(SelectAction[MultiSelect], MultiSlctAction):

    def __init__(self, element: MultiSelect):
        super().__init__(element)

    def should_(self) -> MultiSlctShould:
        return self._element.should_()

    def question(self) -> MultiSlctQuestion:
        return self._element.question()

    def _type(self, option, delay=0.05):
        raise NotImplementedError

    def select(self, option):
        raise NotImplementedError

    def get_values(self):
        raise NotImplementedError

    def remove_option(self, option=None):
        raise NotImplementedError

    def remove_all(self):
        raise NotImplementedError


class SelectHtmlAction(SelectAction[SelectHtml], SlctHtmlAction):

    def __init__(self, element: SelectHtml):
        super().__init__(element)

    def should_(self) -> SlctHtmlShould:
        return self._element.should_()

    def question(self) -> SlctHtmlQuestion:
        return self._element.question()

    def _select(self, option=None):
        raise NotImplementedError

    def hide_options(self):
        raise NotImplementedError

    def get_options(self):
        raise NotImplementedError

    def get_options_as_list(self):
        raise NotImplementedError
