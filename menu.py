from copy import copy

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from datetime import date

myEarliestDate = QtCore.QDate()


class MyCalendar(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)

    def paintCell(self, painter, rect, date, **kwargs):
        QtWidgets.QCalendarWidget.paintCell(self, painter, rect, date)
        if date.day() == myEarliestDate.day() and date.year() == myEarliestDate.year() and date.month() == myEarliestDate.month():
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            painter.setFont(font);
            painter.drawText(rect.bottomLeft(), "Appointment")


class menu_UI(object):

    def setupUi(self, Menu, firstName, lastName, phoneNumber, emailAddress, ID, age, ssn, weight, height,
                creditCardNumber, billingAmount, insuranceNumber, medicationList, appointmentDates, startTimes,
                endTimes, appointmentIDs, doctorID, nurseID, departmentAdminID, num, cur, conn):

        

        earliestDate = None

        numDates = 0
        for row in appointmentDates:
            if (earliestDate == None):
                earliestDate = row[0]
            else:
                if (row[0] < earliestDate):
                    earliestDate = row[0]
            if (numDates == 0):
                numDates = numDates + 1
            elif (numDates == 1):
                numDates = numDates + 1
            elif (numDates == 2):
                numDates = numDates + 1
            elif (numDates == 3):
                numDates = numDates + 1

        earliestDateArray = str(earliestDate)

        earliestDateArray = earliestDateArray.split("-")

        if(earliestDateArray[0] == "None"):
            myYear = 0
            myMonth = 0
            myDay = 0
        else:
            myYear = int(earliestDateArray[0])

            myDay = int(earliestDateArray[2])

            myMonth = int(earliestDateArray[1])

        myEarliestDate.setDate(myYear, myMonth, myDay)

        self.ID = ID
        self.age = age
        self.weight = weight
        self.height = height

        self.doctorID = doctorID
        self.nurseID = nurseID
        self.departmentAdminID = departmentAdminID
        self.phoneNumber = phoneNumber[0:3]+'-'+phoneNumber[3:6]+ "-"+phoneNumber[6:10]
        self.ssn = ssn # no formatting for Employee's DptID (ssn is a placeholder for DptID)
        if(num==1):
            self.ssn = ssn[0:3]+'-'+ssn[3:5]+ "-"+ssn[5:10]

        Menu.setObjectName("Menu")
        Menu.setStyleSheet("background-color: rgb(243,255,255);\n"
                           "")
        self.centralWidget = QtWidgets.QWidget(Menu)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(775, 590))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(225,247,251);\n"
                                     "font: 20pt \"Arial\";\n"
                                     "")
                                    
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 100))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.EditBtn = QtWidgets.QPushButton(self.tab_1)
        
        self.EditBtn.setMinimumSize(QtCore.QSize(90, 50))
        self.EditBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.EditBtn.setFont(font)
        self.EditBtn.setStyleSheet("background-color: rgb(232, 232, 232);\n"
                                     "font: 20pt \"Arial\";\n"
                                     "")
        
        self.EditBtn.setObjectName("EditBtn")
        self.gridLayout.addWidget(
            self.EditBtn, 1, 3, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText(ID)
        self.gridLayout.addWidget(self.lineEdit_5, 6, 1, 1, 1)
        self.lineEdit_5.setEnabled(False)
        self.label_9 = QtWidgets.QLabel(self.tab_1)
        self.label_9.setStyleSheet("font: 30pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 10, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.tab_1)
        self.label_1.setStyleSheet("font: 30pt \"Arial\";")
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText(self.phoneNumber)
        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)
        self.lineEdit_3.setEnabled(False)
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setStyleSheet("font: 30pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_1)
        self.label_10.setStyleSheet("font: 30pt \"Arial\";")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 10, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_1)
        self.label_4.setStyleSheet("font: 30pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setText(medicationList)
        self.gridLayout.addWidget(self.lineEdit_10, 10, 3, 1, 1)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 4, 3, 1, 1)
        self.lineEdit_4.setText(emailAddress)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setText(weight)
        self.gridLayout.addWidget(self.lineEdit_7, 8, 1, 1, 1)
        self.lineEdit_7.setEnabled(False)
        self.label_7 = QtWidgets.QLabel(self.tab_1)
        self.label_7.setStyleSheet("font: 30pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_1)
        self.label_8.setStyleSheet("font: 30pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_1)
        self.label_6.setStyleSheet("font: 30pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 2, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setText(height)
        self.gridLayout.addWidget(self.lineEdit_8, 8, 3, 1, 1)
        self.lineEdit_8.setEnabled(False)
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setStyleSheet("font: 30pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.SaveBtn = QtWidgets.QPushButton(self.tab_1)
        self.SaveBtn.setMinimumSize(QtCore.QSize(90, 50))
        self.SaveBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.SaveBtn.setStyleSheet("background-color: rgb(232, 232, 232);\n"
                                   "font: 20pt \"Arial\";\n"
                                   "")
        self.SaveBtn.setObjectName("SaveBtn")
        self.gridLayout.addWidget(
            self.SaveBtn, 12, 3, 1, 1, QtCore.Qt.AlignRight)
        self.SaveBtn.setEnabled(False)

        self.lineEdit_1 = QtWidgets.QLineEdit(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_1.setText(firstName)
        self.gridLayout.addWidget(self.lineEdit_1, 2, 1, 1, 1)
        self.lineEdit_1.setEnabled(False)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setText(age)
        self.gridLayout.addWidget(self.lineEdit_9, 10, 1, 1, 1)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setText(self.ssn)
        self.gridLayout.addWidget(self.lineEdit_6, 6, 3, 1, 1)
        self.lineEdit_6.setEnabled(False)
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setStyleSheet("font: 30pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText(lastName)
        self.gridLayout.addWidget(self.lineEdit_2, 2, 3, 1, 1)
        self.lineEdit_2.setEnabled(False)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_9.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.calendarWidget_1 = MyCalendar(self.groupBox)
        self.calendarWidget_1.setMaximumSize(QtCore.QSize(20000, 16777215))
        self.calendarWidget_1.setGridVisible(True)
        self.calendarWidget_1.setObjectName("calendarWidget_1")
        self.calendarWidget_1.setVerticalHeaderFormat(0)
        self.calendarWidget_1.setMinimumDate(QtCore.QDate.currentDate())
        self.calendarWidget_1.selectionChanged.connect(self.updateDateSelected)

        self.gridLayout_2.addWidget(self.calendarWidget_1, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setMinimumSize(QtCore.QSize(200, 0))
        self.frame.setStyleSheet("background-color: rgb(205,245,246);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_8.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.timeEdit_17 = QtWidgets.QTimeEdit(self.frame)
        self.timeEdit_17.setStyleSheet("font: 20pt Arial;")
        self.timeEdit_17.setObjectName("timeEdit_17")
        self.gridLayout_8.addWidget(self.timeEdit_17, 3, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("font: 30pt Arial;")
        self.label_16.setObjectName("label_16")
        self.gridLayout_8.addWidget(self.label_16, 2, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_15.setStyleSheet("background-color: rgb(232, 232, 232);\n"
                                         "font: 20pt \"Arial\";\n"
                                         "")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_8.addWidget(self.pushButton_15, 5, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setStyleSheet("font: 30pt Arial;")
        self.label_18.setObjectName("label_18")
        self.gridLayout_8.addWidget(self.label_18, 4, 0, 1, 1)
        self.timeEdit_18 = QtWidgets.QTimeEdit(self.frame)
        self.timeEdit_18.setStyleSheet("font: 20pt Arial;")
        self.timeEdit_18.setObjectName("timeEdit_18")
        # Appt for at least 30 min
        self.timeEdit_18.setTime(QtCore.QTime.currentTime().addSecs(60*30))

        self.gridLayout_8.addWidget(self.timeEdit_18, 4, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setStyleSheet("font: 30pt Arial;")
        self.label_17.setObjectName("label_17")
        self.timeEdit_17.setTime(QtCore.QTime.currentTime())
        self.gridLayout_8.addWidget(self.label_17, 3, 0, 1, 1)
        self.dateEdit_16 = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_16.setStyleSheet("font: 20pt Arial;")
        self.dateEdit_16.setObjectName("dateEdit_16")
        self.dateEdit_16.setDate(QtCore.QDate.currentDate())
        self.gridLayout_8.addWidget(self.dateEdit_16, 2, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_15.setStyleSheet("font: 20pt Arial;")
        self.label_15.setObjectName("label_15")
        self.gridLayout_8.addWidget(self.label_15, 0, 0, 1, 2)
        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setMinimumSize(QtCore.QSize(500, 120))
        self.widget.setStyleSheet("background-color: rgb(205,245,246);\n"
                                  "border-color: rgb(252, 37, 224);")
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton19_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton19_1.setStyleSheet("background-color: rgb(232, 232, 232);\n"
                                          "font: 20pt \"Arial\";\n"
                                          "")
        self.pushButton19_1.setObjectName("pushButton19_1")
        self.gridLayout_3.addWidget(self.pushButton19_1, 2, 0, 1, 1)
        self.pushButton19_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton19_4.setStyleSheet("background-color: rgb(232, 232, 232);\n"
                                          "font: 20pt \"Arial\";\n"
                                          "")
        self.pushButton19_4.setObjectName("pushButton19_4")
        self.gridLayout_3.addWidget(self.pushButton19_4, 2, 3, 1, 1)
        self.lineEdit19_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit19_2.setStyleSheet("font: 15pt Arial;")
        self.lineEdit19_2.setObjectName("lineEdit19_2")
        self.gridLayout_3.addWidget(self.lineEdit19_2, 1, 1, 1, 1)
        self.pushButton19_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton19_3.setStyleSheet("background-color: rgb(232, 232, 232);\n"
                                        "font: 20pt \"Arial\";\n"
                                        "")
        self.pushButton19_3.setObjectName("pushButton19_3")
        self.gridLayout_3.addWidget(self.pushButton19_3, 2, 2, 1, 1)
        self.lineEdit19_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit19_4.setStyleSheet("font: 15pt Arial;")
        self.lineEdit19_4.setObjectName("lineEdit19_4")
        self.gridLayout_3.addWidget(self.lineEdit19_4, 1, 3, 1, 1)
        self.pushButton19_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton19_2.setStyleSheet("background-color: rgb(232, 232, 232);\n"
                                        "font: 20pt \"Arial\";\n"
                                        "")
        self.pushButton19_2.setObjectName("pushButton19_2")
        self.gridLayout_3.addWidget(self.pushButton19_2, 2, 1, 1, 1)
        self.lineEdit19_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit19_3.setStyleSheet("font: 15pt Arial;")
        self.lineEdit19_3.setMaxLength(300)
        self.lineEdit19_3.setReadOnly(True)
        self.lineEdit19_3.setObjectName("lineEdit19_3")
        self.gridLayout_3.addWidget(self.lineEdit19_3, 1, 2, 1, 1)
        self.lineEdit19_1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit19_1.setMaximumSize(QtCore.QSize(589, 16777215))
        self.lineEdit19_1.setStyleSheet("font: 15pt Arial;")
        self.lineEdit19_1.setObjectName("lineEdit19_1")
        self.gridLayout_3.addWidget(self.lineEdit19_1, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.widget, 2, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_19.setStyleSheet("font: 20pt Arial;")
        self.label_19.setObjectName("label_19")
        self.gridLayout_9.addWidget(self.label_19, 1, 0, 1, 1)
        #self.tabWidget.addTab(self.tab_2, "")


        """sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        #QSizePolicy wsize = self.QsizePolicy()
        
        sizePolicy.setRetainSizeWhenHidden(True)
        self.widget.setSizePolicy(sizePolicy)"""

        
        self.lineEdit19_1.setVisible(False)
        self.lineEdit19_2.setVisible(False)
        self.lineEdit19_3.setVisible(False)
        self.lineEdit19_4.setVisible(False)

        self.pushButton19_1.setVisible(False)
        self.pushButton19_2.setVisible(False)
        self.pushButton19_3.setVisible(False)
        self.pushButton19_4.setVisible(False)
        
        if num == 1:
            self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_12.setMaximumSize(QtCore.QSize(500, 50))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.setText(creditCardNumber)
        self.lineEdit_12.setStyleSheet("font: 30pt Arial;")
        self.gridLayout_6.addWidget(self.lineEdit_12, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setStyleSheet("font: 30pt Arial;")
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 3, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_13.setMaximumSize(QtCore.QSize(500, 50))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_13.setText(billingAmount)
        self.lineEdit_13.setStyleSheet("font: 30pt Arial;")
        self.gridLayout_6.addWidget(self.lineEdit_13, 5, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setStyleSheet("font: 30pt Arial;")
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 1, 0, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton_14.setMaximumSize(QtCore.QSize(100, 200))
        self.pushButton_14.setStyleSheet("background-color: rgb(232, 232, 232);\n"
                                     "font: 30pt \"Arial\";\n"
                                     "")
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_6.addWidget(self.pushButton_14, 7, 2, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_11.setMaximumSize(QtCore.QSize(500, 50))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.setText(insuranceNumber)
        self.lineEdit_11.setStyleSheet("font: 30pt Arial;")
        self.gridLayout_6.addWidget(self.lineEdit_11, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setStyleSheet("font: 30pt Arial;")
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 7, 0, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_14.setMaximumSize(QtCore.QSize(500, 50))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.setStyleSheet("font: 30pt Arial;")
        self.gridLayout_6.addWidget(self.lineEdit_14, 7, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setStyleSheet("font: 30pt Arial;")
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 5, 0, 1, 1)
        if num == 1:
            self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textEdit = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit.setMinimumSize(QtCore.QSize(700, 300))
        #self.textEdit.setMaximumSize(QtCore.QSize(16777215, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(5)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 13pt \"Arial\";\n"
                                        "")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        
        self.gridLayout_5.addWidget(self.textEdit, 0, 1, 1, 1)

        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_4)
        #self.calendarWidget.setMaximumSize(QtCore.QSize(16777215, 400))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setVerticalHeaderFormat(0)
        self.gridLayout_5.addWidget(self.calendarWidget, 0, 0, 1, 1)

        if num != 1:
            self.tabWidget.addTab(self.tab_4, "")

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_10.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.widget_3 = QtWidgets.QWidget(self.tab_5)
        #self.widget_3.setMaximumSize(QtCore.QSize(10000, 10000))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.accessLabel = QtWidgets.QLabel(self.widget_3)
        self.accessLabel.setMaximumSize(QtCore.QSize(16777215, 100))
        self.accessLabel.setStyleSheet("font: 40pt \"Arial\";")
        self.accessLabel.setObjectName("accessLabel")
        self.verticalLayout.addWidget(self.accessLabel)
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        #self.widget_2.setMaximumSize(QtCore.QSize(10000, 20000))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.accessEdit = QtWidgets.QLineEdit(self.widget_2)
        self.accessEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.accessEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.accessEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.accessEdit.setStyleSheet("font: 30pt \"Arial\";")
        self.accessEdit.setObjectName("accessEdit")
        self.gridLayout_4.addWidget(self.accessEdit, 0, 0, 1, 1)
        self.accessButton = QtWidgets.QPushButton(self.widget_2)
        self.accessButton.setMinimumSize(QtCore.QSize(0, 80))
        self.accessButton.setMaximumSize(QtCore.QSize(100000, 16777215))
        self.accessButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.accessButton.setStyleSheet("background-color: rgb(232, 232, 232);\n"
                                        "font: 30pt \"Arial\";\n"
                                        "")
        self.accessButton.setObjectName("accessButton")
        self.gridLayout_4.addWidget(self.accessButton, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.gridLayout_10.addWidget(
            self.widget_3, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)

        if num ==4:
            self.tabWidget.addTab(self.tab_5, "")

        self.gridLayout_7.addWidget(
            self.tabWidget, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        Menu.setCentralWidget(self.centralWidget)

        self.retranslateUi(Menu, num)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Menu)



        self.calendarWidget.clicked.connect(lambda: self.showAppointmentsInTextEdit(num, ID, cur, conn))
        
        self.pushButton19_1.clicked.connect(lambda: self.cancelAppt(1, appointmentIDs, cur, conn, self.lineEdit_13))
        self.pushButton19_2.clicked.connect(lambda: self.cancelAppt(3, appointmentIDs, cur, conn, self.lineEdit_13))
        self.pushButton19_3.clicked.connect(lambda: self.cancelAppt(5, appointmentIDs, cur, conn, self.lineEdit_13))
        self.pushButton19_4.clicked.connect(lambda: self.cancelAppt(7, appointmentIDs, cur, conn, self.lineEdit_13))
        self.pushButton_15.clicked.connect(lambda: self.scheduleAppt(cur, conn, self.doctorID, self.nurseID, departmentAdminID, ID, self.dateEdit_16.date(), self.timeEdit_17.time(), self.timeEdit_18.time(), self.lineEdit19_1, self.lineEdit19_2, self.lineEdit19_3, self.lineEdit19_4, self.pushButton19_1, self.pushButton19_2, self.pushButton19_3, self.pushButton19_4, self.lineEdit_13))
        self.pushButton_14.clicked.connect(lambda: self.Pay(ID, cur, conn))
        self.accessButton.clicked.connect(lambda: self.addAccessCode(cur, conn, self.accessEdit))

        
        
        earliestDate = None

        numDates = 0
        for row in appointmentDates:
            if (earliestDate == None):
                earliestDate = row[0]
            else:
                if (row[0] < earliestDate):
                    earliestDate = row[0]
            if (numDates == 0):
                self.lineEdit19_1.setVisible(True)
                self.pushButton19_1.setVisible(True)
                self.lineEdit19_1.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1
            elif (numDates == 1):
                self.lineEdit19_2.setVisible(True)
                self.pushButton19_2.setVisible(True)
                self.lineEdit19_2.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1
            elif (numDates == 2):
                self.lineEdit19_3.setVisible(True)
                self.pushButton19_3.setVisible(True)
                self.lineEdit19_3.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1
            elif (numDates == 3):
                self.lineEdit19_4.setVisible(True)
                self.pushButton19_4.setVisible(True)
                self.lineEdit19_4.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1

        numStarts = 0
        for row in startTimes:
            hours, remainder = divmod(row[0].seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Time formatting
            if(hours<10):
                h = "0" + str(hours)
            else:
                h = str(hours)
            
            if (minutes<10):
                m = "0" + str(minutes)
            else:
                m = str(minutes)

            time = "    " + h + ":" + m

            if (numStarts == 0):
                self.lineEdit19_1.setText(
                    self.lineEdit19_1.text() + time)
                numStarts = numStarts + 1
            elif (numStarts == 1):
                self.lineEdit19_2.setText(
                    self.lineEdit19_2.text() + time)
                numStarts = numStarts + 1
            elif (numStarts == 2):
                self.lineEdit19_3.setText(
                    self.lineEdit19_3.text() + time)
                numStarts = numStarts + 1
            elif (numStarts == 3):
                self.lineEdit19_4.setText(
                    self.lineEdit19_4.text() + time)
                numStarts = numStarts + 1

        numEnds = 0
        for row in endTimes:
            hours, remainder = divmod(row[0].seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Time formatting
            if(hours<10):
                h = "0" + str(hours)
            else:
                h = str(hours)
            
            if (minutes<10):
                m = "0" + str(minutes)
            else:
                m = str(minutes)

            time = "    " + h + ":" + m

            if (numEnds == 0):
                self.lineEdit19_1.setText(
                    self.lineEdit19_1.text() + time)
                numEnds = numEnds + 1
            elif (numEnds == 1):
                self.lineEdit19_2.setText(
                    self.lineEdit19_2.text() + time)
                numEnds = numEnds + 1
            elif (numEnds == 2):
                self.lineEdit19_3.setText(
                    self.lineEdit19_3.text() + time)
                numEnds = numEnds + 1
            elif (numEnds == 3):
                self.lineEdit19_4.setText(
                    self.lineEdit19_4.text() + time)
                numEnds = numEnds + 1

        if (self.lineEdit19_1.isVisible() == True and self.lineEdit19_2.isVisible() == True and self.lineEdit19_3.isVisible() == True and self.lineEdit19_4.isVisible() == True):
            self.pushButton_15.setEnabled(False)



    def addAccessCode(self, cur, conn, accessEdit):
        if (accessEdit.text().isdigit() == False):
            self.show_msg(1, "Access Code Invalid!")
        else:
            self.show_msg(2, "Access Code added.")
            cur.execute('INSERT INTO AccessCodes(AccessCodes) VALUES (%s)', accessEdit.text())
            conn.commit()
            accessEdit.setText("")

    def showAppointmentsInTextEdit(self, num, ID, cur, conn):
        selected_date = QtCore.QDate(self.calendarWidget.selectedDate())

        day = selected_date.day()
        year = selected_date.year()
        month = selected_date.month()

        if day < 10:
            dayString = "0" + str(day)
        else:
            dayString = str(day)

        if month < 10:
            monthString = "0" + str(month)
        else:
            monthString = str(month)

        yearString = str(year)

        dateString = yearString + "-" + monthString + "-" + dayString

        #Doctor
        if num == 2:
            cur.execute(
                "SELECT * FROM Appointment A WHERE Date = (%s) AND DoctorID = (%s)", (dateString, ID)
            )

        # Nurse
        elif num == 3:
            cur.execute(
                "SELECT * FROM Appointment A WHERE Date = (%s) AND NurseID = (%s)", (dateString, ID)
            )

        # Admin
        else:
            cur.execute(
                "SELECT * FROM Appointment A WHERE Date = (%s)", dateString
            )

        data = cur.fetchall()
        #print(data)
        if len(data) == 0:
            self.textEdit.setText(
                "There are no appointments scheduled for the selected date.")
        else:

            finalString = "Appointment ID | Doctor ID | Nurse ID | Patient ID | DeptAdmin ID | Location |Date                  | Start Time | End Time \n\n\n"
            
            for apptTuple in data:
                appointmentIDStr = str(apptTuple[0])
                doctorIDStr = str(apptTuple[1])
                nurseIDStr = str(apptTuple[2])
                patientIDStr = str(apptTuple[3])
                departmentAdminIDStr = str(apptTuple[4])
                locationStr = str(apptTuple[5])
                dateStr = str(apptTuple[6])
                startTimeStr = str(apptTuple[7])
                endTimeStr = str(apptTuple[8])

                """finalString = finalString + appointmentIDStr + "\t" + doctorIDStr + "\t" + nurseIDStr + "\t" \
                              + patientIDStr + "\t" + departmentAdminIDStr + "\t" + locationStr + "\t" + dateStr \
                              + "\t" + startTimeStr + "\t" + endTimeStr + "\n\n\n\n\n"""

                finalString = finalString + "{:<28}{:<16}{:<14}{:<15}{:<22}{:<11}{:<16}{:<15}{:<8}".format(\
                appointmentIDStr, doctorIDStr, nurseIDStr, patientIDStr, departmentAdminIDStr, locationStr,\
                dateStr, startTimeStr, endTimeStr) + "\n\n"   
            
            self.textEdit.setText(finalString)
            


    def retranslateUi(self, Menu, num):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.EditBtn.setText(_translate("Menu", "Edit"))
        self.label_9.setText(_translate("Menu", "Age"))
        self.label_1.setText(_translate("Menu", "First Name"))
        self.label_2.setText(_translate("Menu", "Last Name"))
        self.label_10.setText(_translate("Menu", "Medication List"))
        self.label_4.setText(_translate("Menu", "Email Address"))
        self.label_7.setText(_translate("Menu", "Weight"))
        self.label_8.setText(_translate("Menu", "Height"))
        self.label_6.setText(_translate("Menu", "SSN"))
        self.label_3.setText(_translate("Menu", "Phone Number"))
        self.SaveBtn.setText(_translate("Menu", "Save"))
        self.label_5.setText(_translate("Menu", "ID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_1), _translate("Menu", "Profile"))
        self.label_16.setText(_translate("Menu", "Date:"))
        self.pushButton_15.setText(_translate("Menu", "Schedule"))
        self.label_18.setText(_translate("Menu", "End Time:"))
        self.label_17.setText(_translate("Menu", "Start Time:"))
        self.label_15.setText(_translate(
            "Menu", "You can set up to 4 appointments."))
        self.label_19.setText(_translate("Menu", "Current Appointments"))
        self.pushButton19_1.setText(_translate("Menu", "Cancel Appointment"))
        self.pushButton19_2.setText(_translate("Menu", "Cancel Appointment"))
        self.pushButton19_3.setText(_translate("Menu", "Cancel Appointment"))
        self.pushButton19_4.setText(_translate("Menu", "Cancel Appointment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("Menu", "Appointment"))
        self.label_12.setText(_translate("Menu", "Credit Card Number"))
        self.label_11.setText(_translate("Menu", "Insurance Number"))
        self.pushButton_14.setText(_translate("Menu", "Pay"))
        
        self.label_14.setText(_translate("Menu", "Payment Amount"))
        self.label_13.setText(_translate("Menu", "Billing Amount"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_3), _translate("Menu", "Billing Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_4), _translate("Menu", "Appointment Info"))
        self.accessLabel.setText(_translate(
            "Menu", "<html><head/><body><p align=\"center\">Enter Access Code</p></body></html>"))
        self.accessButton.setText(_translate("Menu", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_5), _translate("Menu", "Access Code"))


        # Employee
        if num != 1:
            self.label_6.setText("DepartmentID")
            self.label_9.setVisible(False)
            self.lineEdit_9.setVisible(False)
            self.label_10.setVisible(False)
            self.lineEdit_10.setVisible(False)

            if num == 2 or num == 3:  # Doct / Nurse
                self.label_7.setText("Specialty")
                self.label_8.setText("Medical License")
            else:  # Admin
                self.label_7.setText("Security code")
                self.label_8.setVisible(False)
                self.lineEdit_8.setVisible(False)


        self.EditBtn.setText(_translate("Menu", "Edit"))
        self.SaveBtn.setText(_translate("Menu", "Save"))

      

    def Pay(self, ID, cur, conn):
        if(self.lineEdit_14.text() == "" or self.IsDigitorSpeChar(self.lineEdit_14.text(), ".", -1) == False):
             self.show_msg( 1, "Payment Amount Must Be A Number!")

        elif (self.lineEdit_13.text() < self.lineEdit_14.text()):
            diff = float(self.lineEdit_14.text()) - float(self.lineEdit_13.text())
            self.lineEdit_14.setText(str(diff))
            self.lineEdit_13.setText("0")
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (0, ID))
            conn.commit()

        elif (self.lineEdit_13.text() == self.lineEdit_14.text()):
            self.lineEdit_14.smsgetText("0")
            self.lineEdit_13.setText("0")
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (0, ID))
            conn.commit()
        # Negative balance?
        else:
            diff2 = float(self.lineEdit_13.text()) - float(self.lineEdit_14.text())
            self.lineEdit_13.setText(str(diff2))
            self.lineEdit_14.setText("0")
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (diff2, ID))
            conn.commit()


    def scheduleAppt(self, cur, conn, doctorID, nurseID, departmentAdminID, ID, Date, StartTime, EndTime, lineEdit1, lineEdit2, lineEdit3, lineEdit4, cancel1, cancel2, cancel3, cancel4, lineEdit13):

        if (lineEdit1.isVisible() == True and lineEdit2.isVisible() == True and lineEdit3.isVisible() == True and lineEdit4.isVisible() == True):
            self.show_msg( 1, "Maximum Scheduled Appointments is 4!\nCannot Exceed this Amount!")
        
        elif(QtCore.QDate.currentDate() > Date):
            self.show_msg( 1, "Cannot Schedule Appointment For Earlier Date.")

        else:
            
            #cur.rowcount = -1

            cur.execute('SELECT AppointmentID FROM Appointment')
            # Generate next appointment ID to be next largest value
            apptID = cur.fetchall()
            largestApptID = 0;
            if apptID != None:
                for x in apptID:
                    if (x[0] >= largestApptID):
                        largestApptID = x[0] + 1

            cur.execute('INSERT INTO Appointment(AppointmentID, DoctorID, NurseID, PatientID, DepartmentAdminID, Location, Date, StartTime, EndTime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', 
            (largestApptID, doctorID, nurseID, self.ID, departmentAdminID, "SBU2", Date.toString("yyyy-MM-dd"), StartTime.toString("hh:mm:ss"), EndTime.toString("hh:mm:ss")))
            
            conn.commit()
            cur.execute('SELECT BillingAmount FROM Patient WHERE PatientID = (%s)', (self.ID))
            bill = cur.fetchall()
            cost = bill[0][0] + 200
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (cost, self.ID))
            self.lineEdit_13.setText(str(cost))
            conn.commit()
          
            if (lineEdit1.isVisible() == False):
                lineEdit1.setVisible(True)
                cancel1.setVisible(True)
                self.setDateAndTimeForViewing(lineEdit1, Date, StartTime, EndTime)

            elif (lineEdit2.isVisible() == False):
                lineEdit2.setVisible(True)
                cancel2.setVisible(True)
                self.setDateAndTimeForViewing(lineEdit2, Date, StartTime, EndTime)

            elif (lineEdit3.isVisible() == False):
                lineEdit3.setVisible(True)
                cancel3.setVisible(True)
                self.setDateAndTimeForViewing(lineEdit3, Date, StartTime, EndTime)

            elif (lineEdit4.isVisible() == False):
                lineEdit4.setVisible(True)
                cancel4.setVisible(True)
                self.setDateAndTimeForViewing(lineEdit4, Date, StartTime, EndTime)
        
        if (self.lineEdit19_1.isVisible() == True and self.lineEdit19_2.isVisible() == True and self.lineEdit19_3.isVisible() == True and self.lineEdit19_4.isVisible() == True):
            self.pushButton_15.setEnabled(False)

    def setDateAndTimeForViewing(self, lineEdit, Date, StartTime, EndTime):

        date = Date.toString("MM'/'dd'/'yyyy")

        sTime = StartTime.toString("    hh:mm")
        eTime = EndTime.toString("  hh:mm")
        lineEdit.setText(date+ sTime + eTime)
        
        # https://doc-snapshots.qt.io/qt5-5.11/qtime.html
        # I can't remove ap for some reason - Daeun

        """
        hours, remainder = divmod(StartTime.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        lineEdit.setText(
            lineEdit.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
        hours2, remainder2 = divmod(EndTime.seconds2, 3600)
        minutes2, seconds2 = divmod(remainder2, 60)
        lineEdit.setText(
            lineEdit.text() + "                " + str(hours2) + ":" + str(minutes2) + ":" + str(seconds2))
        """

    def cancelAppt(self, num, appointmentIDs, cur, conn, lineEdit13):
        
        if (num == 1):
            self.lineEdit19_1.setText("")
            self.lineEdit19_1.setVisible(False)
            self.pushButton19_1.setVisible(False)
            numAppointment = 0
            appointNum = -1
            for row in appointmentIDs:
                if (numAppointment == 0):
                    appointNum = row[0]
                numAppointment = numAppointment + 1
            cur.execute('DELETE FROM Appointment WHERE AppointmentID = (%s)', appointNum)
            conn.commit()

            cur.execute('SELECT BillingAmount FROM Patient WHERE PatientID = (%s)', (self.ID))
            bill = cur.fetchall()
            cost = bill[0][0] - 200
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (cost, self.ID))
            self.lineEdit_13.setText(str(cost))
            conn.commit()

        if (num == 3):
            self.lineEdit19_2.setText("")
            self.lineEdit19_2.setVisible(False)
            self.pushButton19_2.setVisible(False)
            numAppointment = 0
            appointNum = -1
            for row in appointmentIDs:
                if (numAppointment == 1):
                    appointNum = row[0]
                numAppointment = numAppointment + 1
            #print(appointNum)
            cur.execute('DELETE FROM Appointment WHERE AppointmentID = (%s)', appointNum)
            conn.commit()

            cur.execute('SELECT BillingAmount FROM Patient WHERE PatientID = (%s)', (self.ID))
            bill = cur.fetchall()
            cost = bill[0][0] - 200
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (cost, self.ID))
            self.lineEdit_13.setText(str(cost))
            conn.commit()

        if (num == 5):
            self.lineEdit19_3.setText("")
            self.lineEdit19_3.setVisible(False)
            self.pushButton19_3.setVisible(False)
            numAppointment = 0
            appointNum = -1
            for row in appointmentIDs:
                if (numAppointment == 2):
                    appointNum = row[0]
                numAppointment = numAppointment + 1
            cur.execute('DELETE FROM Appointment WHERE AppointmentID = (%s)', appointNum)
            conn.commit()

            cur.execute('SELECT BillingAmount FROM Patient WHERE PatientID = (%s)', (self.ID))
            bill = cur.fetchall()
            cost = bill[0][0] - 200
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (cost, self.ID))
            self.lineEdit_13.setText(str(cost))
            conn.commit()

        if (num == 7):
            self.lineEdit19_4.setText("")
            self.lineEdit19_4.setVisible(False)
            self.pushButton19_4.setVisible(False)
            numAppointment = 0
            appointNum = -1
            for row in appointmentIDs:
                if (numAppointment == 3):
                    appointNum = row[0]
                numAppointment = numAppointment + 1
            cur.execute('DELETE FROM Appointment WHERE AppointmentID = (%s)', appointNum)
            conn.commit()

            cur.execute('SELECT BillingAmount FROM Patient WHERE PatientID = (%s)', (self.ID))
            bill = cur.fetchall()
            cost = bill[0][0] - 200
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (cost, self.ID))
            self.lineEdit_13.setText(str(cost))
            conn.commit()

        if (self.lineEdit19_1.isVisible() == False or self.lineEdit19_2.isVisible() == False or self.lineEdit19_3.isVisible() == False or self.lineEdit19_4.isVisible() == False):
            self.pushButton_15.setEnabled(True)

    def editProfile(self, num, cur, conn):
        self.EditBtn.setEnabled(False)
        self.SaveBtn.setEnabled(True)

        self.lineEdit_1.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_7.setEnabled(True)
        self.lineEdit_8.setEnabled(True)
        self.lineEdit_9.setEnabled(True)
        self.lineEdit_10.setEnabled(True)

        # CANNOT be edited
        if num == 1:  # Patient
            self.lineEdit_5.setEnabled(False)  # ID
            self.lineEdit_10.setEnabled(False)  # Medication List
        else:  # Employee
            self.lineEdit_5.setEnabled(False)  # ID
            self.lineEdit_6.setEnabled(False)  # DepartmentID
            self.lineEdit_7.setEnabled(False)  # Specialty for Doc, Nur and Security Code for Admin

        self.SaveBtn.clicked.connect(lambda: self.saveProfile(num, cur, conn))

    def saveProfile(self, num, cur, conn):

        if (self.IsDigitorSpeChar(self.lineEdit_3.text(), "-", 12) == False) or self.lineEdit_3.text()[3] != '-' or self.lineEdit_3.text()[7] != '-' :
            self.show_msg( 1, "Phone Number Incorrect! \nFormat: xxx-xxx-xxxx")

            # Reset to prvious data
            self.lineEdit_3.setText(self.phoneNumber)

        else:
            # phone number reformatted using self.reformat(str)
            cur.execute(
                'UPDATE Person SET FirstName = (%s), LastName = (%s), PhoneNumber = (%s), EmailAddress = (%s) WHERE ID = (%s)',
                (self.lineEdit_1.text(), self.lineEdit_2.text(), self.reformat(self.lineEdit_3.text()),
                 self.lineEdit_4.text(), self.ID))

        if num == 1:  # Patient
            # Patient Error Checking - SSN

            if (self.IsDigitorSpeChar(self.lineEdit_6.text(), "-", 11) == False) or self.lineEdit_6.text()[3] != '-' or self.lineEdit_6.text()[6] != '-':
                self.show_msg( 1, "SSN Incorrect! Must be 9 numbers long. \nFormat: xxx-xx-xxxx")
                self.lineEdit_6.setText(self.ssn)

            elif (self.IsDigitorSpeChar(self.lineEdit_7.text(), ".", -1) == False):
                self.show_msg( 1, "Weight Must Be A Number.")
                self.lineEdit_7.setText(self.weight)

            elif (self.IsDigitorSpeChar(self.lineEdit_8.text(), ".", -1) == False):
                self.show_msg( 1, "Height Must Be A Number.")
                self.lineEdit_8.setText(self.height)

            elif (self.IsDigitorSpeChar(self.lineEdit_9.text(), "", -1) == False):
                self.show_msg( 1, "Age Must Be A Number.")
                self.lineEdit_9.setText(self.age)

            # Update self with valid inputs
            self.ssn = self.lineEdit_6.text()
            self.weight = self.lineEdit_7.text()
            self.height = self.lineEdit_8.text()
            self.age = self.lineEdit_9.text()

            cur.execute(
                'UPDATE Patient SET SSN = (%s), Weight = (%s), Height = (%s), Age = (%s) WHERE PatientID = (%s)', (
                self.reformat(self.lineEdit_6.text()), self.lineEdit_7.text(), self.lineEdit_8.text(),
                self.lineEdit_9.text(), self.ID))

            if num == 2:  # Doctor
                cur.execute('UPDATE Doctor SET MedicalLicense = (%s) WHERE DoctorID = (%s)',
                            (self.lineEdit_8.text(), self.ID))

            if num == 3:  # Nurse
                cur.execute('UPDATE Nurse SET MedicalLicense = (%s) WHERE NurseID = (%s)',
                            (self.lineEdit_8.text(), self.ID))
            # Admin can't change anything else then Person attributes
            conn.commit()

        self.lineEdit_1.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_10.setEnabled(False)

        self.SaveBtn.setEnabled(False)
        self.EditBtn.setEnabled(True)

    def updateDateSelected(self):
        self.dateEdit_16.setDate(self.calendarWidget_1.selectedDate())


    # Remove dashes 
    def reformat(self, str):
        for char in str:
            if char in "-":
                str = str.replace(char, '')
        return str

    # Check if digit or spechar of len = num
    def IsDigitorSpeChar(self, str, spechar, num):

        # Empty str
        if(str==""):
            return False

        if(num!=-1): # num=-1 when no need to check len
            if len(str)!=num:
                return False

        for char in str:
            if (char.isdigit() == False) and char not in spechar:
                return False

        return True


    def show_msg(self, num, str):
        msg = QtWidgets.QMessageBox()
        # Warning
        if num == 1:
            msg.setIcon(QtWidgets.QMessageBox().Warning)
            msg.setText("\n"+str)
        # Information
        if num == 2:
            msg.setIcon(QtWidgets.QMessageBox().Information)
            msg.setText("\n"+str)

        msg.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    ui = menu_UI()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())
