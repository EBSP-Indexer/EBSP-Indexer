import sys
from os import path, devnull
import kikuchipy as kp
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QDialogButtonBox
import numpy as np
from math import floor

from diffsims.crystallography import ReciprocalLatticeVector
from pyebsdindex import ebsd_index, pcopt
from orix.quaternion import Rotation

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.widgets import Cursor

from utils import FileBrowser, SettingFile, get_setting_file_bottom_top
from ui.ui_pc_selection import Ui_PCSelection
from scripts.signal_loader import crystalMap, EBSDDataset

progressbar_bool = False

FCC = ["ni", "al", "austenite", "cu", "si", "ag", "cu"]
BCC = ["ferrite"]

def find_hkl(phase):
    #TETRAGONAL = ["steel_sigma"]
    if phase.lower() in FCC:
        return [[1, 1, 1], [2, 0, 0], [2, 2, 0], [3, 1, 1]]
    elif phase.lower() in BCC:
        return [[0, 1, 1], [0, 0, 2], [1, 1, 2], [0, 2, 2]]
    #experimental support for TETRAGONAL sigma phase, not sure if correct...
    #elif phase.lower() in TETRAGONAL:
    #    return [[1, 1, 0], [2, 0, 0], [1, 0, 1], [2, 1, 0], [1, 1, 1], [2, 2, 0], [2, 1, 1]]

class PCSelectionDialog(QDialog):
    def __init__(self, parent=None, pattern_path=None):
        super().__init__(parent)
        # pattern path
        self.pattern_path = pattern_path

        # pattern name
        self.pattern_name = path.basename(self.pattern_path)

        # working directory
        self.working_dir = path.dirname(self.pattern_path)

        self.ui = Ui_PCSelection()
        self.ui.setupUi(self)
        self.setupConnections()
        self.setupInitialSettings()
        
        #self.fileBrowserOD = FileBrowser(FileBrowser.OpenDirectory)
        self.fileBrowserOD = FileBrowser(
            mode=FileBrowser.OpenFile,
            filter_name="*.h5"
        )
        self.plot_navigator(0,0)
        self.coordinates = []

    def setupInitialSettings(self):
        self.setting_file = SettingFile(
            path.join(self.working_dir, "project_settings.txt")
        )
        self.program_settings = SettingFile("advanced_settings.txt")
        
        self.s_cal = kp.load(self.pattern_path, lazy=True)
        working_distance = self.s_cal.metadata.Acquisition_instrument.SEM.working_distance
        self.ui.workingDistanceLabel.setText("Working Distance (mm): "+str(working_distance))

        try:
            self.convention = self.setting_file.read("Convention")
        except:
            self.convention = self.program_settings.read("Convention")
        
        try:
            try:
                self.pc = eval(self.setting_file.read("Pattern center (x*, y*, z*)"))
            except:
                self.pc = [
                        float(self.setting_file.read("X star")),
                        float(self.setting_file.read("Y star")),
                        float(self.setting_file.read("Z star")),
                ]
        except:
            if self.s_cal.metadata.Acquisition_instrument.SEM.microscope == "ZEISS SUPRA55 VP":
                self.pc = [
                    0.5605-0.0017*float(working_distance),
                    1.2056-0.0225*float(working_distance),
                    0.483,
                ]
            else:    
                self.pc = np.array([0.5000, 0.5000, 0.5000])
        
        if self.convention == "TSL":
            #Store TSL convention in BRUKER convention
            self.pc[1] = 1 - self.pc[1]
            self.ui.conventionBox.setCurrentIndex(1)
        self.updatePCSpinBox()
        
        self.mp_paths = {}

        i = 1
        while True:
            try:
                mp_path = self.setting_file.read(f"Master pattern {i}")
                try:
                    mp = kp.load(mp_path, lazy=True)
                except Exception as e:
                    print(e.with_traceback(None))
                    continue
                if not len(mp.phase.name):
                    mp.phase.name = path.dirname(mp_path).split("/").pop()
                self.mp_paths[mp.phase.name] = mp_path
                self.ui.listPhases.addItem(mp.phase.name)
                if mp.phase.name not in FCC + BCC:
                    self.ui.listPhases.item(i-1).setFlags(Qt.NoItemFlags)
                i += 1
            except:
                break

        self.is_mp_paths_updated = True
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
    

    def setupConnections(self):
        self.ui.buttonAddPhase.clicked.connect(lambda: self.addPhase())
        self.ui.buttonRemovePhase.clicked.connect(lambda: self.removePhase())
        self.ui.buttonAddPattern.clicked.connect(lambda: self.addPattern())

        self.ui.buttonBox.accepted.connect(lambda: self.saveAndExit())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())
        self.ui.conventionBox.currentTextChanged.connect(lambda: self.updatePCConvention())


    def addPhase(self):
        if self.fileBrowserOD.getFile():
            mp_path = self.fileBrowserOD.getPaths()[0]
            try:
                mp = kp.load(mp_path, lazy=True)
                if not len(mp.phase.name):
                    mp.phase.name = path.basename(path.dirname(mp_path)) #.split("/").pop()
                phase_name = mp.phase.name
            except Exception as e:
                raise e
            if phase_name not in self.mp_paths.keys():
                self.mp_paths[phase_name] = mp_path
                self.ui.listPhases.addItem(phase_name)
                self.is_mp_paths_updated = True
            
            self.fileBrowserOD.setDefaultDir(path.dirname(mp_path))
            if phase_name not in FCC + BCC:
                self.ui.listPhases.item(len(self.mp_paths.keys())-1).setFlags(Qt.NoItemFlags)
            else:
                self.phase = phase_name
                self.ui.listPhases.setCurrentRow(len(self.mp_paths.keys())-1)
        self.changeStateOfButtons()

    def removePhase(self):
        self.mp_paths.pop(str(self.ui.listPhases.currentItem().text()))
        self.ui.listPhases.takeItem(self.ui.listPhases.currentRow())
        self.is_mp_paths_updated = True
        self.ui.listPhases.clearSelection()

        self.changeStateOfButtons()
    
    def addPattern(self):
        if [self.current_x, self.current_y] not in self.coordinates:
            self.coordinates.append([self.current_x, self.current_y])
            self.ui.listCoordinates.addItem(f"({self.current_x}, {self.current_y})")
            print(self.coordinates)
    
    def changeStateOfButtons(self):
        enable = bool(len(list(self.mp_paths.keys())))

        self.ui.buttonRemovePhase.setEnabled(enable)
        self.ui.buttonAddPattern.setEnabled(enable)
        self.ui.buttonRemovePattern.setEnabled(enable)

    def updatePCSpinBox(self):
        self.ui.spinBoxX.setValue(self.pc[0])
        self.ui.spinBoxZ.setValue(self.pc[2])
        if self.convention == "BRUKER":
            self.ui.spinBoxY.setValue(self.pc[1])
        elif self.convention == "TSL":
            self.ui.spinBoxY.setValue(1-self.pc[1])

    def updatePCArrayFromSpinBox(self):
        self.pc[0] = self.ui.spinBoxX.value()
        self.pc[2] = self.ui.spinBoxZ.value()
        if self.convention == "BRUKER":
            self.pc[1] = self.ui.spinBoxY.value()
        elif self.convention == "TSL":
            self.pc[1] = 1 - self.ui.spinBoxY.value()
    
    def updatePCConvention(self):
        self.convention = self.ui.conventionBox.currentText()
        self.updatePCSpinBox()      
    

    def retrieveMPData(self):
        mp_dict = {}
        for name, h5path in self.mp_paths.items():
            mp_i = kp.load(
                path.join(h5path),
                projection="lambert",
                energy=self.s_cal.metadata.Acquisition_instrument.SEM.beam_energy,
                hemisphere="upper",
            )
            mp_dict[name] = mp_i

        ref_dict = {}
        for name in self.mp_paths.keys():
            if name not in FCC + BCC:
                continue
            ref_i = ReciprocalLatticeVector(
                phase=mp_dict[name].phase, hkl=find_hkl(name)
            )
            ref_i = ref_i.symmetrise().unique()
            ref_dict[name] = ref_i

        self.simulator_dict = {}
        for name in self.mp_paths.keys():
            if name not in FCC + BCC:
                continue
            self.simulator_dict[name] = kp.simulations.KikuchiPatternSimulator(
                ref_dict[name]
            )
        
        # To prevent the program from retrieving mp data when not needed:
        self.is_mp_paths_updated = False

    def saveAndExit(self):
        self.close()



################################################################################################################################



    def plot_navigator(self, x=0, y=0):
        self.dataset = EBSDDataset(self.s_cal, self.pattern_path)

        try:
            self.ui.MplWidget.canvas.mpl_disconnect(self.cid)
            self.ui.MplWidget.canvas.mpl_disconnect(self.hover_id)
        except:
            pass

        # plot to MplCanvas
        self.ui.MplWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.MplWidget.canvas.ax.clear()
        self.ui.MplWidget.canvas.ax.axis(False)

        self.cursor = Cursor(
            self.ui.MplWidget.canvas.ax,
            useblit=True,
            color="red",
            linewidth=1,
            linestyle="-",
            alpha=0.5,
        )
        self.cursor.set_active(True)

        self.ui.MplWidget.canvas.ax.imshow(
            self.s_cal.get_image_quality(),
            cmap="gray",
            extent=(0, self.dataset.nav_shape[0], self.dataset.nav_shape[1], 0),
        )
        self.ui.MplWidget.canvas.draw()

        # plot pattern from upper left corner
        self.plot_signal(x, y)
        self.current_x, self.current_y = x, y

        self.cid = self.ui.MplWidget.canvas.mpl_connect(
            "button_press_event", lambda event: self.on_click_navigator(event)
        )
        self.hover_id = self.ui.MplWidget.canvas.mpl_connect(
            "motion_notify_event",
            lambda event: self.on_hover_navigator(event),
        )

    def plot_signal(self, x_index, y_index):
        pattern = self.dataset.ebsd
        signal = pattern.data[y_index, x_index]
        self.ui.MplWidgetPattern.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.MplWidgetPattern.canvas.ax.clear()
        self.ui.MplWidgetPattern.canvas.ax.axis(False)
        self.ui.MplWidgetPattern.canvas.ax.imshow(signal, cmap="gray")
        self.ui.MplWidgetPattern.canvas.draw()

        self.current_x, self.current_y = x_index, y_index

    def on_click_navigator(self, event):
        try:
            self.click_rect.remove()
        except:
            pass

        nav_shape = self.dataset.nav_shape

        if event.inaxes:
            x_text, y_text = (
                event.xdata + nav_shape[0] * 0.1,
                event.ydata - nav_shape[1] * 0.1,
            )
            if event.xdata > nav_shape[0] * 0.7:
                x_text = event.xdata - nav_shape[0] * 0.2
            if event.ydata < nav_shape[1] * 0.3:
                y_text = event.ydata + nav_shape[1] * 0.1
            xytext = (x_text, y_text)

            x, y = floor(event.xdata), floor(event.ydata)
            self.plot_signal(x, y)
            if [x, y] not in self.coordinates:
                self.coordinates.append([x,y])
                self.ui.listCoordinates.addItem(f"({x}, {y})")
                print(self.coordinates)
            self.click_rect = self.ui.MplWidget.canvas.ax.add_patch(
                Rectangle(
                    (x, y),
                    1,
                    1,
                    linewidth=0.5,
                    edgecolor="black",
                    facecolor="red",
                    alpha=1,
                )
            )
            click_annot = self.ui.MplWidget.canvas.ax.annotate(
                text=f"({x}, {y})",
                xy=((x + 0.5, y + 0.5)),
                xytext=xytext,
                annotation_clip=True,
                arrowprops=dict(
                    facecolor="black", width=0.2, headwidth=5, headlength=5
                ),
            )
            click_annot.set_bbox(dict(facecolor="white", alpha=0.5, edgecolor="grey"))
            self.ui.MplWidget.canvas.draw()
            click_annot.remove()
            if self.dataset.datatype == "crystal map":
                phase_name = self.dataset.crystal_map.phases[
                    self.dataset.phase_id_array[y, x]
                ].name
                self.ui.labelPhaseClick.setText(f"{phase_name}")

    def on_hover_navigator(self, event):
        if event.inaxes:
            x_hover, y_hover = floor(event.xdata), floor(event.ydata)
            self.ui.labelxy.setText(f"({x_hover}, {y_hover})")
            if self.dataset.datatype == "crystal map":
                phase_name = self.dataset.crystal_map.phases[
                    self.dataset.phase_id_array[y_hover, x_hover]
                ].name
                self.ui.labelPhaseHover.setText(f"{phase_name}")
        else:
            self.ui.labelxy.setText(f"(x, y)")

