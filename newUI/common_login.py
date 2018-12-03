import sys
import re

# import pymysql -- unused
from PyQt5 import QtCore, QtGui, QtWidgets

# import modules
# from welcome_page import welcome_page_UI
from menu import menu_UI

# newUI- Done
class common_login_UI(object):
    def __init__(self, parent=None):

        # initalize all data for authenticate_user()
        self.firstName = None
        self.lastName = None
        self.phoneNumber = None
        self.emailAddress = None
        self.ID = None
        self.age = None
        self.weight = None
        self.height = None
        self.ssn = None
        self.creditCardNumber = None
        self.billingAmount = None
        self.insuranceNumber = None
        self.medicationList = None
        self.appointmentDates = None
        self.startTimes = None
        self.endTimes = None
        self.appointmentIDs = None
        self.doctorID = None
        self.nurseID = None
        self.departmentAdminID = None

    def setupUi(self, CommonLogin, num):
        CommonLogin.setObjectName("CommonLogin")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        CommonLogin.setFont(font)
        CommonLogin.setStyleSheet("background-color: rgb(243,255,255);")
        self.centralwidget = QtWidgets.QWidget(CommonLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setMaximumSize(QtCore.QSize(600, 400))
        self.widget.setStyleSheet("background-color: rgb(225,247,251);")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit1.setMaximumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setText("")
        self.lineEdit1.setObjectName("lineEdit1")
        self.gridLayout_2.addWidget(self.lineEdit1, 0, 1, 1, 1)
        self.label1 = QtWidgets.QLabel(self.widget)
        self.label1.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setStyleSheet("font: 40pt \"Arial\";\n"
                                  "\n"
                                  "")
        self.label1.setObjectName("label1")
        self.gridLayout_2.addWidget(self.label1, 0, 0, 1, 1)
        self.lineEdit2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit2.setMaximumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit2.setFont(font)
        self.lineEdit2.setText("")
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit2.setEchoMode(QtWidgets.QLineEdit.Password)  # Password
        self.gridLayout_2.addWidget(self.lineEdit2, 1, 1, 1, 1)
        self.label2 = QtWidgets.QLabel(self.widget)
        self.label2.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setStyleSheet("font-weight: bold;\n"
                                  "font: 40pt \"Arial\";\n"
                                  "\n"
                                  "")
        self.label2.setObjectName("label2")
        self.gridLayout_2.addWidget(self.label2, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget, 1, 2, 1, 1)
        self.loginBtn = QtWidgets.QPushButton(self.widget_2)
        self.loginBtn.setMinimumSize(QtCore.QSize(100, 80))
        self.loginBtn.setMaximumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        self.loginBtn.setFont(font)
        self.loginBtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.loginBtn.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.loginBtn.setObjectName("loginBtn")
        self.gridLayout_3.addWidget(self.loginBtn, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)
        CommonLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(CommonLogin)
        QtCore.QMetaObject.connectSlotsByName(CommonLogin)

    def retranslateUi(self, CommonLogin):
        _translate = QtCore.QCoreApplication.translate
        CommonLogin.setWindowTitle(_translate("CommonLogin", "CommonLogin"))
        self.label1.setText(_translate("CommonLogin", "Username"))
        self.label2.setText(_translate("CommonLogin", "Password"))
        self.loginBtn.setText(_translate("CommonLogin", "Login"))


    # Wrapper function to load user profile
    def authenticate_user(self, cur, num):

        exists = 0

        cur.execute(
            "SELECT * FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
            (self.lineEdit1.text(), self.lineEdit2.text()),
        )

        authenticate = cur.fetchall()

        cur.execute(
            "SELECT ID FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
            (self.lineEdit1.text(), self.lineEdit2.text()),
        )

        userID = cur.fetchall()
        if(cur.rowcount != 0):
            userID = re.sub("[^0-9]", "", str(userID))

            userID = int(userID)


            if num == 1:
                cur.execute(
                    "SELECT * FROM Patient P WHERE PatientID = (%s)",
                    (userID),
                )
                if(cur.rowcount != 0):
                    exists = 1

            elif num == 2:
                cur.execute(
                    "SELECT * FROM Doctor D WHERE DoctorID = (%s)",
                    (userID),
                )
                if(cur.rowcount != 0):
                    exists = 1
            elif num == 3:
                cur.execute(
                    "SELECT * FROM Nurse N WHERE NurseID = (%s)",
                    (userID),
                )
                if(cur.rowcount != 0):
                    exists = 1
            else:
                cur.execute(
                    "SELECT * FROM DepartmentAdmin A WHERE DepartmentAdminID = (%s)",
                    (userID),
                )
                if(cur.rowcount != 0):
                    exists = 1

            myUser = cur.fetchall()

            if cur.rowcount == 0:
                # reset data
                self.firstName = None
                self.lastName = None
                self.phoneNumber = None
                self.emailAddress = None
                self.ID = None
                self.age = None
                self.weight = None
                self.height = None
                self.ssn = None
                self.creditCardNumber = None
                self.billingAmount = None
                self.insuranceNumber = None
                self.medicationList = None
                self.appointmentDates = None
                self.startTimes = None
                self.endTimes = None
                self.appointmentIDs = None
                self.doctorID = None
                self.nurseID = None
                self.departmentAdminID = None

        # If user exists in DB
        # Load/store its profile to self obj to pass to test obj(main module)
        if (len(authenticate) == 1 and exists == 1):
            cur.execute(
                "SELECT FirstName FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
                (self.lineEdit1.text(), self.lineEdit2.text()),
            )
            self.firstName = str(cur.fetchone()[0])

            cur.execute(
                "SELECT LastName FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
                (self.lineEdit1.text(), self.lineEdit2.text()),
            )
            self.lastName = str(cur.fetchone()[0])

            cur.execute(
                "SELECT PhoneNumber FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
                (self.lineEdit1.text(), self.lineEdit2.text()),
            )
            self.phoneNumber = str(cur.fetchone()[0])

            cur.execute(
                "SELECT EmailAddress FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
                (self.lineEdit1.text(), self.lineEdit2.text()),
            )
            self.emailAddress = str(cur.fetchone()[0])

            cur.execute(
                "SELECT ID FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
                (self.lineEdit1.text(), self.lineEdit2.text()),
            )
            self.ID = str(cur.fetchone()[0])

            if num == 1:
                cur.execute("SELECT Age FROM Patient P WHERE PatientID = (%s)", self.ID)
                self.age = str(cur.fetchone()[0])

                cur.execute("SELECT SSN FROM Patient P WHERE PatientID = (%s)", self.ID)
                self.ssn = str(cur.fetchone()[0])

                cur.execute("SELECT Weight FROM Patient P WHERE PatientID = (%s)", self.ID)
                self.weight = str(cur.fetchone()[0])

                cur.execute("SELECT Height FROM Patient P WHERE PatientID = (%s)", self.ID)
                self.height = str(cur.fetchone()[0])

                cur.execute(
                    "SELECT CreditCardNumber FROM Patient P WHERE PatientID = (%s)", self.ID
                )
                self.creditCardNumber = str(cur.fetchone()[0])

                cur.execute(
                    "SELECT BillingAmount FROM Patient P WHERE PatientID = (%s)", self.ID
                )
                self.billingAmount = str(cur.fetchone()[0])

                cur.execute(
                    "SELECT InsuranceNumber FROM Patient P WHERE PatientID = (%s)", self.ID
                )
                self.insuranceNumber = str(cur.fetchone()[0])

                cur.execute(
                    "SELECT MedicationList FROM Patient P WHERE PatientID = (%s)", self.ID
                )
                self.medicationList = str(cur.fetchone()[0])

                cur.execute(
                    "SELECT Date FROM Appointment A WHERE PatientID = (%s)", self.ID
                )
                self.appointmentDates = cur.fetchall()

                cur.execute(
                    "SELECT StartTime FROM Appointment A WHERE PatientID = (%s)", self.ID
                )
                self.startTimes = cur.fetchall()

                cur.execute(
                    "SELECT EndTime FROM Appointment A WHERE PatientID = (%s)", self.ID
                )
                self.endTimes = cur.fetchall()

                cur.execute(
                    "SELECT AppointmentID FROM Appointment A WHERE PatientID = (%s)",
                    self.ID,
                )
                self.appointmentIDs = cur.fetchall()

                cur.execute(
                    "SELECT DoctorID FROM Patient P WHERE PatientID = (%s)", self.ID
                )
                self.doctorID = str(cur.fetchone()[0])              
                
                cur.execute(
                    "SELECT NurseID FROM Patient P WHERE PatientID = (%s)", self.ID
                )
                self.nurseID = str(cur.fetchone()[0]) 
                cur.execute(
                    "SELECT AdminID FROM Patient P WHERE PatientID = (%s)", self.ID
                )
                self.departmentAdminID = str(cur.fetchone()[0]) 

            elif num == 2:

                cur.execute(
                    "SELECT DepartmentID FROM Employee E WHERE EmployeeID = (%s)", self.ID
                )
                # patient's ssn = placeholder for DepartmentID
                self.ssn = str(cur.fetchone()[0])

                cur.execute(
                    "SELECT Specialty FROM Doctor D WHERE DoctorID = (%s)", self.ID
                )
                # patient's weight = placeholder for Specialty
                self.weight = str(cur.fetchone()[0])

                cur.execute(
                    "SELECT MedicalLicense FROM Doctor D WHERE DoctorID = (%s)", self.ID
                )
                # patient's height = placeholder for MedicalLicense
                self.height = str(cur.fetchone()[0])

                cur.execute(
                    "SELECT Date FROM Appointment A WHERE DoctorID = (%s)", self.ID
                )
                self.appointmentDates = cur.fetchall()

                cur.execute(
                    "SELECT StartTime FROM Appointment A WHERE DoctorID = (%s)", self.ID
                )
                self.startTimes = cur.fetchall()

                cur.execute(
                    "SELECT EndTime FROM Appointment A WHERE DoctorID = (%s)", self.ID
                )
                self.endTimes = cur.fetchall()

                cur.execute(
                    "SELECT AppointmentID FROM Appointment A WHERE DoctorID = (%s)",
                    self.ID,
                )
                self.appointmentIDs = cur.fetchall()

            elif num == 3:

                cur.execute(
                    "SELECT DepartmentID FROM Employee E WHERE EmployeeID = (%s)", self.ID
                )
                # patient's ssn = placeholder for DepartmentID
                self.ssn = str(cur.fetchone()[0])

                cur.execute(
                    "SELECT Specialty FROM Nurse N WHERE NurseID = (%s)", self.ID
                )
                # patient's weight = placeholder for Specialty
                self.weight = str(cur.fetchone()[0])

                cur.execute(
                    "SELECT MedicalLicense FROM Nurse N WHERE NurseID = (%s)", self.ID
                )
                # patient's height = placeholder for MedicalLicense
                self.height = str(cur.fetchone()[0])


                cur.execute(
                    "SELECT Date FROM Appointment A WHERE NurseID = (%s)", self.ID
                )
                self.appointmentDates = cur.fetchall()

                cur.execute(
                    "SELECT StartTime FROM Appointment A WHERE NurseID = (%s)", self.ID
                )
                self.startTimes = cur.fetchall()

                cur.execute(
                    "SELECT EndTime FROM Appointment A WHERE NurseID = (%s)", self.ID
                )
                self.endTimes = cur.fetchall()

                cur.execute(
                    "SELECT AppointmentID FROM Appointment A WHERE NurseID = (%s)",
                    self.ID,
                )
                self.appointmentIDs = cur.fetchall()

            else:

                cur.execute(
                    "SELECT DepartmentID FROM Employee E WHERE EmployeeID = (%s)", self.ID
                )
                # patient's ssn = placeholder for DepartmentID
                self.ssn = str(cur.fetchone()[0])

                cur.execute(
                    "SELECT SecurityCode FROM DepartmentAdmin D WHERE DepartmentAdminID = (%s)", self.ID
                )
                # patient's weight = placeholder for SecurityCode
                self.weight = str(cur.fetchone()[0])

                cur.execute(
                    "SELECT Date FROM Appointment A WHERE DepartmentAdminID = (%s)", self.ID
                )
                self.appointmentDates = cur.fetchall()

                cur.execute(
                    "SELECT StartTime FROM Appointment A WHERE DepartmentAdminID = (%s)", self.ID
                )
                self.startTimes = cur.fetchall()

                cur.execute(
                    "SELECT EndTime FROM Appointment A WHERE DepartmentAdminID = (%s)", self.ID
                )
                self.endTimes = cur.fetchall()

                cur.execute(
                    "SELECT AppointmentID FROM Appointment A WHERE DepartmentAdminID = (%s)",
                    self.ID,
                )
                self.appointmentIDs = cur.fetchall()

            # print("LOGIN Successful")
        else:
            # reset data
            self.firstName = None
            self.lastName = None
            self.phoneNumber = None
            self.emailAddress = None
            self.ID = None
            self.age = None
            self.weight = None
            self.height = None
            self.ssn = None
            self.creditCardNumber = None
            self.billingAmount = None
            self.insuranceNumber = None
            self.medicationList = None
            self.appointmentDates = None
            self.startTimes = None
            self.endTimes = None
            self.appointmentIDs = None
            self.doctorID = None
            self.nurseID = None
            self.departmentAdminID = None

            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setIcon(QtWidgets.QMessageBox().Warning)
            error_dialog.setText("\nUsername and Password Combination Does Not Exist in System! \nTry Again!")
            error_dialog.exec()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = common_login_UI()
    ui.setupUi(MainWindow, 1)  # default patient

    MainWindow.showMaximized()

    sys.exit(app.exec_())

