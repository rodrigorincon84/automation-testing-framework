from .behavior.action.tab import TabAction
from .behavior.question.tab import TabQuestion
from .behavior.should.tab import TabShould
from .element import Element
from core.interface.tab import Tab as ITab
from ui.driver.client.itf_client import IWebDriverClient


class Tab(Element, ITab):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)

    def _init_behaviors(self):
        self._should = TabShould(self)
        self._question = TabQuestion(self)
        self._action = TabAction(self)

    def build(self) -> ITab:
        super().build()
        return self
