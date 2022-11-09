from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys

FIXED = '''
border: 2px insert rgb(85, 255, 255);
border-radius: 37px;
'''

class Ui_MainWindow(QMainWindow):
    def __init__(self ):
        super(Ui_MainWindow,self).__init__()
        uic.loadUi("design.ui",baseinstance=self, resource_suffix='_rc')
        self.show()
        self.setFixedSize(1280,720)
 
        

    def setColor(bt: QPushButton, color : str)->None:
        bt.setStyleSheet(f'background-color: {color};'+FIXED)


app = QtWidgets.QApplication(sys.argv)
ui = Ui_MainWindow()
app.exec_()