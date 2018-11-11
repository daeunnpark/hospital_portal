import pymysql
import sys
from PyQt5.QtWidgets import QApplication, QWidget

def main():

    app = QApplication(sys.argv)

    root = QWidget()

    root.resize(320, 240)

    root.setWindowTitle("Hello, World")

    root.show()

    conn = pymysql.connect(host='10.245.235.98', port=3306, user='root', passwd='hospitalCSE305!', db='hospital')

    cur = conn.cursor()

    cur.execute("SELECT VERSION()")

    print(cur.description)

    sys.exit(app.exec_())

if __name__ == "__main__": main()
