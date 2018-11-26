import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

# import modules
from welcome_page import welcome_page_UI
from common_signup import common_signup_UI


class access_code_UI(object):
    def __init__(self, parent=None):
        self.rowcount = 0
        self.authenticateCode = -1
    
    def setupUi(self, Access, num):
        Access.setObjectName("Access")

        self.centralwidget = QtWidgets.QWidget(Access)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 400))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 60))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton.setStyleSheet("font: 20pt \"Lucida Calligraphy\";\n"
"color: rgb(46, 125, 132);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.widget_2, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(1400, 100))
        self.label.setStyleSheet("font: 20pt \"Lucida Calligraphy\";\n"
"color: rgb(46, 125, 132);")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        Access.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Access)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.pushButton.setText(_translate("Access", "Enter"))
        self.label.setText(_translate("Access", "Enter Your Access Code Received Via Email:"))

    def authenticate_access_code(self, cur):
        # initalize
        
        cur.execute(
            "SELECT AccessCodes FROM AccessCodes A WHERE AccessCodes = (%s)",
            self.lineEdit.text(),
        )
            
        access = cur.fetchall()
        self.authenticateCode = access
        self.rowcount = cur.rowcount
        print(self.rowcount)
                    
        # Add dialog maybe?
        if self.rowcount == 0:
            print("errorrr")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = access_code_UI()
    ui.setupUi(MainWindow,1)
    MainWindow.showMaximized()
    sys.exit(app.exec_())

