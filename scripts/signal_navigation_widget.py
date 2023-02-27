import sys
import kikuchipy as kp

from scripts.signal_navigation import get_navigation_figure, open_file

from math import floor

from PySide6.QtWidgets import QWidget, QMainWindow

from ui.ui_signal_navigation_widget import Ui_SignalNavigationWidget

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.widgets import Cursor

class SignalNavigationWidget(QWidget):

    def __init__(
        self, mainWindow: QMainWindow
    ) -> None:        
        super().__init__(parent=mainWindow)

        self.ui = Ui_SignalNavigationWidget()
        self.ui.setupUi(self)

        self.setupConnection()

    def setupConnection(self):
        self.ui.pushButtonNav_1.clicked.connect(
            lambda: self.plot_navigator(self.dataset, "1")
        )
        self.ui.pushButtonNav_2.clicked.connect(
            lambda: self.plot_navigator(self.dataset, "2")
        )
    
       
    def load_dataset(self, file_path):

        try:
            self.dataset = open_file(file_path)
        except Exception as e:
            print("open file failed")
            raise e

        self.plot_navigator(self.dataset, navigator="1")

    def plot_navigator(self, dataset, navigator : str, x=0, y=0):
        
        try:
            self.ui.navigatorMplWidget.canvas.mpl_disconnect(self.cid)
            self.ui.navigatorMplWidget.canvas.mpl_disconnect(self.hover_id)
        except:
            pass

        navigator = dataset["navigator"][navigator]
        
        self.ui.navigatorMplWidget.vbl.setContentsMargins(0,0,0,0)
        self.ui.navigatorMplWidget.canvas.ax.clear()
        self.ui.navigatorMplWidget.canvas.ax.axis(False)

        self.cursor = Cursor(self.ui.navigatorMplWidget.canvas.ax, useblit=True, color="red", linewidth=1, linestyle="-", alpha=0.5)
        self.cursor.set_active(True)
        
        self.ui.navigatorMplWidget.canvas.ax.imshow(
            navigator, cmap="gray", extent=(0, dataset["nav_shape"][0], dataset["nav_shape"][1], 0))
        self.ui.navigatorMplWidget.canvas.draw()
        
        # plot pattern from upper left corner
        self.plot_signal(dataset, x, y)
        self.last_x, self.last_y = x, y
        
        # Annotation for tooltip hovering
        #self.annot = self.ui.navigatorMplWidget.canvas.ax.annotate(text="", xy=(0, 0))
        #self.annot.set_visible(False)

        #self.background = self.ui.navigatorMplWidget.canvas.copy_from_bbox(self.ui.navigatorMplWidget.canvas.ax.bbox)
        #self.background.extent(0, dataset["nav_shape"][0], dataset["nav_shape"][1], 0)
        # canvas id to later disconnect
        self.cid = self.ui.navigatorMplWidget.canvas.mpl_connect(
            "button_press_event", lambda event: self.on_click_navigator(event, dataset)
        )
        self.hover_id = self.ui.navigatorMplWidget.canvas.mpl_connect(
            "motion_notify_event",
            lambda event: self.on_hover_navigator(event, dataset["nav_shape"]),
        )

    def plot_signal(self, dataset, x_index, y_index):
        # TODO: figure out whats is going on with axis, seems to be flipped
        self.add_geosim = True
        pattern = dataset["ebsd_data"]
        signal = pattern.data[y_index, x_index]
        #print(dataset["geo_sim"])
        self.ui.signalMplWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.signalMplWidget.canvas.ax.clear()
        self.ui.signalMplWidget.canvas.ax.axis(False)
        self.ui.signalMplWidget.canvas.ax.imshow(signal, cmap="gray")

        if dataset["type"] == "crystal map" and self.add_geosim:
            hkl_lines = dataset["geo_sim"].as_collections((y_index, x_index), zone_axes_labels=False)
            self.ui.signalMplWidget.canvas.ax.add_collection(hkl_lines[0], autolim=False)

        self.ui.signalMplWidget.canvas.draw()
        #self.ui.signalMplWidget.canvas.ax.collections.remove()

    def on_click_navigator(self, event, dataset):
        try:
            self.click_rect.remove()
        except:
            pass
        
        nav_shape = dataset["nav_shape"]
        #signal = dataset["ebds_data"]

        if event.inaxes:
            xytext = (event.xdata, event.ydata)
            if event.xdata > nav_shape[0] * 0.9:
                xytext = (event.xdata - nav_shape[0] * 0.1, event.ydata)
            if event.ydata < nav_shape[1] * 0.1:
                xytext = (event.xdata, event.ydata + nav_shape[1] * 0.05)
            if event.ydata < nav_shape[1] * 0.1 and event.xdata > nav_shape[0] * 0.9:
                xytext = (
                    event.xdata - nav_shape[0] * 0.1,
                    event.ydata + nav_shape[1] * 0.05,
                )

            x, y = floor(event.xdata), floor(event.ydata)
            self.plot_signal(dataset, floor(x), floor(y))
            self.ui.signalIndex.setText(f"({x}, {y})")
            self.click_rect = self.ui.navigatorMplWidget.canvas.ax.add_patch(
                Rectangle(
                    (x, y),
                    1,
                    1,
                    linewidth=1,
                    edgecolor="red",
                    facecolor="red",
                    alpha=0.5,
                )
            )
            click_annot = self.ui.navigatorMplWidget.canvas.ax.annotate(
                text=f"({x}, {y})", xy=((event.xdata, event.ydata)), xytext=xytext)
            click_annot.set_bbox(dict(facecolor='white', alpha=0.5, edgecolor='grey'))
            self.ui.navigatorMplWidget.canvas.draw()
            click_annot.remove()

    def on_hover_navigator(self, event, nav_shape):
        if event.inaxes:
            x_hover, y_hover = floor(event.xdata), floor(event.ydata)
            if (self.last_x != x_hover or self.last_y != y_hover):
            #xytext = (event.xdata, event.ydata)
                self.ui.navigatorCoordinates.setText(f"({x_hover}, {y_hover})")
                self.last_x, self.last_y = x_hover, y_hover
            
            #hover_rec = self.ui.navigatorMplWidget.canvas.ax.add_patch(
            #    Rectangle(
            #        (x_hover, y_hover),
            #        1,
            #        1,
            #        linewidth=1,
            #        edgecolor="red",
            #        facecolor="red",
            #        alpha=0.3,
            #    )
            #)
            
            #hover_rec.set_visible(True)

            #self.ui.navigatorMplWidget.canvas.restore_region(self.background)

            #self.ui.navigatorMplWidget.canvas.ax.draw_artist(hover_annot)
            #self.ui.navigatorMplWidget.canvas.ax.draw_artist(hover_rec)
            #self.ui.navigatorMplWidget.canvas.blit(self.ui.navigatorMplWidget.canvas.ax.bbox)
            #self.ui.navigatorMplWidget.canvas.flush_events()
            
            #hover_rec.remove()

        #else:
        #    hover_annot = self.ui.navigatorMplWidget.canvas.ax.annotate("", xy=(0, 0))
        #    hover_rec = self.ui.navigatorMplWidget.canvas.ax.add_patch(
        #        Rectangle((0, 0), 1, 1, linewidth=1)
        #    )
        #    
        #    hover_annot.set_visible(False)
        #    hover_rec.set_visible(False)

        #self.ui.navigatorMplWidget.canvas.draw()
        #hover_annot.remove()
        #hover_rec.remove()
    