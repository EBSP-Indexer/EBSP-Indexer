from os import path
import kikuchipy as kp
from PySide6.QtCore import QDir
from PySide6.QtWidgets import QDialog, QApplication
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
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
    FCC = ["ni", "al", "austenite", "cu"]
    BCC = ["ferrite"]
    if phase.lower() in FCC:
        return [[1, 1, 1], [2, 0, 0], [2, 2, 0], [3, 1, 1]]
    elif phase.lower() in BCC:
        return [[0, 1, 1], [0, 0, 2], [1, 1, 2], [0, 2, 2]]

def fig2img(fig):
    """Convert a Matplotlib figure to a PIL Image and return it"""
    import io
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img

class PatterCenterDialog(QDialog):

    def __init__(self, working_dir="/Users/olavletholsen/EBSD-data/DI-dataset/Test1/1"):
        super().__init__()
        self.setting_path = path.join(working_dir, "Setting.txt")
        self.working_dir = working_dir
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
        self.ui.buttonBox.accepted.connect(lambda: self.saveAndExit())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())
        self.ui.buttonTune.clicked.connect(lambda: self.refinePatternCenter())
        self.ui.buttonAddPhase.clicked.connect(lambda: self.addPhase())
        self.ui.buttonRemovePhase.clicked.connect(lambda: self.removePhase())

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

    def setupCalibrationPatterns(self):
        self.s_cal = kp.load(self.setting_path)
        self.s_cal.remove_static_background()
        self.s_cal.remove_dynamic_background()

    def plotData(self):
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

        ref = ref_dict["ni"]

        sig_shape = self.s_cal.axes_manager.signal_shape[::-1]
        indexer = ebsd_index.EBSDIndexer(vendor="KIKUCHIPY", sampleTilt=70, camElev=0, patDim=sig_shape)

        data, *_ = indexer.index_pats(self.s_cal.data.reshape((-1,) + sig_shape), PC=self.pc)
        rot = Rotation(data[-1]["quat"])
        detector = kp.detectors.EBSDDetector(sig_shape, sample_tilt=70, pc=self.pc)
        simulator = kp.simulations.KikuchiPatternSimulator(ref)
        sim = simulator.on_detector(detector, rot)

        pat = sim.plot(pattern=self.s_cal.data[0], return_figure=True, zone_axes_labels=False)
        self.ui.MplWidget.canvas.ax.imshow(fig2img(pat))
        self.ui.MplWidget.canvas.draw()


    def refinePatternCenter(self):
        sig_shape = self.s_cal.axes_manager.signal_shape[::-1]
        indexer = ebsd_index.EBSDIndexer(vendor="KIKUCHIPY", sampleTilt=70, camElev=0, patDim=sig_shape)
        self.pc = pcopt.optimize(self.s_cal.data.reshape((-1,) + sig_shape), indexer, self.pc)
        self.updatePCSpinBox()
        self.ui.labelMisfit.setText("Misfit(°): "+str(0.124))
        self.plotData()

    def saveAndExit(self):
        self.sf.write("X star:", str(self.ui.spinBoxX.value()))
        self.sf.write("Y star:", str(self.ui.spinBoxY.value()))
        self.sf.write("Z star:", str(self.ui.spinBoxZ.value()))

        for i in range(1, 5):
            try:
                self.sf.remove("Master pattern "+str(i+1)+':')
            except:
                pass
        for i, path in enumerate(self.mpPaths.values()):
            self.sf.write("Master pattern "+str(i+1)+':', path)

        self.sf.save()
        self.close()