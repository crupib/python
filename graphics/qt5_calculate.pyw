import sys
from math import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtWidgets import (QApplication, QDialog, QLineEdit, QTextBrowser,
        QVBoxLayout)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.updateUi)
        self.setWindowTitle("Calculate")


    def updateUi(self):
        if self.lineedit.text() == "quit" :
           exit() 
        else:
           try:
               text = str(self.lineedit.text())
               self.browser.append("{0} = <b>{1}</b>".format(text,
                                   eval(text)))
           except:
               self.browser.append("<font color=red>{0} is invalid!</font>"
                                .format(text))
           self.lineedit.setText("")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
