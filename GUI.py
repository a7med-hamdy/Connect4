from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from plot import Plotter
from utilities import utilities
from state import state
from search import search
import time

FIXED = '''
border: 2px insert rgb(85, 255, 255);
border-radius: 37px;
'''

EMPTY = "rgb(212, 212, 212)"
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
    
        
        self.util = utilities()

        
        self.labels = [[None for _ in range(7)]for _ in range(6)]
        self.buttons = [None for _ in range(7)]
        self.turn_label = self.findChild(QLabel, "turn")
        self.restart_button = self.findChild(QToolButton, "toolButton")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("restart.png"),
                                          QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restart_button.setIcon(icon)
        self.restart_button.clicked.connect(self.restart)

        self.human_score_label = self.findChild(QLabel, "player_score")
        self.ai_score_label = self.findChild(QLabel, "ai_score")
        self.nodes = self.findChild(QLabel, "lb_nodes")
        self.time = self.findChild(QLabel, "lb_time")

        self.spin = self.findChild(QSpinBox, "spinBox")
        self.combo = self.findChild(QComboBox, "comboBox")

        self.Tabs = self.findChild(QTabWidget, "tabWidget")
        self.plotter = Plotter()
        layout = QVBoxLayout()
        layout.addWidget(self.plotter)
        self.Tabs.widget(1).setLayout(layout)

        for i in range(ROWS):
            for j in range (COLS):
                if i == 0:
                    self.buttons[j] = self.findChild(QPushButton, "bt" + str(j))
                    self.buttons[j].clicked.connect(partial(self.handleButton, int(self.buttons[j].objectName()[-1])))
                self.labels[i][j] = self.findChild(QLabel, "l" + str(i) + str(j))
                self.labels[i][j].setProperty("state", EMPTY)

        self.restart()

    def restart(self):
        self.board = 0
        self.remaining = 42
        self.color = EMPTY
        self.turn_label.setText("Human")
        for i in range(ROWS):
            for j in range (COLS):
                self.labels[i][j].setProperty("state", EMPTY)
                self.setColor(self.labels[i][j])
        self.color = RED
        self.human_score_label.setText(str(0))
        self.ai_score_label.setText(str(0))
        self.time.setText("")
        self.nodes.setText("")


    def setColor(self, lb: QLabel)->None:
        lb.setStyleSheet(f'background-color: {self.color};'+FIXED)
        lb.setProperty("state", self.color)
        self.remaining -= 1
    
    def handleButton(self, column : int)->None:
        found = False
        for i in range(ROWS):
            if self.labels[i][column].property("state") == EMPTY:
                self.setColor(self.labels[i][column])
                found = True
                self.calcScore(i, column)
                break
        if found:
            self.switchTurn(column)
        else:
            print(f"chosen a filled column {column}")

    def switchTurn(self, column: int)-> None:
        if self.color == RED:
            self.color = YELLOW
            self.turn_label.setText("AI")
            k = self.spin.value()
            z = self.combo.currentIndex()
            
            self.board = self.util.update(self.board, column)
            # Create state and search
            stat = state(self.board, column, int(self.ai_score_label.text()), int(self.human_score_label.text()))
            S = search()

            start = end = 0
            # AI makes the move and time is measured
            app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
            if z == 1:
                start = time.time()
                stat = S.search(stat, "AI", k)
                end = time.time()
            else:
                start = time.time()
                stat = S.search(stat, "AI", k, alpha= None, beta= None)
                end = time.time()
            app.restoreOverrideCursor()

            maxs = []
            mins = []
            lbs = []
            unique = []
            terminal = []

            for k in S.tree_nodes:
                lbs.append(k[1])
                unique.append(int(k[0]))
                if(k[2] == "max"):
                    maxs.append(int(k[0]))
                elif(k[2] == "min"):
                    mins.append(int(k[0]))
                else:
                    terminal.append(int(k[0]))

            E = S.tree_edges

            
            self.time.setText(str(end-start) + " sec")
            self.nodes.setText(str(len(S.tree_nodes)))
            self.plotter.set_param(lbs, [tuple(int(item) for item in t) for t in E],
             unique, self.combo.currentText(), maxs, mins, terminal)

            self.board = stat.board
            # make AI move
            self.handleButton(stat.col)
        else:
            self.color = RED
            self.turn_label.setText("Human")

    def calcScore(self, i : int , j : int)->None:
        tmp = 0

        counter_down = 0
        #check down
        i_new = i-1
        while(i_new >= 0):
            if(self.labels[i][j].property("state") == self.labels[i_new][j].property("state")):
                counter_down += 1
            else:
                break
            i_new -= 1
        if counter_down >= 3:
            tmp += 1

        counter_left = 0
        #check left
        j_new = j-1
        while(j_new >= 0):
            if(self.labels[i][j].property("state") == self.labels[i][j_new].property("state")):
                counter_left += 1
            else:
                break
            j_new -= 1


        counter_right = 0
        #check right
        j_new = j+1
        while(j_new < COLS):
            if(self.labels[i][j].property("state") == self.labels[i][j_new].property("state")):
                counter_right += 1
            else:
                break
            j_new += 1

        if counter_left + counter_right >= 3:
            if counter_left + counter_right == 3:
                tmp += 1
            elif counter_left + counter_right == 4:
                if counter_left == 0 or counter_right == 0:
                    tmp += 1
                else:
                    tmp += 2
            elif counter_left + counter_right == 5:
                if counter_left == 0 or counter_right == 0:
                    tmp += 1
                elif counter_left == 1 or counter_right == 1:
                    tmp += 2
                else:
                    tmp += 3
            elif counter_left + counter_right == 6:
                if counter_left == 0 or counter_right == 0:
                    tmp += 1
                elif counter_left == 1 or counter_right == 1:
                    tmp += 2
                elif counter_left == 2 or counter_right == 2:
                    tmp += 3
                else:
                    tmp += 4
            else:
                print("unexpected score error")

        counter_down_left = 0
        #check down left
        j_new = j-1
        i_new = i-1
        while(j_new >= 0 and i_new >= 0):
            if(self.labels[i][j].property("state") == self.labels[i_new][j_new].property("state")):
                counter_down_left += 1
            else:
                break
            i_new -= 1
            j_new -= 1


        counter_down_right = 0
        #check down right
        j_new = j+1
        i_new = i-1
        while(j_new < COLS and i_new >= 0):
            if(self.labels[i][j].property("state") == self.labels[i_new][j_new].property("state")):
                counter_down_right += 1
            else:
                break
            i_new -= 1
            j_new += 1



        counter_up_left = 0
        #check up left
        j_new = j-1
        i_new = i+1
        while(j_new >= 0 and i_new < ROWS):
            if(self.labels[i][j].property("state") == self.labels[i_new][j_new].property("state")):
                counter_up_left += 1
            else:
                break
            i_new += 1
            j_new -= 1

 

        counter_up_right = 0
        #check up right
        j_new = j+1
        i_new = i+1
        while(j_new < COLS and i_new < ROWS):
            if(self.labels[i][j].property("state") == self.labels[i_new][j_new].property("state")):
                counter_up_right += 1
            else:
                break
            i_new += 1
            j_new += 1


        if counter_down_left + counter_up_right >= 3:
            if counter_down_left + counter_up_right == 3:
                tmp += 1
            elif counter_down_left + counter_up_right == 4:
                if counter_down_left == 0 or counter_up_right == 0:
                    tmp += 1
                else:
                    tmp += 2
            elif counter_down_left + counter_up_right == 5:
                if counter_down_left == 0 or counter_up_right == 0:
                    tmp += 1
                elif counter_down_left == 1 or counter_up_right == 1:
                    tmp += 2
                else:
                    tmp += 3
            elif counter_down_left + counter_up_right == 6:
                if counter_down_left == 0 or counter_up_right == 0:
                    tmp += 1
                elif counter_down_left == 1 or counter_up_right == 1:
                    tmp += 2
                elif counter_down_left == 2 or counter_up_right == 2:
                    tmp += 3
                else:
                    tmp += 4
            else:
                print("unexpected score error")



        if counter_down_right + counter_up_left >= 3:
            if counter_down_right + counter_up_left == 3:
                tmp += 1
            elif counter_down_right + counter_up_left == 4:
                if counter_down_right == 0 or counter_up_left == 0:
                    tmp += 1
                else:
                    tmp += 2
            elif counter_down_right + counter_up_left == 5:
                if counter_down_right == 0 or counter_up_left == 0:
                    tmp += 1
                elif counter_down_right == 1 or counter_up_left == 1:
                    tmp += 2
                else:
                    tmp += 3
            elif counter_down_right + counter_up_left == 6:
                if counter_down_right == 0 or counter_up_left == 0:
                    tmp += 1
                elif counter_down_right == 1 or counter_up_left == 1:
                    tmp += 2
                elif counter_down_right == 2 or counter_up_left == 2:
                    tmp += 3
                else:
                    tmp += 4
            else:
                print("unexpected score error")

        
        if self.color == RED:
            curr = int(self.human_score_label.text())
            self.human_score_label.setText(str(curr+tmp))
        else:
            curr = int(self.ai_score_label.text())
            self.ai_score_label.setText(str(curr+tmp))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ui = Ui_MainWindow()
    app.exec_()