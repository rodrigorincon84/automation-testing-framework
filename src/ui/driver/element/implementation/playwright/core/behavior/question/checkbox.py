from .ui_element import Question
from core.interface.checkbox import Checkbox, ChckbxAction, ChckbxQuestion, ChckbxShould


class CheckboxQuestion(Question[Checkbox], ChckbxQuestion):

    def __init__(self, element: Checkbox):
        super().__init__(element)

    def should_(self) -> ChckbxShould:
        return self._element.should_()

    def action(self) -> ChckbxAction:
        return self._element.action()

    def is_checked(self) -> bool:
        return self._encapsulated_element.is_checked()
