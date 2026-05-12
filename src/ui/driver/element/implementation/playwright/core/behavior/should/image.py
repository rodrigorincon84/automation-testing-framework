from .ui_element import Should
from core.interface.image import Image, ImgAction, ImgQuestion, ImgShould


class ImageShould(Should[Image], ImgShould):

    def __init__(self, element: Image):
        super().__init__(element)

    def question(self) -> ImgQuestion:
        return self._element.question()

    def action(self) -> ImgAction:
        return self._element.action()
