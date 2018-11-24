import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

# import modules
# from welcome_page import welcome_page_UI
from menu import menu_UI


class common_login_UI(object):
    def setupUi(self, CommonLogin):
        CommonLogin.setObjectName("CommonLogin")
        CommonLogin.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CommonLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 80, 400, 71))
        self.label.setStyleSheet(
            "color: rgb(46, 125, 132);\n"
            "font-weight: bold;\n"
            'font: 18pt "Lucida Calligraphy";\n'
            "\n"
            ""
        )
        self.label.setObjectName("label")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(2000, 1000, 200, 200))
        self.loginButton.setStyleSheet(
            "color: rgb(46, 125, 132);\n"
            "font-weight: bold;\n"
            'font: 18pt "Lucida Calligraphy";\n'
            "\n"
            ""
        )
        self.loginButton.setObjectName("loginButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(700, 150, 800, 61))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 580, 400, 71))
        self.label_2.setStyleSheet(
            "color: rgb(46, 125, 132);\n"
            "font-weight: bold;\n"
            'font: 18pt "Lucida Calligraphy";\n'
            "\n"
            ""
        )
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(700, 670, 800, 61))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)  # Password
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

        # self.loginButton.clicked.connect(self.changeUI_to_Menu) # set listener
        self.loginButton.clicked.connect(self.authenticateUser)

    def retranslateUi(self, CommonLogin):
        _translate = QtCore.QCoreApplication.translate
        CommonLogin.setWindowTitle(_translate("CommonLogin", "CommonLogin"))
        self.label.setText(_translate("CommonLogin", "Username:"))
        self.label_2.setText(_translate("CommonLogin", "Password:"))
        self.loginButton.setText(_translate("CommonLogin", "Login"))

    def authenticateUser(self):
        cur.execute(
            "SELECT * FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
            (self.lineEdit.text(), self.lineEdit_2.text()),
        )
        authenticate = cur.fetchall()
        if len(authenticate) == 1:
            cur.execute(
                "SELECT FirstName FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
                (self.lineEdit.text(), self.lineEdit_2.text()),
            )
            firstName = str(cur.fetchone()[0])
            cur.execute(
                "SELECT LastName FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
                (self.lineEdit.text(), self.lineEdit_2.text()),
            )
            lastName = str(cur.fetchone()[0])
            cur.execute(
                "SELECT PhoneNumber FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
                (self.lineEdit.text(), self.lineEdit_2.text()),
            )
            phoneNumber = str(cur.fetchone()[0])
            cur.execute(
                "SELECT EmailAddress FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
                (self.lineEdit.text(), self.lineEdit_2.text()),
            )
            emailAddress = str(cur.fetchone()[0])
            cur.execute(
                "SELECT ID FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
                (self.lineEdit.text(), self.lineEdit_2.text()),
            )
            ID = str(cur.fetchone()[0])
            cur.execute("SELECT Age FROM Patient P WHERE PatientID = (%s)", ID)
            age = str(cur.fetchone()[0])
            cur.execute("SELECT Weight FROM Patient P WHERE PatientID = (%s)", ID)
            weight = str(cur.fetchone()[0])
            cur.execute("SELECT Height FROM Patient P WHERE PatientID = (%s)", ID)
            height = str(cur.fetchone()[0])
            cur.execute("SELECT SSN FROM Patient P WHERE PatientID = (%s)", ID)
            ssn = str(cur.fetchone()[0])
            cur.execute(
                "SELECT CreditCardNumber FROM Patient P WHERE PatientID = (%s)", ID
            )
            creditCardNumber = str(cur.fetchone()[0])
            cur.execute(
                "SELECT BillingAmount FROM Patient P WHERE PatientID = (%s)", ID
            )
            billingAmount = str(cur.fetchone()[0])
            cur.execute(
                "SELECT InsuranceNumber FROM Patient P WHERE PatientID = (%s)", ID
            )
            insuranceNumber = str(cur.fetchone()[0])
            cur.execute(
                "SELECT MedicationList FROM Patient P WHERE PatientID = (%s)", ID
            )
            medicationList = str(cur.fetchone()[0])
            cur.execute("SELECT Date FROM Appointment A WHERE PatientID = (%s)", ID)
            appointmentDates = cur.fetchall()
            self.uiNew = menu_UI()
            self.uiNew.setupUi(
                MainWindow,
                firstName,
                lastName,
                phoneNumber,
                emailAddress,
                ID,
                age,
                ssn,
                weight,
                height,
                creditCardNumber,
                billingAmount,
                insuranceNumber,
                medicationList,
                appointmentDates,
            )
            MainWindow.showFullScreen()
        else:
            print("no user")
