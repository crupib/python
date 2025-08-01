import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
   QApplication,
   QMainWindow,
   QLabel,
)
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("My APP 10")
		widget = QLabel("Hello")
		widget.setPixmap(QPixmap("einstein.jpg"))
		self.setCentralWidget(widget)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
