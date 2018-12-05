import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

# import modules
from welcome_page import welcome_page_UI
from common_signup import common_signup_UI

# newUI- Done


class access_code_UI(object):
    def __init__(self, parent=None):
        self.rowcount = 0
        self.authenticateCode = -1

    def setupUi(self, Access, num):
        Access.setObjectName("Access")
        Access.setStyleSheet("background-color: rgb(225,247,251);\n"
                             "")
        self.centralwidget = QtWidgets.QWidget(Access)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(500, 0))
        self.widget.setMaximumSize(QtCore.QSize(650, 400))
        self.widget.setStyleSheet("background-color: rgb(243,255,255);")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(300, 0))
        self.label.setMaximumSize(QtCore.QSize(10000, 100))
        self.label.setStyleSheet("font: 40pt \"Arial\";")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 50))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("font: 30pt \"Arial\";\n"
                                  "\n"
                                  "")

        self.gridLayout_3.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(130, 80))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton.setStyleSheet("font: 30pt \"Arial\";\n"
                                      "background-color: rgb(232, 232, 232);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(
            self.pushButton, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.widget_2, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        Access.setCentralWidget(self.centralwidget)

        self.retranslateUi(Access)
        QtCore.QMetaObject.connectSlotsByName(Access)

    def retranslateUi(self, Access):
        _translate = QtCore.QCoreApplication.translate
        Access.setWindowTitle(_translate("Access", "Access"))
        self.label.setText(_translate(
            "Access", "<html><head/><body><p align=\"center\">Enter Your Access Code </p><p align=\"center\">Received Via Email:</p></body></html>"))
        self.pushButton.setText(_translate("Access", "Enter"))

    def authenticate_access_code(self, cur):
        # initalize

        cur.execute(
            "SELECT AccessCodes FROM AccessCodes A WHERE AccessCodes = (%s)",
            self.lineEdit.text(),
        )

        access = cur.fetchall()
        self.authenticateCode = access
        self.rowcount = cur.rowcount
        if(self.rowcount != 0):
            cur.execute(
                'DELETE FROM AccessCodes WHERE AccessCodes = (%s)', access[0][0])

        if self.rowcount == 0:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setIcon(QtWidgets.QMessageBox().Warning)
            error_dialog.setText("\nAccess Code is Invalid!")
            error_dialog.exec()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = access_code_UI()
    ui.setupUi(MainWindow, 1)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
