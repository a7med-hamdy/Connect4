# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\study\third year\first term\AI\Assignments\Connect4\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("font: 75 10pt \"Consolas\";\n"
"background-color:rgb(0, 0, 40);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"    position: absolute;\n"
"    top: -0.5em;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(170, 0, 0);\n"
"    border: 1px solid white;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(330, 110, 621, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(15)
        self.grid.setObjectName("grid")
        self.l40 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l40.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l40.setText("")
        self.l40.setObjectName("l40")
        self.grid.addWidget(self.l40, 1, 0, 1, 1)
        self.l06 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l06.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l06.setText("")
        self.l06.setObjectName("l06")
        self.grid.addWidget(self.l06, 5, 7, 1, 1)
        self.l33 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l33.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l33.setText("")
        self.l33.setObjectName("l33")
        self.grid.addWidget(self.l33, 2, 3, 1, 1)
        self.l13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l13.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l13.setText("")
        self.l13.setObjectName("l13")
        self.grid.addWidget(self.l13, 4, 3, 1, 1)
        self.l12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l12.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l12.setText("")
        self.l12.setObjectName("l12")
        self.grid.addWidget(self.l12, 4, 2, 1, 1)
        self.l04 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l04.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l04.setText("")
        self.l04.setObjectName("l04")
        self.grid.addWidget(self.l04, 5, 5, 1, 1)
        self.l14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l14.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l14.setText("")
        self.l14.setObjectName("l14")
        self.grid.addWidget(self.l14, 4, 5, 1, 1)
        self.l24 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l24.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l24.setText("")
        self.l24.setObjectName("l24")
        self.grid.addWidget(self.l24, 3, 5, 1, 1)
        self.l01 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l01.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l01.setText("")
        self.l01.setObjectName("l01")
        self.grid.addWidget(self.l01, 5, 1, 1, 1)
        self.l03 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l03.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l03.setText("")
        self.l03.setObjectName("l03")
        self.grid.addWidget(self.l03, 5, 3, 1, 1)
        self.l11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l11.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l11.setText("")
        self.l11.setObjectName("l11")
        self.grid.addWidget(self.l11, 4, 1, 1, 1)
        self.l25 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l25.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l25.setText("")
        self.l25.setObjectName("l25")
        self.grid.addWidget(self.l25, 3, 6, 1, 1)
        self.l52 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l52.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l52.setText("")
        self.l52.setObjectName("l52")
        self.grid.addWidget(self.l52, 0, 2, 1, 1)
        self.l42 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l42.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l42.setText("")
        self.l42.setObjectName("l42")
        self.grid.addWidget(self.l42, 1, 2, 1, 1)
        self.l41 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l41.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l41.setText("")
        self.l41.setObjectName("l41")
        self.grid.addWidget(self.l41, 1, 1, 1, 1)
        self.l00 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l00.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l00.setText("")
        self.l00.setObjectName("l00")
        self.grid.addWidget(self.l00, 5, 0, 1, 1)
        self.l50 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l50.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l50.setText("")
        self.l50.setObjectName("l50")
        self.grid.addWidget(self.l50, 0, 0, 1, 1)
        self.l16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l16.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l16.setText("")
        self.l16.setObjectName("l16")
        self.grid.addWidget(self.l16, 4, 7, 1, 1)
        self.l10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l10.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l10.setText("")
        self.l10.setObjectName("l10")
        self.grid.addWidget(self.l10, 4, 0, 1, 1)
        self.l23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l23.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l23.setText("")
        self.l23.setObjectName("l23")
        self.grid.addWidget(self.l23, 3, 3, 1, 1)
        self.l31 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l31.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l31.setText("")
        self.l31.setObjectName("l31")
        self.grid.addWidget(self.l31, 2, 1, 1, 1)
        self.l22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l22.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l22.setText("")
        self.l22.setObjectName("l22")
        self.grid.addWidget(self.l22, 3, 2, 1, 1)
        self.l30 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l30.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l30.setText("")
        self.l30.setObjectName("l30")
        self.grid.addWidget(self.l30, 2, 0, 1, 1)
        self.l05 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l05.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l05.setText("")
        self.l05.setObjectName("l05")
        self.grid.addWidget(self.l05, 5, 6, 1, 1)
        self.l26 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l26.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l26.setText("")
        self.l26.setObjectName("l26")
        self.grid.addWidget(self.l26, 3, 7, 1, 1)
        self.l15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l15.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l15.setText("")
        self.l15.setObjectName("l15")
        self.grid.addWidget(self.l15, 4, 6, 1, 1)
        self.l32 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l32.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l32.setText("")
        self.l32.setObjectName("l32")
        self.grid.addWidget(self.l32, 2, 2, 1, 1)
        self.l21 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l21.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l21.setText("")
        self.l21.setObjectName("l21")
        self.grid.addWidget(self.l21, 3, 1, 1, 1)
        self.l02 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l02.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l02.setText("")
        self.l02.setObjectName("l02")
        self.grid.addWidget(self.l02, 5, 2, 1, 1)
        self.l20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l20.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l20.setText("")
        self.l20.setObjectName("l20")
        self.grid.addWidget(self.l20, 3, 0, 1, 1)
        self.l51 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l51.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l51.setText("")
        self.l51.setObjectName("l51")
        self.grid.addWidget(self.l51, 0, 1, 1, 1)
        self.l34 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l34.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l34.setText("")
        self.l34.setObjectName("l34")
        self.grid.addWidget(self.l34, 2, 5, 1, 1)
        self.l35 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l35.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l35.setText("")
        self.l35.setObjectName("l35")
        self.grid.addWidget(self.l35, 2, 6, 1, 1)
        self.l36 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l36.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l36.setText("")
        self.l36.setObjectName("l36")
        self.grid.addWidget(self.l36, 2, 7, 1, 1)
        self.l43 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l43.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l43.setText("")
        self.l43.setObjectName("l43")
        self.grid.addWidget(self.l43, 1, 3, 1, 1)
        self.l44 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l44.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l44.setText("")
        self.l44.setObjectName("l44")
        self.grid.addWidget(self.l44, 1, 5, 1, 1)
        self.l45 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l45.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l45.setText("")
        self.l45.setObjectName("l45")
        self.grid.addWidget(self.l45, 1, 6, 1, 1)
        self.l46 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l46.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l46.setText("")
        self.l46.setObjectName("l46")
        self.grid.addWidget(self.l46, 1, 7, 1, 1)
        self.l53 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l53.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l53.setText("")
        self.l53.setObjectName("l53")
        self.grid.addWidget(self.l53, 0, 3, 1, 1)
        self.l54 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l54.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l54.setText("")
        self.l54.setObjectName("l54")
        self.grid.addWidget(self.l54, 0, 5, 1, 1)
        self.l55 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l55.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l55.setText("")
        self.l55.setObjectName("l55")
        self.grid.addWidget(self.l55, 0, 6, 1, 1)
        self.l56 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l56.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"border: 2px insert rgb(85, 255, 255);\n"
"border-radius: 37px;")
        self.l56.setText("")
        self.l56.setObjectName("l56")
        self.grid.addWidget(self.l56, 0, 7, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, -21, 1441, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setStyleSheet("color: yellow;\n"
"font-size: 20px;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.player_score = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.player_score.setStyleSheet("color: rgb(255, 170, 0);\n"
"font-size: 30px;")
        self.player_score.setObjectName("player_score")
        self.horizontalLayout.addWidget(self.player_score)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("color: yellow;\n"
"font-size: 20px;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.turn = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.turn.setStyleSheet("color: rgb(255, 170, 0);\n"
"font-size: 30px;")
        self.turn.setText("")
        self.turn.setObjectName("turn")
        self.horizontalLayout.addWidget(self.turn)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setStyleSheet("color: yellow;\n"
"font-size: 20px;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.ai_score = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.ai_score.setStyleSheet("color: rgb(255, 170, 0);\n"
"font-size: 30px;")
        self.ai_score.setObjectName("ai_score")
        self.horizontalLayout.addWidget(self.ai_score)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(320, 100, 641, 561))
        self.frame.setStyleSheet("border: 2px solid white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(90, 270, 201, 41))
        self.spinBox.setStyleSheet("color: yellow;\n"
"font-size: 25px;")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000000000)
        self.spinBox.setObjectName("spinBox")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(28, 370, 271, 51))
        self.comboBox.setStyleSheet("background-color: white;\n"
"font-size: 20px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(320, 30, 641, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(8, 0, 8, 0)
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt0 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.bt0.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.bt0.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.bt0.setObjectName("bt0")
        self.horizontalLayout_2.addWidget(self.bt0)
        self.bt1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.bt1.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.bt1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.bt1.setObjectName("bt1")
        self.horizontalLayout_2.addWidget(self.bt1)
        self.bt2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.bt2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.bt2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.bt2.setObjectName("bt2")
        self.horizontalLayout_2.addWidget(self.bt2)
        self.bt3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.bt3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.bt3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.bt3.setObjectName("bt3")
        self.horizontalLayout_2.addWidget(self.bt3)
        self.bt4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.bt4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.bt4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.bt4.setObjectName("bt4")
        self.horizontalLayout_2.addWidget(self.bt4)
        self.bt5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.bt5.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.bt5.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.bt5.setObjectName("bt5")
        self.horizontalLayout_2.addWidget(self.bt5)
        self.bt6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.bt6.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.bt6.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.bt6.setObjectName("bt6")
        self.horizontalLayout_2.addWidget(self.bt6)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 270, 51, 41))
        self.label_2.setStyleSheet("color: yellow;\n"
"font-size: 50px;")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(20, 0, 271, 61))
        self.frame_2.setStyleSheet("border: 2px solid white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.tab)
        self.frame_3.setGeometry(QtCore.QRect(990, 0, 271, 61))
        self.frame_3.setStyleSheet("border: 2px solid white;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.gridLayoutWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.spinBox.raise_()
        self.comboBox.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.label_2.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Player Score"))
        self.player_score.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Turn"))
        self.label_3.setText(_translate("MainWindow", "AI score"))
        self.ai_score.setText(_translate("MainWindow", "0"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MinMax"))
        self.comboBox.setItemText(1, _translate("MainWindow", "MinMax with pruning"))
        self.bt0.setText(_translate("MainWindow", "insert"))
        self.bt1.setText(_translate("MainWindow", "insert"))
        self.bt2.setText(_translate("MainWindow", "insert"))
        self.bt3.setText(_translate("MainWindow", "insert"))
        self.bt4.setText(_translate("MainWindow", "insert"))
        self.bt5.setText(_translate("MainWindow", "insert"))
        self.bt6.setText(_translate("MainWindow", "insert"))
        self.label_2.setText(_translate("MainWindow", "K:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Game"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tree"))
