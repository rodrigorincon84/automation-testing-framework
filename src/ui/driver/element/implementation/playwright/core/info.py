from .behavior.action.info import InfoAction
from .behavior.question.info import InfoQuestion
from .behavior.should.info import InfoShould
from .element import Element
from core.interface.info import Info as IInfo
from ui.driver.client.itf_client import IWebDriverClient


class Info(Element, IInfo):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)

    def _init_behaviors(self):
        self._should = InfoShould(self)
        self._question = InfoQuestion(self)
        self._action = InfoAction(self)

    def build(self) -> IInfo:
        super().build()
        return self
