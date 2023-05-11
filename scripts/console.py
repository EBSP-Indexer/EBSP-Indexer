"""
Interactive console widget.  Use to add an interactive python interpreter
in a GUI application.

Original code created by deanhystad, sourcecode from https://python-forum.io/thread-25117.html
"""
import code
import re

import PySide6.QtCore as QtCore
import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets


class LineEdit(QtWidgets.QLineEdit):
    """
    QLIneEdit with a history buffer for recalling previous lines.

    Signals
    -------
    newline : str
        Signal when return key pressed

    """

    newline = QtCore.Signal(str)

    def __init__(self, parent, history: int = 100) -> "LineEdit":
        """
        QLineEdit with a history buffer for recalling previous lines.
        Also accepts tab as input (4 spaces).

        Parameters
        ----------
        parent : QWidget
            The widget which contains the console widget
        history : int
            The max number of lines in the history buffer
        """
        super().__init__(parent=parent)
        self.setObjectName("consoleInput")
        self.historymax = history
        self.clearhistory()
        self.promptpattern = re.compile("^[>\.]")

    def clearhistory(self) -> None:
        """Clear history buffer"""
        self.historyindex = 0
        self.historylist = []

    def event(self, ev: QtCore.QEvent) -> bool:
        """Intercept tab and arrow key presses.  Insert 4 spaces
        when tab pressed instead of moving to next contorl.  When
        arrow up or down are pressed select a line from the history
        buffer.  Emit newline signal when return key is pressed.
        """
        if ev.type() == QtCore.QEvent.KeyPress:
            if ev.key() == int(QtCore.Qt.Key_Tab):
                self.insert("    ")
                return True
            elif ev.key() == int(QtCore.Qt.Key_Up):
                self.recall(self.historyindex - 1)
                return True
            elif ev.key() == int(QtCore.Qt.Key_Down):
                self.recall(self.historyindex + 1)
                return True
            elif ev.key() == int(QtCore.Qt.Key_Home):
                self.recall(0)
                return True
            elif ev.key() == int(QtCore.Qt.Key_End):
                self.recall(len(self.historylist) - 1)
                return True
            elif ev.key() == int(QtCore.Qt.Key_Return):
                self.returnkey()
                return True
        return super().event(ev)

    def returnkey(self) -> None:
        """Return key was pressed.  Add line to history and emit
        the newline signal.
        """
        text = self.text().rstrip()
        self.record(text)
        self.newline.emit(text)
        self.setText("")

    def recall(self, index: int) -> None:
        """Select a line from the history list"""
        length = len(self.historylist)
        if length > 0:
            index = max(0, min(index, length - 1))
            self.setText(self.historylist[index])
            self.historyindex = index

    def record(self, line: str) -> None:
        """Add line to history buffer"""
        self.historyindex += 1
        while len(self.historylist) >= self.historymax - 1:
            self.historylist.pop()
        self.historylist.append(line)
        self.historyindex = min(self.historyindex, len(self.historylist))


class Console(QtWidgets.QWidget):
    """
    A GUI version of code.InteractiveConsole.
    """

    def __init__(
        self,
        parent,
        context,
        history: int = 20,
        blockcount: int = 500,
    ) -> "Console":
        """
        A GUI version of code.InteractiveConsole.

        Parameters
        ----------
        parent : QWidget
            The widget which contains the console widget
        context : dict[str, Any]
            Specifies the dictionary in which code will be executed
        history : int
            The max number of lines in the history buffer
        blockcount : int
            The max number of lines in the output buffer
        """
        super().__init__()
        self.parent = parent
        self.setcontext(context)
        self.buffer = []
        self.progress_bar_mode = False

        # Display for output and stderr
        self.outdisplay: QtWidgets.QPlainTextEdit = self.parent.ui.consoleLog
        self.outdisplay.setMaximumBlockCount(blockcount)
        self.outdisplay.setReadOnly(True)

        # Use color to differentiate input, output and stderr
        self.inpfmt = self.outdisplay.currentCharFormat()
        self.outfmt = QtGui.QTextCharFormat(self.inpfmt)
        self.outfmt.setForeground(QtGui.QBrush(QtGui.QColor(50, 130, 234)))
        self.errfmt = QtGui.QTextCharFormat(self.inpfmt)
        self.errfmt.setForeground(QtGui.QBrush(QtGui.QColor(240, 80, 57)))
        self.setprompt(">>>")

        # Enter commands here
        self.parent.ui.consoleInput = LineEdit(
            parent=self.parent.ui.centralwidget, history=history
        )
        self.parent.ui.inputLayout.addWidget(self.parent.ui.consoleInput)
        self.inpedit = self.parent.ui.consoleInput
        self.inpedit.newline.connect(self.push)
        self.inpedit.setFrame(False)
        # self.setfont(QtGui.QFont.StyleHint.Monospace)

    def setcontext(self, context):
        """Set context for interpreter"""
        self.interp = code.InteractiveInterpreter(context)

    def resetbuffer(self) -> None:
        """Reset the input buffer."""
        self.buffer = []

    def setprompt(self, text: str):
        self.prompt = text

    def flush(self):
        pass

    def push(self, line: str) -> None:
        """Execute entered command.  Command may span multiple lines"""
        if line == "clear":
            self.inpedit.clearhistory()
            self.outdisplay.clear()
        else:
            lines = line.split("\n")
            for line in lines:
                if re.match("^[\>\.] ", line):
                    line = line[2:]
                self.writeoutput(self.prompt + line, self.inpfmt)
                self.setprompt(". ")
                self.buffer.append(line)
            # Built a command string from lines in the buffer
            source = "\n".join(self.buffer)
            more = self.interp.runsource(source, "<console>")
            if not more:
                self.setprompt(">>> ")
                self.resetbuffer()

    def setfont(self, font: QtGui.QFont) -> None:
        """Set font for input and display widgets.  Should be monospaced"""
        self.outdisplay.setFont(font)
        self.inpedit.setFont(font)

    def setscrollbarmax(self) -> None:
        sb = self.outdisplay.verticalScrollBar()
        sb.setValue(sb.maximum())

    def write(self, line: str) -> None:
        """Capture stdout and display in outdisplay"""
        if len(line) != 1 or ord(line[0]) != 10:
            self.writeoutput(line.rstrip(), self.outfmt)

    def errorwrite(self, line: str) -> None:
        """Capture stderr and display in outdisplay"""
        self.writeoutput(line, fmt=self.errfmt)

    def writeoutput(self, line: str, fmt: QtGui.QTextCharFormat = None) -> None:
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
            self.setscrollbarmax()
        if not self.progress_bar_mode:
            sb = self.outdisplay.verticalScrollBar()
            sb.setValue(sb.maximum())
        self.outdisplay.appendPlainText(line.rstrip())
