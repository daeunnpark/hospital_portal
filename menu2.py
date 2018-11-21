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
        Menu.resize(1600, 1200)
        self.centralWidget = QtWidgets.QWidget(Menu)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(200, 100, 2000, 1000))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 20, 300, 61))
        self.label.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(910, 20, 300, 61))
        self.label_2.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 341, 40))
        self.label_3.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(910, 170, 341, 40))
        self.label_4.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 320, 341, 40))
        self.label_5.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(910, 320, 341, 40))
        self.label_6.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 470, 341, 40))
        self.label_7.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(910, 470, 341, 40))
        self.label_8.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 650, 341, 40))
        self.label_9.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(910, 650, 341, 40))
        self.label_10.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(50, 90, 500, 60))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(940, 90, 500, 60))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 220, 500, 60))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(940, 220, 500, 60))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 370, 500, 60))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(940, 370, 500, 60))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_7.setGeometry(QtCore.QRect(50, 540, 500, 60))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_8.setGeometry(QtCore.QRect(940, 540, 500, 60))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_9.setGeometry(QtCore.QRect(50, 720, 500, 60))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_10.setGeometry(QtCore.QRect(940, 720, 500, 60))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setReadOnly(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(430, 40, 1000, 600))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1020, 600))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.gridLayoutWidget_2)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.gridLayout_3.addWidget(self.calendarWidget_2, 0, 0, 0, 0)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(50, 700, 600, 41))
        self.label_11.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";")
        self.label_11.setObjectName("label_11")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.tab_2)
        self.dateTimeEdit.setGeometry(QtCore.QRect(70, 780, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.tab_2)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(70, 830, 194, 22))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.dateTimeEdit_3 = QtWidgets.QDateTimeEdit(self.tab_2)
        self.dateTimeEdit_3.setGeometry(QtCore.QRect(300, 780, 194, 22))
        self.dateTimeEdit_3.setObjectName("dateTimeEdit_3")
        self.dateTimeEdit_4 = QtWidgets.QDateTimeEdit(self.tab_2)
        self.dateTimeEdit_4.setGeometry(QtCore.QRect(300, 830, 194, 22))
        self.dateTimeEdit_4.setObjectName("dateTimeEdit_4")
        self.dateTimeEdit_5 = QtWidgets.QDateTimeEdit(self.tab_2)
        self.dateTimeEdit_5.setGeometry(QtCore.QRect(530, 780, 194, 22))
        self.dateTimeEdit_5.setObjectName("dateTimeEdit_5")
        self.dateTimeEdit_6 = QtWidgets.QDateTimeEdit(self.tab_2)
        self.dateTimeEdit_6.setGeometry(QtCore.QRect(530, 830, 194, 22))
        self.dateTimeEdit_6.setObjectName("dateTimeEdit_6")
        self.dateTimeEdit_7 = QtWidgets.QDateTimeEdit(self.tab_2)
        self.dateTimeEdit_7.setGeometry(QtCore.QRect(760, 780, 194, 22))
        self.dateTimeEdit_7.setObjectName("dateTimeEdit_7")
        self.dateTimeEdit_8 = QtWidgets.QDateTimeEdit(self.tab_2)
        self.dateTimeEdit_8.setGeometry(QtCore.QRect(760, 830, 194, 22))
        self.dateTimeEdit_8.setObjectName("dateTimeEdit_8")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(30, 30, 500, 61))
        self.label_12.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        self.label_12.setObjectName("label_12")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(80, 100, 400, 60))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(30, 300, 500, 61))
        self.label_13.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        self.label_13.setObjectName("label_13")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_12.setGeometry(QtCore.QRect(80, 370, 400, 60))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(30, 550, 500, 61))
        self.label_14.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        self.label_14.setObjectName("label_14")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_13.setGeometry(QtCore.QRect(80, 630, 400, 60))
        self.lineEdit_13.setObjectName("lineEdit_13")
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
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.label.setText(_translate("Menu", "First Name:"))
        self.label_2.setText(_translate("Menu", "Last Name:"))
        self.label_3.setText(_translate("Menu", "Phone Number:"))
        self.label_4.setText(_translate("Menu", "Email Address:"))
        self.label_5.setText(_translate("Menu", "ID:"))
        self.label_6.setText(_translate("Menu", "SSN:"))
        self.label_7.setText(_translate("Menu", "Weight:"))
        self.label_8.setText(_translate("Menu", "Height:"))
        self.label_9.setText(_translate("Menu", "Age:"))
        self.label_10.setText(_translate("Menu", "Medication List:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Menu", "Profile"))
        self.label_11.setText(_translate("Menu", "Appointments:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Menu", "Appointment"))
        self.label_12.setText(_translate("Menu", "Insurance Number:"))
        self.label_13.setText(_translate("Menu", "Credit Card Number:"))
        self.label_14.setText(_translate("Menu", "Billing Amount:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Menu", "Billing Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())

