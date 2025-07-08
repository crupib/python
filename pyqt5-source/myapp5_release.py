import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
   QApplication,
   QMainWindow,
   QPushButton
)
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.button_is_checked = True
		self.setWindowTitle("My APP 5")
		self.button = QPushButton("Push Me!")
		self.button.setCheckable(True)
		self.button.released.connect(self.the_button_was_released)
		self.button.setChecked(self.button_is_checked)
		self.setCentralWidget(self.button)
	def the_button_was_released(self):
		print("Button was released")
		self.button_is_checked = self.button.isChecked()
		print(self.button_is_checked)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
