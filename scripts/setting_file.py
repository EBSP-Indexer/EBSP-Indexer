import os

class SettingFile:
    def __init__(self, file_path):
        self.file = open(file_path, mode="w")

    def write(self, key, value):
        try:
            self.file.write(f"{key}: {value}\n")
        except:
            warnings.warn(f"Could not write '{key}: {value}' to settings file.")

    def close(self):
        self.file.close()