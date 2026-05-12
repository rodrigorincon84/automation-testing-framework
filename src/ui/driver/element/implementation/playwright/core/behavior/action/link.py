from .ui_element import Action
from core.interface.link import Link, LnkAction, LnkQuestion, LnkShould


class LinkAction(Action[Link], LnkAction):

    def __init__(self, element: Link):
        super().__init__(element)

    def should_(self) -> LnkShould:
        return self._element.should_()

    def question(self) -> LnkQuestion:
        return self._element.question()
