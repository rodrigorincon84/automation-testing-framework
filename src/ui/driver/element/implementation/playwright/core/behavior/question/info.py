
from .ui_element import Question
from core.interface.info import Info, InfAction, InfQuestion, InfShould


class InfoQuestion(Question[Info], InfQuestion):

    def __init__(self, element: Info):
        super().__init__(element)

    def should_(self) -> InfShould:
        return self._element.should_()

    def action(self) -> InfAction:
        return self._element.action()
