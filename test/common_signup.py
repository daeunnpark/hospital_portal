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
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 200, 200, 100))
        self.label1.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label1.setObjectName("label")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(250, 200, 500, 50))
        self.lineEdit2.setText("")
        self.lineEdit2.setObjectName("lineEdit")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometrysetGeometry(QtCore.QRect(20, 400, 200, 100))
        self.label2.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label2.setObjectName("label_2")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(1500, 90, 521, 61))
        self.lineEdit2.setText("")
        self.lineEdit2.setObjectName("lineEdit_2")


        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(40, 170, 500, 71))
        self.label3.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label3.setObjectName("label_3")


        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(90, 240, 521, 61))
        self.lineEdit3.setText("")
        self.lineEdit3.setObjectName("lineEdit_3")

        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(1300, 170, 500, 71))
        self.label4.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label4.setObjectName("label_4")
        self.lineEdit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit4.setGeometry(QtCore.QRect(1500, 240, 521, 61))
        self.lineEdit4.setText("")
        self.lineEdit4.setObjectName("lineEdit_4")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(30, 300, 541, 71))
        self.label5.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label5.setObjectName("label_5")
        self.lineEdit5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit5.setGeometry(QtCore.QRect(90, 380, 521, 61))
        self.lineEdit5.setText("")
        self.lineEdit5.setObjectName("lineEdit_5")
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(30, 500, 541, 71))
        self.label6.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label6.setObjectName("label_6")
        self.lineEdit6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit6.setGeometry(QtCore.QRect(90, 580, 521, 61))
        self.lineEdit6.setText("")
        self.lineEdit6.setObjectName("lineEdit_6")
        self.label7 = QtWidgets.QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(1300, 500, 541, 71))
        self.label7.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label7.setObjectName("label_7")
        self.lineEdit7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit7.setGeometry(QtCore.QRect(1500, 580, 521, 61))
        self.lineEdit7.setText("")
        self.lineEdit7.setObjectName("lineEdit_7")
        self.label8 = QtWidgets.QLabel(self.centralwidget)
        self.label8.setGeometry(QtCore.QRect(30, 650, 541, 71))
        self.label8.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 18pt \"Lucida Calligraphy\";\n"
                                   "\n"
                                   "")
        self.label8.setObjectName("label_8")
        self.lineEdit8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit8.setGeometry(QtCore.QRect(90, 730, 521, 61))
        self.lineEdit8.setText("")
        self.lineEdit8.setObjectName("lineEdit_8")
        self.label9 = QtWidgets.QLabel(self.centralwidget)
        self.label9.setGeometry(QtCore.QRect(1300, 650, 541, 71))
        self.label9.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 18pt \"Lucida Calligraphy\";\n"
                                   "\n"
                                   "")
        self.label9.setObjectName("label_9")
        self.lineEdit9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit9.setGeometry(QtCore.QRect(1500, 730, 521, 61))
        self.lineEdit9.setText("")
        self.lineEdit9.setObjectName("lineEdit_9")
        self.label10 = QtWidgets.QLabel(self.centralwidget)
        self.label10.setGeometry(QtCore.QRect(30, 800, 541, 71))
        self.label10.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 18pt \"Lucida Calligraphy\";\n"
                                   "\n"
                                   "")
        self.label10.setObjectName("label_10")
        self.lineEdit10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit10.setGeometry(QtCore.QRect(90, 880, 521, 61))
        self.lineEdit10.setText("")
        self.lineEdit10.setObjectName("lineEdit_10")
        self.label11 = QtWidgets.QLabel(self.centralwidget)
        self.label11.setGeometry(QtCore.QRect(1300, 800, 541, 71))
        self.label11.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 18pt \"Lucida Calligraphy\";\n"
                                    "\n"
                                    "")
        self.label11.setObjectName("label_11")
        self.lineEdit11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit11.setGeometry(QtCore.QRect(1500, 880, 521, 61))
        self.lineEdit11.setText("")
        self.lineEdit11.setObjectName("lineEdit_11")
        self.label12 = QtWidgets.QLabel(self.centralwidget)
        self.label12.setGeometry(QtCore.QRect(30, 950, 541, 71))
        self.label12.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 18pt \"Lucida Calligraphy\";\n"
                                    "\n"
                                    "")
        self.label12.setObjectName("label_12")
        self.lineEdit12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit12.setGeometry(QtCore.QRect(90, 1030, 521, 61))
        self.lineEdit12.setText("")
        self.lineEdit12.setObjectName("lineEdit_12")
        self.label13 = QtWidgets.QLabel(self.centralwidget)
        self.label13.setGeometry(QtCore.QRect(1300, 950, 541, 71))
        self.label13.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 18pt \"Lucida Calligraphy\";\n"
                                    "\n"
                                    "")
        self.label13.setObjectName("label_10")
        self.lineEdit13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit13.setGeometry(QtCore.QRect(1500, 1030, 521, 61))
        self.lineEdit13.setText("")
        self.lineEdit13.setObjectName("lineEdit_13")
        #if (num == 2 or num == 3):
         #   self.lineEdit13.setVisible(False)
          #  self.label13.setVisible(False)
           # self.lineEdit12.setVisible(False)
            #self.label12.setVisible(False)
           # self.lineEdit11.setVisible(False)
           # self.label11.setVisible(False)
           # self.lineEdit10.setVisible(False)
           # self.label10.setVisible(False)
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

        # for now
        #self.pushButton.clicked.connect(lambda: self.CreatePatient(access))

    def retranslateUi(self, CommonSignUp):
        _translate = QtCore.QCoreApplication.translate
        CommonSignUp.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "First Name:"))
        self.label2.setText(_translate("MainWindow", "Last Name:"))
        self.label3.setText(_translate("MainWindow", "Phone Number:"))
        self.label4.setText(_translate("MainWindow", "Email Address:"))
        self.label5.setText(_translate("MainWindow", "Username: "))
        self.label6.setText(_translate("MainWindow", "Password:"))
        self.label7.setText(_translate("MainWindow", "Re-Enter Password:"))
        self.label8.setText(_translate("MainWindow", "Age:"))
        self.label9.setText(_translate("MainWindow", "Weight:"))
        self.label10.setText(_translate("MainWindow", "Height:"))
        self.label11.setText(_translate("MainWindow", "SSN:"))
        self.label12.setText(_translate("MainWindow", "Credit Card Number:"))
        self.label13.setText(_translate("MainWindow", "Insurance Number:"))
        self.pushButton.setText(_translate("Main Window", "Sign Up!"))

"""
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
"""



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = common_login_UI()
    ui.setupUi(MainWindow)

    MainWindow.showMaximized()

    sys.exit(app.exec_())