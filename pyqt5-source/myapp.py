from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,)
import sys
class MainWindow(QMainWindow):
  def __init__(self):
      super().__init__()
      self.setWindowTitle("My App")
      button = QPushButton("Press Me!")
      self.setCentralWidget(button)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
