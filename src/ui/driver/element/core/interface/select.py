from abc import abstractmethod
from typing import List

from .collection_element import CollectionElement
from .element import Element, UIAction, UIQuestion, UIShould


class Select(Element):

    # Builders
    # #####################################################################
    @abstractmethod
    def set_input_mode(self, separator=True) -> "Select":
        ...

    @abstractmethod
    def build(self) -> "Select":
        ...

    @abstractmethod
    def should_(self) -> "SlctShould":
        ...

    @abstractmethod
    def question(self) -> "SlctQuestion":
        ...

    @abstractmethod
    def action(self) -> "SlctAction":
        ...

# ###############################################################################################################
# #########   Select action #################################################################################
# ###############################################################################################################


class SlctAction(UIAction):

    @abstractmethod
    def select(self, option) -> "SlctAction":
        ...

    @abstractmethod
    def show_options(self) -> "SlctAction":
        ...

    @abstractmethod
    def hide_options(self) -> "SlctAction":
        ...

    @abstractmethod
    def remove_option(self, option=None) -> "SlctAction":
        ...

    @abstractmethod
    def get_options(self) -> CollectionElement:
        ...

    @abstractmethod
    def get_options_as_list(self) -> List[str]:
        ...

    @abstractmethod
    def should_(self) -> "SlctShould":
        ...

    @abstractmethod
    def question(self) -> "SlctQuestion":
        ...

# ###############################################################################################################
# #########   Select question ###############################################################################
# ###############################################################################################################


class SlctQuestion(UIQuestion):

    @abstractmethod
    def is_value_already_selected(self, value) -> bool:
        ...

    @abstractmethod
    def are_options_displayed(self) -> bool:
        ...

    @abstractmethod
    def have_an_option_selected(self) -> bool:
        ...

    @abstractmethod
    def should_(self) -> "SlctShould":
        ...

    @abstractmethod
    def action(self) -> "SlctAction":
        ...

# ###############################################################################################################
# #########   Select should #################################################################################
# ###############################################################################################################


class SlctShould(UIShould):

    @abstractmethod
    def have_selected_option(self, option) -> "SlctShould":
        ...

    @abstractmethod
    def have_this_option(self, option: str) -> "SlctShould":
        ...

    @abstractmethod
    def no_have_this_option(self, option: str) -> "SlctShould":
        ...

    @abstractmethod
    def have_an_option_selected(self, default_value=None) -> "SlctShould":
        ...

    @abstractmethod
    def no_have_an_option_selected(self, default_value=None) -> "SlctShould":
        ...

    @abstractmethod
    def no_have_options_to_select(self) -> "SlctShould":
        ...

    @abstractmethod
    def question(self) -> "SlctQuestion":
        ...

    @abstractmethod
    def action(self) -> "SlctAction":
        ...

# ###########################################################################################


class MultiSelect(Select):

    # Builders
    # #####################################################################
    @abstractmethod
    def build(self) -> "MultiSelect":
        ...

    @abstractmethod
    def should_(self) -> "MultiSlctShould":
        ...

    @abstractmethod
    def question(self) -> "MultiSlctQuestion":
        ...

    @abstractmethod
    def action(self) -> "MultiSlctAction":
        ...

# ###############################################################################################################
# #########   MultiSelect action #################################################################################
# ###############################################################################################################


class MultiSlctAction(SlctAction):

    @abstractmethod
    def get_values(self) -> CollectionElement:
        ...

    @abstractmethod
    def remove_all(self) -> "MultiSlctAction":
        ...

    @abstractmethod
    def should_(self) -> "MultiSlctShould":
        ...

    @abstractmethod
    def question(self) -> "MultiSlctQuestion":
        ...

# ###############################################################################################################
# #########   MultiSelect question ###############################################################################
# ###############################################################################################################


class MultiSlctQuestion(SlctQuestion):

    @abstractmethod
    def should_(self) -> "MultiSlctShould":
        ...

    @abstractmethod
    def action(self) -> "MultiSlctAction":
        ...

# ###############################################################################################################
# #########   MultiSelect should #################################################################################
# ###############################################################################################################


class MultiSlctShould(SlctShould):

    @abstractmethod
    def have_selected_options(self, options: List[str]):
        ...

    @abstractmethod
    def question(self) -> "MultiSlctQuestion":
        ...

    @abstractmethod
    def action(self) -> "MultiSlctAction":
        ...

# ###########################################################################################


class SelectHtml(Select):

    # Builders
    # #####################################################################
    @abstractmethod
    def build(self) -> "SelectHtml":
        ...

    @abstractmethod
    def should_(self) -> "SlctHtmlShould":
        ...

    @abstractmethod
    def question(self) -> "SlctHtmlQuestion":
        ...

    @abstractmethod
    def action(self) -> "SlctHtmlAction":
        ...

# ###############################################################################################################
# #########   SelectHtml action #################################################################################
# ###############################################################################################################


class SlctHtmlAction(SlctAction):

    @abstractmethod
    def should_(self) -> "SlctHtmlShould":
        ...

    @abstractmethod
    def question(self) -> "SlctHtmlQuestion":
        ...

# ###############################################################################################################
# #########   SelectHtml question ###############################################################################
# ###############################################################################################################


class SlctHtmlQuestion(SlctQuestion):

    @abstractmethod
    def should_(self) -> "SlctHtmlShould":
        ...

    @abstractmethod
    def action(self) -> "SlctHtmlAction":
        ...

# ###############################################################################################################
# #########   SelectHtml should #################################################################################
# ###############################################################################################################


class SlctHtmlShould(SlctShould):
    ...

    @abstractmethod
    def question(self) -> "SlctHtmlQuestion":
        ...

    @abstractmethod
    def action(self) -> "SlctHtmlAction":
        ...
