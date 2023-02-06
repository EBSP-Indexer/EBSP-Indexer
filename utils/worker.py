import sys
from datetime import timedelta
from contextlib import redirect_stderr, redirect_stdout
from PySide6.QtCore import QThreadPool, QObject, QRunnable, Slot, Signal, QElapsedTimer, QTimer
from PySide6.QtWidgets import QWidget, QListWidget, QListWidgetItem

from scripts.console import ThreadedStdout, Redirect
from ui.ui_worker_widget import Ui_WorkerWidget


class WorkerSignals(QObject):

    isStarted = Signal(bool)
    isFinished = Signal(bool)

    def __init__(self) -> None:
        super().__init__()


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

    signals = WorkerSignals()

    def __init__(self, fn, output=sys.stdout, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.name = fn.__str__()  # TODO CHANGE THIS
        self.args = args
        self.kwargs = kwargs
        self.console = output
        self.threadedStdout = ThreadedStdout()
        self.errorRedirect = Redirect(self.threadedStdout.errorwrite)
        self.setupConnections()

    def setupConnections(self):
        self.threadedStdout.lineSignal.connect(self.console.writeoutput)
        self.threadedStdout.errorSignal.connect(self.console.errorwrite)

    @Slot()  # QtCore.Slot
    def run(self):
        """
        Initialise the runner function with passed args, kwargs, and redirects the output.
        """
        with redirect_stdout(self.threadedStdout), redirect_stderr(self.errorRedirect):
            self.signals.isStarted.emit(True)
            self.fn(*self.args, **self.kwargs)
            self.signals.isFinished.emit(True)


class WorkerWidget(QWidget):
    """
    Widget displaying information about the worker to be shown in the job manager
    """
    ui = Ui_WorkerWidget()
    time = QElapsedTimer()
    timer = QTimer()
    removeMeSignal = Signal(int)

    # TODO: mainWindow should be replaced by a jobManagerList
    def __init__(
        self, job_title: str, output_directory: str, mainWindow: QWidget, worker: Worker
    ) -> None:
        super().__init__(parent=mainWindow)
        self.id = mainWindow.countWorkers() + 1
        self.worker_title = job_title
        self.output_directory = output_directory
        self.worker = worker
        self.ui.setupUi(self)
        self.setupConnections()

    def setupConnections(self):
        # UI
        self.ui.labelJobNumber.setText(f"Job {self.id}")
        self.ui.labelJobName.setText(f"{self.worker_title}")
        self.ui.labelOutput.setText(f"{self.output_directory}")
        self.ui.pushButtonRemove.clicked.connect(self.sendRemoveItem)
        self.timer.timeout.connect(self.updateTimerDisplay)
        self.worker.signals.isStarted.connect(self.time_worker)
        self.worker.signals.isFinished.connect(self.finalize)

        # Signals
        self.removeMeSignal.connect(self.parentWidget().removeWorker)

    def sendRemoveItem(self):
        self.removeMeSignal.emit(self.id)

    def time_worker(self):
        self.time.start()
        self.updateTimerDisplay()
        self.timer.start(1000)

    def finalize(self):
        self.timer.stop()
        self.ui.pushButtonRemove.setEnabled(True)
        self.ui.labelTime.setStyleSheet("QLabel { color : green; }")
        self.ui.labelStatus.setStyleSheet("QLabel { color : green; }")
        self.ui.labelStatus.setText("Completed")

    @Slot()
    def updateTimerDisplay(self):
        self.ui.labelTime.setText(f"{timedelta(milliseconds=self.time.elapsed())}".split(".")[0])


# TODO: Delete when sendTOWorkManager is finished implemented
def toWorker(function, stdout, *args, **kwargs):
    """
    Sends a function to a worker-thread that will redirect to stdout
    """
    worker = Worker(function, stdout, *args, **kwargs)
    QThreadPool.globalInstance().start(worker)


# TODO: Finish and use in all thread-related operations
def sendToJobManager(job_title: str, output_directory: str, listview: QListWidget, stdout, fn, *args, **kwargs):
    """
    Sends a function to a worker-thread that will redirect to stdout
    """
    worker = Worker(fn, stdout, *args, **kwargs)
    workerWidget = WorkerWidget(job_title, output_directory, listview.window(), worker)
    item = QListWidgetItem()
    item.setSizeHint(workerWidget.sizeHint())
    listview.addItem(item)
    listview.setItemWidget(item, workerWidget)
    QThreadPool.globalInstance().start(worker)
