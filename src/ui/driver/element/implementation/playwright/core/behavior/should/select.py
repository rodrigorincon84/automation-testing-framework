from typing import Generic, List

from core.interface.select import (
    MultiSelect, SelectHtml,
    SlctHtmlAction, MultiSlctAction, SlctAction,
    SlctHtmlQuestion, MultiSlctQuestion, SlctQuestion,
    SlctShould, MultiSlctShould, SlctHtmlShould
)
from .ui_element import Should
from core.types.generic_types import TSelect


class SelectShould(Should[TSelect], SlctShould, Generic[TSelect]):

    def __init__(self, element: TSelect):
        super().__init__(element)

    def question(self) -> SlctQuestion:
        return self._element.question()

    def action(self) -> SlctAction:
        return self._element.action()

    def have_selected_option(self, option):
        raise NotImplementedError
        return self

    def be_disabled(self):
        raise NotImplementedError
        return self

    def be_enabled(self):
        raise NotImplementedError
        return self

    def have_this_option(self, option: str):
        raise NotImplementedError
        return self

    def no_have_this_option(self, option: str):
        raise NotImplementedError
        return self

    def have_an_option_selected(self, default_value=None):
        self.action().with_timeout(self.get_timeout()).get_element('span[style="pointer-events: none;"]').should_().with_timeout(self.get_timeout()).have_text(default_value)
        self._after_method()
        return self

    def no_have_an_option_selected(self, default_value=None):
        raise NotImplementedError
        return self

    def no_have_options_to_select(self):
        raise NotImplementedError
        return self

    def have_error(self):
        raise NotImplementedError
        return self


class MultiSelectShould(SelectShould[MultiSelect], MultiSlctShould):

    def __init__(self, element: MultiSelect):
        super().__init__(element)

    def question(self) -> MultiSlctQuestion:
        return self._element.question()

    def action(self) -> MultiSlctAction:
        return self._element.action()

    def have_selected_options(self, options: List[str]):
        raise NotImplementedError
        return self


class SelectHtmlShould(SelectShould[SelectHtml], SlctHtmlShould):

    def __init__(self, element: SelectHtml):
        super().__init__(element)

    def question(self) -> SlctHtmlQuestion:
        return self._element.question()

    def action(self) -> SlctHtmlAction:
        return self._element.action()
