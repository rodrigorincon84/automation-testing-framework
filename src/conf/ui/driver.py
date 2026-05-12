from src.conf.system import System


class Path:
    _VERSION = "current_downloaded"

    CHROMEDRIVER_MAC_PATH = f"{System.PROJECT_PATH}/.local/tool/{_VERSION}/mac-arm64/chromedriver"
    CHROME_BROWSER_MAC_PATH = f"{System.PROJECT_PATH}/.local/tool/{_VERSION}/mac-arm64/chrome.app/Contents/MacOS/Google Chrome for Testing"

    CHROMEDRIVER_LINUX_PATH = f"{System.PROJECT_PATH}/.local/tool/{_VERSION}/linux64/chromedriver"
    CHROME_BROWSER_LINUX_PATH = f"{System.PROJECT_PATH}/.local/tool/{_VERSION}/linux64/chrome/chrome"