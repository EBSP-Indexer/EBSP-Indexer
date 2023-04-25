import sys
from os import path, devnull, mkdir
import kikuchipy as kp
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QDialogButtonBox
import numpy as np
from math import floor, ceil

from diffsims.crystallography import ReciprocalLatticeVector
from pyebsdindex import ebsd_index, pcopt
from orix.quaternion import Rotation
from orix.crystal_map import PhaseList
import hyperspy.api as hs
import dask as da

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.widgets import Cursor

from utils import SettingFile, FileBrowser, sendToJobManager
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
        
        self.s = kp.load(self.pattern_path, lazy=True)
        working_distance = self.s.metadata.Acquisition_instrument.SEM.working_distance
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
            if self.s.metadata.Acquisition_instrument.SEM.microscope == "ZEISS SUPRA55 VP":
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

        
        self.changeStateOfButtons()
    

    def setupConnections(self):
        self.ui.buttonAddPhase.clicked.connect(lambda: self.addPhase())
        self.ui.buttonRemovePhase.clicked.connect(lambda: self.removePhase())
        self.ui.buttonRemovePattern.clicked.connect(lambda: self.removePattern())
        self.ui.listCoordinates.itemSelectionChanged.connect(lambda: self.coordinateListClicked())
        self.ui.buttonGrid.clicked.connect(lambda: self.gridClicked())
        self.ui.buttonUpdateGrid.clicked.connect(lambda: self.gridClicked())
        self.ui.buttonBox.accepted.connect(lambda: self.runPatternCenterOpimization())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())
        self.ui.conventionBox.currentTextChanged.connect(lambda: self.updatePCConvention())

    # Phases
    def addPhase(self):
        if self.fileBrowserOD.getFile():
            mp_path = self.fileBrowserOD.getPaths()[0]
            try:
                mp = kp.load(mp_path, lazy=True)
                if not len(mp.phase.name):
                    mp.phase.name = path.basename(path.dirname(mp_path))
                phase_name = mp.phase.name
            except Exception as e:
                raise e
            if phase_name not in self.mp_paths.keys():
                self.mp_paths[phase_name] = mp_path
                self.ui.listPhases.addItem(phase_name)
            
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
        self.ui.listPhases.clearSelection()

        self.changeStateOfButtons()

    # Patterns
    def addPattern(self, x, y):
        if [x, y] not in self.coordinates:
            self.coordinates.append([x, y])
            self.ui.listCoordinates.addItem(f"({x}, {y})")
    
    def removePattern(self):
        index = self.ui.listCoordinates.currentRow()
        self.ui.listCoordinates.takeItem(self.ui.listCoordinates.currentRow())
        del self.coordinates[index]

        try:
            self.click_rect.remove()
        except:
            pass
        self.update_rectangles()
        self.ui.MplWidget.canvas.draw()

        if len(self.coordinates) == 0:
            self.ui.buttonRemovePattern.setEnabled(False)
    
    def coordinateListClicked(self):
        coords = self.ui.listCoordinates.currentItem().text().split(", ")
        x, y = int(coords[0].strip("()")), int(coords[1].strip("()"))
        self.plot_signal(x, y)

        try:
            self.click_rect.remove()
        except:
            pass
        self.current_rectangle(x,y)
        self.ui.MplWidget.canvas.draw()
        
        self.ui.buttonRemovePattern.setEnabled(True)
    
    def gridClicked(self):
        if self.ui.buttonGrid.isChecked():
            self.coordinates = []
            self.ui.listCoordinates.clear()
            grid_shape = [int(self.ui.spinBoxGridX.value()), int(self.ui.spinBoxGridY.value())]
            self.updateGridButtons(enable=True)
            s_grid, coords = self.s.extract_grid(grid_shape, return_indices=True)
            coords_converted = self.convertGridList(grid_shape, coords)

            for coord in coords_converted:
                self.addPattern(coord[0], coord[1])

            self.update_rectangles()
            self.ui.MplWidget.canvas.draw()
        else:
            self.updateGridButtons(enable=False)
    
    def convertGridList(self, grid_shape, coords):
        x, y = grid_shape[0], grid_shape[1]
        new_list = [[0,0]]*(x*y)
        for i in range(x):
            for j in range(y):
                new_list[j+i*y] = [coords[1][j][i]-1, coords[0][j][i]-1]
        return new_list

    def updateGridButtons(self, enable):
        self.ui.spinBoxGridX.setEnabled(enable)
        self.ui.spinBoxGridY.setEnabled(enable)
        self.ui.buttonUpdateGrid.setEnabled(enable)
        self.ui.labelMultiplicator.setEnabled(enable)

    def changeStateOfButtons(self):
        enable = bool(len(list(self.mp_paths.keys())))
        self.ui.buttonRemovePhase.setEnabled(enable)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enable)

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
    

### INTERACTION WITH NAVIGATOR ###

    def plot_navigator(self, x=0, y=0):
        self.dataset = EBSDDataset(self.s, self.pattern_path)

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

        self.iq = self.s.get_image_quality()
        self.iq = self.iq.compute()
        self.ui.MplWidget.canvas.ax.imshow(
            self.iq,
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
        
        if event.inaxes:
            x, y = floor(event.xdata), floor(event.ydata)
            self.plot_signal(x, y)
            self.addPattern(x, y)
            self.update_rectangles()
            self.current_rectangle(x,y)
            self.ui.MplWidget.canvas.draw()

    def update_rectangles(self):
        try:
            for rect in self.clicked_patterns:
                rect.remove()
        except:
            pass
        self.clicked_patterns = []
        for coordinate in self.coordinates:
            self.clicked_patterns.append(self.ui.MplWidget.canvas.ax.add_patch(
                Rectangle(
                    coordinate,
                    1,
                    1,
                    linewidth=0.5,
                    edgecolor="black",
                    facecolor="lime",
                    alpha=1,
                )
            ))
    
    def current_rectangle(self, x, y):
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

    def on_hover_navigator(self, event):
        if event.inaxes:
            x_hover, y_hover = floor(event.xdata), floor(event.ydata)
            self.ui.labelxy.setText(f"({x_hover}, {y_hover})")
            self.plot_signal(x_hover,y_hover)
        else:
            self.ui.labelxy.setText(f"(x, y)")


### PATTERN CENTER OPTIMIZATION ###

    def runPatternCenterOpimization(self):
        basename, extension = path.basename(self.pattern_path).split(".")
        save_dir = path.join(self.working_dir, f"{basename}_{extension}")    

        sendToJobManager(
            job_title=f"Pattern center optimization {self.pattern_name}",
            output_path=save_dir,
            listview=self.parentWidget().ui.jobList,
            func=self.patternCenterOpimization,
            allow_cleanup=True,
            allow_logging=True,
        )

    def patternCenterOpimization(self):
        basename, extension = path.basename(self.pattern_path).split(".")
        save_dir = path.join(self.working_dir, f"{basename}_{extension}")       

        try:
            mkdir(save_dir)
        except FileExistsError:
            pass

        self.savefig_kw = dict(dpi=400, pad_inches=0, bbox_inches="tight", transparent=True)

        #set up master patterns, set up reciprocal lattice vector
        simulator_dict = self.retrieveMPData()

        #draw positions on map
        self.drawPCs(save_dir=save_dir)

        #Optimize PC, refine PC
        self.optimizePC(simulator_dict, save_dir)
        
        #Figures: Grid, scatter(mark outliers), patterns with lines


        #Overwite project settings file
        self.close()

    def retrieveMPData(self):
        self.energy = self.s.metadata.Acquisition_instrument.SEM.beam_energy

        self.mp_dict = {}
        for name, h5path in self.mp_paths.items():
            if name in FCC + BCC:
                mp_i = kp.load(
                    path.join(h5path),
                    projection="lambert",
                    energy=self.energy,
                )
                mp_i.name = name
                lat_i = mp_i.phase.structure.lattice
                lat_i.setLatPar(10 * lat_i.a, 10 * lat_i.b, 10 * lat_i.c)
                self.mp_dict[name] = mp_i
            
        ref_dict = {}
        for name in self.mp_dict.keys():
            rlv_i = ReciprocalLatticeVector.from_min_dspacing(self.mp_dict[name].phase)
            rlv_i.sanitise_phase()
            rlv_i = rlv_i.unique(use_symmetry=True)
            rlv_i = rlv_i[rlv_i.allowed]
            rlv_i.calculate_structure_factor()
            structure_factor = abs(rlv_i.structure_factor)
            order = np.argsort(structure_factor)[::-1]
            rlv_i = rlv_i[order]
            rlv_i = rlv_i[:4]
            rlv_i.calculate_theta(self.energy * 1e3)
            rlv_i = rlv_i.symmetrise()

            ref_dict[name] = rlv_i

        simulator_dict = {}
        for name in self.mp_dict.keys():
            simulator_dict[name] = kp.simulations.KikuchiPatternSimulator(
                ref_dict[name]
            )
        
        return simulator_dict

    def drawPCs(self, save_dir):
        # Get the right format for coordinates
        cr = np.array(self.coordinates).T
        rc = cr[::-1]
        self.s_cal = kp.signals.LazyEBSD(self.s.data.vindex[tuple(rc)])
        self.s_cal.compute()

        out = da.compute(self.iq)
        iq2 = out[0]
        fig = kp.draw.plot_pattern_positions_in_map(
            rc.T+0.5,
            roi_shape = iq2.shape,
            roi_image = iq2,
            return_figure = True,
        )
        fig.savefig(path.join(save_dir, "maps_pc_cal_patterns.png"), **self.savefig_kw)

    def optimizePC(self, simulator_dict, save_dir):
        phase_list = PhaseList(list(self.mp_dict.values())[0].phase) # only one phase supported, the first FCC/BCC phase

        det_cal0 = self.s_cal.detector
        indexer_cal = det_cal0.get_indexer(phase_list, nBands=12)
        det_cal = self.s_cal.hough_indexing_optimize_pc(
            self.pc,
            indexer=indexer_cal,
            batch=True,
        )
        indexer_cal2 = det_cal.get_indexer(phase_list, nBands=indexer_cal.bandDetectPlan.nBands)
        xmap_cal = self.s_cal.hough_indexing(phase_list, indexer_cal2)
        self.s_cal.axes_manager[0].name = "x"

        xmap_cal_ref, det_cal_ref = self.s_cal.refine_orientation_projection_center(
            xmap_cal,
            det_cal,
            master_pattern=list(self.mp_dict.values())[0],
            energy=self.energy,
            method="LN_NELDERMEAD",
            trust_region=[10, 10, 10, 0.2, 0.2, 0.2],
            rtol=1e-7,
        )
        
        # generate figures
        sim_i = list(simulator_dict.values())[0]
        sim_cal_ref = sim_i.on_detector(det_cal_ref, xmap_cal_ref.rotations.reshape(*xmap_cal_ref.shape))

        # geometrical simulations
        fig, axes = plt.subplots(nrows=ceil(1*np.sqrt(len(self.coordinates)/2)), ncols=ceil(2*np.sqrt(len(self.coordinates)/2)), figsize=(10 * det_cal.aspect_ratio, 6))
        for i, ax in enumerate(axes.ravel()):
            if i >= len(self.coordinates):
                ax.axis("off")
                continue
            ax.imshow(self.s_cal.data[i], cmap="gray")
            lines = sim_cal_ref.as_collections(i)[0]
            ax.add_collection(lines)
            ax.axis("off")
        fig.tight_layout()
        fig.savefig(path.join(save_dir, "pc_geometrical_simulations.png"), **self.savefig_kw)
        
        # scatterplot
        fig = det_cal_ref.plot_pc("scatter", annotate=True, return_figure=True)
        fig.savefig(path.join(save_dir, "pc_scatter_plot.png"), **self.savefig_kw)

        # remove outliers
        is_inlier = xmap_cal_ref.scores > 0.4
        det_cal_ref.pc = det_cal_ref.pc[is_inlier]

        # Write to file
        det_cal_ref.save(path.join(save_dir, "pc_optimization.txt"))

        f = open(path.join(save_dir, "pc_optimization.txt"), "a")
        f.write("\n# Mean pattern center: "+str(det_cal_ref.pc_average.round(4)))
        f.write("\n# Standard deviation: "+str(abs(det_cal_ref.pc_flattened.std(0))))
        f.close()

