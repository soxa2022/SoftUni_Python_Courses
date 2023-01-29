
CREATE DATABASE SoftUni
GO

USE SoftUni
-- •	Towns (Id, Name)
-- •	Addresses (Id, AddressText, TownId)
-- •	Departments (Id, Name)
-- •	Employees (Id, FirstName, MiddleName, LastName, JobTitle, DepartmentId, HireDate, Salary, AddressId)

CREATE TABLE Towns(
    Id INT NOT NULL PRIMARY KEY IDENTITY,
    [Name] NVARCHAR(50)
)

-- Addresses (Id, AddressText, TownId)
CREATE TABLE Addresses(
    Id INT NOT NULL PRIMARY KEY IDENTITY,
    AddressText NVARCHAR(50),
    TownId INT NOT NULL FOREIGN KEY REFERENCES Towns(Id)
)
CREATE TABLE Departments (
    Id INT NOT NULL PRIMARY KEY IDENTITY,
    [Name] NVARCHAR(50) NOT NULL
)
CREATE TABLE Employees(
    Id INT NOT NULL PRIMARY KEY IDENTITY,
    FirstName NVARCHAR(50) NOT NULL,
    MiddleName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    JobTitle NVARCHAR(50) NOT NULL ,
    DepartmentId INT NOT NULL FOREIGN KEY REFERENCES Departments(Id),
    HireDate DATE NOT NULL,
    Salary Decimal(12,2) NOT NULL,
    AddressId INT NOT NULL FOREIGN KEY REFERENCES Addresses(Id)
)

-- BACKUP DATABASE SoftUni
-- TO DISK = 'C:\Anton\softuni-backup.bak'; 



-- USE master
-- DROP DATABASE SoftUni
-- GO
-- RESTORE DATABASE SoftUni
-- FROM DISK = 'C:\Anton\softuni-backup.bak';

INSERT INTO Towns([Name])
    VALUES ('Sofia'), 
            ('Plovdiv'),
             ('Varna'),
             ('Burgas')

INSERT INTO Departments([Name])
    VALUES ('Engineering'), 
            ('Sales'),
             ('Marketing'),
             ('Software Development'),
             ('Quality Assurance')

INSERT INTO Addresses(AddressText,TownId)
    VALUES ('Str. 66',1),
            ('Str. 12',3),
            ('Str. 44',4),
            ('Str. 1',2),
            ('Str. 44',1)

-- (Id, FirstName, MiddleName, LastName, JobTitle, DepartmentId, HireDate, Salary, AddressId)
INSERT INTO Employees(FirstName,MiddleName,LastName,JobTitle,DepartmentId,HireDate,Salary,AddressId)
    VALUES ('Ivan', 'Ivanov','Ivanov','.NET Developer', 4,'2013-02-01', 3500.00,1),
            ('Petar', 'Petrov','Petrov', 'Senior Engineer',1 ,'2004-03-02', 4000.00,2),
            ('Maria', 'Petrova','Ivanova','Intern',4,'2016-08-28', 525.25,3),
            ('Georgi', 'Terziev','Ivanov','CEO',2,'2007-12-09', 3000.00,4),
            ('Peter', 'Pan','Pan',	'Intern', 4,'2016-08-28', 599.88,5)

-- SELECT * FROM Towns
-- ORDER BY [Name] 
-- SELECT * FROM Departments
-- ORDER By [Name]
-- SELECT * FROM Employees
-- ORDER BY Salary DESC

-- SELECT [Name] FROM Towns
-- ORDER BY [Name]
-- SELECT [Name] FROM Departments
-- ORDER BY [Name]
-- SELECT FirstName,LastName,JobTitle,Salary FROM Employees
-- ORDER by Salary DESC

-- UPDATE Employees
-- SET Salary = Salary * 1.10
-- SELECT Salary FROM Employees



-- UPDATE Payments
-- SET TaxRate = TaxRate * 0.97
-- SELECT TaxRate from Payments

USE Hotel
SELECT * FROM Occupancies
TRUNCATE TABLE Occupancies