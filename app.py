#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Import Statements
import pymysql
import sys
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QWidget, QAction, QPushButton, QToolTip, QMessageBox, QMainWindow, qApp, QVBoxLayout, QLabel)
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore, uic

#Application Class Definition
class Application(QMainWindow):

    #Simple class init method - required
    def __init__(self):
        super().__init__()
        #Load UI File: To Edit UI File, Open File .ui file in QtDesigner
        uic.loadUi('mainwindow.ui', self)
        #The widget names are listed in the right panel of QtDesigner. They will need to be used to call them and implement them in python
        #self.pushButton.setText("WOW")
        self.initUI()

    #Function that centers the window in the display upon loading
    def center(self):
        qr = self.frameGeometry();
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

#This is commented out code of when I was trying to implement a label in PyQt manually
    #def firstPage(self):
        #label = QLabel(self)
        #label.setText("Healthcare United Patient Portal")
        #font = QFont("Lucida", 16, QFont.Bold)
        #label.setFont(font)
        #label.setGeometry(QtCore.QRect(100, 100, 900, 100))
        #label.setStyleSheet('color: teal')
        #label.setAlignment(QtCore.Qt.AlignVCenter)
        #vBox = QVBoxLayout(self)
        #vBox.addWidget(label)
        #self.setLayout(vBox)

    #Function that initializes the UI
    def initUI(self):
        #Creates a status bar and sets the initial value to "Ready"
        self.statusBar().showMessage("Ready")
        #Keep this function commented out
        #self.firstPage()
        #See center method above
        self.center()
        #Sets window title
        self.setWindowTitle("HealthCare United Patient Portal")
        #Sets window icon
        self.setWindowIcon(QIcon('icon.PNG'))
        #Displays the window
        self.show()


    #Function that prompts the user whether or not they wont to exit
    def closeEvent(self, event):
        #Displays a message box to prompt the user
        reply = QMessageBox.question(self, 'Message', "Are you sure you want to quit?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            #Quit application
            event.accept()
        else:
            #Stay in application
            event.ignore()

#This code block is used to launch the UI and connect to the database
if __name__ == "__main__":
    #Initialize database connection
    conn = pymysql.connect(host='10.245.235.98', port=3306, user='root', passwd='hospitalCSE305!', db='hospital')
    #Initialize the database cursor
    cur = conn.cursor()
    #Controls start and end of the application
    app = QApplication(sys.argv)
    root = Application()
    sys.exit(app.exec_())
