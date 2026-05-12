from typing import Optional

from .itf_web_driver_utility import IWebDriverUtilityStrategy
from ..element.strategy.itf_strategy_element import IElementStrategy


class WebDriverClient:

    def __init__(self, url: str):
        self._elements: Optional[IElementStrategy] = None
        self._utility: Optional[IWebDriverUtilityStrategy] = None
        self._session_started = False
        self._url: str = url

    def utilities(self) -> Optional[IWebDriverUtilityStrategy]:
        return self._utility

    def set_elements(self, element_strategy: IElementStrategy):
        self._elements = element_strategy

    def is_active(self) -> bool:
        return self._session_started
