import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

# import modules

# newUI- Done


class login_or_register_UI(object):
    def setupUi(self, loginOrRegister, num):
        loginOrRegister.setObjectName("loginOrRegister")
        loginOrRegister.setStyleSheet("background-color: rgb(225,247,251);\n"
                                      "")
        self.centralwidget = QtWidgets.QWidget(loginOrRegister)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(600, 300))
        self.widget.setStyleSheet("background-color: rgb(243,255,255);")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.commonLoginBtn = QtWidgets.QPushButton(self.widget)
        self.commonLoginBtn.setMinimumSize(QtCore.QSize(0, 60))
        self.commonLoginBtn.setStyleSheet("font: 30pt \"Arial\";\n"
                                          "background-color: rgb(232, 232, 232);")
        self.commonLoginBtn.setObjectName("commonLoginBtn")
        self.gridLayout.addWidget(self.commonLoginBtn, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.accesscodeBtn = QtWidgets.QPushButton(self.widget)
        self.accesscodeBtn.setMinimumSize(QtCore.QSize(0, 60))
        self.accesscodeBtn.setStyleSheet("font: 30pt \"Arial\";\n"
                                         "background-color: rgb(232, 232, 232);")
        self.accesscodeBtn.setObjectName("accesscodeBtn")
        self.gridLayout.addWidget(self.accesscodeBtn, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 40pt \"Arial\";\n"
                                 "")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        loginOrRegister.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginOrRegister)
        QtCore.QMetaObject.connectSlotsByName(loginOrRegister)

    def retranslateUi(self, loginOrRegister):
        _translate = QtCore.QCoreApplication.translate
        loginOrRegister.setWindowTitle(
            _translate("loginOrRegister", "Login or Register")
        )
        self.accesscodeBtn.setText(
            _translate("loginOrRegister", "Sign Up")
        )
        self.commonLoginBtn.setText(_translate("loginOrRegister", "Login"))

        self.label_2.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\">Existing User</p></body></html>"))

        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\">New User?</p></body></html>"))


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
