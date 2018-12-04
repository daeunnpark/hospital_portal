# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: localhost (MySQL 5.5.5-10.3.10-MariaDB)
# Database: HealthCareUnited
# Generation Time: 2018-12-04 22:19:49 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table AccessCodes
# ------------------------------------------------------------

DROP TABLE IF EXISTS `AccessCodes`;

CREATE TABLE `AccessCodes` (
  `AccessCodes` int(10) unsigned NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `AccessCodes` WRITE;
/*!40000 ALTER TABLE `AccessCodes` DISABLE KEYS */;

INSERT INTO `AccessCodes` (`AccessCodes`)
VALUES
	(305),
	(305305),
	(330055);

/*!40000 ALTER TABLE `AccessCodes` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Appointment
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Appointment`;

CREATE TABLE `Appointment` (
  `AppointmentID` int(10) unsigned NOT NULL,
  `DoctorID` int(10) unsigned NOT NULL,
  `NurseID` int(10) unsigned NOT NULL,
  `PatientID` int(10) unsigned NOT NULL,
  `DepartmentAdminID` int(10) unsigned NOT NULL,
  `Location` varchar(20) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `StartTime` time DEFAULT NULL,
  `EndTime` time DEFAULT NULL,
  PRIMARY KEY (`AppointmentID`),
  UNIQUE KEY `AppointmentID` (`AppointmentID`),
  KEY `DoctorID` (`DoctorID`),
  KEY `NurseID` (`NurseID`),
  KEY `PatientID` (`PatientID`),
  KEY `DepartmentAdminID` (`DepartmentAdminID`),
  CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`DoctorID`) REFERENCES `doctor` (`DoctorID`),
  CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`NurseID`) REFERENCES `nurse` (`NurseID`),
  CONSTRAINT `appointment_ibfk_3` FOREIGN KEY (`PatientID`) REFERENCES `patient` (`PatientID`),
  CONSTRAINT `appointment_ibfk_4` FOREIGN KEY (`DepartmentAdminID`) REFERENCES `departmentadmin` (`DepartmentAdminID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Appointment` WRITE;
/*!40000 ALTER TABLE `Appointment` DISABLE KEYS */;

INSERT INTO `Appointment` (`AppointmentID`, `DoctorID`, `NurseID`, `PatientID`, `DepartmentAdminID`, `Location`, `Date`, `StartTime`, `EndTime`)
VALUES
	(1,222,333,111,444,'SBU2','2018-12-14','02:00:00','03:00:00'),
	(2,222,333,111,444,'SBU2','2018-12-17','03:00:00','04:00:00'),
	(3,222,333,111,444,'SBU2','2018-12-20','02:30:00','03:00:00'),
	(4,222,333,8765,444,'SBU2','2018-12-18','11:00:00','11:30:00');

/*!40000 ALTER TABLE `Appointment` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table DepartmentAdmin
# ------------------------------------------------------------

DROP TABLE IF EXISTS `DepartmentAdmin`;

CREATE TABLE `DepartmentAdmin` (
  `SecurityCode` int(10) unsigned NOT NULL,
  `DepartmentAdminID` int(10) unsigned NOT NULL,
  KEY `A_ID` (`DepartmentAdminID`),
  CONSTRAINT `A_ID` FOREIGN KEY (`DepartmentAdminID`) REFERENCES `employee` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `DepartmentAdmin` WRITE;
/*!40000 ALTER TABLE `DepartmentAdmin` DISABLE KEYS */;

INSERT INTO `DepartmentAdmin` (`SecurityCode`, `DepartmentAdminID`)
VALUES
	(412341,444);

/*!40000 ALTER TABLE `DepartmentAdmin` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Doctor
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Doctor`;

CREATE TABLE `Doctor` (
  `DoctorID` int(10) unsigned NOT NULL,
  `Specialty` varchar(20) DEFAULT NULL,
  `MedicalLicense` varchar(20) NOT NULL,
  KEY `D_ID` (`DoctorID`),
  CONSTRAINT `D_ID` FOREIGN KEY (`DoctorID`) REFERENCES `employee` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Doctor` WRITE;
/*!40000 ALTER TABLE `Doctor` DISABLE KEYS */;

INSERT INTO `Doctor` (`DoctorID`, `Specialty`, `MedicalLicense`)
VALUES
	(222,'Dermatology','2323');

/*!40000 ALTER TABLE `Doctor` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Employee
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Employee`;

CREATE TABLE `Employee` (
  `EmployeeID` int(10) unsigned NOT NULL,
  `DepartmentID` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY (`EmployeeID`),
  CONSTRAINT `E_ID` FOREIGN KEY (`EmployeeID`) REFERENCES `person` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Employee` WRITE;
/*!40000 ALTER TABLE `Employee` DISABLE KEYS */;

INSERT INTO `Employee` (`EmployeeID`, `DepartmentID`)
VALUES
	(222,2),
	(333,3),
	(444,4),
	(12345,7);

/*!40000 ALTER TABLE `Employee` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Nurse
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Nurse`;

CREATE TABLE `Nurse` (
  `NurseID` int(10) unsigned NOT NULL,
  `Specialty` varchar(20) DEFAULT NULL,
  `MedicalLicense` varchar(20) NOT NULL,
  KEY `N_ID` (`NurseID`),
  CONSTRAINT `N_ID` FOREIGN KEY (`NurseID`) REFERENCES `employee` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Nurse` WRITE;
/*!40000 ALTER TABLE `Nurse` DISABLE KEYS */;

INSERT INTO `Nurse` (`NurseID`, `Specialty`, `MedicalLicense`)
VALUES
	(333,'Gastroenterology','321'),
	(12345,'Psychiatry','123');

/*!40000 ALTER TABLE `Nurse` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Patient
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Patient`;

CREATE TABLE `Patient` (
  `PatientID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Age` int(10) unsigned NOT NULL,
  `Weight` float unsigned NOT NULL,
  `Height` float unsigned NOT NULL,
  `SSN` char(9) DEFAULT NULL,
  `CreditCardNumber` varchar(20) NOT NULL DEFAULT '',
  `BillingAmount` int(10) unsigned DEFAULT NULL,
  `InsuranceNumber` int(10) unsigned NOT NULL,
  `MedicationList` varchar(20) DEFAULT NULL,
  `DoctorID` int(10) unsigned DEFAULT NULL,
  `NurseID` int(10) unsigned DEFAULT NULL,
  `AdminID` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`PatientID`),
  KEY `P_docID` (`DoctorID`),
  KEY `P_nurID` (`NurseID`),
  KEY `P_adminID` (`AdminID`),
  CONSTRAINT `P_ID` FOREIGN KEY (`PatientID`) REFERENCES `person` (`ID`),
  CONSTRAINT `P_adminID` FOREIGN KEY (`AdminID`) REFERENCES `departmentadmin` (`DepartmentAdminID`),
  CONSTRAINT `P_docID` FOREIGN KEY (`DoctorID`) REFERENCES `doctor` (`DoctorID`),
  CONSTRAINT `P_nurID` FOREIGN KEY (`NurseID`) REFERENCES `nurse` (`NurseID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Patient` WRITE;
/*!40000 ALTER TABLE `Patient` DISABLE KEYS */;

INSERT INTO `Patient` (`PatientID`, `Age`, `Weight`, `Height`, `SSN`, `CreditCardNumber`, `BillingAmount`, `InsuranceNumber`, `MedicationList`, `DoctorID`, `NurseID`, `AdminID`)
VALUES
	(111,100,150,1000,'121121212','1234567891234567',600,44,'N',222,333,444),
	(8765,23,20,5,'123232345','1111222233334444',200,2222,'none',222,333,444);

/*!40000 ALTER TABLE `Patient` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Person
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Person`;

CREATE TABLE `Person` (
  `ID` int(10) unsigned NOT NULL,
  `FirstName` varchar(20) NOT NULL,
  `LastName` varchar(20) NOT NULL,
  `PhoneNumber` char(10) NOT NULL,
  `EmailAddress` varchar(30) DEFAULT NULL,
  `Username` varchar(20) NOT NULL,
  `UserPassword` varchar(20) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`,`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Person` WRITE;
/*!40000 ALTER TABLE `Person` DISABLE KEYS */;

INSERT INTO `Person` (`ID`, `FirstName`, `LastName`, `PhoneNumber`, `EmailAddress`, `Username`, `UserPassword`)
VALUES
	(111,'Patient','P','2221222222','pat@gmail.com','pp','pp'),
	(222,'Doctor','D','2345678901','doctor@gmail.com','dd','dd'),
	(333,'Nurse','N','3456789012','nurse@gmail.com','nn','nn'),
	(444,'Admin','A','3456789012','admin@gmail.com','aa','aa'),
	(8765,'apple','juice','3121231234','apple@juice.com','applejuice','aj'),
	(12345,'one','two','1231231432','one@gmail.com','three','four');

/*!40000 ALTER TABLE `Person` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
