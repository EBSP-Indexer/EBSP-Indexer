from os import path
from kikuchipy import load, generators
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QThreadPool

from utils.filebrowser import FileBrowser
from utils.worker import Worker

from ui.ui_pre_indexing_maps import Ui_Dialog

import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar


class PreIndexingMapsDialog(QDialog):
    def __init__(
        self,
        parent,
        pattern_path=None,
    ):
        super().__init__(parent)

        # initate threadpool and text output
        self.threadPool = QThreadPool.globalInstance()
        self.console = parent.console

        self.working_dir = path.dirname(pattern_path)

        self.pattern_path = pattern_path

        self.filenamebase = path.basename(self.pattern_path).split(".")[0]

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{self.windowTitle()} - {self.pattern_path}")
        self.setupConnections()

        try:
            self.s = load(self.pattern_path, lazy=True)
        except Exception as e:
            raise e

        self.scale = self.s.axes_manager["x"].scale
        self.save_fig_kwargs = dict(bbox_inches="tight", pad_inches = 0)
        
        self.fileBrowser = FileBrowser(
            mode=FileBrowser.SaveFile,
            dirpath=self.working_dir,
            filter_name="Hierarchical Data Format (*.h5);;NordifUF Pattern Files (*.dat)",
        )

    def setSavePath(self):
        if self.fileBrowser.getFile():
            self.save_path = self.fileBrowser.getPaths()[0]
            self.ui.folderEdit.setText(path.dirname(self.save_path))
            self.ui.filenameEdit.setText(path.basename(self.save_path))

    def setupConnections(self):
        # self.ui.browseButton.clicked.connect(lambda: self.setSavePath())
        self.ui.buttonBox.accepted.connect(lambda: self.run_pre_indexing_maps())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())

        # choose navigator

        # self.ui.pushButtonMIM.clicked.connect(lambda: self.generate_mean_intensity_map())
        # self.ui.pushButtonVBSE.clicked.connect(lambda: self.generate_rgb_vbse())

    def getOptions(self) -> dict:
        return {
            "Average dot product map": [
                self.ui.checkBoxADP.isChecked(),
                lambda: self.save_adp_map(),
            ],
            "Image quality map": [
                self.ui.checkBoxIQM.isChecked(),
                lambda: self.save_iq_map(),
            ],
            "Virtual backscatter image": [
                self.ui.checkBoxVBSE.isChecked(),
                lambda: self.save_rgb_vbse(),
            ],
            "Mean intensity map": [
                self.ui.checkBoxMIM.isChecked(),
                lambda: self.save_mean_intensity_map(),
            ],
        }

    def save_iq_map(self):
        self.iq_map = self.s.get_image_quality()
        fig, ax = plt.subplots()
        ax.axis("off")
        ax.imshow(self.iq_map, cmap="gray")
        scalebar = ScaleBar(self.scale, "um", location="lower left", box_alpha=0.5, border_pad=0.4)
        ax.add_artist(scalebar)
        plt.savefig(path.join(self.working_dir, "image_quality_map.png"), **self.save_fig_kwargs)

    def save_adp_map(self):
        self.adp_map = self.s.get_average_neighbour_dot_product_map()
        fig, ax = plt.subplots()
        ax.axis("off")
        ax.imshow(self.adp_map, cmap="gray")
        scalebar = ScaleBar(self.scale, "um", location="lower left", box_alpha=0.5, border_pad=0.4)
        ax.add_artist(scalebar)
        plt.savefig(path.join(self.working_dir, "average_dot_product_map.png"), **self.save_fig_kwargs)

    def save_mean_intensity_map(self):
        self.mim_map = self.s.mean(axis=(2, 3))
        fig, ax = plt.subplots()
        ax.axis("off")
        ax.imshow(self.mim_map, cmap="gray")
        scalebar = ScaleBar(self.scale, "um", location="lower left", box_alpha=0.5, border_pad=0.4)
        ax.add_artist(scalebar)
        plt.savefig(path.join(self.working_dir, "mean_intensity_map.png"), **self.save_fig_kwargs)

    def save_rgb_vbse(self):
        vbse_gen = generators.VirtualBSEGenerator(self.s)
        self.vbse_map = vbse_gen.get_rgb_image(r=(3, 1), b=(3, 2), g=(3, 3))
        self.vbse_map.change_dtype("uint8")

        fig, ax = plt.subplots()
        ax.axis("off")
        ax.imshow(self.vbse_map.data)
        scalebar = ScaleBar(self.scale, "um", location="lower left", box_alpha=0.5, border_pad=0.4)
        ax.add_artist(scalebar)
        plt.savefig(path.join(self.working_dir, "vbse_rgb.png"), **self.save_fig_kwargs)

    def plot(self, image):

        self.ui.mplWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.mplWidget.canvas.ax.clear()
        self.ui.mplWidget.canvas.ax.axis(False)
        self.ui.mplWidget.canvas.ax.imshow(image, cmap="gray")
        self.ui.mplWidget.canvas.draw()

    def run_pre_indexing_maps(self):
        # Pass the function to execute
        save_worker = Worker(fn=self.save_pre_indexing_maps, output=self.console)
        # Execute
        self.threadPool.start(save_worker)
        self.accept()

    def save_pre_indexing_maps(self):
        pre_processing_keys = [
            "Mean intensity map",
            "Average dot product map",
            "Image quality map",           
            "Virtual backscatter image",
        ]
        self.options = self.getOptions()

        try:
            for key in pre_processing_keys:
                optionEnabled, optionExecute = self.options[key]
                if optionEnabled:
                    optionExecute()
                    print(f"{key}: OK")
            print(f"Pre-indexing maps generated successfully!")
        except Exception as e:
            print(f"Could not generate pre-indexing maps: {e}")
