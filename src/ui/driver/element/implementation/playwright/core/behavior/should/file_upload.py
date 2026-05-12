from .ui_element import Should
from core.interface.file_upload import FileUpload, FileUpldAction, FileUpldQuestion, FileUpldShould


class FileUploadShould(Should[FileUpload], FileUpldShould):

    def __init__(self, element: FileUpload):
        super().__init__(element)

    def question(self) -> FileUpldQuestion:
        return self._element.question()

    def action(self) -> FileUpldAction:
        return self._element.action()

    def have_text_label(self, label):
        raise NotImplementedError
        return self
