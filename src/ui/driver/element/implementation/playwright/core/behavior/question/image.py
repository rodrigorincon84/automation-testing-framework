from .ui_element import Question
from core.interface.image import Image, ImgAction, ImgQuestion, ImgShould


class ImageQuestion(Question[Image], ImgQuestion):

    def __init__(self, element: Image):
        super().__init__(element)

    def should_(self) -> ImgShould:
        return self._element.should_()

    def action(self) -> ImgAction:
        return self._element.action()
