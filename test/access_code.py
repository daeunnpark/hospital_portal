import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

# import modules
from welcome_page import welcome_page_UI
from common_signup import common_signup_UI


class access_code_UI(object):
    def setupUi(self, Access, num):
        Access.setObjectName("Access")
        Access.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(Access)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QtCore.QRect(30, 100, 50, 171))
        self.label.setStyleSheet(
            'font: 20pt "Lucida Calligraphy";\n' "color: rgb(46, 125, 132);"
        )

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(350, 100, 1400, 111))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(2000, 1000, 241, 81))
        self.pushButton.setStyleSheet(
            'font: 20pt "Lucida Calligraphy";\n' "color: rgb(46, 125, 132);"
        )
        self.pushButton.setObjectName("pushButton")
        Access.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Access)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Access.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Access)
        self.statusbar.setObjectName("statusbar")
        Access.setStatusBar(self.statusbar)

        # temp comment out
        # self.pushButton.clicked.connect(self.authenticateAccess)

        self.retranslateUi(Access)
        QtCore.QMetaObject.connectSlotsByName(Access)

    def retranslateUi(self, Access):
        _translate = QtCore.QCoreApplication.translate
        Access.setWindowTitle(_translate("Access", "Access"))
        self.label.setText(
            _translate("Access", "Enter Your Access Code Received Via Email:")
        )
        self.pushButton.setText(_translate("Access", "Enter"))

    def authenticate_access_code(self, cur):
        # initalize

        cur.execute(
            "SELECT AccessCodes FROM AccessCodes A WHERE AccessCodes = (%s)",
            self.lineEdit.text(),
        )
        access = cur.fetchall()
        self.rowcount = cur.rowcount

        """
        if cur.rowcount != 0:
            self.rowcount = cur.rowcount
            self.uiNew = common_signup_UI()
            self.uiNew.setupUi(MainWindow, access)
            MainWindow.showFullScreen()
        else:
            print("error")
        """
        if self.rowcount == 0:
            print("errorrr")


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = access_code_UI()
    ui.setupUi(MainWindow)

    MainWindow.showMaximized()

    sys.exit(app.exec_())
