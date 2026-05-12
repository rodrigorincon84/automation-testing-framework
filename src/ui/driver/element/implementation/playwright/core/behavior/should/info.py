from .ui_element import Should
from core.interface.info import Info, InfAction, InfQuestion, InfShould


class InfoShould(Should[Info], InfShould):

    def __init__(self, element: Info):
        super().__init__(element)

    def question(self) -> InfQuestion:
        return self._element.question()

    def action(self) -> InfAction:
        return self._element.action()
