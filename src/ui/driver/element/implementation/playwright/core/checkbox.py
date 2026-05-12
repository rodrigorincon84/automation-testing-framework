from .behavior.action.checkbox import CheckboxAction
from .behavior.question.checkbox import CheckboxQuestion
from .behavior.should.checkbox import CheckboxShould
from .element import Element
from core.interface.checkbox import Checkbox as ICheckbox
from ui.driver.client.itf_client import IWebDriverClient


class Checkbox(Element, ICheckbox):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)

    def _init_behaviors(self):
        self._action = CheckboxAction(self)
        self._should = CheckboxShould(self)
        self._question = CheckboxQuestion(self)

    def with_key(self, key) -> ICheckbox:
        return self

    def build(self) -> ICheckbox:
        super().build()
        return self
