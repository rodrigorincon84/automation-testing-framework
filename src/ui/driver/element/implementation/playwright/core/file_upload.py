from .behavior.action.file_upload import FileUploadAction
from .behavior.question.file_upload import FileUploadQuestion
from .behavior.should.file_upload import FileUploadShould
from core.interface.file_upload import FileUpload as IFileUpload
from ui.driver.client.itf_client import IWebDriverClient
from .element import Element


class FileUpload(Element, IFileUpload):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)

    def _init_behaviors(self):
        self._should = FileUploadShould(self)
        self._question = FileUploadQuestion(self)
        self._action = FileUploadAction(self)

    def build(self) -> IFileUpload:
        super().build()
        return self
