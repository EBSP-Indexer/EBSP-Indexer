import sys
import kikuchipy as kp
import matplotlib.pyplot as plt

class SignalNaviagtion():
    def __init__(self) -> None:
        super().__init__

    def plot_navigator(self, file_path, nav_type="mean_intensity"):
        try:
            self.ui.navigatorMplWidget.canvas.mpl_disconnect(self.cid)
        except:
            pass

        s = open_pattern(file_path)
        
        navigator = get_navigation_figure(s, nav_type)

        self.ui.navigatorMplWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.navigatorMplWidget.canvas.ax.clear()
        self.ui.navigatorMplWidget.canvas.ax.axis(False)
        self.cursor = Cursor(self.ui.navigatorMplWidget.canvas.ax, useblit=True, color="yellow", linewidth=3, linestyle="--", alpha=0.8)
        self.cursor.set_active(True)
        self.ui.navigatorMplWidget.canvas.ax.imshow(navigator, cmap="gray")
        self.ui.navigatorMplWidget.canvas.draw()
        #plot pattern from upper left corner
        self.plot_signal(s, 0, 0)
        #canvas id to later disconnect
        self.cid = self.ui.navigatorMplWidget.canvas.mpl_connect("button_press_event", lambda event: self.on_click_navigator(event, s))


    def plot_signal(self, pattern, x_index, y_index):
        
        signal = pattern.data[y_index, x_index]
        
        self.ui.signalMplWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.signalMplWidget.canvas.ax.clear()
        self.ui.signalMplWidget.canvas.ax.axis(False)
        self.ui.signalMplWidget.canvas.ax.imshow(signal, cmap="gray")
        self.ui.signalMplWidget.canvas.draw()

    def on_click_navigator(self, event, s):
        if event.inaxes:
            self.plot_signal(s, int(event.xdata), int(event.ydata))

def open_pattern(file_path):
    s = kp.load(file_path, lazy=True)
    nav_shape = s.axes_manager.navigation_shape
    return s, nav_shape

def get_navigation_figure(pattern, nav_type="mean_intensity"):
    if nav_type == "mean_intensity":
        navigator = pattern.mean(axis=(2,3))
    if nav_type == "iq":
        print("ok")
        navigator = pattern.get_image_quality()

    return navigator