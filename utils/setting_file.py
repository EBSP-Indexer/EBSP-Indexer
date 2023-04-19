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


def get_setting_file_bottom_top(start_path: str, setting_name: str, return_dir_path: bool = False):
    """
    Searches for a file named setting_name recursivly by iterating the path hierarchy
    from bottom to top.

    Returns a SettingFile from the found setting file. If not found returns None.
    If return_dir_path = True, a tuple is returned where the first element is the SettingFile
    and the second is the directory path of the setting_name.

    Parameters
    ----------
    start_path : str
        The starting path from where the search is conducted
    setting_name : str
        The targeted name of the settings file, e.g. "Setting.txt"
    return_dir_path : bool
        Whether the directory path of the found setting file should also be retured.
    """
    if path.isfile(start_path):
        dir_path = path.dirname(start_path)
    else:
        dir_path = start_path
    while dir_path != path.dirname(dir_path):
        if path.isfile(path.join(dir_path, setting_name)):
            if return_dir_path:
                return (SettingFile(path.join(dir_path, setting_name)), dir_path)
            else:
                return SettingFile(path.join(dir_path, setting_name))
        else:
            dir_path = path.dirname(dir_path)
    if return_dir_path:
        print(f"Could not find {setting_name}")
        return (None, None)
    else:
        print(f"Could not find {setting_name}")
        return None