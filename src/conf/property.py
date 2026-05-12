import logging
import os
import platform

from src.util.file import FileUtils
from src.conf.system import OS, System


class Property:

    # dev mode should be only used when running from local.
    # When this mode is enabled, means that the browser does not run in headless, and we can see how the test works
    @staticmethod
    def dev_mode_enabled():
        return os.getenv("DEV_MODE", 'False').lower() == "true"

    @staticmethod
    def take_screenshot():
        return os.getenv("TAKE_SCREENSHOT_ON_FAILURE", 'True').lower() == 'true'

    @staticmethod
    def record_video():
        return os.getenv("RECORD_VIDEO", 'True').lower() == 'true'

    @staticmethod
    def get_system_os():
        return platform.system().lower()

    @staticmethod
    def running_on_mac_os():
        return Property.get_system_os() == OS.MACOS

    @staticmethod
    def is_parallel_enabled():
        return Property.get_worker() is not None

    @staticmethod
    def get_worker():
        return os.environ.get('PYTEST_XDIST_WORKER')

    @staticmethod
    def record_video_should_be_disabled():
        if not Property.record_video():
            logging.debug("RECORD_VIDEO is not enabled")
            return True
        if not Property.dev_mode_enabled() and Property.running_on_mac_os():
            logging.debug("DEV_MODE disabled and macOS > Video should not be recorded")
            return True
        logging.info("Record video is enabled")
        return False

    @staticmethod
    def show_env_vars():
        logging.debug("Env vars configured")
        logging.debug(f"DEV MODE: {Property.dev_mode_enabled()}")
        logging.debug(f"SCREENSHOT: {Property.take_screenshot()}")
        logging.debug(f"VIDEO: {Property.record_video()}")

    @staticmethod
    def get_resources_path():
        return FileUtils.get_file_path(System.PROJECT_PATH, "resources")

    @staticmethod
    def get_framework_type():
        return os.getenv("FRAMEWORK_TYPE", "selenium")
