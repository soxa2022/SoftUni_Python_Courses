create database [Service]
GO 
USE [Service] 
--01
create table Users(
		Id INT primary key identity,
		Username VARCHAR(30) unique NOT NULL,
		[Password] VARCHAR(50)  NOT NULL,
		[Name] VARCHAR(50) ,
		Birthdate DATETIME ,
		Age INT CHECK(Age between 14 and 110),
		Email VARCHAR(50)  NOT NULL		
)
create table Departments(
		Id INT primary key identity,
		[Name] VARCHAR(50) NOT NULL
)

create table Employees(
		Id INT primary key identity,
		FirstName VARCHAR(25),
		LastName VARCHAR(25),
		Birthdate DATETIME,
		Age INT CHECK(Age between 18 and 110),
		DepartmentId INT Foreign Key References Departments(Id)
)

create table Categories(
		Id INT primary key identity,
		[Name] VARCHAR(50) NOT NULL,
		DepartmentId INT Foreign Key References Departments(Id) NOT NULL
)

create table [Status](
		Id INT primary key identity,
		[Label] VARCHAR(20) NOT NULL
)
create table Reports(
		Id INT primary key identity,
		CategoryId INT Foreign Key References Categories(Id) NOT NULL,
		StatusId INT Foreign Key References [Status](Id) NOT NULL,
		OpenDate DATETIME NOT NULL,
		CloseDate DATETIME,
		[Description] VARCHAR(200) NOT NULL,
		UserId INT Foreign Key References [Users](Id) NOT NULL,
		EmployeeId INT Foreign Key References [Employees](Id) 
)
--02
insert into Employees(FirstName,LastName,Birthdate,DepartmentId)
values  ('Marlo','O''Malley', '1958-9-21', 1),
		('Niki','Stanaghan', '1969-11-26', 4),
		('Ayrton','Senna', '1960-03-21', 9),
		('Ronnie','Peterson', '1944-02-14', 9),
		('Giovanna','Amati', '1959-07-20', 5)

insert into Reports(CategoryId,StatusId,OpenDate,CloseDate,[Description],UserId,EmployeeId)
values	(1,1,'2017-04-13',NULL,'Stuck Road on Str.133',6,2),
		(6,3,'2015-09-05','2015-12-06','Charity trail running',3,5),
		(14,2,'2015-09-07',NULL,'Falling bricks on Str.58',5,2),
		(4,3,'2017-07-03','2017-07-06','Cut off streetlight on Str.11',1,1)


--03 
UPDATE Reports
SET CloseDate = Getdate()
WHERE CloseDate is null
--04

DELETE
from Reports
WHERE StatusId = 4
--05

SELECT 
	  [Description],
	  FORMAT(OpenDate,'dd-MM-yyyy') AS OpenDate
FROM Reports AS r
WHERE EmployeeId IS NULL
ORDER BY r.OpenDate,[Description]
--06

SELECT 
	 r.[Description]
	 ,c.[Name]
FROM Reports AS r
JOIN Categories AS c
ON r.CategoryId = c.Id
ORDER BY r.[Description],c.[Name]
--07
SELECT top 5
	c.[Name],
	COUNT(c.[Name]) AS ReportsNumber
FROM Reports AS r
JOIN Categories AS c
ON r.CategoryId = c.Id
GROUP BY c.[Name]
ORDER BY ReportsNumber Desc,c.[Name]
--08

SELECT 
	   u.Username,
	   c.[Name]
FROM Users AS u
JOIN Reports AS r
ON u.Id = r.UserId
JOIN Categories AS c
ON c.Id = r.CategoryId
WHERE FORMAT(u.Birthdate,'dd-MM') = FORMAT(r.OpenDate,'dd-MM')
ORDER BY u.Username, c.[Name]

--09
SELECT
		CONCAT(e.FirstName,' ', e.LastName) AS FullName
		,COUNT (u.Id) AS UsersCount
FROM Employees AS e
LEFT JOIN Reports AS r
ON r.EmployeeId = e.Id
LEFT JOIN Users AS u
ON u.Id = r.UserId
GROUP BY e.FirstName,e.LastName
ORDER BY UsersCount DESC ,FullName
--10
SELECT 
		 CONCAT(ISNULL(e.FirstName,'None'),' ', e.LastName) AS Employee
		,ISNULL(d.[Name],'None') AS Department
		,ISNULL(c.[Name],'None') As Category
		,ISNULL(r.[Description],'None') AS [Description]
		,IIF(r.OpenDate IS NULL, 'None', FORMAT(r.OpenDate,'dd.MM.yyyy')) AS OpenDate
		,ISNULL(s.[Label],'None') AS [Status]
		,ISNULL(u.[Name],'None') AS [User]
FROM Reports AS r
LEFT JOIN Employees AS e
ON r.EmployeeId = e.Id
LEFT JOIN Departments AS d
ON e.DepartmentId = d.Id
LEFT JOIN Users AS u
ON r.UserId = u.Id
LEFT JOIN Categories AS c
ON c.Id = r.CategoryId
LEFT JOIN [Status] AS s
ON s.Id = r.StatusId
ORDER BY e.FirstName DESC,e.LastName DESC, Department,Category,[Description],OpenDate, [Status],[User]
GO
CREATE OR ALTER FUNCTION udf_HoursToComplete(@StartDate DATETIME, @EndDate DATETIME)
RETURNS INT 
	AS
		BEGIN
			IF @StartDate IS NULL OR @EndDate IS NULL
				RETURN 0
		 
		 RETURN DATEDIFF(HOUR,@StartDate,@EndDate)
		END
	GO
SELECT dbo.udf_HoursToComplete(OpenDate, CloseDate) AS TotalHours
   FROM Reports
GO
CREATE OR ALTER PROC usp_AssignEmployeeToReport(@EmployeeId INT, @ReportId INT)
AS
	BEGIN
			IF (SELECT DepartmentId FROM Employees
			WHERE Id = @EmployeeId) = (SELECT c.DepartmentId
								FROM Reports AS r
								JOIN Categories AS c
								ON c.Id = r.CategoryId
								WHERE r.Id = @ReportId)
				BEGIN
				UPDATE Reports
				SET EmployeeId = @EmployeeId
				WHERE Id = @ReportId
				RETURN
				END

	RAISERROR ('Employee doesn''t belong to the appropriate department!', 16, 1) 
		
	END
GO
EXEC usp_AssignEmployeeToReport 30, 1
EXEC usp_AssignEmployeeToReport 17, 2
