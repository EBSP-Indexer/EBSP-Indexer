from typing import Callable
from contextlib import redirect_stderr, redirect_stdout

from PySide6.QtCore import QThreadPool, QObject, QRunnable, Slot, Signal
from PySide6.QtWidgets import QMainWindow, QWidget

from utils.redirect import Redirect
from utils.threads.thdout import ThreadedOutput


class Worker(QRunnable, QObject):
    """
    Inherits from QRunnable and QObject to handle thread setup, signals and wrap-up.

    Attributes
    ----------
    parent : QMainWindow, QWidget
        The parenting QWidget which is either a WorkerWidget or the main application window,
        contains methods for writing output
    func : Callable
        The function callback to run on this worker thread,
        supplied args and kwargs will be passed through to the runner
    args : tuple
        Arguments to pass to the callback function
    kwargs: dict[str, Any]
        Keywords to pass to the callback function
    thdout : ThreadedOutput
        Redirects standard output to the signals outputLine and outputError
    """

    isStarted = Signal(int)
    isFinished = Signal(int)
    isError = Signal(int)

    def __init__(self, parent: QMainWindow | QWidget, func: Callable, *args, **kwargs):
        """
        Parameters
        ----------
        parent : QMainWindow, QWidget
            The parenting QWidget which is either a WorkerWidget or the main application window,
            contains methods for writing output
        func : Callable
            The function callback to run on this worker thread,
            Supplied args and kwargs will be passed through to the runner
        args : tuple
            Arguments to pass to the callback function
        kwargs: dict[str, Any]
            Keywords to pass to the callback function
        """

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
        Initialise the runner function with passed args, kwargs, and redirects standard output and error.

        Raises
        ------
        Exception
            If an error occurs in the task of the thread
        """
        with redirect_stdout(self.thdout), redirect_stderr(self.error_redirect):
            try:
                self.isStarted.emit(self.id)
                self.fn(*self.args, **self.kwargs)
                self.isFinished.emit(self.id)
            except Exception as e:
                self.thdout.errorwrite(f"{e} (See terminal for traceback)")
                self.isError.emit(self.id)
                raise e


def sendToWorker(parent: QMainWindow | QObject, func: Callable, *args, **kwargs):
    """
    Sends a function to a worker-thread with args and kwargs, and redirects standard output and error to parent.

    Parameters
    ----------
    parent : QMainWindow, QWidget
        The parenting QWidget which is either a WorkerWidget or the main application window,
        contains methods for writing output
    func : Callable
        The function callback to run on this worker thread,
        Supplied args and kwargs will be passed through to the runner
    args : tuple
        Arguments to pass to the callback function
    kwargs: dict[str, Any]
        Keywords to pass to the callback function
    """
    worker = Worker(parent, func, *args, **kwargs)
    QThreadPool.globalInstance().start(worker)
