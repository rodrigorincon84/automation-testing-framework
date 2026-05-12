from .ui_element import Action
from core.interface.file_upload import FileUpload, FileUpldAction, FileUpldQuestion, FileUpldShould


class FileUploadAction(Action[FileUpload], FileUpldAction):

    def __init__(self, element: FileUpload):
        super().__init__(element)

    def should_(self) -> FileUpldShould:
        return self._element.should_()

    def question(self) -> FileUpldQuestion:
        return self._element.question()

    def upload_file(self, file_path):
        raise NotImplementedError

    def file_is_pending_to_be_uploaded(self):
        raise NotImplementedError
