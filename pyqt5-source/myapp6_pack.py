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
		self.setWindowTitle("My APP 6")
		self.button = QPushButton("Press Me!")
		self.button.clicked.connect(self.the_button_was_clicked)
		self.setCentralWidget(self.button)
	def the_button_was_clicked(self):
		self.button.setText("You already clicked me.")
		self.button.setEnabled(False)
		self.setWindowTitle("My Oneshot App")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
