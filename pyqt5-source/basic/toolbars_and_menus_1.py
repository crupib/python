import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QToolBar,
    QAction
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)
        
        # Create a toolbar
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        # Create an action (button) and connect it
        button_action = QAction("Click Me", self)
        button_action.setStatusTip("Click to print message")
        button_action.triggered.connect(self.onMyToolBarButtonClick)

        # Add the action to the toolbar
        toolbar.addAction(button_action)

    def onMyToolBarButtonClick(self):
        print("click")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

