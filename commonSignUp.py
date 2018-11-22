# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commonSignUp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CommonSignUp(object):
    def setupUi(self, CommonSignUp):
        CommonSignUp.setObjectName("CommonSignUp")
        CommonSignUp.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CommonSignUp)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 300, 71))
        self.label.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 90, 521, 61))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1300, 20, 300, 71))
        self.label_2.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1500, 90, 521, 61))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 500, 71))
        self.label_3.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 240, 521, 61))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1300, 170, 500, 71))
        self.label_4.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(1500, 240, 521, 61))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 300, 541, 71))
        self.label_5.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 380, 521, 61))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 500, 541, 71))
        self.label_6.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 580, 521, 61))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1300, 500, 541, 71))
        self.label_7.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";\n"
"\n"
"")
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(1500, 580, 521, 61))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        CommonSignUp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CommonSignUp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        CommonSignUp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CommonSignUp)
        self.statusbar.setObjectName("statusbar")
        CommonSignUp.setStatusBar(self.statusbar)

        self.retranslateUi(CommonSignUp)
        QtCore.QMetaObject.connectSlotsByName(CommonSignUp)

    def retranslateUi(self, CommonSignUp):
        _translate = QtCore.QCoreApplication.translate
        CommonSignUp.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "First Name:"))
        self.label_2.setText(_translate("MainWindow", "Last Name:"))
        self.label_3.setText(_translate("MainWindow", "Phone Number:"))
        self.label_4.setText(_translate("MainWindow", "Email Address:"))
        self.label_5.setText(_translate("MainWindow", "Username: "))
        self.label_6.setText(_translate("MainWindow", "Password:"))
        self.label_7.setText(_translate("MainWindow", "Re-Enter Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CommonSignUp = QtWidgets.QMainWindow()
    ui = Ui_CommonSignUp()
    ui.setupUi(CommonSignUp)
    CommonSignUp.show()
    sys.exit(app.exec_())

