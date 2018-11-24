import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

# import modules
from welcome_page import welcome_page_UI
from login_or_register import login_or_register_UI
from common_login import common_login_UI
from access_code import access_code_UI
from common_signup import common_signup_UI
from menu import menu_UI


class test(object):
    # By default, initialize window to welcome_page.UI
    def __init__(self, parent=None):
        w = welcome_page_UI()
        w.setupUi(MainWindow)
        # when user selects an option(pateint for now), set window to login_or_register.py
        w.patientBtn.clicked.connect(self.setwindowTo_login_or_reigster)
        MainWindow.showMaximized()

    # Set window to login_or_register_UI
    def setwindowTo_login_or_reigster(self):
        w = login_or_register_UI()
        w.setupUi(MainWindow)
        w.commonLoginBtn.clicked.connect(self.setwindowTo_common_login)
        w.accesscodeBtn.clicked.connect(self.setwindowTo_access_code)

        MainWindow.showMaximized()

    def setwindowTo_common_login(self):
        w = common_login_UI()
        w.setupUi(MainWindow)
        print(cur)
        # w.cur = cur
        print("beforeall")

        w.loginBtn.clicked.connect(lambda: self.authenticate_user(w))
        # w.authenticate_user(cur))
        # widget.btn_ckt1.clicked.connect(lambda: micCocktail("string"))
        MainWindow.showMaximized()
        print("afterall")

        # if w.firstName is not None:
        #    self.setwindowTo_menu(w)

        print("nonono")
        # MainWindow.showMaximized()

    def authenticate_user(self, w):
        print("AUTHENTIFICATION +++++")
        print(cur)

        cur.execute(
            "SELECT * FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
            (w.lineEdit1.text(), w.lineEdit2.text()),
        )
        print("here?")
        authenticate = cur.fetchall()

        # initalize all data
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
        print("gg")

        if len(authenticate) == 1:
            cur.execute(
                "SELECT FirstName FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
                (w.lineEdit1.text(), w.lineEdit2.text()),
            )
            self.firstName = str(cur.fetchone()[0])

            cur.execute(
                "SELECT LastName FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
                (w.lineEdit1.text(), w.lineEdit2.text()),
            )
            lastName = str(cur.fetchone()[0])

            cur.execute(
                "SELECT PhoneNumber FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
                (w.lineEdit1.text(), w.lineEdit2.text()),
            )
            phoneNumber = str(cur.fetchone()[0])

            cur.execute(
                "SELECT EmailAddress FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
                (w.lineEdit1.text(), w.lineEdit2.text()),
            )
            emailAddress = str(cur.fetchone()[0])

            cur.execute(
                "SELECT ID FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
                (w.lineEdit1.text(), w.lineEdit2.text()),
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

            # moved to test.py

            """
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
            """
            self.setwindowTo_menu()
        else:
            print("no user")

        print("this is all")

    def setwindowTo_access_code(self):
        w = access_code_UI()
        w.setupUi(MainWindow)

        MainWindow.showMaximized()

    def setwindowTo_menu(self):

        w = menu_UI()
        print("first name ")
        print(w.firstName)

        w.setupUi(
            MainWindow,
            self.firstName,
            self.lastName,
            self.phoneNumber,
            self.emailAddress,
            self.ID,
            self.age,
            self.ssn,
            self.weight,
            self.height,
            self.creditCardNumber,
            self.billingAmount,
            self.insuranceNumber,
            self.medicationList,
            self.appointmentDates,
        )

        MainWindow.showMaximized()


"""
 w.lastName,
            w.phoneNumber,
            w.emailAddress,
            w.ID,
            w.age,
            w.ssn,
            w.weight,
            w.height,
            w.creditCardNumber,
            w.billingAmount,
            w.insuranceNumber,
            w.medicationList,
            w.appointmentDates,
    def user_exist(self, cur):
        cur.execute(
            "SELECT * FROM Person P WHERE Username = (%s) AND UserPassword = (%s)",
            (self.lineEdit1.text(), self.lineEdit2.text()),
        )
        authenticate = cur.fetchall()

        if len(authenticate) == 1:
            return True
        return False


    def authenticate_user2(self, w):
        w = w.authenticate_user

        self.setwindowTo_menu()

"""


if __name__ == "__main__":
    # Initialize database connection
    # commented out by Daeun for test run
    """
    conn = pymysql.connect(
        host="localhost", port=3306, user="root", passwd="root", db="hospital"
    )
    """
    conn = pymysql.connect(
        host="10.245.235.98",
        port=3306,
        user="root",
        passwd="hospitalCSE305!",
        db="hospital",
    )

    # Initialize the database cursor
    cur = conn.cursor()
    print(cur)

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    # Create an instance of test
    m = test()

    sys.exit(app.exec_())
