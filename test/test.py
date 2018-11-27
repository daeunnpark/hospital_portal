import sys
import pymysql
from PyQt5 import QtWidgets  # QtCore, QtGui - unused

# from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

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

        # when user selects an option, set window to login_or_register.py
        w.patientBtn.clicked.connect(lambda: self.setwindowTo_login_or_register(1))
        w.doctorBtn.clicked.connect(lambda: self.setwindowTo_login_or_register(2))
        w.nurseBtn.clicked.connect(lambda: self.setwindowTo_login_or_register(3))
        w.departmentAdminBtn.clicked.connect(
            lambda: self.setwindowTo_login_or_register(4)
        )

        MainWindow.showMaximized()

    def setwindowTo_login_or_register(self, num):
        w = login_or_register_UI()
        w.setupUi(MainWindow, num)

        w.commonLoginBtn.clicked.connect(lambda: self.setwindowTo_common_login(num))
        w.accesscodeBtn.clicked.connect(lambda: self.setwindowTo_access_code(num))

        MainWindow.showMaximized()

    def setwindowTo_common_login(self, num):
        w = common_login_UI()
        w.setupUi(MainWindow, num)

        w.loginBtn.clicked.connect(lambda: self.authenticate_user(w, num))

        MainWindow.showMaximized()

    def setwindowTo_access_code(self, num):
        w = access_code_UI()
        w.setupUi(MainWindow, num)

        w.pushButton.clicked.connect(lambda: self.authenticate_access_code(w, num))

        MainWindow.showMaximized()

    def authenticate_user(self, w, num):
        w.authenticate_user(cur, num)

        # if user exists
        if w.ID is not None:
            self.setwindowTo_menu(w)
        # else, still on event listener

    def authenticate_access_code(self, w, num):
        w.authenticate_access_code(cur)

        # if access code exists
        if w.rowcount != 0:
            print(w.authenticateCode[0][0])
            accessCodeReceived = w.authenticateCode[0][0]
            self.setwindowTo_common_signup(num, accessCodeReceived)

    def setwindowTo_common_signup(self, num, accessCodeReceived):
        w = common_signup_UI()
        w.setupUi(MainWindow, num)
        if(num == 1):
            w.pushButton.clicked.connect(lambda: w.CreatePatient(cur, conn, accessCodeReceived))
        if(num == 2):
            w.pushButton.clicked.connect(lambda: w.CreateDoctor(cur, conn, accessCodeReceived))
        if(num == 3):
            w.pushButton.clicked.connect(lambda: w.CreateNurse(cur, conn, accessCodeReceived))
        # if new Patient is created
        if w.newP == True:
            conn.commit()
            self.setwindowTo_common_login(1)
        if w.newD == True:
            conn.commit()
            self.setwindowTo_common_login(2)
        if w.newN == True:
            conn.commit()
            self.setwindowTo_common_login(3)

        MainWindow.showMaximized()

    def setwindowTo_menu(self, w):
        menu_UI().setupUi(
            MainWindow,
            w.firstName,
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
            w.startTimes,
            w.endTimes,
            w.appointmentIDs,
            cur,
            conn,
        )
        # btn clicker too add
        MainWindow.showMaximized()


if __name__ == "__main__":
    # Initialize database connection
    """
    conn = pymysql.connect(
        host="localhost", port=3306, user="root", passwd="root", db="hospital"
    )
    """

    """conn = pymysql.connect(
        host="localhost", port=3306, user="root", passwd="root", db="hospital"
    )"""
    
    conn = pymysql.connect(
        host="10.245.235.98",
        port=3306,
        user="root",
        passwd="hospitalCSE305!",
        db="hospital",
    )

    # Initialize the database cursor
    cur = conn.cursor()

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    # Create an instance of test
    m = test()

    sys.exit(app.exec_())
