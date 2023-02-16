from os import path, mkdir
from datetime import date
import json
import warnings

from PySide6.QtCore import QThreadPool
from PySide6.QtWidgets import QDialog, QDialogButtonBox
import kikuchipy as kp
from kikuchipy.signals.ebsd import EBSD, LazyEBSD
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from orix import io, plot
from orix.crystal_map import CrystalMap, create_coordinate_arrays, PhaseList
from orix.quaternion import Rotation
from orix.vector import Vector3d
from pyebsdindex.ebsd_index import EBSDIndexer

from utils import SettingFile, FileBrowser, sendToJobManager
from ui.ui_hi_setup import Ui_HISetupDialog

# Ignore warnings to avoid crash with integrated console
warnings.filterwarnings("ignore")


class HiSetupDialog(QDialog):
    SG_NUM_TO_PROXY = {"225": "FCC", "227": "FCC", "229": "BCC"}

    def __init__(self, parent, pattern_path=None):
        super().__init__(parent)
        self.threadPool = QThreadPool.globalInstance()
        self.console = self.parentWidget().console
        self.pattern_path = pattern_path
        self.pattern_name = path.basename(pattern_path)
        self.working_dir = path.dirname(pattern_path)

        self.ui = Ui_HISetupDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{self.windowTitle()} - {self.pattern_path}")
        self.fileBrowserOF = FileBrowser(
            mode=FileBrowser.OpenFile, filter_name="Hierarchical Data Format (*.h5);"
        )

        # Load pattern-file to get acquisition resolution
        try:
            s_preview: LazyEBSD = kp.load(self.pattern_path, lazy=True)
        except Exception as e:
            raise e

        self.setupInitialSettings()
        self.setupBinningShapes(s_preview)

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
            self.pc = np.array([0.500, 0.200, 0.500])

        self.update_pc_spinbox()
        self.ui.comboBoxConvention.setCurrentText(self.convention)

        try:
            self.colors = json.loads(self.program_settings.read("Colors"))
        except:
            self.colors = [
                "lime",
                "r",
                "b",
                "yellow",
            ]

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

        self.mp_paths = {}
        i = 1
        while True:
            try:
                mpPath = self.setting_file.read(f"Master pattern {i}")
                phase = path.dirname(mpPath).split("/").pop()
                self.mp_paths[phase] = mpPath
                self.ui.listWidgetPhase.addItem(phase)
                i += 1
            except:
                break

        self.getPhases()

    # TODO
    # Write to use more parameters instead of self
    def save_project_settings(self, binning_shape):
        self.setting_file.delete_all_entries()  # clean up initial dictionary

        ### Sample parameters
        for i, mppath in enumerate(self.mp_paths.values(), 1):
            self.setting_file.write(f"Master pattern {i}", mppath)
        self.setting_file.write("Convention", self.convention)
        self.update_pc_array_from_spinbox()
        if self.convention == "BRUKER":
            self.setting_file.write("Y star", f"{self.pc[1]}")
        elif self.convention == "TSL":
            self.setting_file.write("Y star", f"{1-self.pc[1]}")
        self.setting_file.write("X star", f"{self.pc[0]}")
        self.setting_file.write("Z star", f"{self.pc[2]}")
        self.setting_file.write("Binning", f"({binning_shape})")
        self.setting_file.save()
        print("Project settings saved")

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
        if self.fileBrowserOF.getFile():
            mpPath = self.fileBrowserOF.getPaths()[0]
            phase = path.dirname(mpPath).split("/").pop()
            self.fileBrowserOF.setDefaultDir(mpPath[0 : -len(phase) - 1])

            if phase not in self.mp_paths.keys():
                self.mp_paths[phase] = mpPath
                self.ui.listWidgetPhase.addItem(phase)
        self.getPhases()
        self.checkPhaseList()

    def removePhase(self):
        self.mp_paths.pop(str(self.ui.listWidgetPhase.currentItem().text()))
        self.ui.listWidgetPhase.takeItem(self.ui.listWidgetPhase.currentRow())
        self.getPhases()
        self.checkPhaseList()

    def getPhases(self):
        lw = self.ui.listWidgetPhase
        self.phases = [lw.item(x).text() for x in range(lw.count())]

    def setupConnections(self):
        self.ui.buttonBox.accepted.connect(lambda: self.run_hough_indexing())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())

        self.ui.pushButtonAddPhase.clicked.connect(lambda: self.addPhase())
        self.ui.pushButtonRemovePhase.clicked.connect(lambda: self.removePhase())

        self.ui.comboBoxConvention.currentTextChanged.connect(
            lambda: self.update_pc_convention()
        )

        self.ui.horizontalSliderRho.valueChanged.connect(
            lambda: self.ui.labelRho.setText(f"{self.ui.horizontalSliderRho.value()}%")
        )

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
            "convention": self.ui.comboBoxConvention.currentText(),
        }

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

    def setupBinningShapes(self, signal: LazyEBSD):
        sig_shape = signal.axes_manager.signal_shape[::-1]
        bin_shapes = np.array([])
        for num in range(10, sig_shape[0] + 1):
            if sig_shape[0] % num == 0:
                bin_shapes = np.append(bin_shapes, f"({num}, {num})")
        self.ui.comboBoxBinning.addItems(bin_shapes[::-1])

    # TODO Remove extra print statements
    def hough_indexing(self):
        # Load pattern-file
        options = self.getOptions()
        self.update_pc_array_from_spinbox()
        self.phases = [phase for phase in self.mp_paths.keys()]
        self.set_phases_properties()
        self.rho_mask = (100.0 - options["rho"]) / 100.0
        self.number_bands = options["bands"]
        binning_shape = eval(options["binning"])
        self.save_project_settings(binning_shape)

        print(f"Initializing hough indexing of {self.pattern_name} ...")
        try:
            s = kp.load(self.pattern_path, lazy=options.get("lazy"))
        except Exception as e:
            raise e
        s.detector.pc = self.pc
        sig_shape = s.axes_manager.signal_shape[::-1]
        nav_shape = s.axes_manager.navigation_shape[::-1]
        sample_tilt = s.detector.sample_tilt
        camera_tilt = s.detector.tilt
        print(f"Successfully loaded {self.pattern_name}")
        maps_iq = s.get_image_quality()
        original_sig_shape = None
        if sig_shape != binning_shape:
            print(f"Rebinning signal shape to {binning_shape} ...")
            original_sig_shape = sig_shape
            s = s.rebin(new_shape=nav_shape + binning_shape)
            s.rescale_intensity(dtype_out=np.uint8)
            sig_shape = s.axes_manager.signal_shape[::-1]

        indexer = EBSDIndexer(
            phaselist=self.phase_proxys,  # FCC, BCC or both
            vendor="BRUKER",
            PC=self.pc,
            sampleTilt=sample_tilt,
            camElev=camera_tilt,
            rhoMaskFrac=self.rho_mask,
            nBands=self.number_bands,
            patDim=sig_shape,
        )
        print("Indexing ...")
        data, *_ = indexer.index_pats(s.data.reshape(-1, *sig_shape), verbose=1)
        idx = -1
        xy, _ = create_coordinate_arrays(
            nav_shape,
            step_sizes=(s.axes_manager["y"].scale, s.axes_manager["x"].scale),
        )
        self.xmap = CrystalMap(
            rotations=Rotation(data[idx]["quat"]),
            phase_id=data[idx]["phase"],
            x=xy["x"],
            y=xy["y"],
            phase_list=PhaseList(names=self.phases, space_groups=self.space_groups),
            prop=dict(
                pq=data[idx]["pq"],  # Pattern quality
                cm=data[idx]["cm"],  # Confidence metric
                fit=data[idx]["fit"],  # Pattern fit
                nmatch=data[idx]["nmatch"],  # Number of detected bands matched
                matchattempts=data[idx]["matchattempts"],
                totvotes=data[idx]["totvotes"],
                iq=maps_iq.ravel(),
            ),
            scan_unit="um",
        )
        # io.save(path.join(self.dir_out, "xmap_hi.h5"), self.xmap)
        io.save(
            path.join(self.dir_out, "xmap_hi.ang"),
            self.xmap,
            image_quality_prop="pq",
            confidence_index_prop="cm",
            pattern_fit_prop="fit",
            extra_prop=["nmatch", "matchattempts", "totvotes"],
        )
        print("Result was saved as xmap_hi.ang")  # and xmap_hi.h5
        for key in ["quality", "phase", "orientation"]:
            optionEnabled, optionExecute = options.get(key)
            if optionEnabled:
                optionExecute()
        print("Logging results ...")
        create_log(
            self.dir_out,
            s,
            self.xmap,
            self.mp_paths,
            convention=options["convention"],
            original_signal_shape=original_sig_shape,
        )
        print(f"Finished indexing {self.pattern_name}")

    def run_hough_indexing(self):
        for i in range(1, 100):
            try:
                self.dir_out = path.join(self.working_dir, "hi_results" + str(i))
                mkdir(self.dir_out)
                break
            except FileExistsError:
                pass
        sendToJobManager(
            job_title=f"HI {self.pattern_name}",
            output_path=self.dir_out,
            listview=self.parentWidget().ui.jobList,
            func=self.hough_indexing,
            allow_cleanup=True,
            allow_logging=True
        )

    def set_phases_properties(self):
        for ph in self.phases:
            mp = kp.load(self.mp_paths[ph])
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
            to_plot = ["pq", "cm", "fit", "nmatch", "totvotes", "matchattempts"]
            fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(20, 10))
            for i, a in enumerate(ax.ravel()):
                a.axis("off")
                if i == 5:  # Currently not plotting matchattempts
                    break
                arr = self.xmap.get_map_data(to_plot[i])
                im = a.imshow(arr)
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
            self.bob
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


# TODO Add more Hough related properties, better way to sort?
def create_log(
    dir_out: str,
    signal: EBSD | LazyEBSD = None,
    xmap: CrystalMap = None,
    mp_paths: dict = None,
    pattern_center: np.ndarray = None,
    convention: str = "BRUKER",
    original_signal_shape: str = None,
):
    """
    Assumes convention is BRUKER for pattern center if none is given
    """

    log = SettingFile(path.join(dir_out, "hi_parameters.txt"))
    K = ["strs"]
    ### Time and date
    log.write("Date", f"{date.today()}\n")

    ### SEM parameters
    log.write("Microscope", signal.metadata.Acquisition_instrument.SEM.microscope)
    log.write(
        "Acceleration voltage",
        f"{signal.metadata.Acquisition_instrument.SEM.beam_energy} kV",
    )
    log.write("Sample tilt", f"{signal.detector.sample_tilt} degrees")
    log.write("Camera tilt", f"{signal.detector.tilt} degrees")
    log.write(
        "Working distance",
        signal.metadata.Acquisition_instrument.SEM.working_distance,
    )
    log.write("Magnification", signal.metadata.Acquisition_instrument.SEM.magnification)
    log.write(
        "Navigation shape (rows, columns)",
        signal.axes_manager.navigation_shape[::-1],
    )
    log.write("Signal shape (rows, columns)", signal.axes_manager.signal_shape[::-1])
    if original_signal_shape is not None:
        log.write("Original signal shape (rows, columns)", original_signal_shape)

    log.write("Step size", f"{signal.axes_manager[0].scale} um\n")

    ### HI parameteres

    log.write("kikuchipy version", kp.__version__)

    if mp_paths is not None:
        for i, mp_path in enumerate(mp_paths.values(), 1):
            log.write(f"Master pattern path {i}", mp_path)

    if pattern_center != None:
        displayed_pc = pattern_center
    else:
        if convention == "BRUKER":
            displayed_pc = signal.detector.pc_bruker()
        elif convention == "TSL":
            displayed_pc = signal.detector.pc_tsl()
    log.write("PC convention", f"{convention}")
    log.write("Pattern center (x*, y*, z*)", f"{displayed_pc[0]}")

    if len(xmap.phases.names) > 1:
        for i, ph in enumerate(xmap.phases.names, 1):
            phase_amount = xmap[f"{ph}"].size / xmap.size
            log.write(
                f"Phase {i}: {ph} [% ( # points)] ",
                f"{phase_amount:.1%}, ({xmap[f'{ph}'].size})",
            )

        not_indexed_percent = xmap["not_indexed"].size / xmap.size
        log.write(
            "Not indexed", f"{xmap['not_indexed'].size} ({not_indexed_percent:.1%})"
        )

    log.save()
