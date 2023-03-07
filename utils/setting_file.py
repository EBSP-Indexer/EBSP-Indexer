import os.path as path
import warnings
from typing import Optional, Any, Union


class SettingFile:
    def __init__(self, file_path: str, sep: Optional[str] = ":\t"):
        self.path = file_path
        self.dict = {}
        self.sep = sep
        try:
            self.file = open(file_path, "r")
            for line in self.file:

                if line.strip():  # check if line is not empty
                    (key, value) = line.split(self.sep)
                    self.dict[key] = value
            self.file.close()

        except Exception as e:
            # raise e
            # warnings.warn(f"Could not open settings file '{self.path}'.")
            pass

    def write_all(self, dict: dict[str, Any]):
        for key, value in dict:
            self.dict[f"{key}"] = f"{value}\n"

    def write(self, key, value):
        self.dict[f"{key}"] = f"{value}\n"

    def read(self, key):
        return self.dict.get(key).strip()

    def remove(self, key):
        try:
            self.dict.pop(key)
        except:
            warnings.warn(f"Could not remove {key} from settings file.")

    def delete_all_entries(self):
        self.dict = {}

    def save(self):
        try:
            self.file = open(self.path, "w")
            for key, value in self.dict.items():
                self.file.write(key + self.sep + value)
            self.file.close()
        except:
            warnings.warn(f"Could not save to settings file {self.path}.")

    def close(self):
        self.file.close()


def get_setting_file_bottom_top(start_path: str, target_file_name: str, return_dir_path: bool = False):
    if path.isfile(start_path):
        dir_path = path.dirname(start_path)
    else:
        dir_path = start_path
    while dir_path != path.dirname(dir_path):
        print(f"Searched for {path.join(dir_path, target_file_name)}")
        if path.isfile(path.join(dir_path, target_file_name)):
            if return_dir_path:
                return (SettingFile(path.join(dir_path, target_file_name)), dir_path)
            else:
                return SettingFile(path.join(dir_path, target_file_name))
        else:
            dir_path = path.dirname(dir_path)
    if return_dir_path:
        return (None, None)
    else:
        return None