from abc import abstractmethod

from .element import Element, UIAction, UIQuestion, UIShould


class Link(Element):

    # Builders
    # #####################################################################
    @abstractmethod
    def build(self) -> "Link":
        ...

    # #####################################################################

    @abstractmethod
    def should_(self) -> "LnkShould":
        ...

    @abstractmethod
    def question(self) -> "LnkQuestion":
        ...

    @abstractmethod
    def action(self) -> "LnkAction":
        ...

# ###############################################################################################################
# #########   Link action #######################################################################################
# ###############################################################################################################


class LnkAction(UIAction):

    @abstractmethod
    def should_(self) -> "LnkShould":
        ...

    @abstractmethod
    def question(self) -> "LnkQuestion":
        ...

# ###############################################################################################################
# #########   Link question #####################################################################################
# ###############################################################################################################


class LnkQuestion(UIQuestion):

    @abstractmethod
    def should_(self) -> "LnkShould":
        ...

    @abstractmethod
    def action(self) -> "LnkAction":
        ...

# ###############################################################################################################
# #########   Link should #######################################################################################
# ###############################################################################################################


class LnkShould(UIShould):

    @abstractmethod
    def question(self) -> "LnkQuestion":
        ...

    @abstractmethod
    def action(self) -> "LnkAction":
        ...