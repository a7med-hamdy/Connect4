from functools import partial
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

EMPTY = "empty"
RED = "red"
YELLOW = "yellow"



ROWS = 6
COLS = 7



class Ui_MainWindow(QMainWindow):
    def __init__(self ):
        super(Ui_MainWindow,self).__init__()
        uic.loadUi("design.ui",baseinstance=self, resource_suffix='_rc')
        self.show()
        self.setFixedSize(1280,720)

        self.color = RED
        self.labels = [[None for _ in range(7)]for _ in range(6)]
        self.buttons = [None for _ in range(7)]
        self.turn_label = self.findChild(QLabel, "turn")
        self.turn_label.setText("Human")

        for i in range(ROWS):
            for j in range (COLS):
                if i == 0:
                    self.buttons[j] = self.findChild(QPushButton, "bt" + str(j))
                    self.buttons[j].clicked.connect(partial(self.handleButton, int(self.buttons[j].objectName()[-1])))
                self.labels[i][j] = self.findChild(QLabel, "l" + str(i) + str(j))
                self.labels[i][j].setProperty("state", EMPTY)
        

    def setColor(self, bt: QLabel)->None:
        bt.setStyleSheet(f'background-color: {self.color};'+FIXED)
        bt.setProperty("state", self.color)
        self.switchTurn()
    
    def handleButton(self, column : int):
        for i in range(ROWS):
            if self.labels[i][column].property("state") == EMPTY:
                self.setColor(self.labels[i][column])
                break

    def switchTurn(self):
        if self.color == RED:
            self.color = YELLOW
            self.turn_label.setText("AI")
        else:
            self.color = RED
            self.turn_label.setText("Human")

app = QtWidgets.QApplication(sys.argv)
ui = Ui_MainWindow()
app.exec_()