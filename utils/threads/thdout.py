import PySide6.QtCore as QtCore

class ThreadedOutput(QtCore.QObject):
    """Object to be used in redirecting standard output from a thread through signals"""

    outputLine = QtCore.Signal(str)
    outputError = QtCore.Signal(str)

    def __init__(self) -> None:
        super().__init__()

    def flush(self):
        pass

    def write(self, line: str) -> None:
        """Capture stdout and emit signal"""
        self.outputLine.emit(line)

    def errorwrite(self, line: str) -> None:
        """Capture stderr and emit signal"""
        self.outputError.emit(line)
