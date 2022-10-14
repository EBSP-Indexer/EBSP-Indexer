from cmath import phase
import os
from tkinter import E
from PySide6.QtWidgets import QDialog

from scripts.filebrowser import FileBrowser
from ui.ui_di_setup import Ui_DiSetupDialog

import kikuchipy as kp
import matplotlib.pyplot as plt
import numpy as np
from orix.quaternion import Rotation
from orix import io, sampling, plot

import hyperspy.api as hs
from time import time
import warnings
import gc

# from setting_file import SettingFile


class DiSetupDialog(QDialog):
    """
    Setup dialog box for Dictionary indexing
    """

    def __init__(self, working_dir, pattern_path="Pattern.dat"):
        super().__init__()

        # path for pattern to be indexed
        if pattern_path == "":
            self.pattern_path = os.path.join(working_dir, "Pattern.dat")
        else:
            self.pattern_path = pattern_path

        # working index
        self.working_dir = working_dir

        # master pattern index, as of now fixed and must be adjusted for every computer
        # TODO: read master pattern path from a settings file
        #self.sim_dir = "C:\EBSD data\kikuchipy\ebsd_simulations"

        # Defining phase dictionary
        # TODO: move point group dictionary to an external file that can be edited from GUI
        # TODO: check if we actually need this
        self.pg_dict = {
            "al": "m-3m",
            "austenite": "m-3m",
            "ferrite": "m-3m",
            "ni": "m-3m",
            "si": "m-3m",
            "ti_alpha": "6_mmm",  # 6/mmm
            "ti_beta": "m-3m",
        }

        # Dialog box ui setup
        self.ui = Ui_DiSetupDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{self.windowTitle()} - {self.pattern_path}")
        self.fileBrowserOD = FileBrowser(FileBrowser.OpenDirectory)
        self.setupConnections()

    def setupConnections(self):
        self.ui.buttonBox.accepted.connect(lambda: self.runDictionaryIndexing())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())
        self.ui.pushButtonBrowse.clicked.connect(lambda: self.setSaveDir())

    # read options from interactive elements in dialog box
    def getOptions(self) -> dict:
        return {
            "PC_x": float(self.ui.patternCenterX.text()),
            "PC_y": float(self.ui.patternCenterY.text()),
            "PC_z": float(self.ui.patternCenterZ.text()),
            "Phase": self.ui.listWidgetPhase.selectedItems(),
            "Refine": self.ui.checkBoxRefine.isChecked(),
            "Lazy": self.ui.checkBoxLazy.isChecked(),
        }

    def setSaveDir(self):
        if self.fileBrowserOD.getFile():
            self.sim_dir = self.fileBrowserOD.getPaths()[0]
            self.ui.lineEditPath.setText(self.sim_dir)

    def runDictionaryIndexing(self):

        # get options from input
        self.options = self.getOptions()

        #load selected EBSD pattern
        try:
            self.s = kp.load(self.pattern_path, lazy=self.options["Lazy"])
        except Exception as e:
            raise e

        

        # set pattern center values
        self.pc = (
            self.options["PC_x"],
            self.options["PC_y"],
            self.options["PC_z"],
        )

        # Get phase
        self.phases = [phase.text() for phase in self.options["Phase"]]
        print(self.phases)

        #Refinement
        self.refine = self.options["Refine"]
        
        # TODO: Settings that can be set as user input later
        self.savefig_kwargs = dict(bbox_inches="tight", pad_inches=0, dpi=150)
        self.new_signal_shape = (48, 48)
        self.disori = 2
        self.use_signal_mask = False
        self.n_per_iteration = None
        

        # Create folder for storing DI results in working directory
        i = 1
        while True:
            try:
                self.save_dir = os.path.join(self.working_dir, "di_results" + str(i))
                os.mkdir(self.save_dir)
                break
            except FileExistsError:
                print(
                    f"Directory '{self.save_dir}' exists, will try to create directory '{self.save_dir[:-1] + str(i + 1)}'"
                )
            i += 1

        # Read metadata from pattern file
        self.sem_md = self.s.metadata.Acquisition_instrument.SEM
        self.energy = self.sem_md.beam_energy
        self.sample_tilt = self.sem_md.Detector.EBSD.sample_tilt

        ### Dictionary indexing

        # Rebinning of signal
        self.nav_shape = self.s.axes_manager.navigation_shape
        self.s2 = self.s.rebin(new_shape=self.nav_shape + self.new_signal_shape)
        self.s2.rescale_intensity(dtype_out=np.uint8)

        # Define detector-sample geometry
        self.sig_shape = self.s2.axes_manager.signal_shape[::-1]

        self.detector = kp.detectors.EBSDDetector(
            shape=self.sig_shape,
            sample_tilt=self.sample_tilt,  # Degrees
            pc=self.pc,
            convention="tsl",  # Default is Bruker, TODO: let user choose convention
        )

        ### Create signal mask
        if self.use_signal_mask:
            self.signal_mask = ~kp.filters.Window("circular", self.sig_shape).astype(
                bool
            )

            p = self.s2.inav[0, 0].data
            fig, ax = plt.subplots(ncols=2, figsize=(10, 5))
            ax[0].imshow(p * self.signal_mask, cmap="gray")
            ax[0].set_title("Not used in matching")
            ax[1].imshow(p * ~self.signal_mask, cmap="gray")
            ax[1].set_title("Used in matching")
            fig.savefig(
                os.path.join(self.save_dir, "circular_mask_for_di.png"),
                **self.savefig_kwargs,
            )

        plt.close("all")

        ### Set up dictionary indexing parameters

        self.di_kwargs = dict(
            metric="ncc", keep_n=20, n_per_iteration=self.n_per_iteration
        )
        if self.use_signal_mask:
            self.di_kwargs["signal_mask"] = self.signal_mask

        ### Dictionaries for use with several phases
        # Master pattern dictionary
        self.mp = {}
        # Xmaps dictionary
        self.xmaps = {}
        # Refined xmaps dictionary
        self.xmaps_ref = {}

        for ph in self.phases:

            ###Load simulated master pattern
            self.file_mp = os.path.join(self.sim_dir, ph, f"{ph}_mc_mp_20kv.h5")
            self.mp[f"mp_{ph}"] = kp.load(
                self.file_mp,
                energy=self.energy,  # single energies like 10, 11, 12 etc. or a range like (10, 20)
                projection="lambert",  # stereographic, lambert
                hemisphere="both",  # north, south, both
            )

            ### Sample orientations

            self.rot = sampling.get_sample_fundamental(
                method="cubochoric",
                resolution=self.disori,
                point_group=self.mp[f"mp_{ph}"].phase.point_group,
            )

            ### Simulate one pattern to check the parameters. The master pattern sampling was implemented by Lars Lervik.

            self.sim = self.mp[f"mp_{ph}"].get_patterns(
                rotations=Rotation.from_euler(np.deg2rad([0, 0, 0])),
                # rotations=rot[0],
                detector=self.detector,
                energy=self.energy,  # Defined above
                compute=True,  # if False, sim.compute() must be called at a later time
            )

            fig, _ = self.detector.plot(
                pattern=self.sim.squeeze().data,
                draw_gnomonic_circles=True,
                coordinates="gnomonic",
                return_fig_ax=True,
            )

            fig.savefig(
                os.path.join(self.save_dir, f"pc_{ph}.png"), **self.savefig_kwargs
            )

            ### Generate dictionary

            self.sim_dict = self.mp[f"mp_{ph}"].get_patterns(
                rotations=self.rot,
                detector=self.detector,
                energy=self.energy,
                compute=False,
            )

            self.xmaps[f"xmap_{ph}"] = self.s2.dictionary_indexing(
                dictionary=self.sim_dict, **self.di_kwargs
            )
            self.xmaps[f"xmap_{ph}"].scan_unit = "um"

            ### Save results from DI for phase

            io.save(
                os.path.join(self.save_dir, f"di_results_{ph}.h5"),
                self.xmaps[f"xmap_{ph}"],
            )  # orix' HDF5
            io.save(
                os.path.join(self.save_dir, f"di_results_{ph}.ang"),
                self.xmaps[f"xmap_{ph}"],
            )  # .ang

            ### Inspect dictionary indexing results for phase

            fig = self.xmaps[f"xmap_{ph}"].plot(
                value=self.xmaps[f"xmap_{ph}"].scores[:, 0],
                colorbar=True,
                colorbar_label="Normalized cross correlation score",
                return_figure=True,
                cmap="gray",
            )

            fig.savefig(
                os.path.join(self.save_dir, f"ncc_{ph}.png"), **self.savefig_kwargs
            )

            ### Calculate and save orientation similairty map

            osm = kp.indexing.orientation_similarity_map(self.xmaps[f"xmap_{ph}"])

            fig = self.xmaps[f"xmap_{ph}"].plot(
                value=osm.ravel(),
                colorbar=True,
                colorbar_label="Orientation similarity",
                return_figure=True,
                cmap="gray",
            )

            fig.savefig(
                os.path.join(self.save_dir, f"osm_{ph}.png"), **self.savefig_kwargs
            )

            self.ckey = plot.IPFColorKeyTSL(self.mp[f"mp_{ph}"].phase.point_group)

            # Refinemenet kwargs
            self.ref_kw = dict(detector=self.detector, energy=self.energy, compute=True)

            if self.refine:

                ### Refine xmaps
                self.xmap_ref = self.s2.refine_orientation(
                    xmap=self.xmaps[f"xmap_{ph}"],
                    master_pattern=self.mp[f"mp_{ph}"],
                    trust_region=[1, 1, 1],
                    **self.ref_kw,
                )
                self.xmaps_ref[f"xmap_ref_{ph}"] = self.xmap_ref

                io.save(
                    os.path.join(self.save_dir, f"di_ref_results_{ph}.ang"),
                    self.xmaps_ref[f"xmap_ref_{ph}"],
                )  # .ang

                self.fig = self.xmaps_ref[f"xmap_ref_{ph}"].plot(
                    self.ckey.orientation2color(self.xmaps_ref[f"xmap_ref_{ph}"].orientations), remove_padding=True, return_figure=True
                )

                self.fig.savefig(
                    os.path.join(self.save_dir, f"ipf_ref{ph}.png"),
                    **self.savefig_kwargs,
                )

            self.fig = self.xmaps[f"xmap_{ph}"].plot(
                self.ckey.orientation2color(self.xmaps[f"xmap_{ph}"].orientations), remove_padding=True, return_figure=True
            )

            self.fig.savefig(
                os.path.join(self.save_dir, f"ipf_{ph}.png"), **self.savefig_kwargs
            )

            plt.close()
            del self.sim_dict
            gc.collect()
        
        
        if len(self.phases) > 1:

            self.cm = [self.xmaps[f"xmap_{ph}"] for ph in self.phases]

            #Merge xmaps from indexed phases

            self.xmap_merged = kp.indexing.merge_crystal_maps(
                crystal_maps = self.cm,
                mean_n_best = 1,
                scores_prop = "scores",
                simulation_indices_prop="simulation_indices",
            )

            self.colors = ["lime", "r", "b", "yellow"]

            for i in range(len(self.phases)):
                self.xmap_merged.phases[i].color = self.colors[i]
            
            io.save(os.path.join(self.save_dir, "di_results_merged.h5"), self.xmap_merged)  # orix' HDF5
            io.save(os.path.join(self.save_dir, "di_results_merged.ang"), self.xmap_merged)  # .ang

            ### Plot and save the normalized cross correlation score
            
            fig = self.xmap_merged.plot(
                value=self.xmap_merged.scores[:, 0],
                colorbar=True,
                colorbar_label="Normalized cross correlation score",
                return_figure=True,
                cmap="gray",
            )

            fig.savefig(os.path.join(self.save_dir, "ncc_merged.png"), **self.savefig_kwargs)

            ### Phase map

            fig = self.xmap_merged.plot(remove_padding=True, return_figure=True)
            fig.savefig(os.path.join(self.save_dir, "phase_map.png"), **self.savefig_kwargs)

            #TODO: NCC histogram

            if self.refine:
                self.cm_ref = [self.xmaps_ref[f"xmap_ref_{ph}"] for ph in self.phases]

                ### Merge xmaps from indexed phases

                self.xmap_merged_ref = kp.indexing.merge_crystal_maps(
                    crystal_maps=self.cm_ref,
                )

                ### Set colors of phases and save merged xmaps to file

                for i in range(len(self.phases)):
                    self.xmap_merged_ref.phases[i].color = self.colors[i]

                io.save(
                    os.path.join(self.save_dir, "di_results_ref_merged.h5"), self.xmap_merged_ref
                )  # orix' HDF5
                io.save(
                    os.path.join(self.save_dir, "di_results_ref_merged.ang"), self.xmap_merged_ref
                )  # .ang

                ### Plot and save the normalized cross correlation score for merged map after refinement

                fig = self.xmap_merged_ref.plot(
                    value=self.xmap_merged_ref.scores,
                    colorbar=True,
                    colorbar_label="Normalized cross correlation score after refinement",
                    return_figure=True,
                    cmap="gray",
                )

                fig.savefig(os.path.join(self.save_dir, "ncc_merged_ref.png"), **self.savefig_kwargs)

                ### Phase map

                fig = self.xmap_merged_ref.plot(remove_padding=True, return_figure=True)
                fig.savefig(os.path.join(self.save_dir, "phase_map_ref.png"), **self.savefig_kwargs)

        self.accept()
