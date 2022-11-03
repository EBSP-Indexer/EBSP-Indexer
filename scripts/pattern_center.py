from os import path
from pickle import TRUE
from re import T
import kikuchipy as kp
from PySide6.QtCore import QDir
from PySide6.QtWidgets import QDialog, QApplication
import matplotlib.pyplot as plt
import numpy as np

from diffsims.crystallography import ReciprocalLatticeVector
from diffpy.structure import Atom, Lattice, Structure
from pyebsdindex import ebsd_index, pcopt
from orix.crystal_map.phase_list import Structure
from orix.quaternion import Rotation
from orix.crystal_map import Phase

from utils.filebrowser import FileBrowser
from scripts.setting_file import SettingFile
from ui.ui_pattern_center import Ui_PatternCenterDialog

from mplwidget import MplWidget


def find_hkl(phase):
    FCC = ["ni", "al", "austenite", "cu", "si"]
    BCC = ["ferrite"]
    if phase.lower() in FCC:
        return [[1, 1, 1], [2, 0, 0], [2, 2, 0], [3, 1, 1]]
    elif phase.lower() in BCC:
        return [[0, 1, 1], [0, 0, 2], [1, 1, 2], [0, 2, 2]]


#TODO: Better way to load file from file browser widget.
class PatterCenterDialog(QDialog):
    def __init__(self, parent, working_dir):
        super().__init__(parent)
        self.setting_path = path.join(working_dir, "Setting.txt")
        self.working_dir = working_dir
        self.pattern_index = 0
        self.ui = Ui_PatternCenterDialog()
        self.ui.setupUi(self)
        self.setupConnections()
        self.setupInitialSettings()
        self.setupCalibrationPatterns()

        self.fileBrowserOD = FileBrowser(FileBrowser.OpenDirectory)

    def setupInitialSettings(self):
        self.setting_file_dict = SettingFile(path.join(self.working_dir,"project_settings.txt"))
        try:
            self.pc = np.array(
                [
                    float(self.setting_file_dict.read("X star:")),
                    float(self.setting_file_dict.read("Y star:")),
                    float(self.setting_file_dict.read("Z star:")),
                ]
            )

        except:
            self.pc = np.array([0.5000, 0.3000, 0.5000])
        self.updatePCSpinBox()
        
        self.mp_paths = {}
        for i in range(1, 5):
            try:
                mp_path = self.setting_file_dict.read("Master pattern " + str(i) + ":")
                phase = mp_path.split("/").pop()
                self.mp_paths[phase] = mp_path
                self.ui.listPhases.addItem(phase)
            except:
                pass
        self.is_mp_paths_updated = True

    def setupConnections(self):
        self.ui.buttonAddPhase.clicked.connect(lambda: self.addPhase())
        self.ui.buttonRemovePhase.clicked.connect(lambda: self.removePhase())
        self.ui.toolButtonLeft.clicked.connect(lambda: self.previousPattern())
        self.ui.toolButtonRight.clicked.connect(lambda: self.nextPattern())
        self.ui.buttonTune.clicked.connect(lambda: self.refinePatternCenter())
        self.ui.buttonPlot.clicked.connect(lambda: self.plotData())
        self.ui.buttonBox.accepted.connect(lambda: self.saveAndExit())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())

    def previousPattern(self):
        if self.pattern_index > 0:
            self.pattern_index -= 1
            self.ui.counterLabel.setText(
                "Calibration Pattern: "+str(self.pattern_index+1)+"/"+str(self.nav_size)
                )
            self.plotData()
            
        else:
            pass

    #TODO: Make the program remeber the last phase and pc when moving between calibration patterns
    def nextPattern(self):
        if self.pattern_index < self.nav_size - 1:
            self.pattern_index += 1
            self.ui.counterLabel.setText(
                "Calibration Pattern: "+str(self.pattern_index+1)+"/"+str(self.nav_size)
                )
            self.plotData()
        else:
            pass

    def addPhase(self):
        if self.fileBrowserOD.getFile():
            mp_path = self.fileBrowserOD.getPaths()[0]
            phase = mp_path.split("/").pop()
            self.fileBrowserOD.setDefaultDir(mp_path[0 : -len(phase) - 1])
            if phase not in self.mp_paths.keys():
                self.mp_paths[phase] = mp_path
                self.ui.listPhases.addItem(phase)
                self.is_mp_paths_updated = True

    def removePhase(self):
        self.mp_paths.pop(str(self.ui.listPhases.currentItem().text()))
        self.ui.listPhases.takeItem(self.ui.listPhases.currentRow())
        self.is_mp_paths_updated = True

    def updatePCSpinBox(self):
        self.ui.spinBoxX.setValue(self.pc[0])
        self.ui.spinBoxY.setValue(self.pc[1])
        self.ui.spinBoxZ.setValue(self.pc[2])

    def updatePCArrayFromSpinBox(self):
        self.pc[0] = self.ui.spinBoxX.value()
        self.pc[1] = self.ui.spinBoxY.value()
        self.pc[2] = self.ui.spinBoxZ.value()

    def setupCalibrationPatterns(self):
        self.s_cal = kp.load(self.setting_path)
        sig_shape = self.s_cal.axes_manager.signal_shape[::-1]
        self.nav_size = self.s_cal.axes_manager.navigation_size
        self.pcs = np.zeros(self.nav_size)

        try:
            self.s_cal.detector["shape"] = self.s_cal.axes_manager.signal_shape[::-1]
            self.s_cal.detector = kp.detectors.EBSDDetector(**self.s_cal.detector)
        except:
            print("setupCalibrationPatterns has an error!")

        self.s_cal.remove_static_background()
        self.s_cal.remove_dynamic_background()

        #TODO: Why does only BRUKER convension work?
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
        self.ui.MplWidget.canvas.ax.imshow(self.s_cal.data[0], cmap="gray")

    def refinePatternCenter(self):
        self.updatePCArrayFromSpinBox()
        pattern = self.s_cal.data[self.pattern_index]
        self.pc = pcopt.optimize(pattern, self.indexer, self.pc)
        self.updatePCSpinBox()
        self.plotData()

    def retrieveMPData(self):
        mp_dict = {}
        for name, h5path in self.mp_paths.items():
            mp_i = kp.load(
                path.join(h5path, str(f"{name}_mc_mp_20kv.h5")),
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
        self.updatePCArrayFromSpinBox()

        #Checks which phase to use from list of phases
        try:
            phase_chosen = self.ui.listPhases.currentItem().text()
        except:
            phase_chosen = self.mp_paths.keys()[0]

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
        for name in self.mp_paths.keys():
            geosim_dict[name] = self.simulator_dict[name].on_detector(detector, rot)

        #Draws pattern in MplWidget 
        pattern_image_array = self.s_cal.data[self.pattern_index]
        self.ui.MplWidget.canvas.ax.clear()
        self.ui.MplWidget.canvas.ax.axis("off")
        self.ui.MplWidget.canvas.ax.imshow(pattern_image_array, cmap="gray")
        lines, zone_axes, zone_axes_labels = geosim_dict[phase_chosen].as_collections(
            0,
            zone_axes=True,
            zone_axes_labels=True,
            zone_axes_labels_kwargs=dict(fontsize=12),
        ) #TODO: How does this even work?

        pc_x, pc_y = len(pattern_image_array)*self.pc[0], len(pattern_image_array[0])*self.pc[1]
        self.ui.MplWidget.canvas.ax.plot(pc_x, pc_y, marker="*", markersize=12, color="gold")
        self.ui.MplWidget.canvas.ax.add_collection(lines)
        self.ui.MplWidget.canvas.draw()

        #Updates misfit label
        self.ui.labelMisfit.setText("Misfit(°): "+str(round(data["fit"][-1][0], 4)))

    #TODO: Save average pattern center from calibration patterns
    def saveAndExit(self):
        self.updatePCArrayFromSpinBox()
        self.setting_file_dict.write("X star:", str(self.pc[0]))
        self.setting_file_dict.write("Y star:", str(self.pc[1]))
        self.setting_file_dict.write("Z star:", str(self.pc[2]))
           
        for i in range(1, 5):
            try:
                self.setting_file_dict.remove("Master pattern " + str(i + 1) + ":")
            except:
                pass
        for i, path in enumerate(self.mp_paths.values()):
            self.setting_file_dict.write("Master pattern " + str(i + 1) + ":", path)
        
        self.setting_file_dict.save()
        self.close()
