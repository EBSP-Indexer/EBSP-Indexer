import os
import warnings

class SettingFile:
    def __init__(self, file_path):
        self.path = file_path
        self.file = open(file_path, "r")
        self.dict = {}
        for line in self.file:
            try:
                (key, value) = line.split("\t")
                self.dict[key] = value
            except:
                pass

        self.file.close()

    def write(self, key, value):
        try:
            self.dict[str(key)] = str(value)+'\n'
        except:
            warnings.warn(f"Could not write '{key}: {value}' to settings file.")
    
    def read(self, key):
        try:
            return self.dict[key].strip()
        except:
            warnings.warn(f"Could not read '{key}' from settings file.")

    def remove(self, key):
        try:
            self.dict.pop(key)
        except:
            warnings.warn(f"Could not remove '{key}' from settings file.")

    def save(self):
        try:
            self.file = open(self.path, "w+")
            for key, value in self.dict.items():
                self.file.write(key+'\t'+value)
            self.file.close()
        except:
            warnings.warn(f"Could not save to settings file '{self.path}'.")

    def close(self):
        self.file.close()