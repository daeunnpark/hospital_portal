import sys

from PyQt5 import QtCore, QtGui, QtWidgets

# Unused
# from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
# import pymysql
# import modules
# from login_or_register import login_or_register_UI


class welcome_page_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # Welcome label
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(720, 120, 1500, 200))

        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")

        self.imageLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel1.setGeometry(QtCore.QRect(400, -300, 1999, 1000))

        self.imageLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel2.setGeometry(QtCore.QRect(1850, -300, 1999, 1000))

        self.imageLabel1.setObjectName("imageLabel1")
        self.imageLabel2.setObjectName("imageLabel2")

        self.pixmap = QtGui.QPixmap("icon.PNG")
        self.imageLabel1.setPixmap(self.pixmap)
        self.imageLabel2.setPixmap(self.pixmap)

        # Options
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)

        # absolute geometry
        # self.groupBox.setGeometry(QtCore.QRect(850, 400, 800, 600))
        self.groupBox.setGeometry(QtCore.QRect(400, 300, 800, 600))

        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")

        self.patientBtn = QtWidgets.QPushButton(self.groupBox)
        self.patientBtn.setObjectName("patientButton")
        self.gridLayout.addWidget(self.patientBtn, 0, 0, 1, 1)

        self.doctorBtn = QtWidgets.QPushButton(self.groupBox)
        self.doctorBtn.setObjectName("doctorBtn")
        self.gridLayout.addWidget(self.doctorBtn, 1, 0, 1, 1)

        self.nurseBtn = QtWidgets.QPushButton(self.groupBox)
        self.nurseBtn.setObjectName("nurseBtn")
        self.gridLayout.addWidget(self.nurseBtn, 2, 0, 1, 1)

        self.departmentAdminBtn = QtWidgets.QPushButton(self.groupBox)
        self.departmentAdminBtn.setObjectName("departmentAdminBtn")
        self.gridLayout.addWidget(self.departmentAdminBtn, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome"))
        self.label.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:18pt; font-weight:600;">Welcome to Healthcare United Patient Portal</span></p><p><br/></p></body></html>',
            )
        )
        self.label.setStyleSheet("color: teal")
        self.patientBtn.setText(_translate("MainWindow", "Patient"))
        self.doctorBtn.setText(_translate("MainWindow", "Doctor"))
        self.nurseBtn.setText(_translate("MainWindow", "Nurse"))
        self.departmentAdminBtn.setText(_translate("MainWindow", "Admin"))


# This is only executed with command python welcome_page.py
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = welcome_page_UI()
    ui.setupUi(MainWindow)

    # MainWindow.show()
    MainWindow.showMaximized()

    sys.exit(app.exec_())
