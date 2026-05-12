from .ui_element import Should
from core.interface.tab import Tab, TbAction, TbQuestion, TbShould


class TabShould(Should[Tab], TbShould):

    def __init__(self, element: Tab):
        super().__init__(element)

    def question(self) -> TbQuestion:
        return self._element.question()

    def action(self) -> TbAction:
        return self._element.action()

    def be_a_tab(self):
        raise NotImplementedError
        return self

    def be_active(self):
        raise NotImplementedError
        return self

    def be_no_active(self):
        raise NotImplementedError
        return self
