import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

# import modules
from login_or_register import login_or_register_UI


class welcome_page_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(720, 120, 1500, 200))
        self.imageLabel.setGeometry(QtCore.QRect(400, -300, 1999, 1000))
        self.imageLabel2.setGeometry(QtCore.QRect(1850, -300, 1999, 1000))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel2.setObjectName("imageLabel2")
        self.pixmap = QtGui.QPixmap("icon.PNG")
        self.imageLabel.setPixmap(self.pixmap)
        self.imageLabel2.setPixmap(self.pixmap)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(850, 400, 800, 600))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")

        # Renamed pushButton -> patient Btn for better understanding in test.py
        self.patientBtn = QtWidgets.QPushButton(self.groupBox)
        # self.patientBtn.setObjectName("pushButton")

        self.gridLayout.addWidget(self.patientBtn, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        # self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_5.setGeometry(QtCore.QRect(340, 460, 114, 32))
        # self.pushButton_5.setObjectName("pushButton_5")
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

        # moved to test.py
        # set clicklistener
        # self.pushButton.clicked.connect(self.changeUI_to_SignInOrRegister)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:18pt; font-weight:600;">Welcome to Healthcare United Patient Portal</span></p><p><br/></p></body></html>',
            )
        )
        self.label.setStyleSheet("color: teal")
        self.patientBtn.setText(_translate("MainWindow", "Patient"))
        self.pushButton_2.setText(_translate("MainWindow", "Doctor"))
        self.pushButton_3.setText(_translate("MainWindow", "Nurse"))
        self.pushButton_4.setText(_translate("MainWindow", "Admin"))
        # self.pushButton_5.setText(_translate("MainWindow", "Login"))


""" Moved to test.py
    def changeUI_to_SignInOrRegister(self):  # change UI to Menu

        self.uiNew = loginOrRegister_UI()
        self.uiNew.setupUi(MainWindow)
        MainWindow.showFullScreen()
"""

# main method of MainWindow.py
# This is only executed with command python welcome_page.py
if __name__ == "__main__":
    print("nonono")
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = welcome_page_UI()
    ui.setupUi(MainWindow)

    MainWindow.showMaximized()

    sys.exit(app.exec_())

