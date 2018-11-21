# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(600, 800)
        self.centralWidget = QtWidgets.QWidget(Menu)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(200, 100, 2000, 1000))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listView = QtWidgets.QListView(self.tab)
        self.listView.setGeometry(QtCore.QRect(100, 70, 1800, 800))
        self.listView.setObjectName("listView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(100, 70, 1800, 800))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(100, 70, 1000, 600))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.gridLayoutWidget_2)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.gridLayout_3.addWidget(self.calendarWidget_2, 0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.listView_2 = QtWidgets.QListView(self.tab_3)
        self.listView_2.setGeometry(QtCore.QRect(100, 70, 1800, 800))
        self.listView_2.setObjectName("listView_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.listView_3 = QtWidgets.QListView(self.tab_4)
        self.listView_3.setGeometry(QtCore.QRect(100, 70, 1800, 800))
        self.listView_3.setObjectName("listView_3")
        self.tabWidget.addTab(self.tab_4, "")
        Menu.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Menu)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menuBar.setObjectName("menuBar")
        Menu.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Menu)
        self.mainToolBar.setObjectName("mainToolBar")
        Menu.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Menu)
        self.statusBar.setObjectName("statusBar")
        Menu.setStatusBar(self.statusBar)

        self.retranslateUi(Menu)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Menu", "Profile"))
        self.groupBox_2.setTitle(_translate("Menu", "Calendar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Menu", "Appointment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Menu", "Insurance Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Menu", "Billing Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())

