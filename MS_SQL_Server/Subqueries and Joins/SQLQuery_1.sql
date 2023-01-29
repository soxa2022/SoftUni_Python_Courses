USE SoftUni
GO

-- Problem 01
SELECT TOP(5)
      [e].EmployeeID
      ,[e].JobTitle
      ,[e].AddressID
      ,[a].AddressText
FROM Employees AS [e]
JOIN Addresses AS [a] ON [e].[AddressID] = [a].[AddressID]
ORDER BY AddressID

-- Problem 02
SELECT TOP(50)
    [e].FirstName
    ,[e].LastName
    ,[t].[Name] AS [Town]
    ,[a].AddressText      
FROM Employees AS [e]
JOIN Addresses AS [a] ON [e].[AddressID] = [a].[AddressID]
JOIN Towns AS [t] ON [t].[TownID] = [a].[TownID]
ORDER BY [e].[FirstName],[e].[LastName]

--Problem 03
SELECT 
	  e.EmployeeID
	  ,e.FirstName
	  ,e.LastName
	  ,d.[Name] AS DepartmentName
FROM Employees AS e
--JOIN Departments AS d ON e.DepartmentID = d.DepartmentID AND d.[Name] = 'Sales'
JOIN Departments AS d ON e.DepartmentID = d.DepartmentID 
WHERE d.[Name] = 'Sales'
ORDER BY e.EmployeeID
GO
-- Problem 04
SELECT TOP 5
      e.EmployeeID
      ,e.FirstName
      ,e.Salary
      ,d.Name AS DepartmentName
FROM Employees AS e
JOIN Departments AS d ON e.DepartmentID = d.DepartmentID 
WHERE e.Salary > 15000
ORDER BY e.DepartmentID

-- Problem 05
SELECT TOP 3
        e.EmployeeID
        ,e.FirstName 
FROM Employees AS e
LEFT JOIN EmployeesProjects AS ep ON e.EmployeeID = ep.EmployeeID
WHERE ep.ProjectID IS NULL
ORDER BY e.EmployeeID

-- Problem 06
SELECT 
      e.FirstName
      ,e.LastName
      ,e.HireDate
      ,d.[Name] AS DeptName
FROM Employees as e
JOIN Departments as d ON (e.DepartmentID = d.DepartmentID 
                    AND e.HireDate > '1999-1-1' 
                    AND d.[Name] in ('Sales','Finance'))
-- WHERE e.HireDate > '1999-1-1' AND d.[Name] in ('Sales','Finance')
ORDER BY e.HireDate

-- Problem 07

SELECT TOP 5
      e.EmployeeID
      ,e.FirstName
      ,p.Name AS ProjectName
FROM Employees AS e
JOIN EmployeesProjects AS ep ON e.EmployeeID = ep.EmployeeID
JOIN Projects AS p ON ep.ProjectID = p.ProjectID
                     AND p.StartDate > '2002-08-13'
                     AND p.EndDate IS NULL
-- WHERE p.StartDate > '2002-08-13' AND p.EndDate IS NULL
ORDER BY e.EmployeeID

-- Problem 08
SELECT 
      e.EmployeeID
      ,e.FirstName
      ,IIF(YEAR(p.StartDate) >= 2005,NULL,p.[Name]) AS ProjectName
FROM Employees AS e
JOIN EmployeesProjects AS ep ON e.EmployeeID = ep.EmployeeID
JOIN Projects AS p ON ep.ProjectID = p.ProjectID
WHERE e.EmployeeID = 24

-- SELECT 
--       e.EmployeeID
--       ,e.FirstName
--       ,CASE
--        WHEN YEAR(p.StartDate) >= 2005 THEN NULL
--        ELSE p.[Name]
--        END
--        AS ProjectName
-- FROM Employees AS e
-- JOIN EmployeesProjects AS ep ON e.EmployeeID = ep.EmployeeID
-- JOIN Projects AS p ON ep.ProjectID = p.ProjectID
-- WHERE e.EmployeeID = 24

-- Problem 09
SELECT 
      e.EmployeeID
      ,e.FirstName
      ,e.ManagerID
      ,m.FirstName AS ManagerName
FROM Employees AS e
JOIN Employees AS m ON m.EmployeeID = e.ManagerID
WHERE e.ManagerID IN (3,7)
ORDER BY e.EmployeeID

-- Problem 10
SELECT TOP 50
       e.EmployeeID
       ,CONCAT_WS(' ',e.FirstName,e.LastName) AS EmployeeName
       ,CONCAT_WS(' ',m.FirstName,m.LastName) AS ManagerName
       ,d.Name AS DepartmentName       
FROM Employees AS e
JOIN Employees AS m ON m.EmployeeID = e.ManagerID
JOIN Departments AS d ON e.DepartmentID = d.DepartmentID
ORDER By e.EmployeeID

-- Problem 11
SELECT TOP 1 
    AVG(Salary) AS AVS
FROM Employees
GROUP BY DepartmentID
ORDER BY AVS 

SELECT MIN(MinAvgSalary.AVS) FROM
(
    SELECT 
    AVG(Salary) AS AVS
    FROM Employees
    GROUP BY DepartmentID
) 
AS MinAvgSalary
GO
USE [Geography]
GO
-- Problem 12
SELECT 
       mc.CountryCode
      ,m.MountainRange
      ,p.PeakName
      ,p.Elevation
FROM Peaks AS p
JOIN MountainsCountries AS mc ON p.MountainId = mc.MountainId
JOIN Countries AS c ON mc.CountryCode = c.CountryCode
JOIN Mountains AS m ON mc.MountainId = m.Id
WHERE p.Elevation > 2835 AND c.CountryName = 'Bulgaria'
ORDER BY p.Elevation DESC

-- Problem 13
SELECT 
	c.CountryCode
	,(SELECT COUNT(c.CountryCode) FROM Countries WHERE CountryCode = c.CountryCode) AS MountainRange
FROM Countries AS c
JOIN MountainsCountries AS mc ON c.CountryCode = mc.CountryCode
WHERE c.CountryName IN ('United States', 'Russia','Bulgaria')
GROUP BY c.CountryCode

-- Problem 13.1
SELECT 
	  CountryCode
	,COUNT(MountainId) AS MountainRange
FROM MountainsCountries
WHERE CountryCode IN 
(						SELECT CountryCode 
						FROM Countries 
						WHERE CountryName IN ('United States', 'Russia','Bulgaria')
		) 
GROUP BY CountryCode


-- Problem 14
SELECT TOP 5
		c.CountryName
		,r.RiverName 
 FROM Countries AS c
 LEFT JOIN CountriesRivers AS cr 
 ON c.CountryCode = cr.CountryCode
 LEFT JOIN Rivers AS r 
 ON r.Id = cr.RiverId
 JOIN Continents as co 
 ON co.ContinentCode = c.ContinentCode
 WHERE co.ContinentName = 'Africa'
 ORDER BY c.CountryName

-- Problem 15
SELECT ContinentCode
      ,CurrencyCode
      ,CurrencyUsage
FROM 
(SELECT 
      ContinentCode
      ,CurrencyCode
      ,COUNT(*) AS CurrencyUsage
      ,DENSE_RANK() OVER (PARTITION BY ContinentCode ORDER BY COUNT(*) DESC) AS Rank
     
FROM Countries AS c
GROUP BY CurrencyCode,ContinentCode) AS [Subquery]
WHERE CurrencyUsage > 1 AND Rank = 1
ORDER BY ContinentCode 






-- Problem 16
SELECT 
	COUNT(c.CountryName) AS [Count]
FROM Countries AS c
LEFT JOIN MountainsCountries AS mc ON mc.CountryCode = c.CountryCode
LEFT JOIN Mountains AS m ON m.Id = mc.MountainId
WHERE m.MountainRange IS NULL

-- Problem 17
SELECT TOP 5
	  c.CountryName 
	  ,MAX(p.Elevation) AS HighestPeakElevation 
	  ,MAX(r.Length) AS LongestRiverLength 
FROM Countries AS c
LEFT JOIN MountainsCountries AS mc
ON c.CountryCode = mc.CountryCode
LEFT JOIN Peaks AS p 
ON p.MountainId = mc.MountainId
LEFT JOIN CountriesRivers AS cr 
ON cr.CountryCode = c.CountryCode
LEFT JOIN Rivers AS r 
ON  r.Id = cr.RiverId
GROUP BY c.CountryName
ORDER BY HighestPeakElevation DESC ,LongestRiverLength DESC, c.CountryName 

-- Problem 18
SELECT TOP 5
      CountryName AS Country
      ,IIF(PeakName IS NULL,'(no highest peak)',PeakName) AS [Highest Peak Name]
      ,IIF(Elevation IS NULL, 0, Elevation) AS [Highest Peak Elevation]
      ,IIF(MountainRange IS NULL, '(no mountain)',MountainRange) AS Mountain
FROM
      (
      SELECT 
            c.CountryName
            ,p.PeakName
            ,p.Elevation
            ,m.MountainRange
            ,DENSE_RANK() OVER (PARTITION BY c.CountryName ORDER BY p.Elevation DESC) AS Rank
      FROM Countries AS c
      LEFT JOIN MountainsCountries AS mc
      ON c.CountryCode = mc.CountryCode
      LEFT JOIN Mountains AS m
      ON m.Id = mc.MountainId
      LEFT JOIN Peaks AS p
      ON p.MountainId = mc.MountainId            
      ) AS RankingSubquery
WHERE Rank = 1
ORDER BY CountryName,[Highest Peak Elevation]

