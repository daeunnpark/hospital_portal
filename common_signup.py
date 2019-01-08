import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

# import modules
from common_login import common_login_UI

# newUI- Done
class common_signup_UI(object):
    def __init__(self, parent=None):
        self.newP = False
        self.newD = False
        self.newN = False

    def setupUi(self, CommonSignUp, num):
        CommonSignUp.setObjectName("CommonSignUp")
        CommonSignUp.setStyleSheet("background-color: rgb(243,255,255);\n"
                                   "")
        self.centralwidget = QtWidgets.QWidget(CommonSignUp)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setStyleSheet("background-color: rgb(225,247,251);")
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_15 = QtWidgets.QLabel(self.widget_4)
        self.label_15.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget_4, 1, 0, 1, 2)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 700))
        self.widget_2.setMaximumSize(QtCore.QSize(10000, 10000))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setStyleSheet("font: 30pt Arial;")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setStyleSheet("font: 30pt Arial;")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setStyleSheet("font: 30pt Arial;")
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setStyleSheet("font: 30pt Arial;")
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 6, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setStyleSheet("font: 30pt Arial;")
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setStyleSheet("font: 30pt Arial;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_3.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_3.addWidget(self.lineEdit_6, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setStyleSheet("font: 30pt Arial;")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_3.addWidget(self.lineEdit_12, 6, 1, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_3.addWidget(self.lineEdit_10, 5, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_3.addWidget(self.lineEdit_8, 4, 1, 1, 1)
        self.gridLayout_4.addWidget(self.widget_2, 2, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 700))
        self.widget_3.setMaximumSize(QtCore.QSize(10000, 10000))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setStyleSheet("font: 30pt Arial;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setStyleSheet("font: 30pt Arial;")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget_3)
        self.label_14.setMaximumSize(QtCore.QSize(16777214, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.label_14.setFont(font)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setStyleSheet("font: 30pt Arial;")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setStyleSheet("font: 30pt Arial;")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setStyleSheet("font: 30pt Arial;")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 5, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget_3)
        self.label_13.setStyleSheet("font: 30pt Arial;")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 6, 1, 1, 1)
        self.gridLayout_4.addWidget(self.widget_3, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMaximumSize(QtCore.QSize(200, 60))
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setStyleSheet("font: 30pt Arial;\n"
                                      "background-color: rgb(232, 232, 232);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        CommonSignUp.setCentralWidget(self.centralwidget)


        self.retranslateUi(CommonSignUp, num)
        QtCore.QMetaObject.connectSlotsByName(CommonSignUp)


    def retranslateUi(self, CommonSignUp, num):
        _translate = QtCore.QCoreApplication.translate
        CommonSignUp.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_15.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Sign Up Form</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "FirstName"))
        self.label_6.setText(_translate("MainWindow", "Password"))
        self.label_8.setText(_translate("MainWindow", "Age"))
        self.label_12.setText(_translate("MainWindow", "Credit Card Number"))
        self.label_10.setText(_translate("MainWindow", "Height"))
        self.label_5.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Phone Number"))
        self.label_2.setText(_translate("MainWindow", "LastName"))
        self.label_4.setText(_translate("MainWindow", "Email Address"))
        self.label_7.setText(_translate("MainWindow", "Re-Enter Password"))
        self.label_9.setText(_translate("MainWindow", "Weight"))
        self.label_11.setText(_translate("MainWindow", "SSN"))
        self.label_13.setText(_translate("MainWindow", "Insurance Number"))
        self.pushButton.setText(_translate("MainWindow", "Sign Up!"))

        """sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        sizePolicy.setRetainSizeWhenHidden(True)
        self.widget.setSizePolicy(sizePolicy)"""
        # Employee - Doctor/Nurse
        if(num != 1):    
            # lineEdit_9 =  medical license
            # lineEdit_8 = Specialty

            self.lineEdit_8.deleteLater()
            self.cb = QtWidgets.QComboBox()
            self.cb.setObjectName("comboBox")        
            self.label_8.setText(_translate("MainWindow", "Specialty:"))


            self.cb.addItem("Cardiology")
            self.cb.addItem("Dermatology")
            self.cb.addItem("Gastroenterology")
            self.cb.addItem("Gynaecology")
            self.cb.addItem("Oncology")
            self.cb.addItem("Pediatrics")
            self.cb.addItem("Psychiatry")
            #self.cb.setStyleSheet("font: 30pt Arial;")

            self.cb.setStyleSheet("font: 20pt Arial;\n"
                            "background-color: rgb(255,255,255);\n"
                                   "")

            self.gridLayout_3.addWidget(self.cb, 4, 1, 1, 1)

            


            self.label_9.setText(_translate("MainWindow", "Medical License:"))

            
            self.label_10.setVisible(False)
            self.label_11.setVisible(False)
            self.label_12.setVisible(False)
            self.label_13.setVisible(False)

            self.lineEdit_10.setVisible(False)
            self.lineEdit_11.setVisible(False)
            self.lineEdit_12.setVisible(False)
            self.lineEdit_13.setVisible(False)
            
            """
            if(num==4): # Admin
                self.label_8.setVisible(False)
                self.lineEdit_8.setVisible(False)
                self.label_9.setVisible(False)
                self.lineEdit_9.setVisible(False)
            """


    def CreatePatient(self, cur, conn, accessCodeReceived):
        self.newP = False
        if(self.lineEdit_5.text() == "" or self.lineEdit_6.text() == "" or self.lineEdit_7.text() == ""):
            self.show_msg( 1, "Please Specify Username and Password.")

        if(self.lineEdit_6.text() != self.lineEdit_7.text()):
            self.show_msg( 1, "Passwords Do Not Match!")
            self.lineEdit_7.setText("")

        else:
            cur.execute('SELECT * FROM Person P WHERE Username = (%s)', (self.lineEdit_5.text()))
            if(self.lineEdit_5.text())!= "" and (cur.rowcount != 0):
               self.show_msg( 1, "Username Already Exists! \nTry Another Username.")
               self.lineEdit_5.setText("")

            else:
                
                cur.execute('SELECT * FROM Person P WHERE UserPassword = (%s)', (self.lineEdit_6.text()))
                
                if(cur.rowcount != 0):
                    """Not check Password
                    self.show_msg( 1, "Password Already Exists! Choose Another Password.")"""

                else: 
                    if  (self.IsDigitorSpeChar(self.lineEdit_3.text(), "-", 12) == False) or self.lineEdit_3.text()[3] != '-' or self.lineEdit_3.text()[7] != '-' :
                        self.show_msg( 1, "Phone Number Incorrect! \nFormat: xxx-xxx-xxxx")
                        self.lineEdit_3.setText("")
                    
                    elif (self.IsDigitorSpeChar(self.lineEdit_8.text(), "", -1) == False):
                        self.show_msg( 1, "Age Must Be A Number.")
                        self.lineEdit_8.setText("")

                    elif (self.IsDigitorSpeChar(self.lineEdit_9.text(), ".", -1) == False):
                        self.show_msg( 1, "Weight Must Be A Number.")
                        self.lineEdit_9.setText("")

                    elif (self.IsDigitorSpeChar(self.lineEdit_10.text(), ".", -1) == False):
                        self.show_msg( 1, "Height Must Be A Number.")
                        self.lineEdit_10.setText("")
                    
                    elif (self.IsDigitorSpeChar(self.lineEdit_11.text(), "-", 11) == False) or self.lineEdit_11.text()[3] != '-' or self.lineEdit_11.text()[6] != '-':
                        self.show_msg( 1, "SSN Incorrect! Must be 9 numbers long. \nFormat: xxx-xx-xxxx")
                        self.lineEdit_11.setText("") 

                    else:
                        cur.execute('SELECT DoctorID FROM Doctor')
                        doctor = cur.fetchall()
                        cur.execute('SELECT NurseID FROM Nurse')
                        nurse = cur.fetchall()
                        cur.execute('SELECT DepartmentAdminID FROM DepartmentAdmin')
                        admin = cur.fetchall()

                        if(doctor[0] == None):
                            doctorid = -1
                        else:
                            doctorid = doctor[0][0]
                        if(nurse[0] == None):
                            nurseid = -1
                        else:
                            nurseid = nurse[0][0]
                        if(admin[0] == None):
                            adminid = -1
                        else:
                            adminid = admin[0][0]

                        cur.execute('INSERT INTO Person(ID, FirstName, LastName, PhoneNumber, EmailAddress, Username, UserPassword) VALUES (%s, %s, %s, %s, %s, %s, %s)', (accessCodeReceived, self.lineEdit.text(), self.lineEdit_2.text(), self.reformat(self.lineEdit_3.text()), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text()))
                        conn.commit()
                        cur.execute('INSERT INTO Patient(PatientID, Age, Weight, Height, SSN, CreditCardNumber, BillingAmount, InsuranceNumber, MedicationList, DoctorID, NurseID, AdminID) VALUES (%s, %s, %s, %s, %s, %s, 0.0, %s, "none", %s, %s, %s)', (accessCodeReceived, self.lineEdit_8.text(), self.lineEdit_9.text(), self.lineEdit_10.text(), self.reformat(self.lineEdit_11.text()), self.lineEdit_12.text(), self.lineEdit_13.text(), doctorid, nurseid, adminid))
                        conn.commit()

                        self.show_msg( 2, "Success! \nYou've joined United HealthCare.")
                        self.newP = True
        


    def CreateDoctor(self, cur, conn, accessCodeReceived):
        self.newD = False
        if(self.lineEdit_5.text() == "" or self.lineEdit_6.text() == "" or self.lineEdit_7.text() == ""):
            self.show_msg( 1, "Please Specify Username and Password.")

        if (self.lineEdit_6.text() != self.lineEdit_7.text()):
            self.show_msg( 1, "Passwords Do Not Match!")
            self.lineEdit_7.setText("")


        else:
            cur.execute('SELECT * FROM Person P WHERE Username = (%s)', (self.lineEdit_5.text()))
            
            if(self.lineEdit_5.text())!= "" and (cur.rowcount != 0):
                self.show_msg( 1, "Username Already Exists! \nTry Another Username.")
                lineEdit_5.text().setText("")
            
            else:
                cur.execute('SELECT * FROM Person P WHERE UserPassword = (%s)', (self.lineEdit_6.text()))
                
                if (cur.rowcount != 0):
                    """self.show_msg( 1, "Password Already Exists! \nChoose Another Password.")"""
                
                else:
                    if  (self.IsDigitorSpeChar(self.lineEdit_3.text(), "-", 12) == False) or self.lineEdit_3.text()[3] != '-' or self.lineEdit_3.text()[7] != '-' :
                        self.show_msg( 1, "Phone Number Incorrect! \nFormat: xxx-xxx-xxxx")
                        self.lineEdit_3.setText("")

                    else:

                        cur.execute('INSERT INTO Person(ID, FirstName, LastName, PhoneNumber, EmailAddress, Username, UserPassword) VALUES (%s, %s, %s, %s, %s, %s, %s)', (accessCodeReceived, self.lineEdit.text(), self.lineEdit_2.text(), self.reformat(self.lineEdit_3.text()), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text()))
                        conn.commit()

                        # first elemt at index 0
                        Specialty = self.cb.currentText()
                        deptID = self.cb.currentIndex()+1

                        cur.execute('INSERT INTO Employee(EmployeeID, DepartmentID) VALUES (%s, %s)', (accessCodeReceived, deptID))
                        conn.commit()
                        cur.execute('INSERT INTO Doctor(DoctorID, Specialty, MedicalLicense) VALUES (%s, %s, %s)', (accessCodeReceived, Specialty, self.lineEdit_9.text()))
                        conn.commit()

                        self.show_msg( 2, "Success! \nYou've joined United HealthCare.")
                        self.newD = True

        

    def CreateNurse(self, cur, conn, accessCodeReceived):
        self.newN = False
        if(self.lineEdit_5.text() == "" or self.lineEdit_6.text() == "" or self.lineEdit_7.text() == ""):
            self.show_msg( 1, "Please Specify Username and Password.")

        if (self.lineEdit_6.text() != self.lineEdit_7.text()):
            self.show_msg( 1, "Passwords Do Not Match!")
            self.lineEdit_7.setText("")

        else:
            cur.execute('SELECT * FROM Person P WHERE Username = (%s)', (self.lineEdit_5.text()))
            
            if self.lineEdit_5.text() != "" and (cur.rowcount != 0):
                self.show_msg( 1, "Username Already Exists! \nTry Another Username.")
                self.lineEdit_5.setText("")
            
            else:
                cur.execute('SELECT * FROM Person P WHERE UserPassword = (%s)', (self.lineEdit_6.text()))
                
                if (cur.rowcount != 0):
                    """Not check Password
                    self.show_msg( 1, "Password Already Exists! \nChoose Another Password.")"""
                
                else:
                    if  (self.IsDigitorSpeChar(self.lineEdit_3.text(), "-", 12) == False) or self.lineEdit_3.text()[3] != '-' or self.lineEdit_3.text()[7] != '-' :
                        self.show_msg( 1, "Phone Number Incorrect! \nFormat: xxx-xxx-xxxx")
                        self.lineEdit_3.setText("")
                    else:
                        cur.execute('INSERT INTO Person(ID, FirstName, LastName, PhoneNumber, EmailAddress, Username, UserPassword) VALUES (%s, %s, %s, %s, %s, %s, %s)', (accessCodeReceived, self.lineEdit.text(), self.lineEdit_2.text(), self.reformat(self.lineEdit_3.text()), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text()))
                        conn.commit()
                        
                        # first elemt at index 0
                        Specialty = self.cb.currentText()
                        deptID = self.cb.currentIndex()+1

                        
                        cur.execute('INSERT INTO Employee(EmployeeID, DepartmentID) VALUES (%s, %s)', (accessCodeReceived, deptID))
                        conn.commit()
                        cur.execute('INSERT INTO Nurse(NurseID, Specialty, MedicalLicense) VALUES (%s, %s, %s)', (accessCodeReceived, Specialty, self.lineEdit_9.text()))
                        conn.commit()
                        
                        self.show_msg( 2, "Success! \nYou've joined United HealthCare.")
                        self.newN = True


        

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

        if(num!=-1): # num=-1 when no need to check len, but should't be empty
            if len(str)!=num:
                return False
        

        for char in str:
            if (char.isdigit() == False) and char not in spechar :
                return False 
         
        return True  

    def show_msg(self, num, str):
        
        msg = QtWidgets.QMessageBox()
        # Warning
        if num==1:
            msg.setIcon(QtWidgets.QMessageBox().Warning)
            msg.setText("\n"+str)
        # Information
        if num==2:
            msg.setIcon(QtWidgets.QMessageBox().Information)
            msg.setText("\n"+str)

        msg.exec()

       # Maybe other types of msg here



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = common_signup_UI()
    ui.setupUi(MainWindow, 4)

    MainWindow.showMaximized()

    sys.exit(app.exec_())
