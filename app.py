#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pymysql
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Application(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)

        self.setWindowTitle("HealthCare United Patient Portal")

        self.setWindowIcon(QIcon('icon.PNG'))

        self.show()


if __name__ == "__main__":

    conn = pymysql.connect(host='10.245.235.98', port=3306, user='root', passwd='hospitalCSE305!', db='hospital')

    cur = conn.cursor()

    app = QApplication(sys.argv)

    root = Application()

    sys.exit(app.exec_())
