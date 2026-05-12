from .behavior.action.image import ImageAction
from .behavior.question.image import ImageQuestion
from .behavior.should.image import ImageShould
from core.interface.image import Image as IImage
from ui.driver.client.itf_client import IWebDriverClient
from .element import Element


class Image(Element, IImage):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)

    def _init_behaviors(self):
        self._should = ImageShould(self)
        self._question = ImageQuestion(self)
        self._action = ImageAction(self)

    def build(self) -> IImage:
        super().build()
        return self
