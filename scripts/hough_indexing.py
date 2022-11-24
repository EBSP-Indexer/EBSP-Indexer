from os import path, mkdir
import json
from PySide6.QtCore import QThreadPool
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from utils.setting_file import SettingFile

from utils.filebrowser import FileBrowser
from utils.worker import Worker
from ui.ui_hi_setup import Ui_HISetupDialog

import kikuchipy as kp
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import warnings
from h5py import File
from orix import io, plot
from orix.crystal_map import CrystalMap, create_coordinate_arrays, PhaseList
from orix.quaternion import Rotation
from orix.vector import Vector3d
from pyebsdindex import ebsd_index

# Ignore warnings to avoid crash with integrated console
warnings.filterwarnings("ignore")


class HiSetupDialog(QDialog):
    SG_NUM_TO_PROXY = {"225": "FCC", "227": "FCC", "229": "BCC"}

    def __init__(self, parent, pattern_path=None):
        super().__init__(parent)
        self.threadPool = QThreadPool.globalInstance()
        self.console = parent.console
        self.pattern_path = pattern_path
        self.pattern_name = path.splitext(path.basename(pattern_path))[0]
        self.working_dir = path.dirname(pattern_path)

        self.ui = Ui_HISetupDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{self.windowTitle()} - {self.pattern_path}")
        self.fileBrowserOD = FileBrowser(FileBrowser.OpenDirectory)

        self.load_pattern()
        self.setupInitialSettings()
        self.setupBinningShapes()

        self.setupConnections()
        self.checkPhaseList()

        # self.phases = []
        # self.lat_param = []
        self.space_groups = []
        self.phase_proxys = []
        self.xmap = None
        self.data = None

        # Matplotlib configuration
        plt.rcParams.update({"font.size": 20})
        self.savefig_kwds = dict(pad_inches=0, bbox_inches="tight", dpi=150)

    def setupInitialSettings(self):
        # matplotlib settings
        mpl.use("agg")
        self.savefig_kwargs = dict(bbox_inches="tight", pad_inches=0, dpi=150)

        # standard dictionary indexing kwargs
        self.di_kwargs = dict(metric="ncc", keep_n=20)

        # read current setting from project_settings.txt, advanced_settings.txt
        self.setting_file = SettingFile(
            path.join(self.working_dir, "project_settings.txt")
        )
        self.program_settings = SettingFile("advanced_settings.txt")

        # PC convention, default is TSL
        try:
            self.convention = self.setting_file.read("Convention")
        except:
            self.convention = self.program_settings.read("Convention")

        try:
            self.pc = np.array(
                [
                    float(self.setting_file.read("X star")),
                    float(self.setting_file.read("Y star")),
                    float(self.setting_file.read("Z star")),
                ]
            )

            if self.convention == "TSL":
                self.pc[1] = 1 - self.pc[1]
        except:
            self.pc = np.array([0.400, 0.200, 0.400])

        self.update_pc_spinbox()
        self.ui.comboBoxConvention.setCurrentText(self.convention)

        try:
            self.colors = json.loads(self.program_settings.read("Colors"))
        except:
            self.colors = ['lime', 'r', 'b', 'yellow',]

        try:
            self.colors = json.loads(self.program_settings.read("Colors"))
        except:
            self.colors = [
                "lime",
                "r",
                "b",
                "yellow",
            ]

        if self.program_settings.read("Lazy Loading") == "False":
            self.ui.checkBoxLazy.setChecked(False)

        self.mpPaths = {}
        i = 1
        while True:
            try:
                mpPath = self.setting_file.read("Master pattern " + str(i))
                phase = mpPath.split("/").pop()
                self.mpPaths[phase] = mpPath
                self.ui.listWidgetPhase.addItem(phase)
                i += 1
            except:
                break

    def update_pc_spinbox(self):
        self.ui.patternCenterX.setValue(self.pc[0])
        self.ui.patternCenterZ.setValue(self.pc[2])
        if self.convention == "BRUKER":
            self.ui.patternCenterY.setValue(self.pc[1])
        elif self.convention == "TSL":
            self.ui.patternCenterY.setValue(1 - self.pc[1])

    def update_pc_array_from_spinbox(self):
        self.pc[0] = self.ui.patternCenterX.value()
        self.pc[2] = self.ui.patternCenterZ.value()
        if self.convention == "BRUKER":
            self.pc[1] = self.ui.patternCenterY.value()
        elif self.convention == "TSL":
            self.pc[1] = 1 - self.ui.patternCenterY.value()

    def update_pc_convention(self):
        self.convention = self.ui.comboBoxConvention.currentText()
        self.update_pc_spinbox()

    def addPhase(self):
        if self.fileBrowserOD.getFile():
            mpPath = self.fileBrowserOD.getPaths()[0]
            phase = mpPath.split("/").pop()
            self.fileBrowserOD.setDefaultDir(mpPath[0 : -len(phase) - 1])

            if phase not in self.mpPaths.keys():
                self.mpPaths[phase] = mpPath
                self.ui.listWidgetPhase.addItem(phase)
        self.checkPhaseList()

    def removePhase(self):
        self.mpPaths.pop(str(self.ui.listWidgetPhase.currentItem().text()))
        self.ui.listWidgetPhase.takeItem(self.ui.listWidgetPhase.currentRow())
        self.checkPhaseList()

    def setupConnections(self):
        self.ui.buttonBox.accepted.connect(lambda: self.run_hough_indexing())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())

        self.ui.pushButtonAddPhase.clicked.connect(lambda: self.addPhase())
        self.ui.pushButtonRemovePhase.clicked.connect(lambda: self.removePhase())

        self.ui.comboBoxConvention.currentTextChanged.connect(
            lambda: self.update_pc_convention()
        )

        self.ui.horizontalSliderRho.valueChanged.connect(lambda: self.updateRho())

    def getOptions(self) -> dict:
        return {
            "binning": self.ui.comboBoxBinning.currentText(),
            "bands": self.ui.spinBoxBands.value(),
            "rho": self.ui.horizontalSliderRho.value(),
            "phase_list": self.ui.listWidgetPhase.selectedItems(),
            "lazy": self.ui.checkBoxLazy.isChecked(),
            "quality": [
                self.ui.checkBoxQuality.isChecked(),
                self.generate_combined_map,
            ],
            "phase": [self.ui.checkBoxPhase.isChecked(), self.generate_phase_map],
            "orientation": [
                self.ui.checkBoxOrientation.isChecked(),
                self.generate_orientation_colour,
            ],
        }

    def updateRho(self):
        self.ui.labelRho.setText(f"{self.ui.horizontalSliderRho.value()}%")

    def checkPhaseList(self):
        ok_flag = False
        phase_map_flag = False
        add_phase_flag = True
        n_phases = self.ui.listWidgetPhase.count()
        if n_phases != 0:
            ok_flag = True
            if n_phases == 2:
                phase_map_flag = True
                add_phase_flag = False
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(ok_flag)
        self.ui.checkBoxPhase.setEnabled(phase_map_flag)
        self.ui.checkBoxPhase.setChecked(phase_map_flag)
        self.ui.pushButtonAddPhase.setEnabled(add_phase_flag)

    def setupBinningShapes(self):
        self.sig_shape = self.s.axes_manager.signal_shape[::-1]
        self.bin_shapes = np.array([])
        for num in range(10, self.sig_shape[0] + 1):
            if self.sig_shape[0] % num == 0:
                self.bin_shapes = np.append(self.bin_shapes, f"({num}, {num})")

        self.ui.comboBoxBinning.addItems(self.bin_shapes[::-1])

    def load_pattern(self):
        # Load pattern-file to get acquisition resolution
        try:
            self.s = kp.load(self.pattern_path, lazy=True)
        except Exception as e:
            raise e

    def hough_indexing(self):
        for i in range(1, 100):
            try:
                self.dir_out = path.join(self.working_dir, "hi_results" + str(i))
                mkdir(self.dir_out)
                break
            except FileExistsError:
                print(
                    f"Directory '{self.dir_out}' exists, will try to create directory '{self.dir_out[:-1] + str(i + 1)}'"
                )
        self.update_pc_array_from_spinbox()
        options = self.getOptions()
        self.phases = [phase for phase in self.mpPaths.keys()]
        self.set_phases_properties()
        self.rho_mask = (100.0 - options["rho"]) / 100.0
        self.number_bands = options["bands"]
        self.sig_shape = self.s.axes_manager.signal_shape[::-1]
        self.nav_shape = self.s.axes_manager.navigation_shape
        self.new_signal_shape = eval(options["binning"])
        self.s2 = self.s.rebin(new_shape=self.nav_shape + self.new_signal_shape)
        self.s2.rescale_intensity(dtype_out=np.uint8)
        self.s2.save(
            path.join(self.dir_out, "pattern.h5")
        )  # Not sure if the file must be converted to H5
        file_h5 = File(path.join(self.dir_out, "pattern.h5"), mode="r")
        dset_h5 = file_h5["Scan 1/EBSD/Data/patterns"]
        print(
            f"Dataset has shape: {dset_h5.shape}"
        )  # Navigation dimension is flattened
        self.sig_shape = self.s2.axes_manager.signal_shape[::-1]
        sample_tilt = self.s2.detector.sample_tilt
        camera_tilt = self.s2.detector.tilt

        indexer = ebsd_index.EBSDIndexer(
            phaselist=self.phase_proxys,
            vendor="BRUKER",
            PC=self.pc,
            sampleTilt=sample_tilt,
            camElev=camera_tilt,
            rhoMaskFrac=self.rho_mask,
            nBands=self.number_bands,
            patDim=self.sig_shape,
        )

        print("Indexing ...")
        self.data = indexer.index_pats(patsin=dset_h5, verbose=1)
        # Verbose = 2 will crash because a Matplotlib GUI outside of the main thread will likely fail.

        # Generate CrystalMap from best match
        xy, _ = create_coordinate_arrays(
            shape=self.s2.axes_manager.navigation_shape[::-1],
            step_sizes=tuple(
                i.scale for i in self.s2.axes_manager.navigation_axes[::-1]
            ),
        )

        idx = -1
        self.xmap = CrystalMap(
            rotations=Rotation(self.data[0][idx]["quat"]),
            phase_id=self.data[0][idx]["phase"],
            x=xy["x"],
            y=xy["y"],
            phase_list=PhaseList(names=self.phases, space_groups=self.space_groups),
            prop=dict(
                pq=self.data[0][idx]["pq"],
                cm=self.data[0][idx]["cm"],
                fit=self.data[0][idx]["fit"],
                nmatch=self.data[0][idx]["nmatch"],
                matchattempts0=self.data[0][idx]["matchattempts"][:, 0],
                matchattempts1=self.data[0][idx]["matchattempts"][:, 1],
                totvotes=self.data[0][idx]["totvotes"],
            ),
            scan_unit="um",
        )
        io.save(path.join(self.dir_out, "xmap_hi.h5"), self.xmap)
        io.save(
            path.join(self.dir_out, "xmap_hi.ang"),
            self.xmap,
            image_quality_prop="pq",
            confidence_index_prop="cm",
            pattern_fit_prop="fit",
            extra_prop=["nmatch", "matchattempts0", "matchattempts1", "totvotes"],
        )
        print("Result was saved as xmap_hi.h5 and xmap_hi.ang")
        for key in ["quality", "phase", "orientation"]:
            optionEnabled, optionExecute = options[key]
            if optionEnabled:
                optionExecute()
        print(f"Finished indexing {self.pattern_name}")

    def run_hough_indexing(self):
        hi_worker = Worker(fn=self.hough_indexing, output=self.console)
        self.threadPool.start(hi_worker)

    def set_phases_properties(self):
        for ph in self.phases:
            mp = kp.load(path.join(self.mpPaths[ph], f"{ph}_mc_mp_20kv.h5"))
            try:
                space_group, phase_proxy = (
                    mp.phase.space_group.number,
                    self.SG_NUM_TO_PROXY[f"{mp.phase.space_group.number}"],
                )
            except Exception as e:
                print("Space group is not supported, only 225, 227, 229 is supported")
                raise e
            self.space_groups.append(space_group)
            self.phase_proxys.append(phase_proxy)

    def generate_combined_map(self):
        """
        Plot quality metrics for combined map
        """
        print("Generating quality metric for combined map ...")
        try:
            to_plot = ["pq", "cm", "fit", "nmatch", "matchattempts0", "totvotes"]
            fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(20, 10))
            for i, a in enumerate(ax.ravel()):
                arr = self.xmap.get_map_data(to_plot[i])
                im = a.imshow(arr)
                a.axis("off")
                fig.colorbar(im, ax=a, label=to_plot[i])
                plt.imsave(
                    path.join(self.dir_out, f"maps_{to_plot[i]}.png"),
                    arr,
                    cmap="gray",
                )
            fig.tight_layout()
            fig.savefig(path.join(self.dir_out, "maps_all.png"), **self.savefig_kwds)
        except Exception as e:
            raise e

    def generate_phase_map(self):
        """
        Plot phase map
        """
        print("Generating phase map ...")
        for i, ph in enumerate(self.phases):
            self.xmap.phases[ph].color = self.colors[i]
        try:
            fig = self.xmap.plot(return_figure=True, remove_padding=True)
            fig.savefig(path.join(self.dir_out, "maps_phase.png"), **self.savefig_kwds)
        except Exception as e:
            raise e

    def generate_orientation_colour(self):
        """
        Plot orientation colour key
        """
        print("Generating orientation-colored map ...")
        try:
            ckey = plot.IPFColorKeyTSL(
                self.xmap.phases[0].point_group, direction=Vector3d((0, 0, 1))
            )
            fig = ckey.plot(return_figure=True)
            fig.savefig(
                path.join(self.dir_out, "orientation_colour_key.png"),
                **self.savefig_kwds,
            )

            rgb_all = np.zeros((self.xmap.size, 3))
            for i, phase in self.xmap.phases:
                if i != -1:
                    rgb_i = ckey.orientation2color(self.xmap[phase.name].orientations)
                    rgb_all[self.xmap.phase_id == i] = rgb_i

                fig = self.xmap.plot(rgb_all, remove_padding=True, return_figure=True)
                fig.savefig(
                    path.join(self.dir_out, "maps_ipfz.png"), **self.savefig_kwds
                )
        except Exception as e:
            raise e
