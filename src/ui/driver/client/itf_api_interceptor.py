from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class IApiInterceptor(ABC):

    @abstractmethod
    def wait_for_response_with_url(self, url_pattern: str, timeout: int = 30) -> Optional[Dict[str, Any]]: ...

    @abstractmethod
    def get_captured_response(self, url_pattern: str) -> Optional[Dict[str, Any]]: ...

    @abstractmethod
    def get_all_captured_responses(self) -> Dict[str, Dict[str, Any]]: ...

    @abstractmethod
    def capture_response(self, response: Any) -> Dict[str, Any]: ...

    @abstractmethod
    def clear_captured_responses(self): ...