from .ui_element import Question
from core.interface.tab import Tab, TbAction, TbQuestion, TbShould


class TabQuestion(Question[Tab], TbQuestion):

    def __init__(self, element: Tab):
        super().__init__(element)

    def should_(self) -> TbShould:
        return self._element.should_()

    def action(self) -> TbAction:
        return self._element.action()
