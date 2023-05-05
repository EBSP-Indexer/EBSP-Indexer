import os
from typing import Callable
from datetime import timedelta

from PySide6.QtCore import QThreadPool, Slot, Signal, QElapsedTimer, QTimer, QSize
from PySide6.QtWidgets import QMainWindow, QWidget, QListWidget, QListWidgetItem
from PySide6.QtGui import QTextCharFormat, QBrush, QColor

from utils.threads.worker import Worker
from ui.ui_worker_widget import Ui_WorkerWidget


class WorkerWidget(QWidget):
    """
    Widget displaying information about a worker

    Signals
    ---------
    removeMeSignal : Signal(int)
        Emits the id of the worker widget which is to be removed

    Attributes
    ---------
    worker : Worker
        The worker associated with the worker widget
    id : int
        Unique number used to identify communication across signals between worker, worker widget and job manager
    job_title : str
        The title of the job that is to be executed by the worker
    output_directory : str
        The location where results will appear
    job_item : QListWidgetItem
        The item in the job manager list which contains the worker widget, is resized when the worker widget is resized.
    allow_cleanup : bool
        If the output_directory should be deleted if the task of the worker fails or is cancelled
    ui : Ui_WorkerWidget
        User interface used by the class
    """

    counter = 0
    removeMeSignal = Signal(int)

    # TODO: mainWindow should be replaced by a jobManagerList class
    def __init__(
        self,
        job_title: str,
        output_directory: str,
        mainWindow: QMainWindow,
        jobItem: QListWidgetItem,
        func: Callable,
        allow_cleanup: bool = False,
        allow_logging: bool = False,
        *args,
        **kwargs,
    ) -> None:
        """
        Parameters
        ---------
        job_title : str
            The title of the job that is to be executed by the worker
        output_directory : str
            The location where results will appear
        mainWindow : AppWindow
            The main app winow which contains the job manager (should be replaced by the job manager list later)
        job_item : QListWidgetItem
            The item in the job manager list which contains the worker widget, is resized when the worker widget is resized.
        func : Callable
            The function callback to run on this worker thread,
            Supplied args and kwargs will be passed through to the runner
        allow_cleanup : bool, optional
            If the output_directory should be deleted if the task of the worker fails or is cancelled (default is False)
        args : tuple
            Arguments to pass to the callback function
        kwargs: dict[str, Any]
            Keywords to pass to the callback function
        """

        super().__init__(parent=mainWindow)
        WorkerWidget.counter += 1
        self.id = WorkerWidget.counter
        self.worker = Worker(self, func, *args, **kwargs)
        self.ui = Ui_WorkerWidget()
        self.time = QElapsedTimer()
        self.timer = QTimer()

        self.allow_cleanup = allow_cleanup
        self.allow_logging = allow_logging
        self.job_title = job_title
        self.output_directory = output_directory
        self.jobItem = jobItem
        self.progress_bar_mode = False
        self.ui.setupUi(self)
        self.setupConnections()
        self.outdisplay = self.ui.textBrowserStatus
        # Show Job Manager if hidden
        dw = self.parentWidget().ui.dockWidgetJobManager
        if dw.isHidden():
            dw.setVisible(True)
        dw.raise_()
        

    def setupConnections(self):
        # UI
        self.ui.labelJobNumber.setText(f"Job {self.id} | {self.job_title}")
        self.ui.labelJobName.setText(f"{self.job_title}")
        self.ui.labelOutput.setText(f"{self.output_directory}")
        self.adjustSize(show=True)
        self.inpfmt = self.ui.textBrowserStatus.currentCharFormat()
        self.outfmt = QTextCharFormat(self.inpfmt)
        self.outfmt.setForeground(QBrush(QColor(50, 130, 234)))
        self.errfmt = QTextCharFormat(self.inpfmt)
        self.errfmt.setForeground(QBrush(QColor(240, 80, 57)))

        # Signals
        self.ui.pushButtonRemove.clicked.connect(self.sendRemoveItem)
        self.ui.pushButtonCancel.clicked.connect(self.sendCancelWorker)
        self.ui.pushButtonShow.toggled.connect(lambda show: self.adjustSize(show))
        self.removeMeSignal.connect(self.window().removeWorker)
        self.timer.timeout.connect(self.updateTimerDisplay)
        self.worker.isStarted.connect(self.time_worker)
        self.worker.isFinished.connect(
            lambda id: self.finalize(id, logging=self.allow_logging)
        )
        self.worker.isError.connect(
            lambda id: self.finalize(
                id, failed=True, cleanup=False, logging=self.allow_logging
            )
        )

    def updateActiveJobs(self):
        self.window().updateActiveJobs()

    def sendRemoveItem(self):
        self.removeMeSignal.emit(self.id)

    def sendCancelWorker(self):
        if QThreadPool.globalInstance().tryTake(self.worker):
            self.finalize(id=self.id, cancelled=True, cleanup=self.allow_cleanup)
        else:
            self.ui.pushButtonCancel.setDisabled(True)
            self.ui.pushButtonCancel.setHidden(True)

    # TODO resize jobItem in a job manager class instead so it can be removed from this class
    def adjustSize(self, show):
        super().adjustSize()
        if show:
            self.jobItem.setSizeHint(self.sizeHint() - QSize(100, 50))
        else:
            self.jobItem.setSizeHint(self.sizeHint() - QSize(100, 0))

    @Slot(int)
    def time_worker(self, id):
        if self.id == id:
            self.ui.labelTime.setStyleSheet("QLabel { color: rgb(240, 80, 57); }")
            self.time.start()
            self.updateTimerDisplay()
            self.timer.start(500)
            self.ui.pushButtonCancel.setDisabled(True)
            self.ui.pushButtonCancel.setHidden(True)

    @Slot(int)
    def finalize(
        self,
        id: int,
        failed: bool = False,
        cancelled: bool = False,
        cleanup: bool = False,
        logging: bool = False,
    ):
        """
        #TODO Description here

        Cleanup can only remove empty directories for safety reasons
        """
        if self.id == id:
            self.timer.stop()
            self.ui.pushButtonRemove.setEnabled(True)
            if failed:
                self.ui.labelTime.setStyleSheet("QLabel { color : rgb(240, 80, 57); }")
                self.ui.labelTime.setText(f"Failed in {self.ui.labelTime.text()}")
            elif cancelled:
                self.ui.labelTime.setStyleSheet("QLabel { color : rgb(50, 130, 234); }")
                self.ui.labelTime.setText(f"Cancelled")
            else:
                self.ui.labelTime.setStyleSheet("QLabel { color : rgb(50, 130, 234); }")
                self.ui.labelTime.setText(f"Completed in {self.ui.labelTime.text()}")
            if cleanup:
                try:
                    os.rmdir(path=self.output_directory)
                except Exception as e:
                    self.errorwrite(f"Cleanup failed:\n{e}")
            if logging:
                path = os.path.join(self.output_directory, "log.txt")
                try:
                    self.file = open(path, "w")
                    self.file.write("----------- OUTPUT LOG -----------\n")
                    self.file.write(self.outdisplay.toPlainText())
                    self.file.close()
                except Exception as e:
                    raise e
            self.updateActiveJobs()

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
            sb = self.outdisplay.verticalScrollBar()
            sb.setValue(sb.maximum())
        if not self.progress_bar_mode:
            sb = self.outdisplay.verticalScrollBar()
            sb.setValue(sb.maximum())
        self.outdisplay.append(line.rstrip())


# TODO: Finish and use in all thread-related operations
def sendToJobManager(
    job_title: str,
    output_path: str,
    listview: QListWidget,
    func: Callable,
    allow_cleanup: bool = False,
    allow_logging: bool = False,
    *args,
    **kwargs,
):
    """
    Method for threading a function func with arguments *args and keyword arguments **kwargs, and adds a workerWidget to the listview.
    """
    item = QListWidgetItem()
    workerWidget = WorkerWidget(
        job_title,
        output_path,
        listview.window(),
        item,
        func,
        allow_cleanup,
        allow_logging,
        *args,
        **kwargs,
    )
    listview.addItem(item)
    listview.setItemWidget(item, workerWidget)
    QThreadPool.globalInstance().start(workerWidget.worker)
