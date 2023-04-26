import sys
import kikuchipy as kp
from os import path

from math import floor

from PySide6.QtWidgets import QWidget, QMainWindow, QApplication
from PySide6.QtGui import QStatusTipEvent

from ui.ui_signal_navigation_widget import Ui_SignalNavigationWidget

from utils.threads.thdout import ThreadedOutput
from contextlib import redirect_stdout

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.widgets import Cursor

from utils import FileBrowser

import kikuchipy as kp
import orix

from diffsims.crystallography import ReciprocalLatticeVector

from numpy import argsort

from scripts.signal_loader import crystalMap, EBSDDataset


class SignalNavigationWidget(QWidget):
    def __init__(self, mainWindow: QMainWindow) -> None:
        super().__init__(parent=mainWindow)

        self.ui = Ui_SignalNavigationWidget()
        self.ui.setupUi(self)
        self.ui.navigatorMplWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.signalMplWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.signalMplWidget.setVisible(False)
        self.ui.navigatorMplWidget.setVisible(False)
        self.ui.checkBox.setVisible(False)
        self.ui.buttonBox.setVisible(False)

        self.file_selected = ""
        self.setupConnection()

        self.changetype = True

    def setupConnection(self):
        self.ui.comboBoxNavigator.currentTextChanged.connect(
            lambda: self.plot_navigator(
                self.dataset, self.ui.comboBoxNavigator.currentText()
            )
        )
        self.ui.checkBox.stateChanged.connect(
            lambda: self.plot_signal(self.dataset, self.current_x, self.current_y)
        )

        self.ui.buttonBox.accepted.connect(
            lambda: self.export_image(
                self.dataset.navigator[self.ui.comboBoxNavigator.currentText()],
                self.dataset.ebsd.data[self.current_y, self.current_x],
            )
        )
    def showStatusTip(self, tip: str):
        QApplication.sendEvent(self, QStatusTipEvent(tip))

    def load_dataset(self, file_path):
        self.file_dir = path.dirname(file_path)
        try:
            signal = kp.load(file_path, lazy=True)
        except:
            signal = orix.io.load(file_path)

        if isinstance(signal, kp.signals.ebsd.EBSD):
            self.dataset = EBSDDataset(signal)

        if isinstance(signal, orix.crystal_map.crystal_map.CrystalMap):
            self.dataset = crystalMap(signal, file_path, compute_all=True)
        
        self.ui.signalMplWidget.setVisible(True)
        self.ui.navigatorMplWidget.setVisible(True)
        self.ui.buttonBox.setVisible(True)

        self.plot_navigator(self.dataset, nav_type=list(self.dataset.navigator)[0])
        self.ui.comboBoxNavigator.clear()

        for key, value in self.dataset.navigator.items():
            self.ui.comboBoxNavigator.addItem(key)

        self.ui.checkBox.setChecked(False)

        if self.dataset.datatype == "crystal map":
            show_labels_and_checkbox = True
        else:
            show_labels_and_checkbox = False
        
        self.ui.checkBox.setVisible(show_labels_and_checkbox)

        if show_labels_and_checkbox:
            self.ui.LabelPhase2.setText("Phase:")
            self.ui.labelPhase1.setText("Phase:")
        else:
            self.ui.LabelPhase2.setText("")
            self.ui.labelPhase1.setText("")
        

    def plot_navigator(self, dataset, nav_type: str, x=0, y=0):
        
        if nav_type == "":
            return

        try:
            self.ui.navigatorMplWidget.canvas.mpl_disconnect(self.cid)
            self.ui.navigatorMplWidget.canvas.mpl_disconnect(self.hover_id)
        except:
            pass
        
        
        navigator = dataset.compute_navigator(dataset.navigator[nav_type])
        
        

        # plot to MplCanvas
        
        self.ui.navigatorMplWidget.canvas.ax.clear()
        self.ui.navigatorMplWidget.canvas.ax.axis(False)
        
        self.cursor = Cursor(
            self.ui.navigatorMplWidget.canvas.ax,
            useblit=True,
            color="red",
            linewidth=1,
            linestyle="--",
            alpha=1,
        )
        self.cursor.set_active(True)

        self.ui.navigatorMplWidget.canvas.ax.imshow(
            navigator,
            cmap="gray",
            extent=(0, dataset.nav_shape[0], dataset.nav_shape[1], 0),
        )
        self.ui.signalMplWidget.canvas.fig.tight_layout()
        self.ui.navigatorMplWidget.canvas.draw()

        # plot pattern from upper left corner
        self.plot_signal(dataset, x, y)
        self.current_x, self.current_y = x, y

        self.cid = self.ui.navigatorMplWidget.canvas.mpl_connect(
            "button_press_event", lambda event: self.on_click_navigator(event, dataset)
        )
        self.hover_id = self.ui.navigatorMplWidget.canvas.mpl_connect(
            "motion_notify_event",
            lambda event: self.on_hover_navigator(event),
        )

    def plot_signal(self, dataset, x_index, y_index):
        self.add_geosim = self.ui.checkBox.isChecked()
        pattern = dataset.ebsd
        signal = pattern.data[y_index, x_index]
        self.ui.signalMplWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.signalMplWidget.canvas.ax.clear()
        self.ui.signalMplWidget.canvas.ax.axis(False)
        self.ui.signalMplWidget.canvas.ax.imshow(signal, cmap="gray")
        
        
        if (
            dataset.datatype == "crystal map"
            and self.add_geosim
            and self.dataset.phase_id_array[y_index, x_index]
            != -1
        ):
            phase_id = self.dataset.phase_id_array[y_index, x_index]
            thdout = ThreadedOutput()
            with redirect_stdout(thdout):
                simulator = kp.simulations.KikuchiPatternSimulator(
                    dataset.hkl[phase_id]
                )

                hkl_lines = simulator.on_detector(
                    dataset.ebsd_detector,
                    dataset.crystal_map[y_index, x_index].rotations,
                ).as_collections(zone_axes_labels=False)

            self.ui.signalMplWidget.canvas.ax.add_collection(
                hkl_lines[0], autolim=False
            )
        
        self.ui.signalMplWidget.canvas.draw()

        self.current_x, self.current_y = x_index, y_index

    def on_click_navigator(self, event, dataset):
        try:
            self.click_rect.remove()
        except:
            pass

        nav_shape = dataset.nav_shape

        if event.inaxes:
            try:
                self.x_line.remove()
                self.y_line.remove()    
            except:
                pass

            """x_text, y_text = (
                event.xdata + nav_shape[0] * 0.1,
                event.ydata - nav_shape[1] * 0.1,
            )
            if event.xdata > nav_shape[0] * 0.7:
                x_text = event.xdata - nav_shape[0] * 0.2
            if event.ydata < nav_shape[1] * 0.3:
                y_text = event.ydata + nav_shape[1] * 0.1
            xytext = (x_text, y_text) """

            x, y = floor(event.xdata), floor(event.ydata)
            if x >= self.dataset.nav_shape[0]:
                x -= 1
            if y >= self.dataset.nav_shape[1]:
                y -= 1
        
            self.plot_signal(dataset, x, y)
            self.ui.signalIndex.setText(f"({x}, {y})")
            self.click_rect = self.ui.navigatorMplWidget.canvas.ax.add_patch(
                Rectangle(
                    (x, y),
                    1,
                    1,
                    linewidth=1,
                    edgecolor="black",
                    facecolor="none",
                    alpha=0.5,
                )
            )
            line_kwargs = dict(color="red", linestyle= "dashed", linewidth=1, alpha=0.5)
            self.x_line = self.ui.navigatorMplWidget.canvas.ax.axvline(event.xdata, **line_kwargs)
            self.y_line = self.ui.navigatorMplWidget.canvas.ax.axhline(event.ydata, **line_kwargs)
            
            """ click_annot = self.ui.navigatorMplWidget.canvas.ax.annotate(
                text=f"({x}, {y})",
                xy=((x + 0.5, y + 0.5)),
                xytext=xytext,
                annotation_clip=True,
                arrowprops=dict(
                    facecolor="black", width=0.2, headwidth=5, headlength=5
                ),
            )
            click_annot.set_bbox(dict(facecolor="white", alpha=0.5, edgecolor="grey"))
            
            click_annot.remove() """
            self.ui.navigatorMplWidget.canvas.draw()
            
            

            if self.dataset.datatype == "crystal map":
                phase_id = self.dataset.phase_id_array[y, x]
                if phase_id == -1:
                    self.ui.checkBox.setEnabled(False)
                else:
                    self.ui.checkBox.setEnabled(True)
                phase_name = self.dataset.crystal_map.phases[phase_id].name
                self.ui.labelPhaseClick.setText(f"{phase_name}")

    def on_hover_navigator(self, event):
        if event.inaxes:
            self.cursor.set_active(True)
            x_hover, y_hover = floor(event.xdata), floor(event.ydata)
            if x_hover >= self.dataset.nav_shape[0]:
                x_hover -= 1
            if y_hover >= self.dataset.nav_shape[1]:
                y_hover -= 1
            

            self.ui.navigatorCoordinates.setText(f"({x_hover}, {y_hover})")
            if self.dataset.datatype == "crystal map":
                phase_name = self.dataset.crystal_map.phases[
                    self.dataset.phase_id_array[y_hover, x_hover]
                ].name
                self.ui.labelPhaseHover.setText(f"{phase_name}")
            
        else:
            self.cursor.set_active(False)
            try:
                self.ui.navigatorCoordinates.setText(f"({self.current_x}, {self.current_y})")
                if self.dataset.datatype == "crystal map":
                    phase_name = self.dataset.crystal_map.phases[
                    self.dataset.phase_id_array[self.current_y, self.current_x]
                    ].name
                    self.ui.labelPhaseHover.setText(f"{phase_name}")
            except:
                self.ui.navigatorCoordinates.setText(f"(x, y)")

    def export_image(self, navigator_index: int, signal):
        saveImageBrowser = FileBrowser(
            mode=FileBrowser.SaveFile, dirpath=self.file_dir, filter_name="*.png"
        )
        if saveImageBrowser.getFile():
            image_export_path = saveImageBrowser.getPaths()[0]
            x, y = self.current_x, self.current_y
            fig, ax = plt.subplots(1, 2, figsize=(12, 6))
            ax[0].set_title(self.ui.comboBoxNavigator.currentText())
            ax[0].imshow(
                self.dataset.compute_navigator(navigator_index),
                cmap="gray",
                extent=(0, self.dataset.nav_shape[0], self.dataset.nav_shape[1], 0),
            )
            
            ax[0].add_patch(
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
            ax[0].axis("off")

            ax[1].set_title(f"EBSD signal ({x}, {y})")
            ax[1].imshow(signal, cmap="gray")
            ax[1].axis("off")
            if self.ui.checkBox.isChecked():
                phase_id = self.dataset.phase_id_array[y, x]
                thdout = ThreadedOutput()
                with redirect_stdout(thdout):
                    simulator = kp.simulations.KikuchiPatternSimulator(
                        self.dataset.hkl[phase_id]
                    )

                    hkl_lines = simulator.on_detector(
                        self.dataset.ebsd_detector,
                        self.dataset.crystal_map[y, x].rotations,
                    ).as_collections(zone_axes_labels=False)

                ax[1].add_collection(
                    hkl_lines[0], autolim=False
                )
            fig.savefig(
                image_export_path
            )  # image is saved as .png by default, as of now no other file format is supported
