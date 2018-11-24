import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

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
        w.commonLoginButton.clicked.connect(self.setwindowTo_common_login)
        w.accesscodeBtn.clicked.connect(self.setwindowTo_access_code)

        MainWindow.showMaximized()

    def setwindowTo_common_login(self):
        w = common_login_UI()
        w.setupUi(MainWindow)

        MainWindow.showMaximized()

    def setwindowTo_access_code(self):
        w = access_code_UI()
        w.setupUi(MainWindow)

        MainWindow.showMaximized()


if __name__ == "__main__":
    # Initialize database connection
    # commented out by Daeun for test run
    """
    conn = pymysql.connect(
        host="localhost", port=3306, user="root", passwd="root", db="hospital"
    )
    
    conn = pymysql.connect(
        host="10.245.235.98",
        port=3306,
        user="root",
        passwd="hospitalCSE305!",
        db="hospital",
    )
    
    # Initialize the database cursor
    cur = conn.cursor()
    """

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    # Create an instance of test
    m = test()

    sys.exit(app.exec_())
