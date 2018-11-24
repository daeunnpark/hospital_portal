import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

# import modules
from common_login import common_login_UI


class common_signup_UI(object):
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
                    self.uiLogin = common_login_UI()
                    self.uiLogin.setupUi(MainWindow)
                    MainWindow.showMaximized()
