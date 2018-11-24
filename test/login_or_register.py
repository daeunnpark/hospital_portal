import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

# import modules
class login_or_register_UI(object):
    def setupUi(self, loginOrRegister):
        loginOrRegister.setObjectName("loginOrRegister")
        loginOrRegister.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(loginOrRegister)
        self.centralwidget.setObjectName("centralwidget")

        self.commonLoginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.commonLoginBtn.setObjectName("commonLoginBtn")
        self.commonLoginBtn.setGeometry(QtCore.QRect(100, 200, 900, 100))
        self.commonLoginBtn.setStyleSheet(
            'font: 20pt "Lucida Calligraphy";\n' "color: rgb(46, 125, 132)"
        )

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QtCore.QRect(100, 600, 301, 131))
        self.label.setStyleSheet(
            'font: 20pt "Lucida Calligraphy";\n'
            "color: rgb(0, 0, 0);\n"
            "font-weight:bold;"
        )

        # pushbutton -> accesscodeBtn
        self.accesscodeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.accesscodeBtn.setObjectName("accesscodeBtn")
        self.accesscodeBtn.setGeometry(QtCore.QRect(600, 600, 800, 100))
        self.accesscodeBtn.setStyleSheet(
            'font: 15pt "Lucida Calligraphy";\n' "color: rgb(46, 125, 132)"
        )

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

    #        self.commonLoginBtn.clicked.connect(
    #           self.changeUI_to_CommonLogin
    #      )  # set listener
    #      self.pushButton.clicked.connect(self.changeUI_to_AccessCode)

    def retranslateUi(self, loginOrRegister):
        _translate = QtCore.QCoreApplication.translate
        loginOrRegister.setWindowTitle(
            _translate("loginOrRegister", "Login or Register")
        )
        self.accesscodeBtn.setText(
            _translate("loginOrRegister", "Sign Up Using Your Access Code")
        )
        self.commonLoginBtn.setText(_translate("loginOrRegister", "Login"))
        self.label.setText(_translate("loginOrRegister", "New User?"))


# main class of loginOrRegister.py
# This is only executed with command python login_or_register.py
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = login_or_register_UI()
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
