import sys
import kikuchipy as kp

from scripts.signal_navigation import open_pattern, get_navigation_figure

from math import floor

from PySide6.QtWidgets import QWidget, QMainWindow

from ui.ui_signal_navigation_widget import Ui_SignalNavigationWidget

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class SignalNavigationWidget(QWidget):

    def __init__(
        self, mainWindow: QMainWindow
    ) -> None:        
        super().__init__(parent=mainWindow)

        self.ui = Ui_SignalNavigationWidget()
        self.ui.setupUi(self)

        self.file_selected = ""
        self.setupConnection()

    def setupConnection(self):
        self.ui.pushButtonMeanNav.clicked.connect(
            lambda: self.plot_navigator(self.file_selected, "mean_intensity")
        )
        self.ui.pushButtonIQNav.clicked.connect(
            lambda: self.plot_navigator(self.file_selected, nav_type="iq")
        )
    
    def plot_navigator(self, file_path, nav_type="mean_intensity"):
        try:
            self.ui.navigatorMplWidget.canvas.mpl_disconnect(self.cid)
        except:
            pass
        self.file_selected = file_path
        s, nav_shape = open_pattern(file_path)

        navigator = get_navigation_figure(s, nav_type)

        self.ui.navigatorMplWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.navigatorMplWidget.canvas.ax.clear()

        self.ui.navigatorMplWidget.canvas.ax.axis(False)
        # self.cursor = Cursor(self.ui.navigatorMplWidget.canvas.ax, useblit=True, color="red", linewidth=2, linestyle="--", alpha=0.8)
        # self.cursor.set_active(True)

        self.ui.navigatorMplWidget.canvas.ax.imshow(
            navigator, cmap="gray", extent=(0, nav_shape[0], nav_shape[1], 0)
        )
        self.ui.navigatorMplWidget.canvas.draw()
        # plot pattern from upper left corner
        self.plot_signal(s, 0, 0)

        # Annotation for tooltip hovering
        #self.annot = self.ui.navigatorMplWidget.canvas.ax.annotate(text="", xy=(0, 0))
        #self.annot.set_visible(False)
        # canvas id to later disconnect
        self.cid = self.ui.navigatorMplWidget.canvas.mpl_connect(
            "button_press_event", lambda event: self.on_click_navigator(event, s, nav_shape)
        )
        self.hover_id = self.ui.navigatorMplWidget.canvas.mpl_connect(
            "motion_notify_event",
            lambda event: self.on_hover_navigator(event, nav_shape),
        )

    def plot_signal(self, pattern, x_index, y_index):
        # TODO: figure out whats is going on with axis, seems to be flipped
        signal = pattern.data[y_index, x_index]

        self.ui.signalMplWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.signalMplWidget.canvas.ax.clear()
        self.ui.signalMplWidget.canvas.ax.axis(False)
        self.ui.signalMplWidget.canvas.ax.imshow(signal, cmap="gray")
        self.ui.signalMplWidget.canvas.draw()

    def on_click_navigator(self, event, s, nav_shape):
        try:
            self.click_rect.remove()
        except:
            pass

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
            self.plot_signal(s, floor(x), floor(y))
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
            xytext = (event.xdata, event.ydata)
            x_hover, y_hover = floor(event.xdata), floor(event.ydata)
            if event.xdata > nav_shape[0] * 0.9:
                xytext = (event.xdata - nav_shape[0] * 0.1, event.ydata)
            if event.ydata < nav_shape[1] * 0.1:
                xytext = (event.xdata, event.ydata + nav_shape[1] * 0.05)
            if event.ydata < nav_shape[1] * 0.1 and event.xdata > nav_shape[0] * 0.9:
                xytext = (
                    event.xdata - nav_shape[0] * 0.1,
                    event.ydata + nav_shape[1] * 0.05,
                )
            hover_annot = self.ui.navigatorMplWidget.canvas.ax.annotate(
                f"({x_hover}, {y_hover})", (event.xdata, event.ydata), xytext=xytext)
            hover_annot.set_bbox(dict(facecolor='white', alpha=0.5, edgecolor='grey'))
            hover_rec = self.ui.navigatorMplWidget.canvas.ax.add_patch(
                Rectangle(
                    (x_hover, y_hover),
                    1,
                    1,
                    linewidth=1,
                    edgecolor="red",
                    facecolor="red",
                    alpha=0.3,
                )
            )

            hover_annot.set_visible(True)
            hover_rec.set_visible(True)
            self.ui.navigatorMplWidget.canvas.ax.draw_artist(hover_annot)
            self.ui.navigatorMplWidget.canvas.ax.draw_artist(hover_rec)
            self.ui.navigatorMplWidget.canvas.blit(self.ui.navigatorMplWidget.canvas.ax.bbox)
            #hover_annot.remove()
            #hover_rec.remove()

        else:
            hover_annot = self.ui.navigatorMplWidget.canvas.ax.annotate("", xy=(0, 0))
            hover_rec = self.ui.navigatorMplWidget.canvas.ax.add_patch(
                Rectangle((0, 0), 1, 1, linewidth=1)
            )

            hover_annot.set_visible(False)
            hover_rec.set_visible(False)

        #self.ui.navigatorMplWidget.canvas.draw()
        hover_annot.remove()
        hover_rec.remove()
    