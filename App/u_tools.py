# -*- coding: utf-8 -*-
from PyQt5.QtCore import QUrl
from PyQt5.QtQml import QQmlApplicationEngine
class UTools():                               # Creation of the Python class.
    def __init__(self):                       # Constructor of the class.
        self.us1 = "QML with Python."

    def u_qml(self):
	self.qwid = QQmlApplicationEngine()
	self.qwid.load(QUrl('u_qml.qml'))

if __name__ == "__main__":                    # If file will start from
    ut = UTools()                             # terminal/cmd, etc., create

