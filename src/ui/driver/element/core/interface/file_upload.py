from abc import abstractmethod

from .element import Element, UIAction, UIQuestion, UIShould


# ###############################################################################################################
# #########   FileUpload element ################################################################################
# ###############################################################################################################

class FileUpload(Element):

    # Builders
    # #####################################################################
    @abstractmethod
    def build(self) -> "FileUpload":
        ...

    @abstractmethod
    def should_(self) -> "FileUpldShould":
        ...

    @abstractmethod
    def question(self) -> "FileUpldQuestion":
        ...

    @abstractmethod
    def action(self) -> "FileUpldAction":
        ...

# ###############################################################################################################
# #########   FileUpload action #################################################################################
# ###############################################################################################################


class FileUpldAction(UIAction):

    @abstractmethod
    def should_(self) -> "FileUpldShould":
        ...

    @abstractmethod
    def question(self) -> "FileUpldQuestion":
        ...

    @abstractmethod
    def upload_file(self, file_path) -> "FileUpldAction":
        ...

    @abstractmethod
    def file_is_pending_to_be_uploaded(self) -> "FileUpldAction":
        ...

# ###############################################################################################################
# #########   FileUpload question ###############################################################################
# ###############################################################################################################


class FileUpldQuestion(UIQuestion):

    @abstractmethod
    def should_(self) -> "FileUpldShould":
        ...

    @abstractmethod
    def action(self) -> "FileUpldAction":
        ...


# ###############################################################################################################
# #########   FileUpload should #################################################################################
# ###############################################################################################################

class FileUpldShould(UIShould):

    @abstractmethod
    def question(self) -> "FileUpldQuestion":
        ...

    @abstractmethod
    def action(self) -> "FileUpldAction":
        ...
