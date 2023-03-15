from os import path
import kikuchipy as kp
from PySide6.QtWidgets import QDialog

from utils import FileBrowser
from ui.ui_roi_dialog import Ui_ROIDialog

from matplotlib.widgets import RectangleSelector
import numpy as np
#import matplotlib.pyplot as plt
#from skimage import exposure, img_as_ubyte

#TODO: show image shape in dialog window
#TODO: let user change rectangle shape with spinBox
#TODO: clean up save_file name
#TODO: display x, y coordinates onn hover

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
            self.s = kp.load(self.pattern_path, lazy=True)
        except Exception as e:
            raise e

        self.x_len, self.y_len = self.s.axes_manager.navigation_shape
        
        self.ui.imageShapeLabel.setText(f"({self.x_len}, {self.y_len})")
                
        self.ui.spinBoxXstart.setMaximum(self.x_len)
        self.ui.spinBoxXend.setMaximum(self.x_len)
        self.ui.spinBoxYstart.setMaximum(self.y_len)
        self.ui.spinBoxYend.setMaximum(self.y_len)

        self.generate_mean_intensity_map()

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

    def updateSavePath(self):
        self.options = self.getOptions()
        self.x0 = self.options["x-start"]
        self.x1 = self.options["x-end"]
        self.y0 = self.options["y-start"]
        self.y1 = self.options["y-end"]

        self.save_path = path.join(
            self.working_dir,
            f"{self.filenamebase}_{self.x0}_{self.x1}_{self.y0}_{self.y1}.h5",
        )
        self.ui.folderEdit.setText(path.dirname(self.save_path))
        self.ui.filenameEdit.setText(path.basename(self.save_path))

    def setupConnections(self):
        self.ui.browseButton.clicked.connect(lambda: self.setSavePath())
        self.ui.buttonBox.accepted.connect(lambda: self.run_roi_selection())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())

        #set path names
        self.ui.folderEdit.setText(path.dirname(self.save_path))
        self.ui.filenameEdit.setText(path.basename(self.save_path))

        #set inital spinbox values
        self.ui.spinBoxXstart.textChanged.connect(lambda: self.updateSavePath())
        self.ui.spinBoxXend.textChanged.connect(lambda: self.updateSavePath())
        self.ui.spinBoxYstart.textChanged.connect(lambda: self.updateSavePath())
        self.ui.spinBoxYend.textChanged.connect(lambda: self.updateSavePath())

        # choose navigator

        self.ui.pushButtonMIM.clicked.connect(lambda: self.generate_mean_intensity_map())
        self.ui.pushButtonVBSE.clicked.connect(lambda: self.generate_rgb_vbse())

    def getOptions(self) -> dict:
        return {
            "x-start": self.ui.spinBoxXstart.value(),
            "x-end": self.ui.spinBoxXend.value(),
            "y-start": self.ui.spinBoxYstart.value(),
            "y-end": self.ui.spinBoxYend.value(),
        }

    def generate_mean_intensity_map(self):

        mean_intensity = self.s.mean(axis=(2, 3))
        mean_image = mean_intensity
        #mean_intensity_image = np.uint8(mean_intensity.data/mean_intensity.data.max()*255)
        #mean_image = mean_intensity_image
        #mean_image = exposure.equalize_adapthist(img_as_ubyte(mean_intensity_image))

        self.plot(mean_image)

    def generate_rgb_vbse(self):
        
        vbse_gen = kp.generators.VirtualBSEGenerator(self.s)
        vbse_rgb = vbse_gen.get_rgb_image(r=(3, 1), b=(3, 2), g=(3, 3))
        vbse_rgb.change_dtype("uint8")

        self.plot(vbse_rgb)
    
    def plot(self, image):

        #image = mpimg.imread()
        self.ui.mplWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.mplWidget.canvas.ax.clear()
        self.ui.mplWidget.canvas.ax.axis(False)
        self.ui.mplWidget.canvas.ax.imshow(image, cmap="gray")
        self.ui.mplWidget.canvas.draw()

        self.rs = RectangleSelector(self.ui.mplWidget.canvas.ax, self.line_select_callback,
                                                useblit=True,
                                                button=[1, 3],  # don't use middle button
                                                minspanx=5, minspany=5,
                                                spancoords='data',
                                                interactive=True)

        self.ui.mplWidget.canvas.mpl_connect('button_press_event', self.on_click)
        
    def on_click(self, event):
        if event.button == 1 or event.button == 3 and not self.rs.active:
            self.rs.set_active(True)
        else:
            self.rs.set_active(False) 

    def line_select_callback(self, eclick, erelease):

        self.ui.spinBoxXstart.setValue(int(eclick.xdata))
        self.ui.spinBoxXend.setValue(int(erelease.xdata))
        self.ui.spinBoxYstart.setValue(int(eclick.ydata))
        self.ui.spinBoxYend.setValue(int(erelease.ydata))

    def run_roi_selection(self):
        self.options = self.getOptions()
        self.x0 = self.options["x-start"]
        self.x1 = self.options["x-end"]
        self.y0 = self.options["y-start"]
        self.y1 = self.options["y-end"]

        self.s2 = self.s.inav[self.x0:self.x1, self.y0:self.y1]
        self.save_path = path.join(
            self.working_dir, self.ui.filenameEdit.text()
        )

        try:
            self.s2.save(
                self.save_path,
                overwrite=True,
            )
            print("Processing complete")
            self.accept()
        except Exception as e:
            print(f"Could not save processed pattern: {e}")
            self.reject()
