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

from scripts.filebrowser import FileBrowser
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

class PatterCenterDialog(QDialog):

    def __init__(self, working_dir):
        super().__init__()
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
        self.sf = SettingFile("project_settings.txt")
        self.pc = np.array([
            float(self.sf.read("X star:")), 
            float(self.sf.read("Y star:")), 
            float(self.sf.read("Z star:"))
        ])
        self.updatePCSpinBox()
        
        self.mpPaths = {}
        for i in range(1, 5):
            try:
                mpPath = self.sf.read("Master pattern "+str(i)+':')
                phase = mpPath.split('/').pop()
                self.mpPaths[phase] = mpPath
                self.ui.listPhases.addItem(phase)
            except:
                pass

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
        else:
            pass

    def nextPattern(self):
        if self.pattern_index < self.nav_size-1:
            self.pattern_index += 1
        else:
            pass

    def addPhase(self):
        if self.fileBrowserOD.getFile():
            mpPath = self.fileBrowserOD.getPaths()[0]
            phase = mpPath.split("/").pop()
            self.fileBrowserOD.setDefaultDir(mpPath[0: -len(phase)-1])
            
            if phase not in self.mpPaths.keys():
                self.mpPaths[phase] = mpPath
                self.ui.listPhases.addItem(phase)
    
    def removePhase(self):
        self.mpPaths.pop(str(self.ui.listPhases.currentItem().text()))
        self.ui.listPhases.takeItem(self.ui.listPhases.currentRow())

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
        try:
            self.s_cal.detector["shape"] = self.s_cal.axes_manager.signal_shape[::-1]
            self.s_cal.detector = kp.detectors.EBSDDetector(**self.s_cal.detector)
        except:
            pass

        self.s_cal.remove_static_background()
        self.s_cal.remove_dynamic_background()
        
        self.indexer = ebsd_index.EBSDIndexer(
            phaselist=["FCC", "BCC"],
            vendor="bruker",
            sampleTilt=self.s_cal.detector.sample_tilt,
            camElev=self.s_cal.detector.tilt,
            patDim=sig_shape
        )

    def refinePatternCenter(self):
        self.updatePCArrayFromSpinBox()
        sig_shape = self.s_cal.axes_manager.signal_shape[::-1]
        pattern = self.s_cal.data[self.pattern_index]
        indexer = ebsd_index.EBSDIndexer(
            phaselist=["FCC", "BCC"],
            vendor="bruker",
            sampleTilt=self.s_cal.detector.sample_tilt,
            camElev=0,
            patDim=sig_shape
        )
        self.pc = pcopt.optimize(pattern, indexer, self.pc)
        self.updatePCSpinBox()

        data = indexer.index_pats(pattern, PC=self.pc)
        try:
            self.ui.labelMisfit.setText("Misfit(°): "+str(data["fit"][-1][self.pattern_index]))
        except:
            self.ui.labelMisfit.setText("Misfit(°): Coming in kikuchipy version 0.7")
        self.plotData()

    def plotData(self):
        self.updatePCArrayFromSpinBox()
        try:
            phase_chosen = self.ui.listPhases.currentItem().text()
        except:
            phase_chosen = self.mpPaths.keys[0]

        self.mp_dict = {}
        for name, h5path in self.mpPaths.items():
            mp_i = kp.load(
                path.join(h5path, str(f"{name}_mc_mp_20kv.h5")),
                projection="lambert",
                energy=self.s_cal.metadata.Acquisition_instrument.SEM.beam_energy,
                hemisphere="upper"
            )
            self.mp_dict[name] = mp_i

        ref_dict = {}
        for name in self.mpPaths.keys():
            ref_i = ReciprocalLatticeVector(phase=self.mp_dict[name].phase, hkl=find_hkl(name))
            ref_i = ref_i.symmetrise().unique()
            ref_dict[name] = ref_i

        simulator_dict = {}
        for name in self.mpPaths.keys():
            simulator_dict[name] = kp.simulations.KikuchiPatternSimulator(ref_dict[name])

        detector = kp.detectors.EBSDDetector(
            shape=self.s_cal.detector.shape,
            sample_tilt=self.s_cal.detector.sample_tilt,
            tilt=self.s_cal.detector.tilt,
            pc=self.pc,
            convention=self.indexer.vendor
        )

        data = self.indexer.index_pats(self.s_cal.data[self.pattern_index], PC=self.pc)[0]
        rot = Rotation(data["quat"][-1]) * Rotation.from_axes_angles([0, 0, -1], np.pi / 2)

        geosim_dict = {}
        for name in self.mpPaths.keys():
            geosim_dict[name] = simulator_dict[name].on_detector(detector, rot)

        self.ui.MplWidget.canvas.ax.clear()
        self.ui.MplWidget.canvas.ax.imshow(self.s_cal.data[self.pattern_index], cmap="gray")
        lines, zone_axes, zone_axes_labels = geosim_dict[phase_chosen].as_collections(
            zone_axes=True,
            zone_axes_labels=True,
            zone_axes_labels_kwargs=dict(fontsize=12),
        )

        self.ui.MplWidget.canvas.ax.add_collection(lines)
        self.ui.MplWidget.canvas.draw()

    def saveAndExit(self):
        self.sf.write("X star:", str(self.pc[0]))
        self.sf.write("Y star:", str(self.pc[1]))
        self.sf.write("Z star:", str(self.pc[2]))

        for i in range(1, 5):
            try:
                self.sf.remove("Master pattern "+str(i+1)+':')
            except:
                pass
        for i, path in enumerate(self.mpPaths.values()):
            self.sf.write("Master pattern "+str(i+1)+':', path)

        self.sf.save()
        self.close()