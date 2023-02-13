import os
from typing import Callable
from datetime import timedelta

from PySide6.QtCore import (
    QThreadPool,
    Slot,
    Signal,
    QElapsedTimer,
    QTimer,
)
from PySide6.QtWidgets import QMainWindow, QWidget, QListWidget, QListWidgetItem
from PySide6.QtGui import QPixmap, QTextCharFormat, QBrush, QColor

from utils.threads.worker import Worker
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
        mainWindow: QMainWindow,
        jobItem: QListWidgetItem,
        func: Callable,
        allow_cleanup: bool = False,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(parent=mainWindow)
        WorkerWidget.counter += 1
        self.id = WorkerWidget.counter
        self.worker = Worker(self, func, *args, **kwargs)
        self.ui = Ui_WorkerWidget()
        self.time = QElapsedTimer()
        self.timer = QTimer()

        self.allow_cleanup = allow_cleanup
        self.job_title = job_title
        self.output_directory = output_directory
        self.jobItem = jobItem
        self.progress_bar_mode = False
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
        self.removeMeSignal.connect(self.window().removeWorker)
        self.timer.timeout.connect(self.updateTimerDisplay)
        self.worker.isStarted.connect(self.time_worker)
        self.worker.isFinished.connect(self.finalize)
        self.worker.isError.connect(
            lambda id: self.finalize(id, failed=True, cleanup=self.allow_cleanup)
        )

    def updateActiveJobs(self):
        print("HELLO THIS IS WRONG", self.window())
        self.window().updateActiveJobs()

    def sendRemoveItem(self):
        self.removeMeSignal.emit(self.id)

    def sendCancelWorker(self):
        if QThreadPool.globalInstance().tryTake(self.worker):
            self.finalize(id=self.id, cancelled=True, cleanup=self.allow_cleanup)
        else:
            self.ui.pushButtonCancel.setDisabled(True)

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
            self.ui.pushButtonCancel.setDisabled(True)

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
        *args,
        **kwargs,
    )
    listview.addItem(item)
    listview.setItemWidget(item, workerWidget)
    QThreadPool.globalInstance().start(workerWidget.worker)
