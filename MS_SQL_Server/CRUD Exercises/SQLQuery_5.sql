-- •	Employees (Id, FirstName, LastName, Title, Notes)
-- •	Customers (AccountNumber, FirstName, LastName, PhoneNumber, EmergencyName, EmergencyNumber, Notes)
-- •	RoomStatus (RoomStatus, Notes)
-- •	RoomTypes (RoomType, Notes)
-- •	BedTypes (BedType, Notes)
-- •	Rooms (RoomNumber, RoomType, BedType, Rate, RoomStatus, Notes)
-- •	Payments (Id, EmployeeId, PaymentDate, AccountNumber, FirstDateOccupied, LastDateOccupied, TotalDays, AmountCharged, TaxRate, TaxAmount, PaymentTotal, Notes)
-- •	Occupancies (Id, EmployeeId, DateOccupied, AccountNumber, RoomNumber, RateApplied, PhoneCharge, Notes)
CREATE DATABASE Hotel
GO

USE Hotel

CREATE TABLE Employees (
    Id INT NOT NULL PRIMARY KEY IDENTITY,
    FirstName NVARCHAR(30) NOT NULL,
    LastName  NVARCHAR(30) NOT NULL,
    Title  NVARCHAR(30),
    Notes NVARCHAR(MAX)
)

CREATE TABLE Customers(
    AccountNumber BIGINT NOT NULL PRIMARY KEY,
    FirstName NVARCHAR(30) NOT NULL,
    LastName  NVARCHAR(30) NOT NULL,
    PhoneNumber BIGINT NOT NULL,
    EmergencyName NVARCHAR(50),
    EmergencyNumber BIGINT ,
    Notes NVARCHAR(MAX)

)

CREATE TABLE RoomStatus(
    RoomStatus NVARCHAR(30) NOT NULL PRIMARY KEY,
    Notes NVARCHAR(MAX)
)
CREATE TABLE RoomTypes(
    RoomType NVARCHAR(30) NOT NULL PRIMARY KEY,
    Notes NVARCHAR(MAX)
)
CREATE TABLE BedTypes(
    BedType NVARCHAR(30) NOT NULL PRIMARY KEY,
    Notes NVARCHAR(MAX)
)
-- Rooms (RoomNumber, RoomType, BedType, Rate, RoomStatus, Notes)
CREATE TABLE Rooms(
    RoomNumber SMALLINT NOT NULL PRIMARY KEY,
    RoomType NVARCHAR(30) NOT NULL,
    BedType NVARCHAR(30) NOT NULL,
    Rate TINYINT ,
    RoomStatus NVARCHAR(30) NOT NULL,    
    Notes NVARCHAR(MAX)
)

-- Payments (Id, EmployeeId, PaymentDate, AccountNumber, FirstDateOccupied, LastDateOccupied, TotalDays, AmountCharged, TaxRate, TaxAmount, PaymentTotal, Notes)
CREATE TABLE Payments(
    Id BIGINT NOT NULL PRIMARY KEY IDENTITY,
    EmployeeId INT FOREIGN KEY REFERENCES Employees(Id),
    PaymentDate DATE NOT NULL,   
    AccountNumber BIGINT FOREIGN KEY REFERENCES Customers(AccountNumber),
    FirstDateOccupied DATE NOT NULL,
    LastDateOccupied DATE NOT NULL,
    TotalDays SMALLINT NOT NULL,
    AmountCharged DECIMAL(10,2) NOT NULL,
    TaxRate DECIMAL(10,2) NOT NULL,
    TaxAmount DECIMAL(10,2) NOT NULL,
    PaymentTotal DECIMAL(10,2) NOT NULL,
    Notes NVARCHAR(MAX)
)

-- Occupancies (Id, EmployeeId, DateOccupied, AccountNumber, RoomNumber, RateApplied, PhoneCharge, Notes)
CREATE TABLE Occupancies(
    Id INT NOT NULL PRIMARY KEY IDENTITY,
    EmployeeId INT NOT NULL FOREIGN KEY REFERENCES Employees(Id),
    DateOccupied DATE NOT NULL,    
    AccountNumber BIGINT NOT NULL FOREIGN KEY REFERENCES Customers(AccountNumber),
    RoomNumber SMALLINT NOT NULL FOREIGN KEY REFERENCES Rooms(RoomNumber),
    RateApplied TINYINT,
    PhoneCharge BIT DEFAULT 0,   
    Notes NVARCHAR(MAX)
)
-- (Id, FirstName, LastName, Title, Notes)
INSERT INTO Employees(FirstName, LastName, Title, Notes)
    VALUES  ('Ivan', 'Ivanov','Manager',NULL),
            ('Peter', 'Petrov','Bartender',NULL),
            ('Георги', 'Георгиев', NULL ,NULL)

-- AccountNumber, FirstName, LastName, PhoneNumber, EmergencyName, EmergencyNumber, Notes
INSERT INTO Customers
    VALUES  (123456,'Ivan', 'Ivanov',085477852,NULL,NULL,NULL),
            (233665,'Peter', 'Petrov',02564848,NULL,NULL,NULL),
            (852147,'Георги', 'Георгиев',0878521356,'Todor', 02547852 ,NULL)

INSERT INTO RoomStatus
    VALUES  ('Avalable',NULL),
            ('Not Avalable',NULL),
            ('Closed',NULL)

INSERT INTO RoomTypes
    VALUES  ('Couple',NULL),
            ('Studio',NULL),
            ('Apartment',NULL)

INSERT INTO BedTypes
    VALUES  ('Standart',NULL),
            ('Big',NULL),
            ('Double',NULL)

INSERT INTO Rooms
    VALUES (43, 'Couple', 'Standart', 3, 'Available', NULL),
           (142, 'Studio', 'Big', 4, 'Available', NULL),
           (233, 'Apartment', 'Double', 5, 'Available', NULL)


INSERT INTO Payments(EmployeeId, PaymentDate, AccountNumber, FirstDateOccupied, LastDateOccupied, TotalDays, AmountCharged, TaxRate, TaxAmount, PaymentTotal, Notes)
    VALUES (1,'2022-10-10',123456,'2022-10-8','2022-10-10',2, 200,50,150,400,NULL),
            (2,'2022-10-12',233665,'2022-10-15','2022-10-10',3, 300,50,300,600,NULL),
            (3,'2022-10-12',852147,'2022-10-15','2022-10-10',3, 400,100,300,800,NULL)

--  (EmployeeId, DateOccupied, AccountNumber, RoomNumber, RateApplied, PhoneCharge, Notes)
INSERT INTO Occupancies(EmployeeId, DateOccupied, AccountNumber, RoomNumber, RateApplied, Notes) 
    VALUES (1,'2022-10-8',123456,43, 2, NULL),
           (2,'2022-10-10',233665,142, 2, NULL),
           (3,'2022-10-10',852147,233,2, NULL)          

