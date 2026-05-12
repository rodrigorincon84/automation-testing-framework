from .ui_element import Question
from core.interface.link import Link, LnkAction, LnkQuestion, LnkShould


class LinkQuestion(Question[Link], LnkQuestion):

    def __init__(self, element: Link):
        super().__init__(element)

    def should_(self) -> LnkShould:
        return self._element.should_()

    def action(self) -> LnkAction:
        return self._element.action()
