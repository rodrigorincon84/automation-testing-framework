from .behavior.action.button import ButtonAction
from .behavior.question.button import ButtonQuestion
from .behavior.should.button import ButtonShould
from .element import Element
from core.interface.button import Button as IButton


class Button(Element, IButton):

    def build(self) -> IButton:
        super().build()
        return self

    def _init_behaviors(self):
        self._should = ButtonShould(self)
        self._question = ButtonQuestion(self)
        self._action = ButtonAction(self)
