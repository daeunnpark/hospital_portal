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
        w.patientBtn.clicked.connect(
            lambda: self.setwindowTo_login_or_register(1))
        w.doctorBtn.clicked.connect(
            lambda: self.setwindowTo_login_or_register(2))
        w.nurseBtn.clicked.connect(
            lambda: self.setwindowTo_login_or_register(3))
        w.departmentAdminBtn.clicked.connect(
            lambda: self.setwindowTo_common_login(4)
        )

        MainWindow.showMaximized()

    def setwindowTo_login_or_register(self, num):
        w = login_or_register_UI()
        w.setupUi(MainWindow, num)

        w.commonLoginBtn.clicked.connect(
            lambda: self.setwindowTo_common_login(num))
        w.accesscodeBtn.clicked.connect(
            lambda: self.setwindowTo_access_code(num))

        MainWindow.showMaximized()

    def setwindowTo_common_login(self, num):
        w = common_login_UI()
        w.setupUi(MainWindow, num)

        w.loginBtn.clicked.connect(lambda: self.authenticate_user(w, num))
        MainWindow.showMaximized()

    def setwindowTo_access_code(self, num):
        w = access_code_UI()
        w.setupUi(MainWindow, num)

        w.pushButton.clicked.connect(
            lambda: self.authenticate_access_code(w, num))

        MainWindow.showMaximized()

    def authenticate_user(self, w, num):
        w.authenticate_user(cur, num)

        # if user exists
        if w.ID is not None:
            self.setwindowTo_menu(w, num)
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

        if num == 1:
            w.pushButton.clicked.connect(
                lambda: w.CreatePatient(cur, conn, accessCodeReceived)
            )
        if num == 2:
            w.pushButton.clicked.connect(
                lambda: w.CreateDoctor(cur, conn, accessCodeReceived)
            )
        if num == 3:
            w.pushButton.clicked.connect(
                lambda: w.CreateNurse(cur, conn, accessCodeReceived)
            )

        """
        # Previous code for Redirection, not working
        if w.newP == True:
            # conn.commit()
            self.setwindowTo_common_login(1)

        if w.newD == True:
            # conn.commit()
            self.setwindowTo_common_login(2)
        if w.newN == True:
            # conn.commit()
            self.setwindowTo_common_login(3)
        """
        MainWindow.showMaximized()

        # New code for Redirection, fails to load menu when user has no appt
        w.pushButton.clicked.connect(lambda: self.setLoginNewUser(w, num))

    def setLoginNewUser(self, w, num):
        if w.newP == True:
            conn.commit()
            self.setwindowTo_common_login(1)
        if w.newD == True:
            conn.commit()
            self.setwindowTo_common_login(2)
        if w.newN == True:
            conn.commit()
            self.setwindowTo_common_login(3)

    def setwindowTo_menu(self, w, num):
        menu = menu_UI()
        # if you are updating args of menu.setupUI(), update common_login.py, menu.py as well
        menu.setupUi(
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
            w.doctorID,
            w.nurseID,
            w.departmentAdminID,
            num,
            cur,
            conn,
        )
        menu.EditBtn.clicked.connect(lambda: menu.editProfile(num, cur, conn))
        MainWindow.showMaximized()


if __name__ == "__main__":
    # Initialize database connection

    """conn = pymysql.connect(
        host="10.245.235.98",
        port=3306,
        user="root",
        passwd="hospitalCSE305!",
        db="hospital",
    )"""

    conn = pymysql.connect(
        host="localhost", port=3306, user="root", passwd="", db="test2"
    )

    # Initialize the database cursor
    cur = conn.cursor()

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    # Create an instance of test
    m = test()

    ret = app.exec_()
    conn.commit()
    cur.close()
    del cur
    conn.close()
    sys.exit(ret)
