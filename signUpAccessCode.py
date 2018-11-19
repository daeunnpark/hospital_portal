# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signUpAccessCode.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Access(object):
    def setupUi(self, Access):
        Access.setObjectName("Access")
        Access.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Access)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 40, 1400, 171))
        self.label.setStyleSheet("font: 20pt \"Lucida Calligraphy\";\n"
"color: rgb(46, 125, 132);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(600, 550, 1400, 111))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(2000, 1000, 241, 81))
        self.pushButton.setStyleSheet("font: 20pt \"Lucida Calligraphy\";\n"
"color: rgb(46, 125, 132);")
        self.pushButton.setObjectName("pushButton")
        Access.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Access)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Access.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Access)
        self.statusbar.setObjectName("statusbar")
        Access.setStatusBar(self.statusbar)

        self.retranslateUi(Access)
        QtCore.QMetaObject.connectSlotsByName(Access)

    def retranslateUi(self, Access):
        _translate = QtCore.QCoreApplication.translate
        Access.setWindowTitle(_translate("Access", "Access"))
        self.label.setText(_translate("Access", "Enter Your Access Code Received Via Email:"))
        self.pushButton.setText(_translate("Access", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Access()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

