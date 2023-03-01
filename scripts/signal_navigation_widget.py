import sys
import kikuchipy as kp
from os import path

from scripts.signal_navigation import open_file

from math import floor

from PySide6.QtWidgets import QWidget, QMainWindow

from ui.ui_signal_navigation_widget import Ui_SignalNavigationWidget

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.widgets import Cursor


class SignalNavigationWidget(QWidget):
    def __init__(self, mainWindow: QMainWindow) -> None:
        super().__init__(parent=mainWindow)

        self.ui = Ui_SignalNavigationWidget()
        self.ui.setupUi(self)
        self.ui.checkBox.setVisible(False)

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

        self.ui.pushButtonExportImage.clicked.connect(
            lambda: self.export_image(
                self.dataset["navigator"][self.ui.comboBoxNavigator.currentText()],
                self.dataset["ebsd_data"].data[self.current_y, self.current_x],
            )
        )

    def load_dataset(self, file_path):
        self.file_dir = path.dirname(file_path)
        try:
            self.dataset = open_file(file_path)
            self.file_selected = file_path
        except Exception as e:
            print("open file failed")
            raise e

        self.plot_navigator(self.dataset, navigator=list(self.dataset["navigator"])[0])
        self.ui.comboBoxNavigator.clear()

        for key in self.dataset["navigator"].keys():
            self.ui.comboBoxNavigator.addItem(key)

        if self.dataset["type"] == "crystal map":
            self.ui.checkBox.setVisible(True)
            self.ui.checkBox.setChecked(False)
        else:
            self.ui.checkBox.setVisible(False)
            self.ui.checkBox.setChecked(False)

    def plot_navigator(self, dataset, navigator: str, x=0, y=0):
        if navigator == "":
            return

        try:
            self.ui.navigatorMplWidget.canvas.mpl_disconnect(self.cid)
            self.ui.navigatorMplWidget.canvas.mpl_disconnect(self.hover_id)
        except:
            pass
        navigator = dataset["navigator"][navigator]

        #plot to MplCanvas
        self.ui.navigatorMplWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.navigatorMplWidget.canvas.ax.clear()
        self.ui.navigatorMplWidget.canvas.ax.axis(False)

        self.cursor = Cursor(
            self.ui.navigatorMplWidget.canvas.ax,
            useblit=True,
            color="red",
            linewidth=1,
            linestyle="-",
            alpha=0.5,
        )
        self.cursor.set_active(True)

        self.ui.navigatorMplWidget.canvas.ax.imshow(
            navigator,
            cmap="gray",
            extent=(0, dataset["nav_shape"][0], dataset["nav_shape"][1], 0),
        )
        self.ui.navigatorMplWidget.canvas.draw()

        # plot to self.fig_to_save

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
        pattern = dataset["ebsd_data"]
        signal = pattern.data[y_index, x_index]
        self.ui.signalMplWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.signalMplWidget.canvas.ax.clear()
        self.ui.signalMplWidget.canvas.ax.axis(False)
        self.ui.signalMplWidget.canvas.ax.imshow(signal, cmap="gray")

        if dataset["type"] == "crystal map" and self.add_geosim:
            hkl_lines = dataset["geo_sim"].as_collections(
                (y_index, x_index), zone_axes_labels=False
            )
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

        nav_shape = dataset["nav_shape"]

        if event.inaxes:
            x_text, y_text = (
                event.xdata + nav_shape[0] * 0.1,
                event.ydata - nav_shape[1] * 0.1,
            )
            if event.xdata > nav_shape[0] * 0.7:
                x_text = event.xdata - nav_shape[0] * 0.2
            if event.ydata < nav_shape[1] * 0.3:
                y_text = event.ydata + nav_shape[1] * 0.1
            xytext = (x_text, y_text)

            x, y = floor(event.xdata), floor(event.ydata)
            self.plot_signal(dataset, x, y)
            self.ui.signalIndex.setText(f"({x}, {y})")
            self.click_rect = self.ui.navigatorMplWidget.canvas.ax.add_patch(
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
            click_annot = self.ui.navigatorMplWidget.canvas.ax.annotate(
                text=f"({x}, {y})",
                xy=((x + 0.5, y + 0.5)),
                xytext=xytext,
                annotation_clip=True,
                arrowprops=dict(
                    facecolor="black", width=0.2, headwidth=5, headlength=5
                ),
            )
            click_annot.set_bbox(dict(facecolor="white", alpha=0.5, edgecolor="grey"))
            self.ui.navigatorMplWidget.canvas.draw()
            click_annot.remove()

    def on_hover_navigator(self, event):
        if event.inaxes:
            x_hover, y_hover = floor(event.xdata), floor(event.ydata)
            self.ui.navigatorCoordinates.setText(f"({x_hover}, {y_hover})")
        else:
            self.ui.navigatorCoordinates.setText(f"(x, y)")

    def export_image(self, navigator, signal):
        x, y = self.current_x, self.current_y
        fig, ax = plt.subplots(1, 2, figsize=(12, 6))
        ax[0].set_title(self.ui.comboBoxNavigator.currentText())
        ax[0].imshow(navigator)
        ax[0].add_patch(Rectangle(
                    (x, y),
                    1,
                    1,
                    linewidth=0.5,
                    edgecolor="black",
                    facecolor="red",
                    alpha=1,
                ))

        ax[1].set_title(f"EBSD signal ({x}, {y})")
        ax[1].imshow(signal, cmap="gray")
        if self.ui.checkBox.isChecked():    
            hkl_lines = self.dataset["geo_sim"].as_collections(
                    (y, x), zone_axes_labels=False
                )
            ax[1].add_collection(
                hkl_lines[0], autolim=False
                )
        #plt.tight_layout()
        fig.savefig(path.join(self.file_dir, "pattern.png"))
