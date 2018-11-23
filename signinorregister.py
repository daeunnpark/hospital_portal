# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signinorregister.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from first import *


class Ui_SignInOrRegister(object):
    def setupUi(self, SignInOrRegister):
        SignInOrRegister.setObjectName("SignInOrRegister")
        SignInOrRegister.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SignInOrRegister)
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
        SignInOrRegister.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SignInOrRegister)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SignInOrRegister)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SignInOrRegister)
        QtCore.QMetaObject.connectSlotsByName(SignInOrRegister)

        self.commonLoginButton.clicked.connect(
            self.changeUI_to_CommonLogin
        )  # set listener
        self.pushButton.clicked.connect(self.changeUI_to_AccessCode)

    def retranslateUi(self, SignInOrRegister):
        _translate = QtCore.QCoreApplication.translate
        SignInOrRegister.setWindowTitle(
            _translate("SignInOrRegister", "SignInOrRegister")
        )
        self.pushButton.setText(
            _translate("SignInOrRegister", "Sign Up Using Your Access Code")
        )
        self.commonLoginButton.setText(_translate("SignInOrRegister", "Login"))
        self.label.setText(_translate("SignInOrRegister", "New User?"))

    def changeUI_to_CommonLogin(self):  # change UI to Menu
        self.uiLogin = Ui_CommonLogin()
        self.uiLogin.setupUi(MainWindow)
        MainWindow.showMaximized()

    def changeUI_to_AccessCode(self):  # change UI to Menu
        self.uiAccess = Ui_Access()
        self.uiAccess.setupUi(MainWindow)
        MainWindow.showMaximized()
