# PySide2 tutorial 1


import sys
from PySide2 import QtWidgets


app = QtWidgets.QApplication(sys.argv)

hello = QtWidgets.QPushButton("Hello world!")
hello.resize(100, 30)

hello.show()

sys.exit(app.exec_())

