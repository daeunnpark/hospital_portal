# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# This is generated from .ui files.
# command line: exec python3 -m PyQt5.uic.pyuic first.ui -o fisrt.py -x to convert .ui file to .py file

from PyQt5 import QtCore, QtGui, QtWidgets

class login_page(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 120, 403, 22))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(340, 270, 103, 153))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 460, 114, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_5.clicked.connect(self.changeUI_to_Menu) # set listener
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Welcome to Healthcare United Patient Portal</span></p><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Patient"))
        self.pushButton_2.setText(_translate("MainWindow", "Doctor"))
        self.pushButton_3.setText(_translate("MainWindow", "Nurse"))
        self.pushButton_4.setText(_translate("MainWindow", "Admin"))
        self.pushButton_5.setText(_translate("MainWindow", "Login"))

    def changeUI_to_Menu(self): # change UI to Menu
        ui = Ui_Menu()
        ui.setupUi(MainWindow)
        MainWindow.show()

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(600, 800)
        self.centralWidget = QtWidgets.QWidget(Menu)
        self.centralWidget.setObjectName("centralWidget")
        self.toolBox = QtWidgets.QToolBox(self.centralWidget)
        self.toolBox.setGeometry(QtCore.QRect(60, 10, 471, 361))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 471, 225))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 471, 225))
        self.page_2.setObjectName("page_2")
        self.groupBox = QtWidgets.QGroupBox(self.page_2)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 441, 221))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 411, 175))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.gridLayoutWidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_2.addWidget(self.calendarWidget, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_2, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.toolBox.addItem(self.page_5, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.toolBox.addItem(self.page_6, "")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(50, 420, 481, 261))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listView = QtWidgets.QListView(self.tab)
        self.listView.setGeometry(QtCore.QRect(100, 10, 256, 192))
        self.listView.setObjectName("listView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 0, 441, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 411, 175))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.gridLayoutWidget_2)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.gridLayout_3.addWidget(self.calendarWidget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        Menu.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Menu)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menuBar.setObjectName("menuBar")
        Menu.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Menu)
        self.mainToolBar.setObjectName("mainToolBar")
        Menu.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Menu)
        self.statusBar.setObjectName("statusBar")
        Menu.setStatusBar(self.statusBar)

        self.retranslateUi(Menu)
        self.toolBox.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Menu", "Profile"))
        self.groupBox.setTitle(_translate("Menu", "Calendar"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Menu", "Appointment"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("Menu", "Insurance Information"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), _translate("Menu", "Billing Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Menu", "Profile"))
        self.groupBox_2.setTitle(_translate("Menu", "Calendar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Menu", "Appointment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Menu", "Insurance Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Menu", "Billing Info"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = login_page() # set login page as UI
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


