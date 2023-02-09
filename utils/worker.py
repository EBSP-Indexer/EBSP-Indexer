import os
import sys
from datetime import timedelta
from contextlib import redirect_stderr, redirect_stdout
from PySide6.QtCore import (
    QThreadPool,
    QObject,
    QRunnable,
    Slot,
    Signal,
    QElapsedTimer,
    QTimer,
)
from PySide6.QtWidgets import QWidget, QListWidget, QListWidgetItem
from PySide6.QtGui import QPixmap, QTextCharFormat, QBrush, QColor

from scripts.console import ThreadedStdout, Redirect
from ui.ui_worker_widget import Ui_WorkerWidget


class WorkerWidget(QWidget):
    """
    Widget displaying information about the worker to be shown in the job manager
    """

    counter = 0
    removeMeSignal = Signal(int)

    # TODO: mainWindow should be replaced by a jobManagerList
    def __init__(
        self,
        job_title: str,
        output_directory: str,
        mainWindow: QWidget,
        jobItem: QListWidgetItem,
        fn,
        allow_cleanup: bool = False,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(parent=mainWindow)
        WorkerWidget.counter += 1
        self.id = WorkerWidget.counter
        self.worker = Worker(self, fn, output=self.parent().console, *args, **kwargs)
        self.ui = Ui_WorkerWidget()
        self.time = QElapsedTimer()
        self.timer = QTimer()

        self.allow_cleanup = allow_cleanup
        self.job_title = job_title
        self.output_directory = output_directory
        self.jobItem = jobItem
        self.ui.setupUi(self)
        self.setupConnections()
        self.outdisplay = self.ui.textBrowserStatus

    def setupConnections(self):
        # UI
        self.ui.labelJobNumber.setText(f"Job {self.id}: {self.job_title}")
        self.ui.labelJobName.setText(f"{self.job_title}")
        self.ui.labelOutput.setText(f"{self.output_directory}")
        self.ui.labelStatusIcon.setPixmap(
            QPixmap(":/linea_basic/resources/linea_basic_icons/basic_clock.svg").scaled(
                40, 40
            )
        )
        self.jobItem.setSizeHint(self.sizeHint())
        self.inpfmt = self.ui.textBrowserStatus.currentCharFormat()
        self.outfmt = QTextCharFormat(self.inpfmt)
        self.outfmt.setForeground(QBrush(QColor(0, 0, 255)))
        self.errfmt = QTextCharFormat(self.inpfmt)
        self.errfmt.setForeground(QBrush(QColor(255, 0, 0)))

        # Signals
        self.ui.pushButtonRemove.clicked.connect(self.sendRemoveItem)
        self.ui.pushButtonCancel.clicked.connect(self.sendCancelWorker)
        self.ui.pushButtonShow.clicked.connect(self.adjustSize)
        self.removeMeSignal.connect(self.parentWidget().removeWorker)
        self.timer.timeout.connect(self.updateTimerDisplay)
        self.worker.isStarted.connect(self.time_worker)
        self.worker.isStarted.connect(self.parentWidget().updateActiveJobs)
        self.worker.isFinished.connect(self.finalize)
        self.worker.isFinished.connect(self.parentWidget().updateActiveJobs)
        self.worker.isError.connect(lambda id: self.finalize(id, failed=True, cleanup=self.allow_cleanup))
        self.worker.isError.connect(self.parentWidget().updateActiveJobs)

    def sendRemoveItem(self):
        self.removeMeSignal.emit(self.id)

    def sendCancelWorker(self):
        if QThreadPool.globalInstance().tryTake(self.worker):
            self.finalize(id=self.id, cancelled=True, cleanup=self.allow_cleanup)

    def adjustSize(self):
        super().adjustSize()
        self.jobItem.setSizeHint(self.sizeHint())

    @Slot(int)
    def time_worker(self, id):
        if self.id == id:
            self.ui.labelTime.setStyleSheet("QLabel { color : red; }")
            self.time.start()
            self.updateTimerDisplay()
            self.timer.start(500)

    @Slot(int)
    def finalize(
        self,
        id: int,
        failed: bool = False,
        cancelled: bool = False,
        cleanup: bool = False,
    ):
        """
        #TODO Description here

        Cleanup can only remove empty directories for safety reasons
        """
        if self.id == id:
            self.timer.stop()
            self.ui.pushButtonRemove.setEnabled(True)
            if failed:
                self.ui.labelStatusIcon.setPixmap(
                    QPixmap(
                        ":/linea_basic/resources/linea_arrows_icons/arrows_exclamation.svg"
                    ).scaled(40, 40)
                )
                self.ui.labelTime.setStyleSheet("QLabel { color : red; }")
                self.ui.labelTime.setText(f"Failed in {self.ui.labelTime.text()}")
            elif cancelled:
                self.ui.labelStatusIcon.setPixmap(
                    QPixmap(
                        ":/linea_basic/resources/linea_arrows_icons/arrows_circle_remove.svg"
                    ).scaled(40, 40)
                )
                self.ui.labelTime.setStyleSheet("QLabel { color : green; }")
                self.ui.labelTime.setText(f"Cancelled")
            else:
                self.ui.labelStatusIcon.setPixmap(
                    QPixmap(
                        ":/linea_basic/resources/linea_arrows_icons/arrows_circle_check.svg"
                    ).scaled(40, 40)
                )
                self.ui.labelTime.setStyleSheet("QLabel { color : green; }")
                self.ui.labelTime.setText(f"Completed in {self.ui.labelTime.text()}")
            if cleanup:
                try:
                    os.rmdir(path=self.output_directory)
                except Exception as e:
                    self.errorwrite(f"Cleanup failed:\n{e}")

    @Slot()
    def updateTimerDisplay(self):
        self.ui.labelTime.setText(
            f"{timedelta(milliseconds=self.time.elapsed())}".split(".")[0]
        )

    @Slot(str)
    def write(self, line: str) -> None:
        """Capture stdout and display in outdisplay"""
        if len(line) != 1 or ord(line[0]) != 10:
            self.writeoutput(line.rstrip(), self.outfmt)

    @Slot(str)
    def errorwrite(self, line: str) -> None:
        """Capture stderr and display in outdisplay"""
        self.writeoutput(line, fmt=self.errfmt)

    def writeoutput(self, line: str, fmt: QTextCharFormat = None) -> None:
        """Set text formatting and display line in outdisplay"""
        # TODO: Make more efficient in handling of progress bars
        if fmt is not None:
            self.outdisplay.setCurrentCharFormat(fmt)
        else:
            self.outdisplay.setCurrentCharFormat(self.outfmt)
        if "\r" not in line:
            self.progress_bar_mode = False
        if self.progress_bar_mode:
            content = self.outdisplay.toPlainText().split("\n")
            self.outdisplay.setPlainText("\n".join(content[:-2]))
        if "\r" in line:
            self.progress_bar_mode = True
        self.outdisplay.append(line.rstrip())


class Worker(QRunnable, QObject):
    """
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
        self, workerWidget: WorkerWidget, fn, output=sys.stdout, *args, **kwargs
    ):
        QObject.__init__(self)
        QRunnable.__init__(self)
        self.workerWidget = workerWidget
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.console = output
        self.threadedStdout = ThreadedStdout()
        self.errorRedirect = Redirect(self.threadedStdout.errorwrite)
        self.setupConnections()

    def setupConnections(self):
        self.threadedStdout.lineToWorker.connect(self.workerWidget.write)
        self.threadedStdout.errorToWorker.connect(self.workerWidget.errorwrite)

    @Slot()
    def run(self):
        """
        Initialise the runner function with passed args, kwargs, and redirects the output.
        """
        with redirect_stdout(self.threadedStdout), redirect_stderr(self.errorRedirect):
            try:
                self.isStarted.emit(self.workerWidget.id)
                self.fn(*self.args, **self.kwargs)
                self.isFinished.emit(self.workerWidget.id)
            except Exception as e:
                self.isError.emit(self.workerWidget.id)
                self.workerWidget.errorwrite(str(e))
                raise e


# TODO: Delete when sendTOWorkManager is finished implemented
def toWorker(function, stdout, *args, **kwargs):
    """
    Sends a function to a worker-thread that will redirect to stdout
    """
    worker = Worker(0, function, stdout, *args, **kwargs)
    QThreadPool.globalInstance().start(worker)


# TODO: Finish and use in all thread-related operations
def sendToJobManager(
    job_title: str,
    output_directory: str,
    listview: QListWidget,
    fn,
    allow_cleanup: bool = False,
    *args,
    **kwargs,
):
    """
    Threads a function fn with arguments *args and keyword arguments **kwargs, and adds a workerWidget to the listview.
    """
    item = QListWidgetItem()
    workerWidget = WorkerWidget(
        job_title, output_directory, listview.window(), item, fn, allow_cleanup, *args, **kwargs
    )
    listview.addItem(item)
    listview.setItemWidget(item, workerWidget)
    QThreadPool.globalInstance().start(workerWidget.worker)
