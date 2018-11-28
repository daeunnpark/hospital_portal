import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

# import modules
from common_login import common_login_UI


class common_signup_UI(object):
    def __init__(self, parent=None):
        self.newP = False
        self.newD = False
        self.newN = False

    def setupUi(self, CommonSignUp, num):

        CommonSignUp.setObjectName("CommonSignUp")

        self.centralwidget = QtWidgets.QWidget(CommonSignUp)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 2000, 1000))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_11.setObjectName("label_11")

        self.gridLayout_2.addWidget(self.label_11, 5, 2, 1, 1)

        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_2.addWidget(self.lineEdit_10, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 5, 0, 1, 1)

        self.lineEdit_11 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 5, 3, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("color: rgb(46, 125, 132);\n"
                                 "font-weight: bold;\n"
                                 "font: 12pt Lucida Calligraphy;")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt Lucida Calligraphy;")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt Lucida Calligraphy;")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 2, 1, 1, 1)

        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 2, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt Lucida Calligraphy;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 3, 1, 1, 1)

        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 3, 3, 1, 1)

        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 4, 3, 1, 1)

        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 2, 1, 1)

        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt Lucida Calligraphy;")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)

        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 6, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_2.addWidget(self.lineEdit_12, 6, 1, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_2.addWidget(self.lineEdit_13, 6, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 6, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        # self.pushButton.setGeometry(QtCore.QRect(2000, 1200, 400, 81))
        self.pushButton.setGeometry(QtCore.QRect(50, 100, 200, 50))
        self.pushButton.setStyleSheet("font: 20pt \"Lucida Calligraphy\";\n"
                                      "color: rgb(46, 125, 132);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 7, 8, 1, 1)

        if(num == 2 or num == 3):
            self.label_13.setVisible(False)
            self.label_12.setVisible(False)
            self.label_11.setVisible(False)
            self.label_10.setVisible(False)
            self.lineEdit_13.setVisible(False)
            self.lineEdit_12.setVisible(False)
            self.lineEdit_11.setVisible(False)
            self.lineEdit_10.setVisible(False)

        CommonSignUp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CommonSignUp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        CommonSignUp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CommonSignUp)
        self.statusbar.setObjectName("statusbar")
        CommonSignUp.setStatusBar(self.statusbar)

        self.retranslateUi(CommonSignUp, num)
        QtCore.QMetaObject.connectSlotsByName(CommonSignUp)

    def retranslateUi(self, CommonSignUp, num):
        _translate = QtCore.QCoreApplication.translate
        CommonSignUp.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_11.setText(_translate("MainWindow", "SSN:"))
        self.label_10.setText(_translate("MainWindow", "Height:"))
        self.label.setText(_translate("MainWindow", "FirstName:"))
        self.label_2.setText(_translate("MainWindow", "LastName:"))
        self.label_3.setText(_translate("MainWindow", "Phone Number:"))
        self.label_4.setText(_translate("MainWindow", "Email Address:"))
        self.label_7.setText(_translate("MainWindow", "Re-Enter Password:"))
        self.label_5.setText(_translate("MainWindow", "Username:"))
        self.label_6.setText(_translate("MainWindow", "Password:"))

        if(num == 1):
            self.label_8.setText(_translate("MainWindow", "Age:"))
            self.label_9.setText(_translate("MainWindow", "Weight:"))
        elif(num == 2 or num == 3):
            self.label_8.setText(_translate("MainWindow", "Specialty:"))
            self.label_9.setText(_translate("MainWindow", "Medical License:"))

        self.label_12.setText(_translate("MainWindow", "Credit Card Number:"))
        self.label_13.setText(_translate("MainWindow", "Insurance Number:"))
        self.pushButton.setText(_translate("MainWindow", "Sign In!"))


    def CreatePatient(self, cur, conn, accessCodeReceived):
        self.newP = False
        if(self.lineEdit_6.text() == "" or self.lineEdit_7.text() == "" or self.lineEdit_5.text() == ""):
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText("Error: Must Specify Username and Password!")
            error_dialog.exec()
        if(self.lineEdit_6.text() != self.lineEdit_7.text()):
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText("Error: Passwords Do Not Match!")
            error_dialog.exec()
        else:
            cur.execute('SELECT * FROM Person P WHERE Username = (%s)', (self.lineEdit_5.text()))
            if(cur.rowcount != 0):
                error_dialog = QtWidgets.QMessageBox()
                error_dialog.setText("Error: Username Already Exists! Try Another Username")
                error_dialog.exec()
            else:
                cur.execute('SELECT * FROM Person P WHERE UserPassword = (%s)', (self.lineEdit_6.text()))
                if(cur.rowcount != 0):
                    error_dialog = QtWidgets.QMessageBox()
                    error_dialog.setText("Error: Password Already Exists! Try Another Password")
                    error_dialog.exec()
                else: # phone number inlcuding dashes = 10+2
                    if(len(self.lineEdit_3.text()) != 12 or self.lineEdit_3.text()[3] != '-' or self.lineEdit_3.text()[7] != '-') :
                        error_dialog = QtWidgets.QMessageBox()
                        error_dialog.setText("Error: Phone Number Incorrect! Format: xxx-xxx-xxxx")
                        error_dialog.exec()
                    elif(len(self.lineEdit_11.text()) != 11): # SSN including dashes = 9+2
                        error_dialog = QtWidgets.QMessageBox()
                        error_dialog.setText("Error: SSN Incorrect! Must be 9 numbers long")
                        error_dialog.exec()
                    else:
                        # replaced by reformat(str)
                        """
                        number = self.lineEdit_3.text()
                        for char in number:
                            if char in "-":
                                number = number.replace(char, '')
                        number2 = self.lineEdit_11.text()
                        for char2 in number2:
                            if char2 in "-":
                                number2 = number2.replace(char2, '')
                        """
                        cur.execute('INSERT INTO Person(ID, FirstName, LastName, PhoneNumber, EmailAddress, Username, UserPassword) VALUES (%s, %s, %s, %s, %s, %s, %s)', (accessCodeReceived, self.lineEdit.text(), self.lineEdit_2.text(), self.reformat(self.lineEdit_3.text()), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text()))
                    
                        cur.execute('INSERT INTO Patient(PatientID, Age, Weight, Height, SSN, CreditCardNumber, BillingAmount, InsuranceNumber, MedicationList) VALUES (%s, %s, %s, %s, %s, %s, 0.0, %s, "none")', (accessCodeReceived, self.lineEdit_8.text(), self.lineEdit_9.text(), self.lineEdit_10.text(), self.reformat(self.lineEdit_11.text()), self.lineEdit_12.text(), self.lineEdit_13.text()))
                        conn.commit()
                        self.newP = True

    def CreateDoctor(self, cur, conn, accessCodeReceived):
        self.newD = False
        if (self.lineEdit_6.text() == "" or self.lineEdit_7.text() == "" or self.lineEdit_5.text() == ""):
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText("Error: Must Specify Username and Password!")
            error_dialog.exec()
        if (self.lineEdit_6.text() != self.lineEdit_7.text()):
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText("Error: Passwords Do Not Match!")
            error_dialog.exec()
        else:
            cur.execute('SELECT * FROM Person P WHERE Username = (%s)', (self.lineEdit_5.text()))
            if (cur.rowcount != 0):
                error_dialog = QtWidgets.QMessageBox()
                error_dialog.setText("Error: Username Already Exists! Choose Another Username")
                error_dialog.exec()
            else:
                cur.execute('SELECT * FROM Person P WHERE UserPassword = (%s)', (self.lineEdit_6.text()))
                if (cur.rowcount != 0):
                    error_dialog = QtWidgets.QMessageBox()
                    error_dialog.setText("Error: Password Already Exists! Choose Another Password")
                    error_dialog.exec()
                else:
                    if (len(self.lineEdit_3.text()) != 12 or self.lineEdit_3.text()[3] != '-' or self.lineEdit_3.text()[7] != '-' or self.lineEdit_3.text()[0].isdigit() == False
                        or self.lineEdit_3.text()[1].isdigit() == False or self.lineEdit_3.text()[2].isdigit() == False or self.lineEdit_3.text()[4].isdigit() == False
                        or self.lineEdit_3.text()[5].isdigit() == False or self.lineEdit_3.text()[6].isdigit() == False or self.lineEdit_3.text()[8].isdigit() == False
                        or self.lineEdit_3.text()[9].isdigit() == False or self.lineEdit_3.text()[10].isdigit() == False or self.lineEdit_3.text()[11].isdigit() == False):
                        error_dialog = QtWidgets.QMessageBox()
                        error_dialog.setText("Error: Phone Number Incorrect! Format: xxx-xxx-xxxx")
                        error_dialog.exec()
                    else:
                        cur.execute('INSERT INTO Person(ID, FirstName, LastName, PhoneNumber, EmailAddress, Username, UserPassword) VALUES (%s, %s, %s, %s, %s, %s, %s)', (accessCodeReceived, self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text()))
                        conn.commit()
                        role = self.lineEdit_8.text()
                        deptID = 8
                        if(role == "Pediatrics" or role == "pediatrics"):
                            deptID = 1
                        elif(role == "Dermatology" or role == "dermatology"):
                            deptID = 2
                        elif(role == "Oncology" or role == "oncology"):
                            deptID = 3
                        elif(role == "Gynaecology" or role == "gynaecology"):
                            deptID = 4
                        elif(role == "Gastroenterology" or role == "gastroenterology"):
                            deptID = 5
                        elif(role == "Cardiology" or role == "cardiology"):
                            deptID = 6
                        elif(role == "Psychiatry" or role == "psychiatry"):
                            deptID = 7
                        cur.execute('INSERT INTO Employee(EmployeeID, DepartmentID) VALUES (%s, %s)', (accessCodeReceived, deptID))
                        conn.commit()
                        cur.execute('INSERT INTO Doctor(DoctorID, Specialty, MedicalLicense) VALUES (%s, %s, %s)', (accessCodeReceived, self.lineEdit_8.text(), self.lineEdit_9.text()))
                        conn.commit()
                        self.newD = True


    def CreateNurse(self, cur, conn, accessCodeReceived):
        self.newN = False
        if (self.lineEdit_6.text() == "" or self.lineEdit_7.text() == "" or self.lineEdit_5.text() == ""):
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText("Error: Must Specify Username and Password!")
            error_dialog.exec()
        if (self.lineEdit_6.text() != self.lineEdit_7.text()):
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText("Error: Passwords Do Not Match!")
            error_dialog.exec()
        else:
            cur.execute('SELECT * FROM Person P WHERE Username = (%s)', (self.lineEdit_5.text()))
            if (cur.rowcount != 0):
                error_dialog = QtWidgets.QMessageBox()
                error_dialog.setText("Error: Username Already Exists! Choose Another One")
                error_dialog.exec()
            else:
                cur.execute('SELECT * FROM Person P WHERE UserPassword = (%s)', (self.lineEdit_6.text()))
                if (cur.rowcount != 0):
                    error_dialog = QtWidgets.QMessageBox()
                    error_dialog.setText("Error: Password Already Exists! Choose Another One")
                    error_dialog.exec()
                else:
                    if (len(self.lineEdit_3.text()) != 12 or self.lineEdit_3.text()[3] != '-' or self.lineEdit_3.text()[7] != '-' or self.lineEdit_3.text()[0].isdigit() == False
                        or self.lineEdit_3.text()[1].isdigit() == False or self.lineEdit_3.text()[2].isdigit() == False or self.lineEdit_3.text()[4].isdigit() == False
                        or self.lineEdit_3.text()[5].isdigit() == False or self.lineEdit_3.text()[6].isdigit() == False or self.lineEdit_3.text()[8].isdigit() == False
                        or self.lineEdit_3.text()[9].isdigit() == False or self.lineEdit_3.text()[10].isdigit() == False or self.lineEdit_3.text()[11].isdigit() == False):
                        error_dialog = QtWidgets.QMessageBox()
                        error_dialog.setText("Error: Phone Number Incorrect! Format: xxx-xxx-xxxx")
                        error_dialog.exec()
                    else:
                        cur.execute('INSERT INTO Person(ID, FirstName, LastName, PhoneNumber, EmailAddress, Username, UserPassword) VALUES (%s, %s, %s, %s, %s, %s, %s)', (accessCodeReceived, self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text()))
                        conn.commit()
                        role = self.lineEdit_8.text()
                        deptID = 8
                        if (role == "Pediatrics" or role == "pediatrics"):
                            deptID = 1
                        elif (role == "Dermatology" or role == "dermatology"):
                            deptID = 2
                        elif (role == "Oncology" or role == "oncology"):
                            deptID = 3
                        elif (role == "Gynaecology" or role == "gynaecology"):
                            deptID = 4
                        elif (role == "Gastroenterology" or role == "gastroenterology"):
                            deptID = 5
                        elif (role == "Cardiology" or role == "cardiology"):
                            deptID = 6
                        elif (role == "Psychiatry" or role == "psychiatry"):
                            deptID = 7
                        cur.execute('INSERT INTO Employee(EmployeeID, DepartmentID) VALUES (%s, %s)', (accessCodeReceived, deptID))
                        conn.commit()
                        cur.execute('INSERT INTO Nurse(NurseID, Specialty, MedicalLicense) VALUES (%s, %s, %s)', (accessCodeReceived, self.lineEdit_8.text(), self.lineEdit_9.text()))
                        conn.commit()
                        self.newN = True


        # Remove dashes in str
    def reformat(self, str):
        for char in str:
            if char in "-":
                str = str.replace(char, '')
        return str

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = common_signup_UI()
    ui.setupUi(MainWindow)

    MainWindow.showMaximized()

    sys.exit(app.exec_())