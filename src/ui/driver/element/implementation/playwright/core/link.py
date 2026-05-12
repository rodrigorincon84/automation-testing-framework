from .behavior.action.link import LinkAction
from .behavior.question.link import LinkQuestion
from .behavior.should.link import LinkShould
from core.interface.link import Link as ILink
from ui.driver.client.itf_client import IWebDriverClient
from .element import Element


class Link(Element, ILink):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)

    def _init_behaviors(self):
        self._should = LinkShould(self)
        self._question = LinkQuestion(self)
        self._action = LinkAction(self)

    def build(self) -> ILink:
        super().build()
        return self
