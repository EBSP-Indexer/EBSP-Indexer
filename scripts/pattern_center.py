import sys
from os import path, devnull
import kikuchipy as kp
from PySide6.QtWidgets import QDialog, QDialogButtonBox
import numpy as np

from diffsims.crystallography import ReciprocalLatticeVector
from pyebsdindex import ebsd_index, pcopt
from orix.quaternion import Rotation

from utils.filebrowser import FileBrowser
from utils.setting_file import SettingFile
from ui.ui_pattern_center import Ui_PatternCenter

progressbar_bool = False

def find_hkl(phase):
    FCC = ["ni", "al", "austenite", "cu", "si"]
    BCC = ["ferrite"]
    #TETRAGONAL = ["steel_sigma"]
    if phase.lower() in FCC:
        return [[1, 1, 1], [2, 0, 0], [2, 2, 0], [3, 1, 1]]
    elif phase.lower() in BCC:
        return [[0, 1, 1], [0, 0, 2], [1, 1, 2], [0, 2, 2]]
    #experimental support for TETRAGONAL sigma phase, not sure if correct...
    #elif phase.lower() in TETRAGONAL:
    #    return [[1, 1, 0], [2, 0, 0], [1, 0, 1], [2, 1, 0], [1, 1, 1], [2, 2, 0], [2, 1, 1]]


class PatterCenterDialog(QDialog):
    def __init__(self, parent=None, file_selected=None):
        super().__init__(parent)
        self.file_selected = file_selected
        self.setting_path = self.findSettingsFile()
        self.ui = Ui_PatternCenter()
        self.ui.setupUi(self)
        self.setupConnections()
        self.setupCalibrationPatterns()
        self.setupInitialSettings()
        
        #self.fileBrowserOD = FileBrowser(FileBrowser.OpenDirectory)
        self.fileBrowserOD = FileBrowser(
            mode=FileBrowser.OpenFile,
        )

    def findSettingsFile(self):
        if self.file_selected[-11:] == "Setting.txt":
            setting_path = self.file_selected
            return setting_path

        if path.exists(path.join(self.file_selected, "Setting.txt")):
            setting_path = path.join(self.file_selected, "Setting.txt")
            return setting_path

        if path.exists(path.join(path.dirname(self.file_selected), "Setting.txt")):
            setting_path = path.join(path.dirname(self.file_selected), "Setting.txt")
            return setting_path

    def setupInitialSettings(self):
        self.setting_file = SettingFile(path.join(path.dirname(self.setting_path),"project_settings.txt"))
        self.program_settings = SettingFile("advanced_settings.txt")
        
        try:
            self.convention = self.setting_file.read("Convention")
        except:
            self.convention = self.program_settings.read("Convention")
        
        try:
            self.pc = [
                    float(self.setting_file.read("X star")),
                    float(self.setting_file.read("Y star")),
                    float(self.setting_file.read("Z star")),
            ]
        except:
            self.pc = np.array([0.5000, 0.7000, 0.5000])
        
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
                phase = path.dirname(mp_path).split("/").pop()
                self.mp_paths[phase] = mp_path
                self.ui.listPhases.addItem(phase)
                i += 1
            except:
                break

        """
        i = 1
        while True:
            try:
                mp_path = self.setting_file.read("Master pattern " + str(i))
                phase = mp_path.split("/").pop()
                self.mp_paths[phase] = mp_path
                self.ui.listPhases.addItem(phase)
                
                i += 1
                self.phase = phase
            except:
                break
        """

        if len(list(self.mp_paths.keys())) != 0:
            self.ui.listPhases.setCurrentRow(0)
            self.phase = self.ui.listPhases.currentItem().text()
        else:
            self.changeStateOfButtons()

        self.is_mp_paths_updated = True
        self.enabled = False
        self.ui.bandButton.setDisabled(True)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
    
    def changeStateOfButtons(self):
        enable = bool(len(list(self.mp_paths.keys())))
        
        self.ui.buttonPlot.setEnabled(enable)
        self.ui.buttonTune.setEnabled(enable)
        self.ui.toolButtonLeft.setEnabled(enable)
        self.ui.toolButtonRight.setEnabled(enable)
        self.ui.buttonRemovePhase.setEnabled(enable)

    def setupCalibrationPatterns(self):
        self.pattern_index = 0
        self.s_cal = kp.load(self.setting_path)
        sig_shape = self.s_cal.axes_manager.signal_shape[::-1]
        self.nav_size = self.s_cal.axes_manager.navigation_size

        self.s_cal.remove_static_background(show_progressbar=progressbar_bool)
        self.s_cal.remove_dynamic_background(show_progressbar=progressbar_bool)

        working_distance = self.s_cal.metadata.Acquisition_instrument.SEM.working_distance
        self.ui.workingDistanceLabel.setText("Working Distance (mm): "+str(working_distance))

        self.indexer = ebsd_index.EBSDIndexer(
            phaselist=["FCC", "BCC"],
            vendor="BRUKER", 
            sampleTilt=self.s_cal.detector.sample_tilt,
            camElev=self.s_cal.detector.tilt,
            patDim=sig_shape,
        )

        self.ui.counterLabel.setText(
            "Calibration Pattern: "+str(self.pattern_index+1)+"/"+str(self.nav_size)
        )
        self.ui.MplWidget.canvas.ax.axis("off")
        self.ui.MplWidget.canvas.ax.imshow(self.s_cal.data[0], cmap="gray")

        self.pcs = {}
        self.pattern_ignored = False
        for i in range(self.nav_size):
            self.pcs[i] = ["", [0.0, 0.0, 0.0], False]

    def setupConnections(self):
        self.ui.buttonAddPhase.clicked.connect(lambda: self.addPhase())
        self.ui.buttonRemovePhase.clicked.connect(lambda: self.removePhase())
        self.ui.toolButtonLeft.clicked.connect(lambda: self.previousPattern())
        self.ui.toolButtonRight.clicked.connect(lambda: self.nextPattern())
        self.ui.buttonTune.clicked.connect(lambda: self.refinePatternCenter())
        self.ui.buttonPlot.clicked.connect(lambda: self.plotClicked())
        self.ui.buttonBox.accepted.connect(lambda: self.saveAndExit())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())
        self.ui.bandButton.clicked.connect(lambda: self.bandButtonClicked())
        self.ui.ignoreCheckBox.clicked.connect(lambda: self.ignoreButtonClicked())
        self.ui.conventionBox.currentTextChanged.connect(lambda: self.updatePCConvention())

    def previousPattern(self):
        if self.pattern_index > 0:
            #Saves current phase in pcs dictionary
            self.pcs[self.pattern_index][0] = self.phase
            self.pcs[self.pattern_index][1] = self.pc
            self.pcs[self.pattern_index][2] = self.pattern_ignored

            #Gets values for previous phase
            self.pattern_index -= 1
            self.phase = self.pcs.get(self.pattern_index)[0]
            self.pc = self.pcs.get(self.pattern_index)[1]
            self.pattern_ignored = self.pcs.get(self.pattern_index)[2]
            self.ui.counterLabel.setText(
                "Calibration Pattern: "+str(self.pattern_index+1)+"/"+str(self.nav_size)
                )
            self.ui.ignoreCheckBox.setChecked(self.pattern_ignored)
            self.updatePCSpinBox()
            self.plotData()

    #TODO: Make the program remeber the last phase and pc when moving between calibration patterns
    def nextPattern(self):
        if self.pattern_index < self.nav_size-1:
            self.pcs[self.pattern_index][0] = self.phase
            self.pcs[self.pattern_index][1] = self.pc
            self.pcs[self.pattern_index][2] = self.pattern_ignored

            self.pattern_index += 1
            if self.pcs.get(self.pattern_index)[1][0] == 0.0:
                self.pc = self.pcs.get(self.pattern_index-1)[1]
            else:
                self.pc = self.pcs.get(self.pattern_index)[1]
            if self.pcs.get(self.pattern_index)[0] == "":
                self.phase = self.pcs.get(self.pattern_index-1)[0]
            else:
                self.phase = self.pcs.get(self.pattern_index)[0]
            self.pattern_ignored = self.pcs.get(self.pattern_index)[2]

            self.ui.counterLabel.setText(
                "Calibration Pattern: "+str(self.pattern_index+1)+"/"+str(self.nav_size)
                )
            self.ui.ignoreCheckBox.setChecked(self.pattern_ignored)
            self.updatePCSpinBox()
            self.plotData()

    def addPhase(self):
        if self.fileBrowserOD.getFile():
            mp_path = self.fileBrowserOD.getPaths()[0]
            phase = path.basename(path.dirname(mp_path)) #.split("/").pop()
            self.fileBrowserOD.setDefaultDir(path.dirname(mp_path))
            if phase not in self.mp_paths.keys():
                self.mp_paths[phase] = mp_path
                self.ui.listPhases.addItem(phase)
                self.is_mp_paths_updated = True
            self.phase = phase
            self.ui.listPhases.setCurrentRow(len(self.mp_paths.keys())-1)
        self.changeStateOfButtons()

    def removePhase(self):
        #if str(self.ui.listPhases.currentItem().text()) is None:
        #    self.ui.listPhases.setCurrentRow(-1)
        self.mp_paths.pop(str(self.ui.listPhases.currentItem().text()))
        self.ui.listPhases.takeItem(self.ui.listPhases.currentRow())
        self.is_mp_paths_updated = True
        self.ui.listPhases.clearSelection()

        self.changeStateOfButtons()

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

    def updatePCDict(self, pattern_index, phase, pc, pattern_ignored):
        self.pcs[pattern_index] = [phase, pc, pattern_ignored]
    
    def plotClicked(self):
        self.updatePCArrayFromSpinBox()

        #Checks which phase to use from list of phases
        try:
            self.phase = self.ui.listPhases.currentItem().text()
        except:
            self.ui.listPhases.setCurrentRow(0)
            self.phase = self.ui.listPhases.currentItem().text()
        
        self.plotData()

    def refinePatternCenter(self):
        self.updatePCArrayFromSpinBox()

        #Checks which phase to use from list of phases
        try:
            self.phase = self.ui.listPhases.currentItem().text()
        except:
            self.ui.listPhases.setCurrentRow(0)
            self.phase = self.ui.listPhases.currentItem().text()

        pattern = self.s_cal.data[self.pattern_index]
        self.pc = pcopt.optimize(pattern, self.indexer, self.pc)
        self.updatePCSpinBox()
        self.plotData()

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
            ref_i = ReciprocalLatticeVector(
                phase=mp_dict[name].phase, hkl=find_hkl(name)
            )
            ref_i = ref_i.symmetrise().unique()
            ref_dict[name] = ref_i

        self.simulator_dict = {}
        for name in self.mp_paths.keys():
            self.simulator_dict[name] = kp.simulations.KikuchiPatternSimulator(
                ref_dict[name]
            )
        
        # To prevent the program from retrieving mp data when not needed:
        self.is_mp_paths_updated = False

    def plotData(self):
        self.updatePCDict(self.pattern_index, self.phase, self.pc, self.pattern_ignored)

        #Updates data from master pattern (simulator_dict) if phase list has been updated
        if self.is_mp_paths_updated:
            self.retrieveMPData()
        
        #Sets up data needed for plotting
        detector = kp.detectors.EBSDDetector(
            shape=self.s_cal.detector.shape,
            sample_tilt=self.s_cal.detector.sample_tilt,
            tilt=self.s_cal.detector.tilt,
            pc=self.pc,
            convention=self.indexer.vendor,
        )

        data = self.indexer.index_pats(self.s_cal.data[self.pattern_index], PC=self.pc)[0]
        rot = Rotation(data["quat"][-1]) * Rotation.from_axes_angles([0, 0, -1], np.pi / 2)

        geosim_dict = {}

        sys.stdout = open(devnull, 'w')
        for name in self.mp_paths.keys():
            geosim_dict[name] = self.simulator_dict[name].on_detector(detector, rot)

        sys.stdout = sys.__stdout__


        #Draws pattern in MplWidget 
        self.pattern_image = self.s_cal.data[self.pattern_index]
        self.ui.MplWidget.canvas.ax.clear()
        self.ui.MplWidget.canvas.ax.axis("off")
        self.ui.MplWidget.canvas.ax.imshow(self.pattern_image, cmap="gray")
        self.lines, zone_axes, zone_axes_labels = geosim_dict[self.phase].as_collections(
            0,
            zone_axes=True,
            zone_axes_labels=True,
            zone_axes_labels_kwargs=dict(fontsize=12),
        ) #TODO: How does this even work?

        pc_x, pc_y = len(self.pattern_image)*self.pc[0], len(self.pattern_image[0])*self.pc[1]
        self.ui.MplWidget.canvas.ax.plot(pc_x, pc_y, marker="*", markersize=12, color="gold")
        self.ui.MplWidget.canvas.ax.add_collection(self.lines)
        self.ui.MplWidget.canvas.draw()

        #Updates misfit label
        self.ui.labelMisfit.setText("Misfit(°): "+str(round(data["fit"][-1][0], 4)))

        self.bands_enabled = False
        self.bandButtonClicked()
        self.ui.bandButton.setEnabled(True)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)

    def bandButtonClicked(self):
        if not self.bands_enabled:
            self.ui.MplWidget.canvas.ax.add_collection(self.lines)
            self.ui.MplWidget.canvas.draw()
            self.ui.bandButton.setText("Hide bands")
            self.bands_enabled = True

        elif self.bands_enabled:
            self.ui.MplWidget.canvas.ax.clear()
            self.ui.MplWidget.canvas.ax.axis("off")
            self.ui.MplWidget.canvas.ax.imshow(self.pattern_image, cmap="gray")
            pc_x, pc_y = len(self.pattern_image)*self.pc[0], len(self.pattern_image[0])*self.pc[1]
            self.ui.MplWidget.canvas.ax.plot(pc_x, pc_y, marker="*", markersize=12, color="gold")
            self.ui.MplWidget.canvas.draw()
            self.ui.bandButton.setText("Show bands")
            self.bands_enabled = False
    
    def ignoreButtonClicked(self):
        if self.ui.ignoreCheckBox.isChecked():
            self.pattern_ignored = True
        else:
            self.pattern_ignored = False

    def saveAndExit(self):
        self.setting_file.delete_all_entries()  # clean up initial dictionary

        ### Sample parameters
        for i, path in enumerate(self.mp_paths.values(), 1):
            self.setting_file.write(f"Master pattern {i}", path)

        x_sum, y_sum, z_sum = 0, 0, 0
        n = 0
        for i in range(self.nav_size):
            pattern_included = not self.pcs.get(i)[2]
            if self.pcs.get(i)[1][0] > 0 and pattern_included:
                x, y, z = self.pcs.get(i)[1][0], self.pcs.get(i)[1][1], self.pcs.get(i)[1][2]
                x_sum += x
                y_sum += y
                z_sum += z
                n += 1
                if self.program_settings.read("Individual PC data") == "True":
                    self.setting_file.write("Calibration PC"+str(i), str([round(x, 4),round(y, 4), round(z, 4)]))

        x_average = round(x_sum/n, 4)
        y_average = round(y_sum/n, 4)
        z_average = round(z_sum/n, 4)

        self.setting_file.write("Convention", self.convention)
        self.setting_file.write("X star", f"{x_average}")
        
        if self.convention == "BRUKER":
            self.setting_file.write("Y star", f"{y_average}")
        elif self.convention == "TSL":
            self.setting_file.write("Y star", f"{1-y_average}")

        self.setting_file.write("Z star", f"{z_average}")
        
        self.setting_file.save()
        self.close()