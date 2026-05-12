from typing import Generic

from .ui_element import Question
from core.interface.select import (
    MultiSelect, SelectHtml,
    SlctAction, MultiSlctAction, SlctHtmlAction,
    SlctQuestion, MultiSlctQuestion, SlctHtmlQuestion,
    SlctShould, MultiSlctShould, SlctHtmlShould
)
from core.types.generic_types import TSelect


class SelectQuestion(Question[TSelect], SlctQuestion, Generic[TSelect]):

    def __init__(self, element: TSelect):
        super().__init__(element)

    def should_(self) -> SlctShould:
        return self._element.should_()

    def action(self) -> SlctAction:
        return self._element.action()

    def is_value_already_selected(self, value) -> bool:
        if value is None:
            return False
        return self._encapsulated_element.text_content() == value

    def are_options_displayed(self) -> bool:
        e = self._element.get_parameter("driver").Element().from_css(".rt-SelectGroup").build()
        return e.question().with_timeout(2).is_displayed()

    def have_an_option_selected(self) -> bool:
        raise NotImplementedError


class MultiSelectQuestion(SelectQuestion[MultiSelect], MultiSlctQuestion):

    def __init__(self, element: MultiSelect):
        super().__init__(element)

    def should_(self) -> MultiSlctShould:
        return self._element.should_()

    def action(self) -> MultiSlctAction:
        return self._element.action()


class SelectHtmlQuestion(SelectQuestion[SelectHtml], SlctHtmlQuestion):

    def __init__(self, element: SelectHtml):
        super().__init__(element)

    def should_(self) -> SlctHtmlShould:
        return self._element.should_()

    def action(self) -> SlctHtmlAction:
        return self._element.action()

    def are_options_displayed(self) -> bool:
        raise NotImplementedError
