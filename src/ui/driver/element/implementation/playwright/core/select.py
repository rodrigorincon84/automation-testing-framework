from .behavior.action.select import SelectAction, MultiSelectAction, SelectHtmlAction
from .behavior.question.select import SelectQuestion, MultiSelectQuestion, SelectHtmlQuestion
from .behavior.should.select import SelectShould, MultiSelectShould, SelectHtmlShould
from core.interface.select import Select as ISelect, MultiSelect as IMultiSelect, SelectHtml as ISelectHtml
from ui.driver.client.itf_client import IWebDriverClient
from .element import Element


class Select(Element, ISelect):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)
        self._mode = "select"
        self._use_separator_value = True

    def set_input_mode(self, separator=True) -> ISelect:
        self._mode = "input"
        self._use_separator_value = separator
        return self

    def _init_behaviors(self):
        self._should = SelectShould(self)
        self._question = SelectQuestion(self)
        self._action = SelectAction(self)

    def build(self) -> ISelect:
        super().build()
        return self

# **********************************************************************************************************************
# **********************************************************************************************************************


class MultiSelect(Select, IMultiSelect):

    def __init__(self, driver: IWebDriverClient,):
        super().__init__(driver)

    def _init_behaviors(self):
        self._should = MultiSelectShould(self)
        self._question = MultiSelectQuestion(self)
        self._action = MultiSelectAction(self)

    def build(self) -> IMultiSelect:
        super().build()
        return self

# **********************************************************************************************************************
# **********************************************************************************************************************


class SelectHtml(Select, ISelectHtml):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)

    def _init_behaviors(self):
        self._should = SelectHtmlShould(self)
        self._question = SelectHtmlQuestion(self)
        self._action = SelectHtmlAction(self)

    def build(self) -> ISelectHtml:
        super().build()
        return self
