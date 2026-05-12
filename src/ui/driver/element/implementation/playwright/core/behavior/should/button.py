from .ui_element import Should
from core.interface.button import Button, BtnAction, BtnQuestion, BtnShould


class ButtonShould(Should[Button], BtnShould):

    def __init__(self, element: Button):
        super().__init__(element)

    def question(self) -> BtnQuestion:
        return self._element.question()

    def action(self) -> BtnAction:
        return self._element.action()

    def be_selected(self) -> "ButtonShould":
        raise NotImplementedError
        return self
