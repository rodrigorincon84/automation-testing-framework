import json
import re
from datetime import datetime

from faker import Faker


class StringUtils:

    @staticmethod
    def sanitize(string):
        return re.sub(r'[^a-zA-Z0-9]', '_', string)

    @staticmethod
    def random_string(length, prefix=None):
        if prefix:
            return Faker().pystr(min_chars=length, max_chars=length, prefix=prefix)
        return Faker().pystr(min_chars=length, max_chars=length)

    @staticmethod
    def now_as_str():
        now = datetime.now()
        str_date = now.strftime("%Y%m%d%H%M%S") + f"{now.microsecond:06d}"
        return str_date

    @staticmethod
    def is_empty(string):
        return len(string) == 0

    @staticmethod
    def is_json(string):
        try:
            json.loads(string)
        except ValueError:
            return False
        return True

    @staticmethod
    def is_subsequence(sub: str, full: str) -> bool:
        """Check if `sub` is a subsequence of `full` (case-insensitive)."""
        it = iter(full.lower())
        return all(char in it for char in sub.lower())

    @staticmethod
    def normalize_regexp_for_bdd_step(regexp):
        return re.sub(r"\\\\", r"\\", regexp)