from abc import abstractmethod

from .element import Element, UIAction, UIQuestion, UIShould


# ###############################################################################################################
# #########   Checkbox element ##################################################################################
# ###############################################################################################################

class Checkbox(Element):

    # Builders
    # #####################################################################
    @abstractmethod
    def with_key(self, key) -> "Checkbox":
        ...

    @abstractmethod
    def build(self) -> "Checkbox":
        ...

    @abstractmethod
    def should_(self) -> "ChckbxShould":
        ...

    @abstractmethod
    def question(self) -> "ChckbxQuestion":
        ...

    @abstractmethod
    def action(self) -> "ChckbxAction":
        ...

# ###############################################################################################################
# #########   Checkbox action ###################################################################################
# ###############################################################################################################


class ChckbxAction(UIAction):

    @abstractmethod
    def should_(self) -> "ChckbxShould":
        ...

    @abstractmethod
    def question(self) -> "ChckbxQuestion":
        ...

    @abstractmethod
    def check(self) -> "ChckbxAction":
        ...

    @abstractmethod
    def uncheck(self) -> "ChckbxAction":
        ...

# ###############################################################################################################
# #########   Checkbox question #################################################################################
# ###############################################################################################################


class ChckbxQuestion(UIQuestion):

    @abstractmethod
    def should_(self) -> "ChckbxShould":
        ...

    @abstractmethod
    def action(self) -> "ChckbxAction":
        ...

    @abstractmethod
    def is_checked(self) -> bool:
        ...


# ###############################################################################################################
# #########   Checkbox should ###################################################################################
# ###############################################################################################################


class ChckbxShould(UIShould):

    @abstractmethod
    def question(self) -> "ChckbxQuestion":
        ...

    @abstractmethod
    def action(self) -> "ChckbxAction":
        ...

    @abstractmethod
    def be_checked(self) -> "ChckbxShould":
        ...

    @abstractmethod
    def be_no_checked(self) -> "ChckbxShould":
        ...

    @abstractmethod
    def have_text_label(self, text) -> "ChckbxShould":
        ...
