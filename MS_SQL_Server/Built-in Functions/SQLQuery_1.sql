USE SoftUni
GO

-- Problem 01
SELECT FirstName, LastName FROM Employees
WHERE LEFT(FirstName,2) = 'Sa'
-- WHERE FirstName LIKE 'Sa%'

-- Problem 02
SELECT FirstName,LastName FROM Employees
WHERE CHARINDEX('ei',LastName) > 0 
-- WHERE LastName LIKE '%ei%'

-- Problem 03
SELECT FirstName FROM Employees
WHERE DepartmentID IN (3,10 ) AND (YEAR(Hiredate) BETWEEN 1995 AND 2005)
-- WHERE (DepartmentID = 3 OR DepartmentID = 10 ) AND (YEAR(Hiredate) BETWEEN 1995 AND 2005)

-- Problem 04
SELECT FirstName,LastName FROM Employees
-- WHERE JobTitle NOT LIKE '%engineer%'
WHERE CHARINDEX('engineer',JobTitle) = 0 

-- Problem 05
SELECT [Name] FROM Towns
WHERE LEN([Name]) IN (5,6)
ORDER BY [Name]

-- Problem 06
SELECT * FROM Towns
-- WHERE [Name] 
-- LIKE 'M%' OR [Name]
-- LIKE 'K%' OR [Name] 
-- LIKE 'B%' OR [Name]
-- LIKE 'E%'
-- WHERE LEFT([Name],1) IN ('M','K','B','E')
WHERE [Name] LIKE '[MKBE]%'
ORDER BY [Name]

-- Problem 07
SELECT * FROM Towns
WHERE NOT ([Name] LIKE 'D%' OR [Name] LIKE 'R%' OR [Name] LIKE 'B%')
ORDER BY [Name]

-- Problem 08
GO
CREATE VIEW [V_EmployeesHiredAfter2000] AS
SELECT FirstName,LastName 
FROM Employees 
WHERE DATEPART(YEAR,HireDate) > 2000
GO

-- Problem 09
SELECT FirstName,LastName FROM Employees
WHERE LEN([LastName]) = 5

-- Problem 10
SELECT 
    EmployeeID
    ,FirstName
    ,LastName
    ,Salary
    ,DENSE_RANK() OVER (PARTITION BY Salary ORDER BY EmployeeID) AS Rank
FROM Employees
WHERE Salary BETWEEN 10000 AND 50000 
ORDER BY Salary DESC

-- Problem 11

SELECT * FROM (
		SELECT 
			EmployeeID
			,FirstName
			,LastName
			,Salary
			,DENSE_RANK() OVER (PARTITION BY Salary ORDER BY EmployeeID) AS [Rank]
		
		FROM Employees
		WHERE Salary BETWEEN 10000 AND 50000
		) AS RankingTABLE
WHERE [Rank] = 2
ORDER BY [Salary] DESC

-- Problem 12
USE [Geography]
GO
--SELECT CountryName,IsoCode FROM Countries
--WHERE `LOWER(CountryName) LIKE '%a%a%a%'
--ORDER BY IsoCode

SELECT 
		 CountryName AS [Country Name],
		 IsoCode AS [Iso Code]
	FROM Countries
WHERE LEN([CountryName]) - LEN(REPLACE(LOWER([CountryName]), 'a','')) >= 3
ORDER BY [Iso Code]

--Problem 13
SELECT p.[PeakName]
      ,r.[RiverName]
      ,LOWER(CONCAT(STUFF(p.PeakName,(LEN(p.PeakName)),1,NULL),r.[RiverName])) AS Mix
FROM
    Rivers AS r,
    Peaks AS p
WHERE RIGHT(p.[PeakName],1) = LEFT(r.[RiverName],1)
ORDER BY [Mix]
GO

USE Diablo
GO
-- Problem 14
SELECT TOP (50) 
     [Name]
    ,FORMAT([Start],'yyyy-MM-dd') AS [Start]
FROM [Games]
WHERE YEAR([Start]) BETWEEN 2011 AND 2012
ORDER BY [Start],[Name]

-- Problem 15
SELECT [Username]
       ,SUBSTRING([Email],CHARINDEX('@',[Email])+1,LEN([Email])) AS [Email Provider]
FROM [Users]
ORDER BY [Email Provider], [Username]

-- Problem 16
SELECT 
      [Username]
      ,[IpAddress] 
    
FROM [Users]
WHERE [IpAddress] LIKE '___.1%.%.___'
ORDER BY [Username]

-- Problem 17
SELECT 
      [Name] AS [Game]
      ,CASE
        WHEN DATEPART(HOUR,[Start]) >= 0 AND DATEPART(HOUR,[Start]) < 12 THEN 'Morning'
        WHEN DATEPART(HOUR,[Start]) >= 12 AND DATEPART(HOUR,[Start]) < 18 THEN 'Afternoon'
        ELSE 'Evening'
        END 
        AS [Part of the Day]
      ,CASE
        WHEN [Duration] <= 3 THEN 'Extra Short'
        WHEN [Duration] BETWEEN 4 AND 6 THEN 'Short'
        WHEN [Duration] > 6 THEN 'Long'
        ELSE 'Extra Long'
        END
        As [Duration]
FROM Games
ORDER BY [Game],[Duration]
GO
-- Problem 18
USE [Orders]
GO

SELECT 
      [ProductName]
      ,[OrderDate]
      ,DATEADD(Day,3,OrderDate) AS [Pay Due]
      ,DATEADD(Month,1,OrderDate) AS [Delivery Due]
FROM [Orders]