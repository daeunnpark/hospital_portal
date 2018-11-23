# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# This is generated from .ui files.
# command line: exec python3 -m PyQt5.uic.pyuic first.ui -o fisrt.py -x to convert .ui file to .py file

from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QApplication
import pymysql
#from menu import *

class login_page(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(720, 120, 1500, 200))
        self.imageLabel.setGeometry(QtCore.QRect(400, -300, 1999, 1000))
        self.imageLabel2.setGeometry(QtCore.QRect(1850, -300, 1999, 1000))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel2.setObjectName("imageLabel2")
        self.pixmap = QtGui.QPixmap('icon.PNG')
        self.imageLabel.setPixmap(self.pixmap)
        self.imageLabel2.setPixmap(self.pixmap)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(850, 400, 800, 600))
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
        #self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_5.setGeometry(QtCore.QRect(340, 460, 114, 32))
        #self.pushButton_5.setObjectName("pushButton_5")
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

        self.pushButton.clicked.connect(self.changeUI_to_LoginOrRegister) # set listener

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Welcome to Healthcare United Patient Portal</span></p><p><br/></p></body></html>"))
        self.label.setStyleSheet('color: teal')
        self.pushButton.setText(_translate("MainWindow", "Patient"))
        self.pushButton_2.setText(_translate("MainWindow", "Doctor"))
        self.pushButton_3.setText(_translate("MainWindow", "Nurse"))
        self.pushButton_4.setText(_translate("MainWindow", "Admin"))
        #self.pushButton_5.setText(_translate("MainWindow", "Login"))

    def changeUI_to_LoginOrRegister(self): # change UI to Menu
        self.uiNew = Ui_SignInOrRegister()
        self.uiNew.setupUi(MainWindow)
        MainWindow.showFullScreen()

class Ui_SignInOrRegister(object):
        def setupUi(self, SignInOrRegister):
            SignInOrRegister.setObjectName("SignInOrRegister")
            SignInOrRegister.resize(800, 600)
            self.centralwidget = QtWidgets.QWidget(SignInOrRegister)
            self.centralwidget.setObjectName("centralwidget")
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(1000, 880, 1000, 200))
            self.pushButton.setStyleSheet("font: 15pt \"Lucida Calligraphy\";\n"
                                          "color: rgb(46, 125, 132)")
            self.pushButton.setObjectName("pushButton")
            self.commonLoginButton = QtWidgets.QPushButton(self.centralwidget)
            self.commonLoginButton.setGeometry(QtCore.QRect(300, 400, 2000, 200))
            self.commonLoginButton.setStyleSheet("font: 20pt \"Lucida Calligraphy\";\n"
                                            "color: rgb(46, 125, 132)")
            self.commonLoginButton.setObjectName("pushButton_2")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(300, 900, 301, 131))
            self.label.setStyleSheet("font: 20pt \"Lucida Calligraphy\";\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "font-weight:bold;")
            self.label.setObjectName("label")
            SignInOrRegister.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(SignInOrRegister)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(SignInOrRegister)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(SignInOrRegister)
            QtCore.QMetaObject.connectSlotsByName(SignInOrRegister)

            self.commonLoginButton.clicked.connect(self.changeUI_to_CommonLogin)  # set listener
            self.pushButton.clicked.connect(self.changeUI_to_AccessCode)

        def retranslateUi(self, SignInOrRegister):
            _translate = QtCore.QCoreApplication.translate
            SignInOrRegister.setWindowTitle(_translate("SignInOrRegister", "SignInOrRegister"))
            self.pushButton.setText(_translate("SignInOrRegister", "Sign Up Using Your Access Code"))
            self.commonLoginButton.setText(_translate("SignInOrRegister", "Login"))
            self.label.setText(_translate("SignInOrRegister", "New User?"))

        def changeUI_to_CommonLogin(self):  # change UI to Menu
             self.uiLogin = Ui_CommonLogin()
             self.uiLogin.setupUi(MainWindow)
             MainWindow.showMaximized()

        def changeUI_to_AccessCode(self):  # change UI to Menu
             self.uiAccess = Ui_Access()
             self.uiAccess.setupUi(MainWindow)
             MainWindow.showMaximized()


class Ui_CommonLogin(object):
    def setupUi(self, CommonLogin):
        CommonLogin.setObjectName("CommonLogin")
        CommonLogin.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CommonLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 80, 400, 71))
        self.label.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label.setObjectName("label")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(2000, 1000, 200, 200))
        self.loginButton.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 18pt \"Lucida Calligraphy\";\n"
                                   "\n"
                                   "")
        self.loginButton.setObjectName("loginButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(700, 150, 800, 61))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 580, 400, 71))
        self.label_2.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(700, 670, 800, 61))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)    #Password
        CommonLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CommonLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CommonLogin)
        self.statusbar.setObjectName("statusbar")
        CommonLogin.setStatusBar(self.statusbar)

        self.retranslateUi(CommonLogin)
        QtCore.QMetaObject.connectSlotsByName(CommonLogin)

        #self.loginButton.clicked.connect(self.changeUI_to_Menu) # set listener
        self.loginButton.clicked.connect(self.authenticateUser)

    def retranslateUi(self, CommonLogin):
        _translate = QtCore.QCoreApplication.translate
        CommonLogin.setWindowTitle(_translate("CommonLogin", "CommonLogin"))
        self.label.setText(_translate("CommonLogin", "Username:"))
        self.label_2.setText(_translate("CommonLogin", "Password:"))
        self.loginButton.setText(_translate("CommonLogin", "Login"))

    def authenticateUser(self):
        cur.execute('SELECT * FROM Person P WHERE Username = (%s) AND UserPassword = (%s)', (self.lineEdit.text(), self.lineEdit_2.text()))
        authenticate = cur.fetchall()
        if(len(authenticate) == 1):
            cur.execute('SELECT FirstName FROM Person P WHERE Username = (%s) AND UserPassword = (%s)',
                        (self.lineEdit.text(), self.lineEdit_2.text()))
            firstName = str(cur.fetchone()[0])
            cur.execute('SELECT LastName FROM Person P WHERE Username = (%s) AND UserPassword = (%s)',
                        (self.lineEdit.text(), self.lineEdit_2.text()))
            lastName = str(cur.fetchone()[0])
            cur.execute('SELECT PhoneNumber FROM Person P WHERE Username = (%s) AND UserPassword = (%s)',
                        (self.lineEdit.text(), self.lineEdit_2.text()))
            phoneNumber = str(cur.fetchone()[0])
            cur.execute('SELECT EmailAddress FROM Person P WHERE Username = (%s) AND UserPassword = (%s)',
                        (self.lineEdit.text(), self.lineEdit_2.text()))
            emailAddress = str(cur.fetchone()[0])
            cur.execute('SELECT ID FROM Person P WHERE Username = (%s) AND UserPassword = (%s)',
                        (self.lineEdit.text(), self.lineEdit_2.text()))
            ID = str(cur.fetchone()[0])
            cur.execute('SELECT Age FROM Patient P WHERE PatientID = (%s)', ID)
            age = str(cur.fetchone()[0])
            cur.execute('SELECT Weight FROM Patient P WHERE PatientID = (%s)', ID)
            weight = str(cur.fetchone()[0])
            cur.execute('SELECT Height FROM Patient P WHERE PatientID = (%s)', ID)
            height = str(cur.fetchone()[0])
            cur.execute('SELECT SSN FROM Patient P WHERE PatientID = (%s)', ID)
            ssn = str(cur.fetchone()[0])
            cur.execute('SELECT CreditCardNumber FROM Patient P WHERE PatientID = (%s)', ID)
            creditCardNumber = str(cur.fetchone()[0])
            cur.execute('SELECT BillingAmount FROM Patient P WHERE PatientID = (%s)', ID)
            billingAmount = str(cur.fetchone()[0])
            cur.execute('SELECT InsuranceNumber FROM Patient P WHERE PatientID = (%s)', ID)
            insuranceNumber = str(cur.fetchone()[0])
            cur.execute('SELECT MedicationList FROM Patient P WHERE PatientID = (%s)', ID)
            medicationList = str(cur.fetchone()[0])
            cur.execute('SELECT Date FROM Appointment A WHERE PatientID = (%s)', ID)
            appointmentDates = cur.fetchall()
            self.uiNew = Ui_Menu()
            self.uiNew.setupUi(MainWindow, firstName, lastName, phoneNumber, emailAddress, ID, age, ssn, weight, height, creditCardNumber, billingAmount, insuranceNumber, medicationList, appointmentDates)
            MainWindow.showFullScreen()
        else:
            print("no user")

class Ui_Menu(object):
    def setupUi(self, Menu, firstName, lastName, phoneNumber, emailAddress, ID, age, ssn, weight, height, creditCardNumber, billingAmount, insuranceNumber, medicationList, appointmentDates):
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
        self.lineEdit.setText(firstName)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(940, 90, 500, 60))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setText(lastName)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 220, 500, 60))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setText(phoneNumber)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(940, 220, 500, 60))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setText(emailAddress)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 370, 500, 60))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setText(ID)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(940, 370, 500, 60))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setText(ssn)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_7.setGeometry(QtCore.QRect(50, 540, 500, 60))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setText(weight)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_8.setGeometry(QtCore.QRect(940, 540, 500, 60))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setText(height)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_9.setGeometry(QtCore.QRect(50, 720, 500, 60))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setText(age)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_10.setGeometry(QtCore.QRect(940, 720, 500, 60))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setText(medicationList)
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
        earliestDate = None
        for row in appointmentDates:
            if(earliestDate == None):
                earliestDate = row[0]
            else:
                if(row[0] < earliestDate):
                    earliestDate = row[0]

        self.calendarWidget_2.setSelectedDate(earliestDate)
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
        self.lineEdit_11.setText(insuranceNumber)
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(30, 300, 500, 61))
        self.label_13.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        self.label_13.setObjectName("label_13")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_12.setGeometry(QtCore.QRect(80, 370, 400, 60))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.setText(creditCardNumber)
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(30, 550, 500, 61))
        self.label_14.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        self.label_14.setObjectName("label_14")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_13.setGeometry(QtCore.QRect(80, 630, 400, 60))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_13.setText(billingAmount)
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

class Ui_Access(object):
    def setupUi(self, Access):
        Access.setObjectName("Access")
        Access.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Access)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 40, 1400, 171))
        self.label.setStyleSheet("font: 20pt \"Lucida Calligraphy\";\n"
"color: rgb(46, 125, 132);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(600, 550, 1400, 111))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(2000, 1000, 241, 81))
        self.pushButton.setStyleSheet("font: 20pt \"Lucida Calligraphy\";\n"
"color: rgb(46, 125, 132);")
        self.pushButton.setObjectName("pushButton")
        Access.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Access)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Access.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Access)
        self.statusbar.setObjectName("statusbar")
        Access.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.authenticateAccess)

        self.retranslateUi(Access)
        QtCore.QMetaObject.connectSlotsByName(Access)

    def retranslateUi(self, Access):
        _translate = QtCore.QCoreApplication.translate
        Access.setWindowTitle(_translate("Access", "Access"))
        self.label.setText(_translate("Access", "Enter Your Access Code Received Via Email:"))
        self.pushButton.setText(_translate("Access", "Enter"))

    def authenticateAccess(self):
        cur.execute('SELECT AccessCodes FROM AccessCodes A WHERE AccessCodes = (%s)', self.lineEdit.text())
        access = cur.fetchall()
        if (cur.rowcount != 0):
            self.uiNew = Ui_CommonSignUp()
            self.uiNew.setupUi(MainWindow, access)
            MainWindow.showFullScreen()
        else:
            print("error")

class Ui_CommonSignUp(object):
    def setupUi(self, CommonSignUp, access):
        CommonSignUp.setObjectName("CommonSignUp")
        CommonSignUp.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CommonSignUp)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 300, 71))
        self.label.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 90, 521, 61))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1300, 20, 300, 71))
        self.label_2.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1500, 90, 521, 61))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 500, 71))
        self.label_3.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 240, 521, 61))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1300, 170, 500, 71))
        self.label_4.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(1500, 240, 521, 61))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 300, 541, 71))
        self.label_5.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 380, 521, 61))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 500, 541, 71))
        self.label_6.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 580, 521, 61))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1300, 500, 541, 71))
        self.label_7.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(1500, 580, 521, 61))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 650, 541, 71))
        self.label_8.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 18pt \"Lucida Calligraphy\";\n"
                                   "\n"
                                   "")
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(90, 730, 521, 61))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1300, 650, 541, 71))
        self.label_9.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 18pt \"Lucida Calligraphy\";\n"
                                   "\n"
                                   "")
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(1500, 730, 521, 61))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 800, 541, 71))
        self.label_10.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 18pt \"Lucida Calligraphy\";\n"
                                   "\n"
                                   "")
        self.label_10.setObjectName("label_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(90, 880, 521, 61))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1300, 800, 541, 71))
        self.label_11.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 18pt \"Lucida Calligraphy\";\n"
                                    "\n"
                                    "")
        self.label_11.setObjectName("label_11")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(1500, 880, 521, 61))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 950, 541, 71))
        self.label_12.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 18pt \"Lucida Calligraphy\";\n"
                                    "\n"
                                    "")
        self.label_12.setObjectName("label_12")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(90, 1030, 521, 61))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1300, 950, 541, 71))
        self.label_13.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 18pt \"Lucida Calligraphy\";\n"
                                    "\n"
                                    "")
        self.label_13.setObjectName("label_10")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(1500, 1030, 521, 61))
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        CommonSignUp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CommonSignUp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(2000, 1200, 400, 81))
        self.pushButton.setStyleSheet("font: 20pt \"Lucida Calligraphy\";\n"
                                      "color: rgb(46, 125, 132);")
        self.pushButton.setObjectName("pushButton")
        CommonSignUp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CommonSignUp)
        self.statusbar.setObjectName("statusbar")
        CommonSignUp.setStatusBar(self.statusbar)

        self.retranslateUi(CommonSignUp)
        QtCore.QMetaObject.connectSlotsByName(CommonSignUp)

        self.pushButton.clicked.connect(lambda: self.CreatePatient(access))

    def retranslateUi(self, CommonSignUp):
        _translate = QtCore.QCoreApplication.translate
        CommonSignUp.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "First Name:"))
        self.label_2.setText(_translate("MainWindow", "Last Name:"))
        self.label_3.setText(_translate("MainWindow", "Phone Number:"))
        self.label_4.setText(_translate("MainWindow", "Email Address:"))
        self.label_5.setText(_translate("MainWindow", "Username: "))
        self.label_6.setText(_translate("MainWindow", "Password:"))
        self.label_7.setText(_translate("MainWindow", "Re-Enter Password:"))
        self.label_8.setText(_translate("MainWindow", "Age:"))
        self.label_9.setText(_translate("MainWindow", "Weight:"))
        self.label_10.setText(_translate("MainWindow", "Height:"))
        self.label_11.setText(_translate("MainWindow", "SSN:"))
        self.label_12.setText(_translate("MainWindow", "Credit Card Number:"))
        self.label_13.setText(_translate("MainWindow", "Insurance Number:"))
        self.pushButton.setText(_translate("Main Window", "Sign Up!"))

    def CreatePatient(self, access):
        if(self.lineEdit_6.text() == "" or self.lineEdit_7.text() == "" or self.lineEdit_5.text() == ""):
            print("error empty")
        if(self.lineEdit_6.text() != self.lineEdit_7.text()):
            print("error not same")
        else:
            cur.execute('SELECT * FROM Person P WHERE Username = (%s)', (self.lineEdit_5.text()))
            if(cur.rowcount != 0):
                print("error: Username Already Exists")
            else:
                cur.execute('SELECT * FROM Person P WHERE UserPassword = (%s)', (self.lineEdit_6.text()))
                if(cur.rowcount != 0):
                    print("error: UserPassword Already Exists")
                else:
                    cur.execute('INSERT INTO Person(ID, FirstName, LastName, PhoneNumber, EmailAddress, Username, UserPassword) VALUES (%s, %s, %s, %s, %s, %s, %s)', (access, self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text()))
                    cur.execute('INSERT INTO Patient(PatientID, Age, Weight, Height, SSN, CreditCardNumber, BillingAmount, InsuranceNumber, MedicationList) VALUES (%s, %s, %s, %s, %s, %s, 20.00, %s, "none")', (access, self.lineEdit_8.text(), self.lineEdit_9.text(), self.lineEdit_10.text(), self.lineEdit_11.text(), self.lineEdit_12.text(), self.lineEdit_13.text()))
                    conn.commit()
                    self.uiLogin = Ui_CommonLogin()
                    self.uiLogin.setupUi(MainWindow)
                    MainWindow.showMaximized()

if __name__ == "__main__":
    import sys
    # Initialize database connection
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='hospital')
    #conn = pymysql.connect(host='10.245.235.98', port=3306, user='root', passwd='hospitalCSE305!', db='hospital')
    # Initialize the database cursor
    cur = conn.cursor()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = login_page() # set login page as UI
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    #conn.commit()
    sys.exit(app.exec_())


