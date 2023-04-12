import gc
import os

import kikuchipy as kp
from PySide6.QtWidgets import QDialog, QDialogButtonBox

from ui.ui_pattern_processing import Ui_PatternProcessingDialog
from utils import FileBrowser, sendToJobManager


class PatternProcessingDialog(QDialog):
    def __init__(self, parent=None, pattern_path=None):
        super().__init__(parent)

        self.working_dir = os.path.dirname(pattern_path)
        self.pattern_name = os.path.basename(pattern_path)
        self.pattern_path = pattern_path
        self.filenamebase = os.path.basename(self.pattern_path).split(".")[0]

        # Standard filename of processed pattern
        self.save_path = os.path.join(self.working_dir, f"{self.filenamebase}.h5")

        self.ui = Ui_PatternProcessingDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{self.windowTitle()} - {self.pattern_path}")
        self.setupConnections()

        try:
            self.s_preview = kp.load(self.pattern_path, lazy=True)
        except Exception as e:
            raise e

        self.showImage(self.s_preview.inav[1, 1])

        self.gaussian_window = kp.filters.Window("gaussian", std=1)

        self.fileBrowser = FileBrowser(
            mode=FileBrowser.SaveFile,
            dirpath=self.working_dir,
            filter_name="Hierarchical Data Format (*.h5);;NordifUF Pattern Files (*.dat)",
        )

        self.setupInitialSettings()

    def setupConnections(self):
        self.ui.browseButton.clicked.connect(lambda: self.setSavePath())
        self.ui.buttonBox.accepted.connect(lambda: self.run_processing())
        self.ui.buttonBox.rejected.connect(lambda: self.close_dialog())
        self.ui.folderEdit.setText(self.working_dir)
        self.ui.filenameEdit.setText(os.path.basename(self.save_path))

        # Whenever user checks/unchecks boxes the preview window updates to show the result of current choices
        self.ui.staticBackgroundBox.stateChanged.connect(
            lambda: self.preview_processing()
        )
        self.ui.dynamicBackgroundBox.stateChanged.connect(
            lambda: self.preview_processing()
        )
        self.ui.averageBox.stateChanged.connect(lambda: self.preview_processing())

    def close_dialog(self):
        del self.s
        gc.collect()
        self.reject()

    def setSavePath(self):
        if self.fileBrowser.getFile():
            self.save_path = self.fileBrowser.getPaths()[0]
            self.working_dir = os.path.dirname(self.save_path)
            self.ui.folderEdit.setText(self.working_dir)
            self.ui.filenameEdit.setText(os.path.basename(self.save_path))

    def setupInitialSettings(self):
        processing_steps = self.filenamebase.split("_")[1:]
        for step in processing_steps:
            if step == "sb":
                self.ui.staticBackgroundBox.setEnabled(False)
            if step == "db":
                self.ui.dynamicBackgroundBox.setEnabled(False)
            if step == "adp":
                self.ui.averageBox.setEnabled(False)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        """        
        self.sf = SettingFile(path.join(self.working_dir, "project_settings.txt"))

        try:
            self.rsb = self.sf.read("Remove static bacground")
            self.rdb = self.sf.read("Remove dynamic bacground")
            self.anp = self.sf.read("Average neighbour patterns")
        except:
            self.rsb = False
            self.rdb = False
            self.anp = False

        """

    def remove_static(self, dataset, show_progressbar=True):
        dataset.remove_static_background(show_progressbar=show_progressbar)

    def remove_dynamic(self, dataset, show_progressbar=True):
        dataset.remove_dynamic_background(show_progressbar=show_progressbar)

    def average_neighbour(self, dataset, show_progressbar=True):
        dataset.average_neighbour_patterns(
            self.gaussian_window, show_progressbar=show_progressbar
        )

    def showImage(self, dataset):

        self.ui.previewWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.previewWidget.canvas.ax.clear()
        self.ui.previewWidget.canvas.ax.axis(False)
        self.ui.previewWidget.canvas.ax.imshow(dataset.data, cmap="gray")
        self.ui.previewWidget.canvas.draw()

    def preview_processing(self):
        s_prev = self.s_preview.deepcopy().inav[0:3, 0:3]
        extensions = ""
        box_checked = False
        if self.ui.staticBackgroundBox.isChecked():
            self.remove_static(dataset=s_prev, show_progressbar=False)
            extensions += "_sb"
            box_checked = True
        if self.ui.dynamicBackgroundBox.isChecked():
            self.remove_dynamic(dataset=s_prev, show_progressbar=False)
            extensions += "_db"
            box_checked = True
        if self.ui.averageBox.isChecked():
            self.average_neighbour(dataset=s_prev, show_progressbar=False)
            extensions += "_adp"
            box_checked = True

        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(box_checked)

        self.ui.filenameEdit.setText(f"{self.filenamebase}{extensions}.h5")

        self.showImage(s_prev.inav[1, 1])

        del s_prev

    def run_processing(self):
        try:
            s = kp.load(self.pattern_path, lazy=False)
        except Exception as e:
            raise e
        sendToJobManager(
            job_title=f"SN Improvement {self.pattern_name}",
            output_path=os.path.join(self.working_dir, self.ui.filenameEdit.text()),
            listview=self.parentWidget().ui.jobList,
            func=self.apply_processing,
            dataset=s,
        )

    def apply_processing(self, dataset):
        print("Applying processing ...")
        if self.ui.staticBackgroundBox.isChecked():
            self.remove_static(dataset=dataset)
            print("Static background removed")
        if self.ui.dynamicBackgroundBox.isChecked():
            self.remove_dynamic(dataset=dataset)
            print("Dynamic background removed")
        if self.ui.averageBox.isChecked():
            self.average_neighbour(dataset=dataset)
            print("Averaged neighbouring patterns")

        self.save_path = os.path.join(
            self.working_dir, self.ui.filenameEdit.text()
        )  # Get current save path
        try:
            dataset.save(
                self.save_path,
                overwrite=True,
            )
            print(f"Processed dataset saved as {self.ui.filenameEdit.text()}")
            del dataset
            gc.collect()
        except Exception as e:
            print(f"Could not save processed pattern: {e}")
            del dataset
            gc.collect()
            self.reject()
