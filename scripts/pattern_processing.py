from os import path
from kikuchipy import load, filters
from PySide6.QtWidgets import QDialog

from scripts.filebrowser import FileBrowser
from ui.ui_pattern_processing_dialog import Ui_PatternProcessingWindow


class PatternProcessingDialog(QDialog):
    def __init__(
        self, working_dir, pattern_path="Pattern.dat", save_name="Pattern_processed.h5"
    ):
        super().__init__()
        if pattern_path == "":
            self.pattern_path = path.join(working_dir, "Pattern.dat")
        else:
            self.pattern_path = pattern_path
        self.working_dir = working_dir
        self.save_path = f"{self.working_dir}/{save_name}"
        self.ui = Ui_PatternProcessingWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{self.windowTitle()} - {self.pattern_path}")
        self.setupConnections()

        try:
            self.s = load(self.pattern_path, lazy=True)
        except Exception as e:
            raise e
        self.gaussian_window = filters.Window("gaussian", std=1)

        self.options = self.getOptions()
        self.fileBrowser = FileBrowser(
            mode=FileBrowser.SaveFile,
            dirpath=self.working_dir,
            filter_name="Hierarchical Data Format (*.h5);;NordifUF Pattern Files (*.dat)",
        )

    def setupConnections(self):
        self.ui.browseButton.clicked.connect(lambda: self.setSavePath())
        self.ui.buttonBox.accepted.connect(lambda: self.apply_processing())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())
        self.ui.pathLineEdit.setText(self.save_path)
        

    def setSavePath(self):
        if self.fileBrowser.getFile():
            self.save_path = self.fileBrowser.getPaths()[0]
            self.ui.pathLineEdit.setText(self.save_path)

    def getOptions(self) -> dict:
        return {
            "static": {
                self.ui.staticBackgroundBox.isChecked(),
                self.s.remove_static_background(),
            },
            "dynamic": {
                self.ui.dynamicBackgroundBox.isChecked(),
                self.s.remove_dynamic_background(),
            },
            "average": {
                self.ui.averageBox.isChecked(),
                self.s.average_neighbour_patterns(self.gaussian_window),
            },
        }

    def apply_processing(self):
        self.options = self.getOptions()
        for optionName, optionInfo in self.options.items():
            optionEnabled, optionExecute = optionInfo
            print(f"{optionName}: {optionEnabled}")
            if optionEnabled:
                optionExecute
        try:
            filepath = self.ui.pathLineEdit.text()
            self.s.save(
                filename=filepath,
                overwrite=True,
                extension=path.splitext(filepath)[1][1:],
            )
            self.accept()
        except Exception as e:
            print(f"Could not save processed pattern: {e}")
            self.reject()
