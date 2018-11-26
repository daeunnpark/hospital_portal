import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

# import modules
class login_or_register_UI(object):
    def setupUi(self, loginOrRegister, num):
        loginOrRegister.setObjectName("loginOrRegister")
        self.centralwidget = QtWidgets.QWidget(loginOrRegister)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.commonLoginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.commonLoginBtn.setObjectName("commonLoginBtn")
        #self.commonLoginBtn.setGeometry(QtCore.QRect(100, 200, 900, 100))
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

        self.gridLayout_2.addWidget(self.commonLoginBtn, 1, 0, QtCore.Qt.AlignCenter)
        self.commonLoginBtn.setFixedWidth(1000)
        self.commonLoginBtn.setFixedHeight(200)
        self.gridLayout_2.addWidget(self.label, 0, 0, QtCore.Qt.AlignLeft)
        self.label.setFixedWidth(400)
        self.gridLayout_2.addWidget(self.accesscodeBtn, 0, 0, QtCore.Qt.AlignHCenter)
        self.accesscodeBtn.setFixedWidth(1000)
        self.accesscodeBtn.setFixedHeight(200)


        if num == 4:
            self.label.setVisible(False)
            self.accesscodeBtn.setVisible(False)
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
    ui.setupUi(MainWindow, 1)  # default Patient

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
