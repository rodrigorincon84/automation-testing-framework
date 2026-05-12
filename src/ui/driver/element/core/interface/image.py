from abc import abstractmethod

from .element import Element, UIAction, UIQuestion, UIShould


class Image(Element):

    # Builders
    # #####################################################################
    @abstractmethod
    def build(self) -> "Image":
        ...

    # #####################################################################

    @abstractmethod
    def should_(self) -> "ImgShould":
        ...

    @abstractmethod
    def question(self) -> "ImgQuestion":
        ...

    @abstractmethod
    def action(self) -> "ImgAction":
        ...

# ###############################################################################################################
# #########   Image action ######################################################################################
# ###############################################################################################################


class ImgAction(UIAction):

    @abstractmethod
    def should_(self) -> "ImgShould":
        ...

    @abstractmethod
    def question(self) -> "ImgQuestion":
        ...

# ###############################################################################################################
# #########   Image question ####################################################################################
# ###############################################################################################################


class ImgQuestion(UIQuestion):

    @abstractmethod
    def should_(self) -> "ImgShould":
        ...

    @abstractmethod
    def action(self) -> "ImgAction":
        ...

# ###############################################################################################################
# #########   Image should ######################################################################################
# ###############################################################################################################


class ImgShould(UIShould):

    @abstractmethod
    def question(self) -> "ImgQuestion":
        ...

    @abstractmethod
    def action(self) -> "ImgAction":
        ...
