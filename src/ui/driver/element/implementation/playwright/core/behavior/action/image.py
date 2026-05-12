from .ui_element import Action
from core.interface.image import Image, ImgAction, ImgQuestion, ImgShould


class ImageAction(Action[Image], ImgAction):

    def __init__(self, element: Image):
        super().__init__(element)

    def should_(self) -> ImgShould:
        return self._element.should_()

    def question(self) -> ImgQuestion:
        return self._element.question()
