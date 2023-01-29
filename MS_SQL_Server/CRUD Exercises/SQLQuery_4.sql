CREATE DATABASE CarRental
GO
USE CarRental;
-- 	Categories (Id, CategoryName, DailyRate, WeeklyRate, MonthlyRate, WeekendRate)
-- 	Cars (Id, PlateNumber, Manufacturer, Model, CarYear, CategoryId, Doors, Picture, Condition, Available)
-- 	Employees (Id, FirstName, LastName, Title, Notes)
-- 	Customers (Id, DriverLicenceNumber, FullName, Address, City, ZIPCode, Notes)
--  RentalOrders (Id, EmployeeId, CustomerId, CarId, TankLevel, KilometrageStart, KilometrageEnd, TotalKilometrage, StartDate, EndDate, TotalDays, RateApplied, TaxRate, OrderStatus, Notes)



CREATE TABLE Categories(
    Id INT NOT NULL PRIMARY KEY IDENTITY,
    CategoryName NVARCHAR(50) NOT NULL,
    DailyRate TINYINT ,
    WeeklyRate TINYINT ,
    MontlyRate TINYINT ,
    WeekendRate TINYINT ,   
)

CREATE TABLE Cars(
    Id INT NOT NULL PRIMARY KEY IDENTITY,
    PlateNumber VARCHAR(20) NOT NULL UNIQUE,
    Manufacturer VARCHAR(50) NOT NULL,
    Model  VARCHAR(50) NOT NULL,
    CarYear SMALLINT NOT NULL,
    CategoryId INT NOT NULL FOREIGN KEY REFERENCES Categories(Id),
    Doors TINYINT NOT NULL,
    Picture VARBINARY(MAX),
    Condition VARCHAR(MAX),
    Available BIT NOT NULL DEFAULT 1
)
-- Id, FirstName, LastName, Title, Notes
CREATE TABLE Employees(
    Id INT NOT NULL PRIMARY KEY IDENTITY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Title VARCHAR(50),
    Notes VARCHAR(MAX)
)
-- Id, DriverLicenceNumber, FullName, Address, City, ZIPCode, Notes
CREATE TABLE Customers(
    Id INT NOT NULL PRIMARY KEY IDENTITY,
    DriverLicenceNumber BIGINT NOT NULL UNIQUE,
    FullName VARCHAR(50) NOT NULL,
    [Address] VARCHAR(50) NOT NULL,
    City VARCHAR(50) NOT NULL,
    ZIPCode SMALLINT ,    
    Notes VARCHAR(MAX)
)
-- (Id, EmployeeId, CustomerId, CarId, TankLevel, KilometrageStart, KilometrageEnd, TotalKilometrage, StartDate, EndDate, TotalDays, RateApplied, TaxRate, OrderStatus, Notes)
CREATE TABLE RentalOrders(
    Id INT NOT NULL PRIMARY KEY IDENTITY,
    CustomerId INT NOT NULL FOREIGN KEY REFERENCES Customers(Id),
    EmployeeId INT NOT NULL FOREIGN KEY REFERENCES Employees(Id),
    CarId INT NOT NULL FOREIGN KEY REFERENCES Cars(Id),
    TankLevel TINYINT ,
    KilometrageStart INT,
    KilometrageEnd INT,
    TotalKilometrage INT,
    StartDate DATE,
    EndDate DATE,
    TotalDays SMALLINT,
    RateApplied BIT DEFAULT 1,
    TaxRate DECIMAL(10,2) NOT NULL,
    OrderStatus VARCHAR(50) NOT NULL,
    Notes VARCHAR(MAX)
)

INSERT INTO Categories(CategoryName,DailyRate,WeeklyRate,MontlyRate,WeekendRate)
    VALUES ('TRUCK', 1, 1, 1, 2),
            ('SPORT', 2, 2, 3, 4),
            ('SEDAN', 4, 2, 4, 2)
            
-- PlateNumber, Manufacturer, Model, CarYear, CategoryId, Doors, Picture, Condition, Available
INSERT INTO Cars(PlateNumber,Manufacturer,Model,CarYear,CategoryId,Doors,Picture,Condition)
    VALUES ('CB8566BB', 'BMW', 'X5', 2015, 2, 5, NULL, 'Good'),
            ('CB6666AB', 'FORD', 'F50', 2019, 1, 4, NULL, 'Good'),
            ('CB0505HA', 'AUDI', 'A6', 2018, 3, 45, NULL, 'Good')
            
-- FirstName, LastName, Title, Notes
INSERT INTO Employees(FirstName,LastName,Title,Notes)
    VALUES ('Ivan','Ivanov', NULL,NULL),
            ('Peter','Petrov','Casher', NULL),
            ('Asen','Sokolov','Manager', NULL)

-- DriverLicenceNumber, FullName, Address, City, ZIPCode, Notes
INSERT INTO Customers(DriverLicenceNumber,FullName,[Address],City,ZIPCode,Notes)
    VALUES (1846541,'Peter Ivanov', 'Str. 66','Sofia',NULL,NULL),
            (1522216,'Ivan Petrov','Str. Summer', 'Sofia', NULL,NULL),
            (1742634,'Asen Sokolov','Str. Ami Bue', 'Sofia',NULL,NULL)

-- EmployeeId, CustomerId, CarId, TankLevel, KilometrageStart, KilometrageEnd, TotalKilometrage, StartDate, EndDate, TotalDays,  TaxRate, OrderStatus, Notes            
INSERT INTO RentalOrders(EmployeeId, CustomerId, CarId, TankLevel, KilometrageStart, KilometrageEnd, TotalKilometrage, StartDate, EndDate, TotalDays,  TaxRate, OrderStatus, Notes)
    VALUES (1, 1, 1, 80, 12000, 14500,2500,'2022-10-18','2022-10-21',3, 500,'Complete',NULL),
           (2, 2, 2, 70, 22000, 23500,1500,'2022-10-19','2022-10-21',2, 800,'Complete',NULL),
           (2, 2, 2, 65, 18000, 20700,2700,'2022-10-22','2022-10-25',3, 900,'Complete',NULL)   

