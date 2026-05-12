import logging
from abc import ABC
from typing import Optional, Dict, List

from src.conf.property import Property
from src.util.directory import DirectoryUtils
from src.util.file import FileUtils
from .itf_client import IWebDriverClient


class WebDriverUtility(ABC):

    def __init__(self, driver: IWebDriverClient):
        self._driver = driver
        self._scenario_name: Optional[str] = None
        self._video_path: Optional[str] = None

    def set_video_directory(self, directory: str):
        self._video_path = FileUtils.get_file_path("videos", directory)
        DirectoryUtils.create_video_directory(self._video_path)
        logging.info(f"Directory created to store video: {self._video_path}")

    def start_recording(self, scenario_name: str):
        if Property.record_video_should_be_disabled():
            logging.info("Video recording is disabled")
            return False
        self._scenario_name = scenario_name
        logging.info(f"Starting video recording for scenario: {self._scenario_name}")
        return True

    def stop_recording(self) -> Optional[Dict[str, List[str]]]:
        if not Property.record_video_should_be_disabled():
            logging.debug(f"Analyzing if {self._video_path} contains videos")
            if DirectoryUtils.contains_video_files(self._video_path):
                return DirectoryUtils.list_video_files(self._video_path)
            else:
                logging.info(f"Video file/s not found for scenario: {self._scenario_name}")
        return None
