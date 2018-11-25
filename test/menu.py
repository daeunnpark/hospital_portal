import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets


class menu_UI(object):
    def setupUi(self, Menu, firstName, lastName, phoneNumber, emailAddress, ID, age, ssn, weight, height, creditCardNumber, billingAmount, insuranceNumber, medicationList, appointmentDates, startTimes, endTimes, appointmentIDs, cur, conn):

        Menu.setObjectName("Menu")
        #Menu.resize(1600, 1200)
        Menu.resize(800, 600)

        self.centralWidget = QtWidgets.QWidget(Menu)
        self.centralWidget.setObjectName("centralWidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QtCore.QRect(200, 100, 2000, 1000))
        
        # tab1: Profile 
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")

        # firstName
        self.label_1 = QtWidgets.QLabel(self.tab_1)
        self.label_1.setObjectName("label_1")
        self.label_1.setGeometry(QtCore.QRect(10, 20, 300, 61))
        self.label_1.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")

        self.lineEdit_1 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_1.setGeometry(QtCore.QRect(50, 90, 500, 60))
        self.lineEdit_1.setReadOnly(True)
        self.lineEdit_1.setText(firstName)
        
        # lastName  
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QtCore.QRect(910, 20, 300, 61))
        self.label_2.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setGeometry(QtCore.QRect(940, 90, 500, 60))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setText(lastName)
        
        # phoneNumber
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QtCore.QRect(20, 170, 341, 40))
        self.label_3.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 220, 500, 60)) 
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setText(phoneNumber)
        
        # emailAddress
        self.label_4 = QtWidgets.QLabel(self.tab_1)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QtCore.QRect(910, 170, 341, 40))
        self.label_4.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setGeometry(QtCore.QRect(940, 220, 500, 60))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setText(emailAddress)
        
        # ID
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QtCore.QRect(20, 320, 341, 40))
        self.label_5.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 370, 500, 60))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setText(ID)
        
        # ssn
        self.label_6 = QtWidgets.QLabel(self.tab_1)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QtCore.QRect(910, 320, 341, 40))
        self.label_6.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setGeometry(QtCore.QRect(940, 370, 500, 60))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setText(ssn)
        
        # weight
        self.label_7 = QtWidgets.QLabel(self.tab_1)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QtCore.QRect(20, 470, 341, 40))
        self.label_7.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")

        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setGeometry(QtCore.QRect(50, 540, 500, 60))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setText(weight)
        
        # height
        self.label_8 = QtWidgets.QLabel(self.tab_1)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QtCore.QRect(910, 470, 341, 40))
        self.label_8.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")

        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setGeometry(QtCore.QRect(940, 540, 500, 60))     
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setText(height)
        
        # age
        self.label_9 = QtWidgets.QLabel(self.tab_1)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(QtCore.QRect(20, 650, 341, 40))
        self.label_9.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")

        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setGeometry(QtCore.QRect(50, 720, 500, 60))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setText(age)

        # medicationList
        self.label_10 = QtWidgets.QLabel(self.tab_1)
        self.label_10.setObjectName("label_10")
        self.label_10.setGeometry(QtCore.QRect(910, 650, 341, 40))
        self.label_10.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")

        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setGeometry(QtCore.QRect(940, 720, 500, 60))      
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setText(medicationList)
        self.tabWidget.addTab(self.tab_1, "")


        # tab2: Appointment Calendar
        
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        # Appointment info
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.label_11.setGeometry(QtCore.QRect(50, 700, 600, 41))
        self.label_11.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 18pt \"Lucida Calligraphy\";")

        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setGeometry(QtCore.QRect(430, 80, 1000, 600))
        
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1020, 600))
        
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.gridLayoutWidget_2)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.calendarWidget_2.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        earliestDate = None
        self.gridLayout_3.addWidget(self.calendarWidget_2, 0, 0, 0, 0)
        # switched the order of last two lines

        # 1
        self.dateTimeEdit_1 = QtWidgets.QLineEdit(self.tab_2)
        self.dateTimeEdit_1.setObjectName("dateTimeEdit_1")
        self.dateTimeEdit_1.setGeometry(QtCore.QRect(0, 780, 500, 80))
        self.dateTimeEdit_1.setVisible(False)
        self.dateTimeEdit_1.setReadOnly(True)
        
        self.pushButtonCancel_1 = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonCancel_1.setObjectName("pushButtonCancel_1")
        self.pushButtonCancel_1.setGeometry(QtCore.QRect(30, 870, 400, 80))
        self.pushButtonCancel_1.setStyleSheet("color: rgb(46, 125, 132);\n"
                                            "font-weight: bold;\n"
                                            "font: 12pt \"Lucida Calligraphy\";")
        self.pushButtonCancel_1.setVisible(False)
                                            
        # 3
        self.dateTimeEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.dateTimeEdit_3.setObjectName("dateTimeEdit_3")
        self.dateTimeEdit_3.setGeometry(QtCore.QRect(510, 780, 500, 80))
        self.dateTimeEdit_3.setVisible(False)
        self.dateTimeEdit_3.setReadOnly(True)

        self.pushButtonCancel_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonCancel_3.setObjectName("pushButtonCancel_3")
        self.pushButtonCancel_3.setGeometry(QtCore.QRect(540, 870, 400, 80))
        self.pushButtonCancel_3.setStyleSheet("color: rgb(46, 125, 132);\n"
                                             "font-weight: bold;\n"
                                             "font: 12pt \"Lucida Calligraphy\";")
        self.pushButtonCancel_3.setVisible(False)


        # 5
        self.dateTimeEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.dateTimeEdit_5.setObjectName("dateTimeEdit_5")
        self.dateTimeEdit_5.setGeometry(QtCore.QRect(1020, 780, 500, 80))
        self.dateTimeEdit_5.setVisible(False)
        self.dateTimeEdit_5.setReadOnly(True)
        
        self.pushButtonCancel_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonCancel_5.setObjectName("pushButtonCancel_5")
        self.pushButtonCancel_5.setGeometry(QtCore.QRect(1050, 870, 400, 80))
        self.pushButtonCancel_5.setStyleSheet("color: rgb(46, 125, 132);\n"
                                             "font-weight: bold;\n"
                                             "font: 12pt \"Lucida Calligraphy\";")
        self.pushButtonCancel_5.setVisible(False)


        # 7
        self.dateTimeEdit_7 = QtWidgets.QLineEdit(self.tab_2)
        self.dateTimeEdit_7.setObjectName("dateTimeEdit_7")
        self.dateTimeEdit_7.setGeometry(QtCore.QRect(1540, 780, 500, 80))
        self.dateTimeEdit_7.setVisible(False)
        self.dateTimeEdit_7.setReadOnly(True)

        self.pushButtonCancel_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonCancel_7.setGeometry(QtCore.QRect(1570, 870, 400, 80))
        self.pushButtonCancel_7.setObjectName("pushButtonCancel_7")
        self.pushButtonCancel_7.setStyleSheet("color: rgb(46, 125, 132);\n"
                                             "font-weight: bold;\n"
                                             "font: 12pt \"Lucida Calligraphy\";")
        self.pushButtonCancel_7.setVisible(False)


        numDates = 0
        for row in appointmentDates:
            if(earliestDate == None):
                earliestDate = row[0]
            else:
                if(row[0] < earliestDate):
                    earliestDate = row[0]
            if(numDates == 0):
                self.dateTimeEdit_1.setVisible(True)
                self.pushButtonCancel_1.setVisible(True)
                self.dateTimeEdit_1.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1
            elif(numDates == 1):
                self.dateTimeEdit_3.setVisible(True)
                self.pushButtonCancel_3.setVisible(True)
                self.dateTimeEdit_3.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1
            elif(numDates == 2):
                self.dateTimeEdit_5.setVisible(True)
                self.pushButtonCancel_5.setVisible(True)
                self.dateTimeEdit_5.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1
            elif(numDates == 3):
                self.dateTimeEdit_7.setVisible(True)
                self.pushButtonCancel_7.setVisible(True)
                self.dateTimeEdit_7.setText(row[0].strftime('%m/%d/%Y'))
                numDates = numDates + 1
        
        numStarts = 0
        for row in startTimes:
            if (numStarts == 0):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.dateTimeEdit_1.setText(self.dateTimeEdit_1.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
                numStarts = numStarts + 1
            elif (numStarts == 1):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.dateTimeEdit_3.setText(self.dateTimeEdit_3.text() + "               " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
                numStarts = numStarts + 1
            elif (numStarts == 2):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.dateTimeEdit_1.setText(self.dateTimeEdit_1.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
                numStarts = numStarts + 1
            elif (numStarts == 3):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.dateTimeEdit_1.setText(
                    self.dateTimeEdit_1.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(
                        seconds))
                numStarts = numStarts + 1
       
        numEnds = 0
        for row in endTimes:
            if (numEnds == 0):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.dateTimeEdit_1.setText(self.dateTimeEdit_1.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
                numEnds = numEnds + 1
            elif (numEnds == 1):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.dateTimeEdit_3.setText(self.dateTimeEdit_3.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
                numEnds = numEnds + 1
            elif (numEnds == 2):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.dateTimeEdit_1.setText(self.dateTimeEdit_1.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
                numEnds = numEnds + 1
            elif (numEnds == 3):
                hours, remainder = divmod(row[0].seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.dateTimeEdit_1.setText(self.dateTimeEdit_1.text() + "                " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
                numEnds = numEnds + 1
        
        if(earliestDate != None):
            self.calendarWidget_2.setSelectedDate(earliestDate)
        
       
        
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(0, 10, 700, 41))
        self.label_16.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt \"Lucida Calligraphy\";")
        self.label_16.setObjectName("label_16")
        
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setObjectName("label_17")
        self.label_17.setGeometry(QtCore.QRect(1440, 10, 700, 41))
        self.label_17.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt \"Lucida Calligraphy\";")
        
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setObjectName("label_18")
        self.label_18.setGeometry(QtCore.QRect(1440, 80, 700, 41))
        self.label_18.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt \"Lucida Calligraphy\";")
        
        self.dateWidget = QtWidgets.QDateEdit(self.tab_2)
        self.dateWidget.setGeometry(QtCore.QRect(1440, 120, 400, 41))
        self.dateWidget.setObjectName("dateWidget")

        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setObjectName("label_19")
        self.label_19.setGeometry(QtCore.QRect(1440, 200, 700, 41))
        self.label_19.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt \"Lucida Calligraphy\";")
        
        self.timeStartWidget = QtWidgets.QDateEdit(self.tab_2)
        self.timeStartWidget.setGeometry(QtCore.QRect(1440, 240, 400, 41))
        self.timeStartWidget.setObjectName("timeStartWidget")
        self.label_20.setObjectName("label_20")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(1440, 320, 700, 41))
        self.label_20.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt \"Lucida Calligraphy\";")
        

        self.timeEndWidget = QtWidgets.QDateEdit(self.tab_2)
        self.timeEndWidget.setGeometry(QtCore.QRect(1440, 360, 400, 41))
        self.timeEndWidget.setObjectName("timeEndWidget")

        self.pushButtonSchedule = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonSchedule.setObjectName("pushButtonSchedule")
        self.pushButtonSchedule.setGeometry(QtCore.QRect(1490, 520, 300, 80))
        
        self.tabWidget.addTab(self.tab_2, "")

        # tab3: Billing
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        # insuranceNumber
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setObjectName("label_12")
        self.label_12.setGeometry(QtCore.QRect(30, 30, 500, 61))
        self.label_12.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.setGeometry(QtCore.QRect(80, 100, 400, 60))
        self.lineEdit_12.setText(insuranceNumber)

        # creditCardNumber
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setObjectName("label_13")
        self.label_13.setGeometry(QtCore.QRect(30, 300, 500, 61))
        self.label_13.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")

        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_13.setGeometry(QtCore.QRect(80, 370, 400, 60))
        self.lineEdit_13.setText(creditCardNumber)
        
        # Billing Amount
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setObjectName("label_14")
        self.label_14.setGeometry(QtCore.QRect(30, 550, 500, 61))
        self.label_14.setStyleSheet("color: rgb(46, 125, 132);\n"
"font-weight: bold;\n"
"font: 12pt \"Lucida Calligraphy\";")
        
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_14.setGeometry(QtCore.QRect(80, 630, 400, 60))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.setText(billingAmount)

        # Payment Amount
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setObjectName("label_15")
        self.label_15.setGeometry(QtCore.QRect(1000, 30, 500, 61))
        self.label_15.setStyleSheet("color: rgb(46, 125, 132);\n"
                                    "font-weight: bold;\n"
                                    "font: 12pt \"Lucida Calligraphy\";")
        

        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_15.setGeometry(QtCore.QRect(1100, 80, 400, 60))
        
        # Pay btn
        self.pushButtonPay = QtWidgets.QPushButton(self.tab_3)
        self.pushButtonPay.setObjectName("pushButtonPay")
        self.pushButtonPay.setGeometry(QtCore.QRect(1100, 200, 300, 60))


        self.tabWidget.addTab(self.tab_3, "")

        Menu.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Menu)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 21))
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

        self.pushButtonCancel_1.clicked.connect(lambda: self.cancelAppt(1, appointmentIDs, cur, conn))
        self.pushButtonCancel_3.clicked.connect(lambda: self.cancelAppt(3, appointmentIDs, cur, conn))
        self.pushButtonCancel_5.clicked.connect(lambda: self.cancelAppt(5, appointmentIDs, cur, conn))
        self.pushButtonCancel_7.clicked.connect(lambda: self.cancelAppt(7, appointmentIDs, cur, conn))
        self.pushButtonSchedule.clicked.connect(self.scheduleAppt)
        self.pushButtonPay.clicked.connect(lambda: self.Pay(ID, cur, conn))

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Menu", "Profile"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Menu", "Appointment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Menu", "Billing Info"))
        
        self.label_1.setText(_translate("Menu", "First Name:"))
        self.label_2.setText(_translate("Menu", "Last Name:"))
        self.label_3.setText(_translate("Menu", "Phone Number:"))
        self.label_4.setText(_translate("Menu", "Email Address:"))
        self.label_5.setText(_translate("Menu", "ID:"))
        self.label_6.setText(_translate("Menu", "SSN:"))
        self.label_7.setText(_translate("Menu", "Weight:"))
        self.label_8.setText(_translate("Menu", "Height:"))
        self.label_9.setText(_translate("Menu", "Age:"))
        self.label_10.setText(_translate("Menu", "Medication List:"))
        self.label_11.setText(_translate("Menu", "Appointments: {Date    Start Time    End Time}"))
        self.label_12.setText(_translate("Menu", "Insurance Number:"))
        self.label_13.setText(_translate("Menu", "Credit Card Number:"))
        self.label_14.setText(_translate("Menu", "Billing Amount:"))
        self.label_15.setText(_translate("Menu", "Payment Amount:"))
        self.label_16.setText(_translate("Menu", "Next Appointment Highlighted in Gray"))
        self.label_17.setText(_translate("Menu", "Schedule Appointment: Max 4"))
        self.label_18.setText(_translate("Menu", "Date:"))
        self.label_19.setText(_translate("Menu", "Start Time:"))
        self.label_20.setText(_translate("Menu", "End Time:"))

        self.pushButtonCancel_1.setText(_translate("Menu", "Cancel Appointment"))
        self.pushButtonCancel_3.setText(_translate("Menu", "Cancel Appointment"))
        self.pushButtonCancel_5.setText(_translate("Menu", "Cancel Appointment"))
        self.pushButtonCancel_7.setText(_translate("Menu", "Cancel Appointment"))
        self.pushButtonSchedule.setText(_translate("Menu", "Schedule:"))

        self.pushButtonPay.setText(_translate("Menu", "Pay"))

    def Pay(self, ID, cur, conn):
        if(self.lineEdit_14.text() < self.lineEdit_15.text()):
            diff = float(self.lineEdit_15.text()) - float(self.lineEdit_14.text())
            self.lineEdit_15.setText(str(diff))
            self.lineEdit_14.setText("0")
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (0, ID))
            conn.commit()
        elif(self.lineEdit_14.text() == self.lineEdit_15.text()):
            self.lineEdit_15.setText("0")
            self.lineEdit_14.setText("0")
            cur.execute('UPDATE Patient SET BillingAmount = (%s) WHERE PatientID = (%s)', (0, ID))
            conn.commit()
        else:
            diff2 = float(self.lineEdit_14.text()) - float(self.lineEdit_15.text())
            self.lineEdit_14.setText(str(diff2))
            self.lineEdit_15.setText("0")
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
            self.dateTimeEdit.setText("")
            self.dateTimeEdit.setVisible(False)
            self.pushButtonCancel_.setVisible(False)
            numAppointment = 0
            appointNum = -1
            for row in appointmentIDs:
                if(numAppointment == 0):
                    appointNum = row[0]
                    numAppointment = numAppointment + 1
            cur.execute('DELETE FROM Appointment WHERE AppointmentID = (%s)', appointNum)
            conn.commit()
        if(num == 3):
            self.dateTimeEdit_3.setText("")
            self.dateTimeEdit_3.setVisible(False)
            self.pushButtonCancel_3.setVisible(False)
            numAppointment = 0
            appointNum = -1
            for row in appointmentIDs:
                if (numAppointment == 1):
                    appointNum = row[0]
                    numAppointment = numAppointment + 1
            cur.execute('DELETE FROM Appointment WHERE AppointmentID = (%s)', appointNum)
            conn.commit()
        if(num == 5):
            self.dateTimeEdit.setText("")
            self.dateTimeEdit.setVisible(False)
            self.pushButtonCancel_.setVisible(False)
            numAppointment = 0
            appointNum = -1
            for row in appointmentIDs:
                if (numAppointment == 2):
                    appointNum = row[0]
                    numAppointment = numAppointment + 1
            cur.execute('DELETE FROM Appointment WHERE AppointmentID = (%s)', appointNum)
            conn.commit()
        if(num == 7):
            self.dateTimeEdit.setText("")
            self.dateTimeEdit.setVisible(False)
            self.pushButtonCancel_.setVisible(False)
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

