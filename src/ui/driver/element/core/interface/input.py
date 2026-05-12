from abc import abstractmethod

from .element import Element, UIAction, UIQuestion, UIShould


# ###############################################################################################################
# #########   Input element #####################################################################################
# ###############################################################################################################

class Input(Element):

    # Builders
    # #####################################################################
    @abstractmethod
    def from_label(self, label_locator: str) -> "Input":
        ...

    @abstractmethod
    def of_type(self, input_type: str) -> "Input":
        ...

    @abstractmethod
    def build(self) -> "Input":
        ...

    @abstractmethod
    def should_(self) -> "InptShould":
        ...

    @abstractmethod
    def question(self) -> "InptQuestion":
        ...

    @abstractmethod
    def action(self) -> "InptAction":
        ...

# ###############################################################################################################
# #########   Input action ######################################################################################
# ###############################################################################################################


class InptAction(UIAction):

    @abstractmethod
    def should_(self) -> "InptShould":
        ...

    @abstractmethod
    def question(self) -> "InptQuestion":
        ...

    @abstractmethod
    def clear(self):
        ...

    @abstractmethod
    def type(self, text, clean_field_before_type=True, delay=0.05):
        ...
    write = type

# ###############################################################################################################
# #########   Input question ####################################################################################
# ###############################################################################################################


class InptQuestion(UIQuestion):

    @abstractmethod
    def should_(self) -> "InptShould":
        ...

    @abstractmethod
    def action(self) -> "InptAction":
        ...

# ###############################################################################################################
# #########   Input should ######################################################################################
# ###############################################################################################################


class InptShould(UIShould):

    @abstractmethod
    def question(self) -> "InptQuestion":
        ...

    @abstractmethod
    def action(self) -> "InptAction":
        ...

    @abstractmethod
    def contain_value(self, text) -> "InptShould":
        ...

# ###############################################################################################################
# ###############################################################################################################


# ###############################################################################################################
# #########   TextArea element ##################################################################################
# ###############################################################################################################

class TextArea(Input):

    @abstractmethod
    def build(self) -> "TextArea":
        ...

    @abstractmethod
    def should_(self) -> "TxtAreaShould":
        ...

    @abstractmethod
    def question(self) -> "TxtAreaQuestion":
        ...

    @abstractmethod
    def action(self) -> "TxtAreaAction":
        ...

# ###############################################################################################################
# #########   Textarea action ###################################################################################
# ###############################################################################################################


class TxtAreaAction(InptAction):

    @abstractmethod
    def should_(self) -> "TxtAreaShould":
        ...

    @abstractmethod
    def question(self) -> "TxtAreaQuestion":
        ...

# ###############################################################################################################
# #########   Textarea question #################################################################################
# ###############################################################################################################


class TxtAreaQuestion(InptQuestion):

    @abstractmethod
    def should_(self) -> "TxtAreaShould":
        ...

    @abstractmethod
    def action(self) -> "TxtAreaAction":
        ...

# ###############################################################################################################
# #########   Textarea should ###################################################################################
# ###############################################################################################################


class TxtAreaShould(InptShould):

    @abstractmethod
    def question(self) -> "TxtAreaQuestion":
        ...

    @abstractmethod
    def action(self) -> "TxtAreaAction":
        ...

# ###############################################################################################################
# ###############################################################################################################

# ###############################################################################################################
# #########   CodeEditor element ################################################################################
# ###############################################################################################################


class CodeEditor(Input):

    @abstractmethod
    def associated_label(self, locator, text) -> "CodeEditor":
        ...

    @abstractmethod
    def build(self) -> "CodeEditor":
        ...

    @abstractmethod
    def should_(self) -> "CodeEdtrShould":
        ...

    @abstractmethod
    def question(self) -> "CodeEdtrQuestion":
        ...

    @abstractmethod
    def action(self) -> "CodeEdtrAction":
        ...

# ###############################################################################################################
# #########   CodeEditor action #################################################################################
# ###############################################################################################################


class CodeEdtrAction(InptAction):

    @abstractmethod
    def should_(self) -> "CodeEdtrShould":
        ...

    @abstractmethod
    def question(self) -> "CodeEdtrQuestion":
        ...

# ###############################################################################################################
# #########   CodeEditor question ###############################################################################
# ###############################################################################################################


class CodeEdtrQuestion(InptQuestion):

    @abstractmethod
    def should_(self) -> "CodeEdtrShould":
        ...

    @abstractmethod
    def action(self) -> "CodeEdtrAction":
        ...

# ###############################################################################################################
# #########   CodeEditor should #################################################################################
# ###############################################################################################################


class CodeEdtrShould(InptShould):

    @abstractmethod
    def question(self) -> "CodeEdtrQuestion":
        ...

    @abstractmethod
    def action(self) -> "CodeEdtrAction":
        ...

    @abstractmethod
    def be_not_empty(self):
        ...

# ###############################################################################################################
# ###############################################################################################################

# ###############################################################################################################
# #########   Datepicker element ################################################################################
# ###############################################################################################################


class Datepicker(Input):

    @abstractmethod
    def build(self) -> "Datepicker":
        ...

    @abstractmethod
    def should_(self) -> "DatepckrShould":
        ...

    @abstractmethod
    def question(self) -> "DatepckrQuestion":
        ...

    @abstractmethod
    def action(self) -> "DatepckrAction":
        ...

# ###############################################################################################################
# #########   Datepicker action #################################################################################
# ###############################################################################################################


class DatepckrAction(InptAction):

    @abstractmethod
    def should_(self) -> "DatepckrShould":
        ...

    @abstractmethod
    def question(self) -> "DatepckrQuestion":
        ...

    @abstractmethod
    def set_date(self, date_: str):
        ...

    @abstractmethod
    def pick_first_selectable_date(self):
        ...

# ###############################################################################################################
# #########   Datepicker question ###############################################################################
# ###############################################################################################################


class DatepckrQuestion(InptQuestion):

    @abstractmethod
    def should_(self) -> "DatepckrShould":
        ...

    @abstractmethod
    def action(self) -> "DatepckrAction":
        ...

    @abstractmethod
    def is_calendar_open(self):
        ...

    @abstractmethod
    def has_a_date_selected(self) -> bool:
        ...

# ###############################################################################################################
# #########   Datepicker should #################################################################################
# ###############################################################################################################


class DatepckrShould(InptShould):

    @abstractmethod
    def question(self) -> "DatepckrQuestion":
        ...

    @abstractmethod
    def action(self) -> "DatepckrAction":
        ...

    @abstractmethod
    def have_a_configured_date(self):
        ...
