import logging
import os
from pathlib import Path
from typing import Dict, List

from conf.system import System


class DirectoryUtils:

    @staticmethod
    def create_video_directory(video_path=None) -> str:
        path = video_path if video_path is not None else "videos"
        os.makedirs(path, exist_ok=True)
        return path

    @staticmethod
    def create_log_directory():
        os.makedirs(f"{System.PROJECT_PATH}/logs", exist_ok=True)

    @staticmethod
    def contains_video_files(video_path_directory: str) -> bool:
        logging.debug(f"Directory to analyze: {video_path_directory}")
        p = Path(video_path_directory)
        if not p.is_dir():
            logging.warning(f"Invalid video directory: {video_path_directory}")
            return False

        logging.info(f"Looking for .mp4/.webm files in {video_path_directory}")
        exts = ("mp4", "webm")
        for ext in exts:
            for f in p.glob(f"*.{ext}"):
                try:
                    if f.stat().st_size > 0:
                        logging.info(f"Valid video found: {f}")
                        return True
                    else:
                        logging.warning(f"Zero-byte file skipped: {f}")
                except OSError as e:
                    logging.error(f"Cannot access {f}: {e}")
        return False

    @staticmethod
    def list_video_files(directory: str) -> Dict[str, List[str]]:
        p = Path(directory)
        video_dict: Dict[str, List[str]] = {}
        for ext in ("mp4", "webm"):
            matches = p.glob(f"*.{ext}")
            video_dict[ext] = [str(path.resolve()) for path in matches]
        return video_dict
