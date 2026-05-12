from .ui_element import Question
from core.interface.button import Button, BtnAction, BtnQuestion, BtnShould


class ButtonQuestion(Question[Button], BtnQuestion):

    def __init__(self, element: Button):
        super().__init__(element)

    def should_(self) -> BtnShould:
        return self._element.should_()

    def action(self) -> BtnAction:
        return self._element.action()
