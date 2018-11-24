import sys

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

    def setupUi(self, CommonLogin):
        CommonLogin.setObjectName("CommonLogin")
        CommonLogin.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(CommonLogin)
        self.centralwidget.setObjectName("centralwidget")

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
        # self.lineEdit2.setText("")
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit2.setEchoMode(QtWidgets.QLineEdit.Password)  # Password
        CommonLogin.setCentralWidget(self.centralwidget)

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
    def authenticate_user(self, cur):

        cur.execute(
            "SELECT * FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
            (self.lineEdit1.text(), self.lineEdit2.text()),
        )
        authenticate = cur.fetchall()

        # If user exists in DB
        # Load/store its profile to self obj to pass to test obj(main module)
        if len(authenticate) == 1:
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
            # Add dialog maybe
            print("no user")


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = common_login_UI()
    ui.setupUi(MainWindow)

    MainWindow.showMaximized()

    sys.exit(app.exec_())
