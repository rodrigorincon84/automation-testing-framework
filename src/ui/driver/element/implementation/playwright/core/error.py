from .behavior.action.error import ErrorAction, WarnAction
from .behavior.question.error import ErrorQuestion, WarnQuestion
from .behavior.should.error import ErrorShould, WarnShould
from .element import Element
from core.interface.error import Error as IError, Warn as IWarn
from ui.driver.client.itf_client import IWebDriverClient


class Error(Element, IError):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)
        self._error_expression = None

    def _init_behaviors(self):
        self._should = ErrorShould(self)
        self._question = ErrorQuestion(self)
        self._action = ErrorAction(self)

    def with_error(self, error) -> IError:
        self._value = error
        return self

    def with_error_expression(self, error_expression) -> IError:
        self._error_expression = f"^{error_expression}$"
        return self

    def build(self) -> IError:
        super().build()
        return self


class Warn(Error, IWarn):

    def __init__(self, driver: IWebDriverClient):
        super().__init__(driver)

    def _init_behaviors(self):
        self._should = WarnShould(self)
        self._question = WarnQuestion(self)
        self._action = WarnAction(self)

    def with_error_type(self, error_type):
        return self

    def build(self) -> IWarn:
        super().build()
        return self
