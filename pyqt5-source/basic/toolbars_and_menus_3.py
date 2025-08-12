import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QSizePolicy  # <-- ADD THIS
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        # Create the toolbar
        toolbar = QToolBar("My main toolbar")
        toolbar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # <-- KEY LINE
        self.addToolBar(toolbar)
        self.S = "Hello"
        # Add an action to the toolbar
        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)

        # Set status bar
        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self):
        print("click", self.S)


app = QApplication(sys.argv)
window = MainWindow()
window.resize(400, 300)  # Optional: set initial size
window.show()
app.exec_()

