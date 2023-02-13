import sys
from typing import Callable, Optional, TextIO, Union
from contextlib import redirect_stderr, redirect_stdout

from PySide6.QtCore import QThreadPool, QObject, QRunnable, Slot, Signal
from PySide6.QtWidgets import QMainWindow, QWidget

from utils.redirect import Redirect
from utils.threads.thdout import ThreadedOutput


class Worker(QRunnable, QObject):
    """
    #TODO CHANGE DESCRIPTION

    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    """

    isStarted = Signal(int)
    isFinished = Signal(int)
    isError = Signal(int)

    def __init__(
        self,
        parent: QMainWindow | QWidget,
        func: Callable,
        *args,
        **kwargs
    ):
        QObject.__init__(self, parent=parent)
        QRunnable.__init__(self)
        if issubclass(parent.__class__, QMainWindow):
            self.id = None
            self.write_line = parent.console.write
            self.write_error = parent.console.errorwrite
        else:
            self.id = parent.id
            self.write_line = parent.write
            self.write_error = parent.errorwrite

        self.fn = func
        self.args = args
        self.kwargs = kwargs
        self.thdout = ThreadedOutput()
        self.error_redirect = Redirect(self.thdout.errorwrite)
        self.setupConnections()

    def setupConnections(self):
        self.thdout.outputLine.connect(self.write_line)
        self.thdout.outputError.connect(self.write_error)
        self.isStarted.connect(self.parent().updateActiveJobs)
        self.isFinished.connect(self.parent().updateActiveJobs)
        self.isError.connect(self.parent().updateActiveJobs)

    @Slot()
    def run(self) -> None:
        """
        Initialise the runner function with passed args, kwargs, and redirects the output.
        """
        with redirect_stdout(self.thdout), redirect_stderr(self.error_redirect):
            try:
                self.isStarted.emit(self.id)
                self.fn(*self.args, **self.kwargs)
                self.isFinished.emit(self.id)
            except Exception as e:
                self.isError.emit(self.id)
                self.thdout.errorwrite(str(e))
                raise e


def sendToWorker(parent: QObject, func: Callable, *args, **kwargs):
    """
    Sends a function to a worker-thread that will redirect to stdout
    """
    worker = Worker(parent, func, *args, **kwargs)
    QThreadPool.globalInstance().start(worker)
