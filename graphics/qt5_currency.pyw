import sys
import urllib.request
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtWidgets import (QApplication, QDialog, QLineEdit, QTextBrowser,
        QVBoxLayout, QLabel, QComboBox, QDoubleSpinBox, QGridLayout)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.create_widgets()
        self.layout_widgets()
        self.create_connections()
        self.prepare()
        self.setWindowTitle("Currency")


    def create_widgets(self):
        self.dateLabel = QLabel()
        self.fromComboBox = QComboBox()
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 10000000.00)
        self.fromSpinBox.setValue(1.00)
        self.toComboBox = QComboBox()
        self.toLabel = QLabel("1.00")


    def layout_widgets(self):
        grid = QGridLayout()
        grid.addWidget(self.dateLabel, 0, 0)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        self.setLayout(grid)


    def create_connections(self):
        self.fromComboBox.currentIndexChanged.connect(self.updateUi)
        self.toComboBox.currentIndexChanged.connect(self.updateUi)
        self.fromSpinBox.valueChanged.connect(self.updateUi)


    def prepare(self):
        date = self.getdata()
        self.dateLabel.setText(date)
        rates = sorted(self.rates.keys())
        self.fromComboBox.addItems(rates)
        self.toComboBox.addItems(rates)


    def updateUi(self):
        to = str(self.toComboBox.currentText())
        from_ = str(self.fromComboBox.currentText())
        if to and from_:
            amount = ((self.rates[from_] / self.rates[to]) *
                    self.fromSpinBox.value())
            self.toLabel.setText("{0:.2f}".format(amount))

    def getdata(self): # Idea taken from the Python Cookbook
        self.rates = {}
        descflag = "n"
        try:
            date = "Unknown"
            fh = urllib.request.urlopen("https://www.bankofcanada.ca/valet/observations/group/FX_RATES_DAILY/csv?start_date=2022-05-17")
            for line in fh:
                line = line.rstrip()
                fields = line.split(b',')
                if line.startswith(b'"id"'):
                   print("found id")
                   descflag = "y"
                elif descflag == "y" :
                     print(fields[-1].decode("utf-8"))
                     print(fields[1].decode("utf-8"))
                     print(fields[0].decode("utf-8"))
                else:
                     continue
            return "Exchange Rates Date: " + str(date)
        except ValueError:
            return "Failed to download:\n{0}".format(ValueError)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()

