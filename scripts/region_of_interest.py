from os import path
import kikuchipy as kp
from PySide6.QtWidgets import QDialog

from utils import FileBrowser
from ui.ui_roi_dialog import Ui_ROIDialog

from scripts.signal_loader import EBSDDataset

from matplotlib.widgets import RectangleSelector
import numpy as np

# import matplotlib.pyplot as plt
# from skimage import exposure, img_as_ubyte

# TODO: show image shape in dialog window
# TODO: let user change rectangle shape with spinBox
# TODO: clean up save_file name
# TODO: display x, y coordinates onn hover


class RegionOfInteresDialog(QDialog):
    def __init__(
        self,
        parent,
        pattern_path=None,
    ):
        super().__init__(parent)

        self.working_dir = path.dirname(pattern_path)

        self.pattern_path = pattern_path

        self.filenamebase = path.basename(self.pattern_path).split(".")[0]

        # Standard filename of processed pattern
        self.save_path = path.join(
            self.working_dir, f"{self.filenamebase}_x0_x1_y0_y1.h5"
        )

        self.ui = Ui_ROIDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{self.windowTitle()} - {self.pattern_path}")
        self.setupConnections()

        try:
            ebsd_signal = kp.load(self.pattern_path, lazy=True)
        except Exception as e:
            raise e

        self.dataset = EBSDDataset(ebsd_signal)

        for key in self.dataset.navigator.keys():
            self.ui.comboBoxNavigator.addItem(key)

        self.dataset.nav_shape

        self.x_len, self.y_len = self.dataset.nav_shape

        self.ui.imageShapeLabel.setText(f"({self.x_len}, {self.y_len})")

        self.ui.spinBoxXstart.setMaximum(self.x_len)
        self.ui.spinBoxXend.setMaximum(self.x_len)
        self.ui.spinBoxYstart.setMaximum(self.y_len)
        self.ui.spinBoxYend.setMaximum(self.y_len)

        self.plot_navigator()

        self.fileBrowser = FileBrowser(
            mode=FileBrowser.SaveFile,
            dirpath=self.working_dir,
            filter_name="Hierarchical Data Format (*.h5);;NordifUF Pattern Files (*.dat)",
        )

    def setupConnections(self):
        self.ui.browseButton.clicked.connect(lambda: self.setSavePath())
        self.ui.buttonBox.accepted.connect(lambda: self.run_roi_selection())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())

        # set path names
        self.ui.folderEdit.setText(path.dirname(self.save_path))
        self.ui.filenameEdit.setText(path.basename(self.save_path))

        # set inital spinbox values
        self.ui.spinBoxXstart.textChanged.connect(lambda: self.update_selection())
        self.ui.spinBoxXend.textChanged.connect(lambda: self.update_selection())
        self.ui.spinBoxYstart.textChanged.connect(lambda: self.update_selection())
        self.ui.spinBoxYend.textChanged.connect(lambda: self.update_selection())

        # choose navigator
        self.ui.comboBoxNavigator.currentTextChanged.connect(
            lambda: self.plot_navigator()
        )

    def setSavePath(self):
        if self.fileBrowser.getFile():
            self.save_path = self.fileBrowser.getPaths()[0]
            self.ui.folderEdit.setText(path.dirname(self.save_path))
            self.ui.filenameEdit.setText(path.basename(self.save_path))

    def update_selection(self):
        selection = self.getSelection()
        x0, x1, y0, y1 = selection
        if x1-x0 > 0 and y1-y0 > 0:
            pattern_name = f"{self.filenamebase}_{x0}_{x1}_{y0}_{y1}.h5"
        else:
            pattern_name = path.basename(self.save_path)
        self.ui.filenameEdit.setText(pattern_name)

        self.rs.extents = selection

    def getSelection(self) -> dict:
        return (
            self.ui.spinBoxXstart.value(),
            self.ui.spinBoxXend.value(),
            self.ui.spinBoxYstart.value(),
            self.ui.spinBoxYend.value(),
        )

    def plot_navigator(self):
        #try:
        #    self.ui.navigatorMplWidget.canvas.mpl_disconnect(self.click_id)
        #except:
        #    pass
        nav_key = self.ui.comboBoxNavigator.currentText()
        navigator = self.dataset.compute_navigator(self.dataset.navigator[nav_key])

        self.ui.mplWidget.vbl.setContentsMargins(10, 10, 10, 10)
        self.ui.mplWidget.canvas.ax.clear()
        self.ui.mplWidget.canvas.ax.axis(False)
        self.ui.mplWidget.canvas.ax.imshow(navigator, cmap="gray", extent=(0, self.dataset.nav_shape[0], self.dataset.nav_shape[1], 0))
        self.ui.mplWidget.canvas.draw()

        self.rs = RectangleSelector(
            self.ui.mplWidget.canvas.ax,
            self.line_select_callback,
            useblit=True,
            button=[1, 3],  # don't use middle button
            minspanx=5,
            minspany=5,
            spancoords="data",
            interactive=True,
            use_data_coordinates=True
        )

        self.click_id = self.ui.mplWidget.canvas.mpl_connect("button_press_event", self.on_click)

    def on_click(self, event):
        if event.button == 1 or event.button == 3 and not self.rs.active:
            self.rs.set_active(True)
        else:
            self.rs.set_active(False)

    def line_select_callback(self, eclick, erelease):
        
        self.spinBoxBlockSignal(True)
        
        self.ui.spinBoxXstart.setValue(int(eclick.xdata))
        self.ui.spinBoxXend.setValue(int(erelease.xdata))
        self.ui.spinBoxYstart.setValue(int(eclick.ydata))
        self.ui.spinBoxYend.setValue(int(erelease.ydata))
        
        self.spinBoxBlockSignal(False)

        selection = self.getSelection()
        x0, x1, y0, y1 = selection
        if x1-x0 > 0 and y1-y0 > 0:
            pattern_name = f"{self.filenamebase}_{x0}_{x1}_{y0}_{y1}.h5"
        else:
            pattern_name = path.basename(self.save_path)
        self.ui.filenameEdit.setText(pattern_name)

    def spinBoxBlockSignal(self, block : bool):
        self.ui.spinBoxXstart.blockSignals(block)
        self.ui.spinBoxXend.blockSignals(block)
        self.ui.spinBoxYstart.blockSignals(block)
        self.ui.spinBoxYend.blockSignals(block)

    def run_roi_selection(self):
        selection = self.getSelection()
        x0, x1, y0, y1 = selection

        ebsd_roi = self.dataset.ebsd.inav[x0 : x1, y0 : y1]
        self.save_path = path.join(self.working_dir, self.ui.filenameEdit.text())

        try:
            ebsd_roi.save(
                self.save_path,
                overwrite=True,
            )
            print("Processing complete")
            self.accept()
        except Exception as e:
            print(f"Could not save processed pattern: {e}")
            self.reject()
