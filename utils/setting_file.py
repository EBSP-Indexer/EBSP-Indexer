import os
import warnings

class SettingFile:
    def __init__(self, file_path):
        self.path = file_path
        self.dict = {}
        try:
            self.file = open(file_path, "r")
            for line in self.file:
                
                if line.strip():
                    (key, value) = line.split(":\t")
                    self.dict[key] = value
            self.file.close()

        except Exception as e:
            #raise e
            #warnings.warn(f"Could not open settings file '{self.path}'.")
            pass
        

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
                self.file.write(key+':\t'+value)
            self.file.close()
        except:
            warnings.warn(f"Could not save to settings file {self.path}.")

    def close(self):
        self.file.close()