from abc import abstractmethod

from .element import Element, UIAction, UIQuestion, UIShould


class Info(Element):

    # Builders
    # #####################################################################
    @abstractmethod
    def build(self) -> "Info":
        ...

    # #####################################################################
    @abstractmethod
    def should_(self) -> "InfShould":
        ...

    @abstractmethod
    def question(self) -> "InfQuestion":
        ...

    @abstractmethod
    def action(self) -> "InfAction":
        ...

# ###############################################################################################################
# #########   Info action #######################################################################################
# ###############################################################################################################


class InfAction(UIAction):

    @abstractmethod
    def should_(self) -> "InfShould":
        ...

    @abstractmethod
    def question(self) -> "InfQuestion":
        ...

# ###############################################################################################################
# #########   Info question #####################################################################################
# ###############################################################################################################


class InfQuestion(UIQuestion):

    @abstractmethod
    def should_(self) -> "InfShould":
        ...

    @abstractmethod
    def action(self) -> "InfAction":
        ...

# ###############################################################################################################
# #########   Info should #######################################################################################
# ###############################################################################################################


class InfShould(UIShould):

    @abstractmethod
    def question(self) -> "InfQuestion":
        ...

    @abstractmethod
    def action(self) -> "InfAction":
        ...
