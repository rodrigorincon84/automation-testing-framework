from typing import Optional

from src.ui.driver.client.itf_client import IWebDriverClient
from src.ui.driver.client.playwright.chrome.web_driver import PlaywrightChromeWebDriverClient
from src.ui.driver.client.selenium.chrome.web_driver import SeleniumChromeWebDriverClient


class UIDriverManager:
    """Fluent builder for configuring and creating UI WebDrivers."""
    def __init__(self):
        self._browser: str | None = None
        self._tool: str | None = None
        self._environment: Optional[str] = None

    def with_chrome(self) -> "UIDriverManager":
        self._browser = "chrome"
        return self

    def with_firefox(self) -> "UIDriverManager":
        self._browser = "firefox"
        return self

    def with_selenium(self) -> "UIDriverManager":
        self._tool = "selenium"
        return self

    def with_playwright(self) -> "UIDriverManager":
        self._tool = "playwright"
        return self

    def for_environment(self, url: str) -> "UIDriverManager":
        self._environment = url
        return self

    def create(self) -> IWebDriverClient:
        if not self._environment:
            raise ValueError("Environment must be set before calling create().")
        if not (self._environment.startswith('http://') or self._environment.startswith('https://')):
            raise ValueError(f"Malformed url [{self._environment}]: Wrong protocol.")
        if not self._tool or not self._browser:
            raise ValueError("Both browser and tool must be set before calling create().")
        if self._browser == "chrome" and self._tool == "selenium":
            return SeleniumChromeWebDriverClient(self._environment)
        if self._browser == "chrome" and self._tool == "playwright":
            return PlaywrightChromeWebDriverClient(self._environment)
        raise NotImplementedError(f"Driver for [{self._browser}, {self._tool}] not implemented.")
