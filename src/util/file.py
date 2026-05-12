import os
import json

JSON_FORMAT = "json"
CSV_FORMAT = "csv"


class FileUtils:

    @staticmethod
    def get_file_path(*args):
        return os.path.join(*args)

    @staticmethod
    def get_file_directory(file_path):
        return os.path.dirname(file_path)

    @staticmethod
    def get_file_format(file):
        format_ = file.split(".")[-1]
        if format_ == JSON_FORMAT:
            return JSON_FORMAT
        if format_ == CSV_FORMAT:
            return CSV_FORMAT

    @staticmethod
    def get_json_data(data):
        if data is None:
            return None
        json_obj = json.load(open(data, 'r'))
        return json_obj

    @staticmethod
    def is_json_file(file):
        return file.endswith(".json")

    @staticmethod
    def is_csv_file(file):
        return file.endswith(".csv")
