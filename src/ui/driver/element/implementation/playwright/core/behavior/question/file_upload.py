from .ui_element import Question
from core.interface.file_upload import FileUpload, FileUpldAction, FileUpldQuestion, FileUpldShould


class FileUploadQuestion(Question[FileUpload], FileUpldQuestion):

    def __init__(self, element: FileUpload):
        super().__init__(element)

    def should_(self) -> FileUpldShould:
        return self._element.should_()

    def action(self) -> FileUpldAction:
        return self._element.action()
