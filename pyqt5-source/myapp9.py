import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
   QApplication,
   QMainWindow,
   QLabel,
)
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("My APP 9")
		widget = QLabel("Hello")
		font = widget.font()
		font.setPointSize(30)
		widget.setFont(font)
		widget.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
		self.setCentralWidget(widget)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
