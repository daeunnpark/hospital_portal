import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

# from first import *


class loginOrRegister_UI(object):
    def setupUi(self, loginOrRegister):
        print("setupUI")
        loginOrRegister.setObjectName("loginOrRegister")
        loginOrRegister.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(loginOrRegister)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1000, 880, 1000, 200))
        self.pushButton.setStyleSheet(
            'font: 15pt "Lucida Calligraphy";\n' "color: rgb(46, 125, 132)"
        )
        self.pushButton.setObjectName("pushButton")
        self.commonLoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.commonLoginButton.setGeometry(QtCore.QRect(300, 400, 2000, 200))
        self.commonLoginButton.setStyleSheet(
            'font: 20pt "Lucida Calligraphy";\n' "color: rgb(46, 125, 132)"
        )
        self.commonLoginButton.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 900, 301, 131))
        self.label.setStyleSheet(
            'font: 20pt "Lucida Calligraphy";\n'
            "color: rgb(0, 0, 0);\n"
            "font-weight:bold;"
        )
        self.label.setObjectName("label")
        loginOrRegister.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginOrRegister)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        loginOrRegister.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginOrRegister)
        self.statusbar.setObjectName("statusbar")
        loginOrRegister.setStatusBar(self.statusbar)

        self.retranslateUi(loginOrRegister)
        QtCore.QMetaObject.connectSlotsByName(loginOrRegister)

    #        self.commonLoginButton.clicked.connect(
    #           self.changeUI_to_CommonLogin
    #      )  # set listener
    #      self.pushButton.clicked.connect(self.changeUI_to_AccessCode)

    def retranslateUi(self, loginOrRegister):
        print("retranslate")
        _translate = QtCore.QCoreApplication.translate
        loginOrRegister.setWindowTitle(
            _translate("loginOrRegister", "Login or Register")
        )
        self.pushButton.setText(
            _translate("loginOrRegister", "Sign Up Using Your Access Code")
        )
        self.commonLoginButton.setText(_translate("loginOrRegister", "Login"))
        self.label.setText(_translate("loginOrRegister", "New User?"))


# main class of loginOrRegister.py
# This is only executed with command python login_page.py
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = loginOrRegister_UI()
    ui.setupUi(MainWindow)

    MainWindow.showMaximized()

    sys.exit(app.exec_())
"""
    def changeUI_to_CommonLogin(self):  # change UI to Menu
        self.uiLogin = Ui_CommonLogin()
        self.uiLogin.setupUi(loginOrRegister)
        loginOrRegister.showMaximized()

    def changeUI_to_AccessCode(self):  # change UI to Menu
        self.uiAccess = Ui_Access()
        self.uiAccess.setupUi(loginOrRegister)
        loginOrRegister.showMaximized()
"""
