import sys
from contextlib import redirect_stderr, redirect_stdout
from PySide6.QtCore import QRunnable, Slot, QThreadPool

from scripts.console import ThreadedStdout, Redirect


class Worker(QRunnable):
    """
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    """

    def __init__(self, fn, output=sys.stdout, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.console = output
        self.threadedStdout = ThreadedStdout()
        self.errorRedirect = Redirect(self.threadedStdout.errorwrite)
        self.threadedStdout.lineSignal.connect(self.console.writeoutput)
        self.threadedStdout.errorSignal.connect(self.console.errorwrite)

    @Slot()  # QtCore.Slot
    def run(self):
        """
        Initialise the runner function with passed args, kwargs, and redirects the output.
        """
        with redirect_stdout(self.threadedStdout), redirect_stderr(self.errorRedirect):
            self.fn(*self.args, **self.kwargs)

def toWorker(function, console, *args, **kwargs):
    """
    Sends a function to a worker-thread that will output the result to
    """
    worker = Worker(function, console, *args, **kwargs)
    QThreadPool.globalInstance().start(worker)
    