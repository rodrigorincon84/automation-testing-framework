from abc import abstractmethod

from .element import Element, UIAction, UIQuestion, UIShould


class Tab(Element):

    # Builders
    # #####################################################################
    @abstractmethod
    def build(self) -> "Tab":
        ...

    # #####################################################################

    @abstractmethod
    def should_(self) -> "TbShould":
        ...

    @abstractmethod
    def question(self) -> "TbQuestion":
        ...

    @abstractmethod
    def action(self) -> "TbAction":
        ...

# ###############################################################################################################
# #########   Tab action #################################################################################
# ###############################################################################################################


class TbAction(UIAction):

    @abstractmethod
    def should_(self) -> "TbShould":
        ...

    @abstractmethod
    def question(self) -> "TbQuestion":
        ...

# ###############################################################################################################
# #########   Tab question ###############################################################################
# ###############################################################################################################


class TbQuestion(UIQuestion):

    @abstractmethod
    def should_(self) -> "TbShould":
        ...

    @abstractmethod
    def action(self) -> "TbAction":
        ...

# ###############################################################################################################
# #########   Tab should #################################################################################
# ###############################################################################################################


class TbShould(UIShould):

    @abstractmethod
    def question(self) -> "TbQuestion":
        ...

    @abstractmethod
    def action(self) -> "TbAction":
        ...

    @abstractmethod
    def be_a_tab(self) -> "TbShould":
        ...

    @abstractmethod
    def be_active(self) -> "TbShould":
        ...

    @abstractmethod
    def be_no_active(self) -> "TbShould":
        ...
