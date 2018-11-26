import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets


class menu_UI(object):
    def setupUi(self, Menu, firstName, lastName, phoneNumber, emailAddress, ID, age, ssn, weight, height,
                creditCardNumber, billingAmount, insuranceNumber, medicationList, appointmentDates, startTimes,
                endTimes, appointmentIDs, cur, conn):
        Menu.setObjectName("Menu")
        self.centralWidget = QtWidgets.QWidget(Menu)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_1.setText(firstName)
        self.lineEdit_1.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_1, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_1)
        self.label_4.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setText(age)
        self.lineEdit_9.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_9, 10, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText(lastName)
        self.lineEdit_2.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_2, 2, 3, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText(phoneNumber)
        self.lineEdit_3.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setText(weight)
        self.lineEdit_7.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_7, 8, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_8, 8, 3, 1, 1)
        self.lineEdit_8.setText(height)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText(ID)
        self.lineEdit_5.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_5, 6, 1, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setText(medicationList)
        self.lineEdit_10.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_10, 10, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.tab_1)
        self.label_1.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText(emailAddress)
        self.lineEdit_4.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_4, 4, 3, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_6, 6, 3, 1, 1)
        self.lineEdit_6.setText(ssn)
        self.label_7 = QtWidgets.QLabel(self.tab_1)
        self.label_7.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_1)
        self.label_6.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_1)
        self.label_8.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_1)
        self.label_9.setStyleSheet("color: rgb(46, 125, 132);\n"
                                   "font-weight: bold;\n"
                                   "font: 12pt \"Lucida Calligraphy\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 10, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_1)
        self.label_10.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt \"Lucida Calligraphy\";")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 10, 2, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        earliestDate = None

        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setMaximumSize(QtCore.QSize(589, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setVisible(False)
        self.gridLayout_2.addWidget(self.lineEdit, 18, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setVisible(False)
        self.gridLayout_2.addWidget(self.lineEdit_11, 18, 1, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_15.setMaxLength(300)
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setVisible(False)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_2.addWidget(self.lineEdit_15, 18, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 19, 1, 1, 1)
        self.pushButton_2.setVisible(False)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 19, 3, 1, 1)
        self.pushButton_3.setVisible(False)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 19, 4, 1, 1)
        self.pushButton_4.setVisible(False)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 19, 0, 1, 1)
        self.pushButton.setVisible(False)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_2.addWidget(self.lineEdit_16, 18, 4, 1, 1)
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setVisible(False)
        numDates = 0
        for row in appointmentDates:
            if (earliestDate == None):
                earliestDate = row[0]
            else:
                if (row[0] < earliestDate):
                    earliestDate = row[0]
            if (numDates == 0):
                self.lineEdit.setVisible(True)
                self.pushButton.setVisible(True)
                self.lineEdit.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1
            elif (numDates == 1):
                self.lineEdit_11.setVisible(True)
                self.pushButton_2.setVisible(True)
                self.lineEdit_11.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1
            elif (numDates == 2):
                self.lineEdit_15.setVisible(True)
                self.pushButton_3.setVisible(True)
                self.lineEdit_15.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1
            elif (numDates == 3):
                self.lineEdit_16.setVisible(True)
                self.pushButton_4.setVisible(True)
                self.lineEdit_16.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1

        numStarts = 0
        for row in startTimes:
            if (numStarts == 0):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit.setText(
                    self.lineEdit.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(
                        seconds))
                numStarts = numStarts + 1
            elif (numStarts == 1):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit_11.setText(
                    self.lineEdit_11.text() + "               " + str(hours) + ":" + str(minutes) + ":" + str(
                        seconds))
                numStarts = numStarts + 1
            elif (numStarts == 2):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit_15.setText(
                    self.lineEdit_15.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(
                        seconds))
                numStarts = numStarts + 1
            elif (numStarts == 3):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit_16.setText(
                    self.lineEdit_16.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(
                        seconds))
                numStarts = numStarts + 1

        numEnds = 0
        for row in endTimes:
            if (numEnds == 0):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit.setText(
                    self.lineEdit.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(
                        seconds))
                numEnds = numEnds + 1
            elif (numEnds == 1):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit_11.setText(
                    self.lineEdit_11.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(
                        seconds))
                numEnds = numEnds + 1
            elif (numEnds == 2):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit_15.setText(
                    self.lineEdit_15.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(
                        seconds))
                numEnds = numEnds + 1
            elif (numEnds == 3):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.lineEdit_16.setText(
                    self.lineEdit_16.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(
                        seconds))
                numEnds = numEnds + 1

        #if (earliestDate != None):
            #self.calendarWidget_2.setSelectedDate(earliestDate)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_11.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 18pt \"Lucida Calligraphy\";")
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 17, 0, 1, 4)
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 3, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 5, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 1, 3, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.groupBox_2)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.gridLayout_3.addWidget(self.calendarWidget_2, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setStyleSheet("color: rgb(46, 125, 132);\n"
                                 "font-weight: bold;\n"
                                 "font: 12pt Lucida Calligraphy")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 9, 2)
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 3, 1, 2)
        self.dateEdit = QtWidgets.QDateEdit(self.tab_2)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 2, 3, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.tab_2)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_2.addWidget(self.timeEdit, 4, 3, 1, 1)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.tab_2)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.gridLayout_2.addWidget(self.timeEdit_2, 6, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 7, 3, 2, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt \"Lucida Calligraphy\";")
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_12.setMaximumSize(QtCore.QSize(300, 50))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setText(insuranceNumber)
        self.verticalLayout.addWidget(self.lineEdit_12)
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt \"Lucida Calligraphy\";")
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_13.setMaximumSize(QtCore.QSize(300, 50))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout.addWidget(self.lineEdit_13)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setText(creditCardNumber)
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt \"Lucida Calligraphy\";")
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_14.setMaximumSize(QtCore.QSize(300, 50))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setText(billingAmount)
        self.verticalLayout.addWidget(self.lineEdit_14)
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt Lucida Calligraphy;")
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.verticalLayout.addWidget(self.lineEdit_17)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        Menu.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Menu)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName("menuBar")
        Menu.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Menu)
        self.mainToolBar.setObjectName("mainToolBar")
        Menu.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Menu)
        self.statusBar.setObjectName("statusBar")
        Menu.setStatusBar(self.statusBar)

        self.retranslateUi(Menu)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Menu)

        self.pushButton.clicked.connect(lambda: self.cancelAppt(1, appointmentIDs, cur, conn))
        self.pushButton_2.clicked.connect(lambda: self.cancelAppt(3, appointmentIDs, cur, conn))
        self.pushButton_3.clicked.connect(lambda: self.cancelAppt(5, appointmentIDs, cur, conn))
        self.pushButton_4.clicked.connect(lambda: self.cancelAppt(7, appointmentIDs, cur, conn))
        self.pushButton_5.clicked.connect(self.scheduleAppt)
        self.pushButton_6.clicked.connect(lambda: self.Pay(ID, cur, conn))

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.label_4.setText(_translate("Menu", "Email Address:"))
        self.label_3.setText(_translate("Menu", "Phone Number:"))
        self.label_1.setText(_translate("Menu", "First Name:"))
        self.label_7.setText(_translate("Menu", "Weight:"))
        self.label_2.setText(_translate("Menu", "Last Name:"))
        self.label_5.setText(_translate("Menu", "ID:"))
        self.label_6.setText(_translate("Menu", "SSN:"))
        self.label_8.setText(_translate("Menu", "Height:"))
        self.label_9.setText(_translate("Menu", "Age:"))
        self.label_10.setText(_translate("Menu", "Medication List:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Menu", "Profile"))
        self.pushButton_2.setText(_translate("Menu", "Cancel Appointment"))
        self.pushButton_3.setText(_translate("Menu", "Cancel Appointment"))
        self.pushButton_4.setText(_translate("Menu", "Cancel Appointment"))
        self.pushButton.setText(_translate("Menu", "Cancel Appointment"))
        self.label_11.setText(_translate("Menu", "Appointments: { Date | Start Time | End Time}"))
        self.label_18.setText(_translate("Menu", "Start Time:"))
        self.label_19.setText(_translate("Menu", "End Time:"))
        self.label_17.setText(_translate("Menu", "Date:"))
        self.label.setText(_translate("Menu", "Next Appointment Highlighted in Gray: "))
        self.label_15.setText(_translate("Menu", "Schedule Appointment: Max 4"))
        self.pushButton_5.setText(_translate("Menu", "Schedule:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Menu", "Appointment"))
        self.label_12.setText(_translate("Menu", "Insurance Number:"))
        self.label_13.setText(_translate("Menu", "Credit Card Number:"))
        self.label_14.setText(_translate("Menu", "Billing Amount:"))
        self.label_16.setText(_translate("Menu", "Payment Amount:"))
        self.pushButton_6.setText(_translate("Menu", "Pay"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Menu", "Billing Info"))

    def Pay(self, ID, cur, conn):
        if(self.lineEdit_14.text() < self.lineEdit_17.text()):
            diff = float(self.lineEdit_17.text()) - float(self.lineEdit_14.text())
            self.lineEdit_17.setText(str(diff))
            self.lineEdit_14.setText("0")
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (0, ID))
            conn.commit()
        elif(self.lineEdit_14.text() == self.lineEdit_17.text()):
            self.lineEdit_17.setText("0")
            self.lineEdit_14.setText("0")
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (0, ID))
            conn.commit()
        else:
            diff2 = float(self.lineEdit_14.text()) - float(self.lineEdit_17.text())
            self.lineEdit_14.setText(str(diff2))
            self.lineEdit_17.setText("0")
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (diff2, ID))
            conn.commit()

    def scheduleAppt(self, cur, conn):
        apptID = 1
        cur.rowcount = -1
        while (cur.rowcount != 0):
            cur.execute('SELECT * FROM Appointment WHERE AppointmentID = (%s)', apptID)
            apptID = apptID + 1



    def cancelAppt(self, num, appointmentIDs, cur, conn):
        if(num == 1):
            self.lineEdit.setText("")
            self.lineEdit.setVisible(False)
            self.pushButton.setVisible(False)
            numAppointment = 0
            appointNum = -1
            for row in appointmentIDs:
                if(numAppointment == 0):
                    appointNum = row[0]
                    numAppointment = numAppointment + 1
            cur.execute('DELETE FROM Appointment WHERE AppointmentID = (%s)', appointNum)
            conn.commit()
        if(num == 3):
            self.lineEdit_11.setText("")
            self.lineEdit_11.setVisible(False)
            self.pushButton_2.setVisible(False)
            numAppointment = 0
            appointNum = -1
            for row in appointmentIDs:
                if (numAppointment == 1):
                    appointNum = row[0]
                    numAppointment = numAppointment + 1
            cur.execute('DELETE FROM Appointment WHERE AppointmentID = (%s)', appointNum)
            conn.commit()
        if(num == 5):
            self.lineEdit_15.setText("")
            self.lineEdit_15.setVisible(False)
            self.pushButton_3.setVisible(False)
            numAppointment = 0
            appointNum = -1
            for row in appointmentIDs:
                if (numAppointment == 2):
                    appointNum = row[0]
                    numAppointment = numAppointment + 1
            cur.execute('DELETE FROM Appointment WHERE AppointmentID = (%s)', appointNum)
            conn.commit()
        if(num == 7):
            self.lineEdit_16.setText("")
            self.lineEdit_16.setVisible(False)
            self.pushButton_4.setVisible(False)
            numAppointment = 0
            appointNum = -1
            for row in appointmentIDs:
                if (numAppointment == 3):
                    appointNum = row[0]
                    numAppointment = numAppointment + 1
            cur.execute('DELETE FROM Appointment WHERE AppointmentID = (%s)', appointNum)
            conn.commit()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = menu_UI()
    ui.setupUi(MainWindow)

    MainWindow.show()
    # MainWindow.showMaximized()

    sys.exit(app.exec_())

