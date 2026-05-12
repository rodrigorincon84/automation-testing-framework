import logging, os, platform

from pyvirtualdisplay import Display
from selenium import webdriver

from src.conf.property import Property
from src.conf.system import System
from src.conf.system import OS
from src.conf.ui.driver import Path


class Resources:

    @staticmethod
    def get_chrome_driver_log():
        return f"{System.PROJECT_PATH}/reports/logs/chromedriver.log"

    @staticmethod
    def get_chrome_driver_path():
        match Property.get_system_os():
            case OS.MACOS:
                return Path.CHROMEDRIVER_MAC_PATH
            case OS.LINUX | OS.ALPINE:
                return Path.CHROMEDRIVER_LINUX_PATH
            case _:
                return Path.CHROMEDRIVER_MAC_PATH

    @staticmethod
    def get_browser_path():
        match Property.get_system_os():
            case OS.MACOS:
                return Path.CHROME_BROWSER_MAC_PATH
            case OS.LINUX | OS.ALPINE:
                return Path.CHROME_BROWSER_LINUX_PATH
            case _:
                return Path.CHROME_BROWSER_MAC_PATH

    @staticmethod
    def get_ffmepg_config():
        match Property.get_system_os():
            case OS.LINUX | OS.ALPINE:
                display =  os.environ.get('XVFB_DISPLAY', ':99')
                logging.info(f"FFmpeg will capture from display {display} (hardcoded for CI)")
                return [
                    "ffmpeg",
                    "-y",  # Overwrite output files without asking
                    "-f", "x11grab",  # Input format for X11 screen capture
                    "-s", "1920x1080",  # Video size
                    "-i", display,
                    "-r", "10",  # Frame rate
                    "-c:v", "libx264",  # Video codec
                    "-preset", "ultrafast",  # Encoding speed/quality trade-off
                    "-crf", "35"  # Quality (lower = better, 0-51)
                ]
        return None

    @staticmethod
    def get_chrome_options():
        options = webdriver.ChromeOptions()
        options.binary_location = Resources.get_browser_path()
        options.add_argument("--remote-debugging-pipe")
        worker_id = os.environ.get('PYTEST_XDIST_WORKER', 'main')
        options.add_argument(f"--user-data-dir=/tmp/chrome_testing_{worker_id}")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--window-position=0,0")
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-infobars')  # Removes banner about "Chrome is being controlled by..."
        options.add_argument('--ignore-certificate-errors')
        if not Property.dev_mode_enabled():
            logging.info("DEV_MODE is not enabled, configuring headless mode")
            # Only use headless when NOT recording video
            # Xvfb needs the browser to render to capture video
            if not Property.record_video():
                logging.info("Video recording disabled, using headless mode")
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
            else:
                logging.info("Video recording enabled, browser will render to Xvfb display")
            options.add_argument('--no-sandbox')
            # options.add_argument('--enable-automation')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-setuid-sandbox')
        return options

    @staticmethod
    def starts_x11_server():
        if Property.record_video_should_be_disabled():
            return None
        else:
            logging.info("Starting virtual server process")
            match platform.system().lower():
                case OS.LINUX | OS.ALPINE:
                    logging.info(f"Starting Xvfb on display :99")
                    process = Display(visible=False, size=(1920, 1080), backend="xvfb").start()
                    actual_display = f":{process.display}"
                    os.environ['XVFB_DISPLAY'] = actual_display
                    logging.info(f"Xvfb running on display {actual_display} (PID: {process.pid})")
                    logging.info(f"Virtual server process started (id={process.pid})")
                    return process

    @staticmethod
    def finish_x11_server(x11_process):
        if not(Property.record_video_should_be_disabled() or x11_process is None):
            logging.info(f"Finishing virtual server process (id={x11_process.pid})")
            match platform.system().lower():
                case OS.LINUX | OS.ALPINE:
                    x11_process.stop()
                    logging.info("Xvfb display stopped > Virtual server process finished")
