# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patientsignup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 30, 651, 481))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_height = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_height.setObjectName("lineEdit_height")
        self.gridLayout.addWidget(self.lineEdit_height, 4, 3, 1, 1)
        self.lineEdit_firstname = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_firstname.setObjectName("lineEdit_firstname")
        self.gridLayout.addWidget(self.lineEdit_firstname, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_Creditcard = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Creditcard.setObjectName("lineEdit_Creditcard")
        self.gridLayout.addWidget(self.lineEdit_Creditcard, 6, 1, 1, 1)
        self.lineEdit_SSN = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_SSN.setObjectName("lineEdit_SSN")
        self.gridLayout.addWidget(self.lineEdit_SSN, 5, 1, 1, 1)
        self.lineEdit_lastname = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_lastname.setObjectName("lineEdit_lastname")
        self.gridLayout.addWidget(self.lineEdit_lastname, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_email = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.gridLayout.addWidget(self.lineEdit_email, 2, 1, 1, 1)
        self.lineEdit_Insurance = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Insurance.setObjectName("lineEdit_Insurance")
        self.gridLayout.addWidget(self.lineEdit_Insurance, 7, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 2, 1, 1)
        self.lineEdit_phone = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.gridLayout.addWidget(self.lineEdit_phone, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.lineEdit_weight = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_weight.setObjectName("lineEdit_weight")
        self.gridLayout.addWidget(self.lineEdit_weight, 4, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(540, 510, 164, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "PROFILE"))
        self.label_4.setText(_translate("MainWindow", "Email Address"))
        self.label_5.setText(_translate("MainWindow", "Age"))
        self.label_3.setText(_translate("MainWindow", "Phone Number"))
        self.label_10.setText(_translate("MainWindow", "Insurace Number"))
        self.label_2.setText(_translate("MainWindow", "Lastname"))
        self.label_8.setText(_translate("MainWindow", "SSN"))
        self.label.setText(_translate("MainWindow", "Firstname"))
        self.label_7.setText(_translate("MainWindow", "Height"))
        self.label_9.setText(_translate("MainWindow", "Credit Card Number"))
        self.label_6.setText(_translate("MainWindow", "Weight"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
