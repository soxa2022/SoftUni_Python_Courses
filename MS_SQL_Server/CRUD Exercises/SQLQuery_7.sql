USE SoftUni
GO
-- SELECT * FROM Departments
-- SELECT [Name] FROM Departments
-- SELECT FirstName,LastName,Salary FROM Employees
-- SELECT FirstName,MiddleName,LastName FROM Employees
-- SELECT FirstName + '.'+ LastName+ '@softuni.bg' AS 'Full Email Address'
-- FROM Employees
-- SELECT DISTINCT Salary FROM Employees
-- SELECT * FROM Employees
-- WHERE Jobtitle = 'Sales Representative'
-- SELECT FirstName,LastName,JobTitle FROM Employees
-- WHERE Salary>= 20000 and Salary <= 30000
-- SELECT FirstName,LastName,JobTitle FROM Employees
-- WHERE Salary BETWEEN 20000 and 30000
-- SELECT FirstName +' '+ MiddleName +' '+ LastName AS 'Full Name' 
-- FROM Employees
-- WHERE Salary IN (25000, 14000, 12500,23600)
-- SELECT FirstName, LastName FROM Employees
-- WHERE ManagerID is NULL
-- SELECT TOP(5) FirstName,LastName FROM Employees
-- ORDER BY Salary DESC
-- SELECT FirstName, LastName FROM Employees
-- WHERE NOT DepartmentID <> 4
-- SELECT FirstName, LastName FROM Employees
-- WHERE NOT DepartmentID = 4
-- SELECT * FROM Employees
-- ORDER BY Salary DESC,FirstName,LastName DESC,MiddleName
-- CREATE VIEW V_EmployeesSalaries AS 
-- SELECT FirstName,LastName,Salary FROM Employees
-- CREATE VIEW V_EmployeeNameJobTitle AS
-- SELECT FirstName +' '+ IIF(MiddleName is NULL,'',MiddleName) + ' ' + LastName AS 'Full Name',JobTitle
-- FROM Employees
-- SELECT DISTINCT Jobtitle FROM Employees
-- SELECT TOP(10) * FROM Projects
-- ORDER BY StartDate ,[Name]
-- SELECT TOP(7) FirstName, LastName, HireDate FROM Employees
-- ORDER BY HireDate DESC
-- BEGIN TRANSACTION
-- UPDATE Employees
-- SET Salary = Salary * 1.12
-- WHERE DepartmentID IN (1, 2,4, 11)
-- SELECT Salary FROM Employees
-- -- UPDATE Employees
-- -- SET Salary = Salary / 1.12
-- -- WHERE DepartmentID IN (1, 2,4, 11)
-- ROLLBACK TRANSACTION
USE GEOGRAPHY
GO

-- SELECT PeakName FROM Peaks
-- ORDER BY PeakName
-- SELECT TOP(30) CountryName,[Population] FROM Countries
-- WHERE ContinentCode = 'EU'
-- ORDER BY [Population] DESC, CountryName

SELECT CountryName,CountryCode,
CASE
    WHEN CurrencyCode = 'EUR' THEN 'Euro'
    ELSE 'Not Euro'
END AS Currency
FROM Countries
ORDER BY CountryName


-- USE Diablo
-- GO

-- SELECT [Name] FROM Characters
-- ORDER BY [Name]