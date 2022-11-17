from os import path, mkdir
from PySide6.QtCore import QThreadPool
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from utils.setting_file import SettingFile

from utils.filebrowser import FileBrowser
from utils.worker import Worker
from ui.ui_hi_setup import Ui_HISetupDialog

import kikuchipy as kp
import matplotlib.pyplot as plt
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

    PHASE_PARAMETERS = {
        "al": (0.404, 225, "FCC"),
        "austenite": (0.3595, 225, "FCC"),
        "ferrite": (0.28684, 229, "BCC"),
        "ni": (0.35236, 225, "FCC"),
        "si": (0.543070, 227, "FCC"),
        "ti_beta": (0.33065, 229, "BCC"),
    }

    def __init__(self, parent, pattern_path=None):
        super().__init__(parent)
        self.threadPool = QThreadPool.globalInstance()
        self.pattern_path = pattern_path
        self.pattern_name = path.splitext(path.basename(pattern_path))[0]
        self.working_dir = path.dirname(pattern_path)

        self.ui = Ui_HISetupDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{self.windowTitle()} - {self.pattern_path}")
        self.fileBrowserOD = FileBrowser(FileBrowser.OpenDirectory)

        self.setupInitialSettings()

        self.setupConnections()
        self.checkPhaseList()

        self.phases = []
        self.lat_param = []
        self.space_groups = []
        self.phase_proxys = []
        self.xmap = None
        self.data = None

        # Matplotlib configuration
        plt.rcParams.update({"font.size": 20})
        self.savefig_kwds = dict(pad_inches=0, bbox_inches="tight", dpi=150)

    def setupInitialSettings(self):
        self.setting_file = SettingFile(path.join(self.working_dir, "project_settings.txt"))
        self.program_settings = SettingFile("advanced_settings.txt")

        # PC convention, default is TSL
        try:
            self.convention = self.setting_file.read("Convention")
        except:
            self.convention = self.program_settings.read("Convetion")
        else:
            self.convention = "TSL"

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
            self.pc = np.array([0.000, 0.000, 0.000])
    

        self.updatePCpatternCenter()

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

    def updatePCpatternCenter(self):
        self.ui.patternCenterX.setValue(self.pc[0])
        self.ui.patternCenterZ.setValue(self.pc[2])
        if self.convention == "BRUKER":
            self.ui.patternCenterY.setValue(self.pc[1])
        elif self.convention == "TSL":
            self.ui.patternCenterY.setValue(1-self.pc[1])

    def updatePCArrayFrompatternCenter(self):
        self.pc[0] = self.ui.patternCenterX.value()
        self.pc[2] = self.ui.patternCenterZ.value()
        if self.convention == "BRUKER":
            self.pc[1] = self.ui.patternCenterY.value()
        elif self.covention == "TSL":
            self.pc[1] = 1 - self.ui.patternCenterY.value()
            
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

    def getOptions(self) -> dict:
        return {
            "phase_list": self.ui.listWidgetPhase.selectedItems(),
            "lazy": self.ui.checkBoxLazy.isChecked(),
            "pre": [self.ui.checkBoxPre.isChecked(), self.generate_pre_maps],
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

    def checkPhaseList(self):
        flag = False
        if self.ui.listWidgetPhase.count() != 0:
            flag = True
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(flag)
        print()  
        print(self.mpPaths)

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

        self.updatePCArrayFrompatternCenter()
        options = self.getOptions()
        self.phases = [phase for phase, _ in self.mpPaths.items()]
        self.set_phases_properties()
        try:
            self.s = kp.load(filename=self.pattern_path, lazy=options["lazy"])
        except Exception as e:
            raise e
        optionEnabled, optionExecute = options["pre"]
        if optionEnabled:
            optionExecute()
        self.sig_shape = self.s.axes_manager.signal_shape[::-1]
        self.s.save(
            path.join(self.dir_out, "pattern.h5")
        )  # Not sure if the file must be converted to H5
        file_h5 = File(path.join(self.dir_out, "pattern.h5"), mode="r")
        dset_h5 = file_h5["Scan 1/EBSD/Data/patterns"]
        print(f"Dataset has shape: {dset_h5.shape}")  # Navigation dimension is flattened

        sample_tilt = self.s.detector.sample_tilt
        camera_tilt = self.s.detector.tilt

        indexer = ebsd_index.EBSDIndexer(
            phaselist=self.phase_proxys,
            vendor="BRUKER",
            PC=self.pc,
            sampleTilt=sample_tilt,
            camElev=camera_tilt,
            patDim=self.sig_shape,
        )

        print("Indexing ...")
        self.data = indexer.index_pats(patsin=dset_h5, verbose=1)
        # Verbose = 2 will crash because a Matplotlib GUI outside of the main thread will likely fail.

        # Generate CrystalMap from best match
        xy, _ = create_coordinate_arrays(
            shape=self.s.axes_manager.navigation_shape[::-1],
            step_sizes=tuple(
                i.scale for i in self.s.axes_manager.navigation_axes[::-1]
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
        #self.hough_indexing()
        # Pass the function to execute
        hi_worker = Worker(lambda: self.hough_indexing())
        # # Execute
        self.threadPool.start(hi_worker)

    def set_phases_properties(self):
        for phase in self.phases:
            a, space_group, phase_proxy = self.PHASE_PARAMETERS[phase]
            self.lat_param.append(a)
            self.space_groups.append(space_group)
            self.phase_proxys.append(phase_proxy)

    def generate_pre_maps(self):
        print("Generating maps of input data ...")
        mean_intensity = self.s.mean(axis=(2, 3))
        plt.imsave(
            path.join(self.dir_out, "mean_intensity.png"),
            mean_intensity.data,
            cmap="gray",
        )

        vbse_gen = kp.generators.VirtualBSEGenerator(self.s)
        red = (2, 1)
        green = (2, 2)
        blue = (2, 3)
        vbse_rgb_img = vbse_gen.get_rgb_image(r=red, g=green, b=blue)
        vbse_rgb_img.change_dtype("uint8")
        plt.imsave(path.join(self.dir_out, "vbse_rgb.png"), vbse_rgb_img.data)

        iq = self.s.get_image_quality()
        adp = self.s.get_average_neighbour_dot_product_map()
        plt.imsave(path.join(self.dir_out, "maps_iq.png"), iq, cmap="gray")
        plt.imsave(path.join(self.dir_out, "maps_adp.png"), adp, cmap="gray")

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
        try:
            fig = self.xmap.plot(return_figure=True, remove_padding=True)
            fig.savefig(
                path.join(self.dir_out, "maps_phase.png"), **self.savefig_kwds
            )
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


