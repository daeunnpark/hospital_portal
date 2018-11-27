import sys
import re

# import pymysql -- unused
from PyQt5 import QtCore, QtGui, QtWidgets

# import modules
# from welcome_page import welcome_page_UI
from menu import menu_UI


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


    def setupUi(self, CommonLogin, num):
        CommonLogin.setObjectName("CommonLogin")

        self.centralwidget = QtWidgets.QWidget(CommonLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # Login
        # Username
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setObjectName("label1")
        self.label1.setGeometry(QtCore.QRect(20, 200, 200, 100))
        self.label1.setStyleSheet(
            "color: rgb(46, 125, 132);\n"
            "font-weight: bold;\n"
            'font: 18pt "Lucida Calligraphy";\n'
            "\n"
            ""
        )

        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(250, 200, 500, 50))
        self.lineEdit1.setObjectName("lineEdit1")

        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setObjectName("loginBtn")
        self.loginBtn.setGeometry(QtCore.QRect(1000, 200, 200, 50))
        self.loginBtn.setStyleSheet(
            "color: rgb(46, 125, 132);\n"
            "font-weight: bold;\n"
            'font: 18pt "Lucida Calligraphy";\n'
            "\n"
            ""
        )

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setObjectName("label2")
        self.label2.setGeometry(QtCore.QRect(20, 400, 200, 100))
        self.label2.setStyleSheet(
            "color: rgb(46, 125, 132);\n"
            "font-weight: bold;\n"
            'font: 18pt "Lucida Calligraphy";\n'
            "\n"
            ""
        )

        # Password
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(250, 400, 800, 50))
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit2.setEchoMode(QtWidgets.QLineEdit.Password)  # Password
        CommonLogin.setCentralWidget(self.centralwidget)

        self.gridLayout_2.addWidget(self.label1, 0, 0, QtCore.Qt.AlignLeading)
        self.gridLayout_2.addWidget(self.lineEdit1, 0, 1, QtCore.Qt.AlignLeading)
        self.label1.setFixedWidth(400)
        self.lineEdit1.setFixedWidth(600)
        self.lineEdit1.setFixedHeight(100)
        self.gridLayout_2.addWidget(self.label2, 1, 0, QtCore.Qt.AlignLeading)
        self.gridLayout_2.addWidget(self.lineEdit2, 1, 1, QtCore.Qt.AlignLeading)
        self.label2.setFixedWidth(400)
        self.lineEdit2.setFixedWidth(600)
        self.lineEdit2.setFixedHeight(100)
        self.gridLayout_2.addWidget(self.loginBtn, 5, 1, QtCore.Qt.AlignTrailing)
        self.loginBtn.setFixedWidth(600)

        self.menubar = QtWidgets.QMenuBar(CommonLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CommonLogin)
        self.statusbar.setObjectName("statusbar")
        CommonLogin.setStatusBar(self.statusbar)

        self.retranslateUi(CommonLogin)
        QtCore.QMetaObject.connectSlotsByName(CommonLogin)

    def retranslateUi(self, CommonLogin):
        _translate = QtCore.QCoreApplication.translate
        CommonLogin.setWindowTitle(_translate("CommonLogin", "CommonLogin"))
        self.label1.setText(_translate("CommonLogin", "Username:"))
        self.label2.setText(_translate("CommonLogin", "Password:"))
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
            if(num == 1):
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

            # Add dialog maybe?
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText("Error: Username and Password Combination Does Not Exist in System! Try Again!")
            error_dialog.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = common_login_UI()
    ui.setupUi(MainWindow, 1)  # default patient

    MainWindow.showMaximized()

    sys.exit(app.exec_())
