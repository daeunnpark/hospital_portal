#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pymysql
import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QPushButton, QToolTip, QMessageBox
from PyQt5.QtGui import QIcon, QFont


class Application(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        patientButton = QPushButton('Patient', self)

        doctorButton = QPushButton('Doctor', self)

        nurseButton = QPushButton('Nurse', self)

        adminButton = QPushButton('Administrator', self)

        patientButton.setToolTip('Select this if you are a patient')

        doctorButton.setToolTip('Select this if you are a doctor')

        nurseButton.setToolTip('Select this if you are a nurse')

        adminButton.setToolTip('Select this if you are an administrator')

        patientButton.resize(patientButton.sizeHint())

        doctorButton.resize(doctorButton.sizeHint())

        nurseButton.resize(nurseButton.sizeHint())

        adminButton.resize(adminButton.sizeHint())

        self.setGeometry(300, 300, 300, 220)

        self.center()

        self.setWindowTitle("HealthCare United Patient Portal")

        self.setWindowIcon(QIcon('icon.PNG'))

        self.show()

    def center(self):

        qr = self.frameGeometry();
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', "Are you sure you want to quit?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()

        else:
            event.ignore()


if __name__ == "__main__":

    conn = pymysql.connect(host='10.245.235.98', port=3306, user='root', passwd='hospitalCSE305!', db='hospital')

    cur = conn.cursor()

    app = QApplication(sys.argv)

    root = Application()

    sys.exit(app.exec_())
