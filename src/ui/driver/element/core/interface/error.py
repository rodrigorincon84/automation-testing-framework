from abc import abstractmethod

from .element import Element, UIAction, UIQuestion, UIShould


# ###############################################################################################################
# #########   Error element #####################################################################################
# ###############################################################################################################

class Error(Element):

    # Builders
    # #####################################################################
    @abstractmethod
    def with_error(self, error) -> "Error":
        ...

    @abstractmethod
    def with_error_expression(self, error_expression) -> "Error":
        ...

    @abstractmethod
    def build(self) -> "Error":
        ...

    @abstractmethod
    def should_(self) -> "ErrShould":
        ...

    @abstractmethod
    def question(self) -> "ErrQuestion":
        ...

    @abstractmethod
    def action(self) -> "ErrAction":
        ...


# ###############################################################################################################
# #########   Error action ######################################################################################
# ###############################################################################################################

class ErrAction(UIAction):

    @abstractmethod
    def should_(self) -> "ErrShould":
        ...

    @abstractmethod
    def question_(self) -> "ErrQuestion":
        ...

# ###############################################################################################################
# #########   Error question ####################################################################################
# ###############################################################################################################


class ErrQuestion(UIQuestion):

    @abstractmethod
    def should_(self) -> "ErrShould":
        ...

    @abstractmethod
    def action(self) -> "ErrAction":
        ...

# ###############################################################################################################
# #########   Error should ######################################################################################
# ###############################################################################################################


class ErrShould(UIShould):

    @abstractmethod
    def question_(self) -> "ErrQuestion":
        ...

    @abstractmethod
    def action(self) -> "ErrAction":
        ...

    @abstractmethod
    def error_be_present(self):
        ...

    @abstractmethod
    def error_be_not_present(self):
        ...

# ###############################################################################################################
# #########   Warning element ###################################################################################
# ###############################################################################################################


class Warn(Error):

    @abstractmethod
    def should_(self) -> "WrnShould":
        ...

    @abstractmethod
    def question(self) -> "WrnQuestion":
        ...

    @abstractmethod
    def action(self) -> "WrnAction":
        ...

    @abstractmethod
    def with_error_type(self, error_type) -> "Warn":
        ...

    @abstractmethod
    def build(self) -> "Warn":
        ...


# ###############################################################################################################
# #########   Warning action ####################################################################################
# ###############################################################################################################

class WrnAction(ErrAction):

    @abstractmethod
    def should_(self) -> "WrnShould":
        ...

    @abstractmethod
    def question_(self) -> "WrnQuestion":
        ...

# ###############################################################################################################
# #########   Warning question ##################################################################################
# ###############################################################################################################


class WrnQuestion(ErrQuestion):

    @abstractmethod
    def should_(self) -> "WrnShould":
        ...

    @abstractmethod
    def action(self) -> "WrnAction":
        ...

# ###############################################################################################################
# #########   Warning should ####################################################################################
# ###############################################################################################################


class WrnShould(ErrShould):

    @abstractmethod
    def question_(self) -> "WrnQuestion":
        ...

    @abstractmethod
    def action(self) -> "WrnAction":
        ...
