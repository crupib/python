import sys
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
   QApplication,
   QMainWindow,
   QLabel,
)
basedir = os.path.dirname(__file__)
print("Current working folder:",os.getcwd())
print("Paths are relative to:", basedir)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("My APP 10")
		widget = QLabel("Hello")
		widget.setPixmap(QPixmap(os.path.join(basedir,"einstein.jpg")))
		self.setCentralWidget(widget)
		widget.setScaledContents(True)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
