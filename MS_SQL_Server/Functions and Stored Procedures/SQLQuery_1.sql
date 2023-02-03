USE SoftUni
GO

-- Problem 01

CREATE PROC usp_GetEmployeesSalaryAbove35000 AS
    SELECT 
         FirstName
        ,LastName
    FROM Employees
    WHERE Salary > 35000
EXEC dbo.usp_GetEmployeesSalaryAbove35000

-- Problem 02

GO
CREATE PROC usp_GetEmployeesSalaryAboveNumber(@Num DECIMAL(18,4))   AS
   
    SELECT 
          FirstName
          ,LastName
    FROM Employees
    WHERE Salary >= @Num
GO
EXEC dbo.usp_GetEmployeesSalaryAboveNumber 48100
--Problem 03
GO
CREATE PROCEDURE usp_GetTownsStartingWith(@String NVARCHAR(MAX)) AS
	SELECT
		  [Name]
	FROM Towns
	WHERE [Name] LIKE CONCAT(@String,'%')
GO

EXEC  usp_GetTownsStartingWith 'b'
GO
--Problem 04

CREATE OR ALTER PROC usp_GetEmployeesFromTown(@Town NVARCHAR(50)) AS
	
	SELECT 
		  e.FirstName
		  ,e.LastName		  
	FROM Employees AS e
	JOIN Addresses AS a 
	ON e.AddressID = a.AddressID
	JOIN Towns AS t
	ON t.TownID = a.TownID
	WHERE t.[Name] = @Town
GO

EXEC usp_GetEmployeesFromTown 'Sofia'
GO
--Problem 05
CREATE FUNCTION ufn_GetSalaryLevel(@salary DECIMAL(18,4)) 
RETURNS VARCHAR(20) AS
BEGIN
DECLARE @SalaryLevel VARCHAR(20)
IF @salary < 30000 
	BEGIN
	SET @SalaryLevel = 'Low'
	END
ELSE IF @salary BETWEEN 30000 AND 50000 
	BEGIN
	SET @SalaryLevel = 'Average'
	END
ELSE 
	BEGIN
	SET @SalaryLevel = 'High'
	END
RETURN @SalaryLevel
END;
GO

SELECT 
	Salary
	,dbo.ufn_GetSalaryLevel(Salary) AS [Salar Level]
FROM Employees
GO
--Problem 06
CREATE PROC usp_EmployeesBySalaryLevel(@level VARCHAR(10)) AS	
	SELECT 
		  FirstName,
		  LastName		  
	FROM Employees
	WHERE  dbo.ufn_GetSalaryLevel(Salary) =  @level
GO

EXEC usp_EmployeesBySalaryLevel 'high'
--Problem 07
GO

CREATE OR ALTER FUNCTION ufn_IsWordComprised(@setOfLetters VARCHAR(MAX), @word VARCHAR(MAX)) 
RETURNS BIT AS
BEGIN
DECLARE @position INT = 1
BEGIN
	WHILE @position <= LEN(@word)
	BEGIN
		IF CHARINDEX((SUBSTRING(@word, @position, 1)),@setOfLetters) != 0
			BEGIN						
			SET @position += 1
			
			END
		ELSE
			RETURN 0	
			
	END
END
RETURN 1
END

GO

--Problem 08
GO

GO
CREATE OR ALTER PROC usp_DeleteEmployeesFromDepartment (@departmentId INT) AS
BEGIN
		DECLARE @EmployeesForDelete TABLE (Id INT)
		INSERT INTO @EmployeesForDelete 
		SELECT 
			  EmployeeID 
		FROM Employees
		WHERE DepartmentID = @departmentId

		DELETE EmployeesProjects
		WHERE EmployeeID IN (SELECT * 
							 FROM  @EmployeesForDelete)

		ALTER TABLE Departments
		ALTER COLUMN ManagerId INT NULL

		UPDATE Departments
		SET ManagerID = NULL
		WHERE ManagerID IN (SELECT * 
							 FROM  @EmployeesForDelete)
		UPDATE Employees
		SET ManagerID = NULL
		WHERE ManagerID IN (SELECT * 
							 FROM  @EmployeesForDelete)
		
		DELETE 
		FROM Employees
		WHERE DepartmentID = @departmentId
		
		DELETE 
		FROM Departments
		WHERE DepartmentID = @departmentId

		SELECT 
			  COUNT(*)
		FROM Employees
		WHERE DepartmentID = @departmentId
		
END
GO

EXEC usp_DeleteEmployeesFromDepartment 7
	
GO

-- Problem 09
GO
USE BANK
GO
CREATE PROC usp_GetHoldersFullName 
AS	
	SELECT
		CONCAT(FirstName, ' ' ,LastName) AS [Full Name]
	FROM AccountHolders

GO
--Problem 10
GO
CREATE PROC usp_GetHoldersWithBalanceHigherThan @number DECIMAL (18,4) AS
	 SELECT
		    FirstName
		   ,LastName
	 FROM AccountHolders as ah
	 JOIN
		 (SELECT
				AccountHolderId
				,SUM(Balance) AS TotalBalance
		 FROM Accounts
		 GROUP BY AccountHolderId	 
		 ) AS a
	 ON ah.Id = a.AccountHolderId
	 WHERE a.TotalBalance > @number
	 ORDER BY ah.FirstName,ah.LastName
GO 
CREATE PROC usp_GetHoldersWithBalanceHigherThan @number DECIMAL (18,2) AS
	 SELECT
		   FirstName
		   ,LastName
	 FROM AccountHolders as ah
	 JOIN
	 (SELECT
			AccountHolderId
		    ,SUM(Balance) AS TotalBalance
	 FROM Accounts
	 GROUP BY AccountHolderId
	 HAVING SUM(Balance) > @number
	 ) AS a
	 ON ah.Id = a.AccountHolderId
	 ORDER BY ah.FirstName,ah.LastName
GO
EXEC  usp_GetHoldersWithBalanceHigherThan 10000
GO
--Problem 11
GO
CREATE OR ALTER FUNCTION ufn_CalculateFutureValue(@sum DECIMAL(18,4),@interestrate FLOAT, @years INT) 
RETURNS DECIMAL(18,4) AS
	BEGIN
	RETURN ROUND(@sum * (POWER((1 + @interestrate), @years)),4)
	END
GO
	SELECT dbo.ufn_CalculateFutureValue(1000,0.1,5)
--Problem 12
GO
CREATE OR ALTER PROC usp_CalculateFutureValueForAccount @acountid INT, @interestrate FLOAT AS

	BEGIN
			 SELECT 
					a.Id
				   ,ah.FirstName
				   ,ah.LastName
				   ,a.Balance AS [Current Balance]
				   ,dbo.ufn_CalculateFutureValue(a.Balance,@interestrate,5) AS [Balance in 5 years]
			 FROM Accounts AS a
			 JOIN AccountHolders AS ah
			 ON ah.id = a.AccountHolderId
			 WHERE a.Id = @acountid
	END
GO
EXEC usp_CalculateFutureValueForAccount 1, 0.1
GO
USE Diablo
--Problem 13
GO
CREATE OR ALTER FUNCTION ufn_CashInUsersGames(@gameName VARCHAR(20)) 
RETURNS TABLE AS
	RETURN 
			SELECT						
				   SUM(Cash) AS SumCash
			FROM
				(
				  SELECT 
					   g.[Name]
					  ,ug.Cash
					  ,ROW_NUMBER() OVER (ORDER BY ug.Cash DESC) AS RankCash
				 FROM UsersGames AS ug
				 JOIN Games as g
				 ON ug.GameId = g.Id
				 WHERE g.[Name] = @gameName
				 ) AS SubQuery
				 WHERE RankCash % 2 != 0			
	
GO
SELECT * FROM dbo.ufn_CashInUsersGames('Love in a mist')
GO

			