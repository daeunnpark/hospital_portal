# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commonlogin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CommonLogin(object):
    def setupUi(self, CommonLogin):
        CommonLogin.setObjectName("CommonLogin")
        CommonLogin.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CommonLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 80, 181, 71))
        self.label.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 150, 321, 61))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 280, 181, 71))
        self.label_2.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 370, 321, 61))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        CommonLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CommonLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CommonLogin)
        self.statusbar.setObjectName("statusbar")
        CommonLogin.setStatusBar(self.statusbar)

        self.retranslateUi(CommonLogin)
        QtCore.QMetaObject.connectSlotsByName(CommonLogin)

    def retranslateUi(self, CommonLogin):
        _translate = QtCore.QCoreApplication.translate
        CommonLogin.setWindowTitle(_translate("CommonLogin", "CommonLogin"))
        self.label.setText(_translate("CommonLogin", "Username:"))
        self.label_2.setText(_translate("CommonLogin", "Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_CommonLogin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

