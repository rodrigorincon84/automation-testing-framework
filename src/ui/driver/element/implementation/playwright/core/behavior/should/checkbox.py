from playwright.sync_api import expect

from .ui_element import Should
from core.interface.checkbox import Checkbox, ChckbxAction, ChckbxQuestion, ChckbxShould


class CheckboxShould(Should[Checkbox], ChckbxShould):

    def __init__(self, element: Checkbox):
        super().__init__(element)

    def question(self) -> ChckbxQuestion:
        return self._element.question()

    def action(self) -> ChckbxAction:
        return self._element.action()

    def be_checked(self):
        expect(self._encapsulated_element).to_be_checked()
        return self

    def be_no_checked(self):
        expect(self._encapsulated_element).not_to_be_checked()
        return self
