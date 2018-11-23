import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

# import modules
from login_page import login_page_UI


if __name__ == "__main__":

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

    # Load login_page_UI
    ui = login_page_UI()

    # Set MainWindow to login_page
    ui.setupUi(MainWindow)
    print("222")
    MainWindow.showMaximized()
    ui.pushButton.clicked.connect(ui.changeUI_to_SignInOrRegister)
    print("333")
    sys.exit(app.exec_())
