from .ui_element import Action
from core.interface.tab import Tab, TbAction, TbQuestion, TbShould


class TabAction(Action[Tab], TbAction):

    def __init__(self, element: Tab):
        super().__init__(element)

    def should_(self) -> TbShould:
        return self._element.should_()

    def question(self) -> TbQuestion:
        return self._element.question()
