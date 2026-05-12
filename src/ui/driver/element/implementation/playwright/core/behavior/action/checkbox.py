from .ui_element import Action
from core.interface.checkbox import Checkbox,  ChckbxAction,  ChckbxQuestion, ChckbxShould


class CheckboxAction(Action[Checkbox], ChckbxAction):

    def __init__(self, element: Checkbox):
        super().__init__(element)

    def should_(self) -> ChckbxShould:
        return self._element.should_()

    def question(self) -> ChckbxQuestion:
        return self._element.question()

    def check(self) -> "ChckbxAction":
        self._encapsulated_element.check()
        return self

    def uncheck(self) -> "ChckbxAction":
        raise NotImplementedError
