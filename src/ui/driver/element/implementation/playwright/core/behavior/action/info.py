from .ui_element import Action
from core.interface.info import Info, InfAction, InfQuestion, InfShould


class InfoAction(Action[Info], InfAction):

    def __init__(self, element: Info):
        super().__init__(element)

    def should_(self) -> InfShould:
        return self._element.should_()

    def question(self) -> InfQuestion:
        return self._element.question()
