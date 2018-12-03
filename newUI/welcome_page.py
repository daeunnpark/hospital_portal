import sys

from PyQt5 import QtCore, QtGui, QtWidgets


# Done but logo to add
class welcome_page_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(243,255,255);\n""")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100000))


        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")

        # Logo
        self.pixmap = QtGui.QPixmap("icon.PNG")
        self.label_2.setPixmap(self.pixmap)

        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(250, 0))
        self.widget.setMaximumSize(QtCore.QSize(300, 300))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(225, 247, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 247, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 247, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 255, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 140, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 114, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 247, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 247, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 247, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 255, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 140, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 114, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 247, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 247, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 247, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 255, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 140, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 114, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.AlternateBase, brush)
        self.widget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.widget.setFont(font)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-color: rgb(225,247,251);\n"
                                  "border-width: 10px;")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.patientBtn = QtWidgets.QPushButton(self.widget)
        self.patientBtn.setMinimumSize(QtCore.QSize(200, 0))
        self.patientBtn.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.patientBtn.setFont(font)
        self.patientBtn.setStyleSheet("background-color: rgb(232, 232, 232);\n"
                                      "font: 30pt \"Arial\";")
        self.patientBtn.setObjectName("pushButton")
        self.gridLayout.addWidget(self.patientBtn, 0, 0, 1, 1)

        self.doctorBtn = QtWidgets.QPushButton(self.widget)
        self.doctorBtn.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.doctorBtn.setFont(font)
        self.doctorBtn.setStyleSheet("background-color: rgb(232, 232, 232);\n"
                                     "font: 30pt \"Arial\";\n"
                                     "")
        self.doctorBtn.setObjectName("doctorBtn")
        self.gridLayout.addWidget(self.doctorBtn, 1, 0, 1, 1)
        self.nurseBtn = QtWidgets.QPushButton(self.widget)
        self.nurseBtn.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.nurseBtn.setFont(font)
        self.nurseBtn.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.nurseBtn.setObjectName("nurseBtn")
        self.gridLayout.addWidget(self.nurseBtn, 2, 0, 1, 1)

        self.departmentAdminBtn = QtWidgets.QPushButton(self.widget)
        self.departmentAdminBtn.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.departmentAdminBtn.setFont(font)
        self.departmentAdminBtn.setStyleSheet(
            "background-color: rgb(232, 232, 232);")
        self.departmentAdminBtn.setObjectName("departmentAdminBtn")
        self.gridLayout.addWidget(self.departmentAdminBtn, 3, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:96pt;\">Healthcare United </span></p><p align=\"center\"><span style=\" font-size:96pt;\">Patient Portal</span></p></body></html>"))
        #self.imageLabel1.setPixmap(self.pixmap)
        self.patientBtn.setText(_translate("MainWindow", "Patient"))
        self.doctorBtn.setText(_translate("MainWindow", "Doctor"))
        self.nurseBtn.setText(_translate("MainWindow", "Nurse"))
        self.departmentAdminBtn.setText(_translate("MainWindow", "Admin"))


# This is only executed with command python welcome_page.py
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = welcome_page_UI()
    ui.setupUi(MainWindow)

    # MainWindow.show()
    MainWindow.showMaximized()

    sys.exit(app.exec_())
