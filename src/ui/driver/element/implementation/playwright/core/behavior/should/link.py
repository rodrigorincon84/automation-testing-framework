from .ui_element import Should
from core.interface.link import Link, LnkAction, LnkQuestion, LnkShould


class LinkShould(Should[Link], LnkShould):

    def __init__(self, element: Link):
        super().__init__(element)

    def question(self) -> LnkQuestion:
        return self._element.question()

    def action(self) -> LnkAction:
        return self._element.action()
