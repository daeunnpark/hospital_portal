from PyQt5 import QtCore, QtGui, QtWidgets

# from PyQt5.QtWidgets import QApplication
import pymysql

from login_page import login_page_UI

if __name__ == "__main__":
    import sys

    # Initialize database connection
    # conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='hospital')
    conn = pymysql.connect(
        host="10.245.235.98",
        port=3306,
        user="root",
        passwd="hospitalCSE305!",
        db="hospital",
    )
    # Initialize the database cursor
    cur = conn.cursor()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = login_page_UI()  # set login page as UI
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
