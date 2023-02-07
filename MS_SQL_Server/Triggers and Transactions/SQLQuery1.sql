USE Bank
GO
--Problem 1

CREATE TABLE Logs(
	LogId INT PRIMARY KEY IDENTITY,
	AccountID INT NOT NULL,
	OldSum DECIMAL(18,2) NOT NULL,
	NewSum DECIMAL(18,2) NOT NULL
	)

GO
CREATE OR ALTER TRIGGER tr_logs 
ON Accounts FOR UPDATE AS
	 INSERT INTO Logs(AccountID,OldSum,NewSum)
	 SELECT i.id,d.Balance,i.Balance
	 FROM inserted AS i
	 JOIN deleted as d
	 ON i.Id = d.Id
GO
UPDATE Accounts
SET Balance -= 100
WHERE Id IN (1,6,8)
SELECT * FROM Logs
GO
--Problem 02
CREATE TABLE NotificationEmails(
	Id INT PRIMARY KEY IDENTITY,
	Recipient INT NOT NULL,
	[Subject] VARCHAR(100) NOT NULL,
	[Body] VARCHAR(200) NOT NULL
	)
GO
CREATE OR ALTER TRIGGER tr_emails_logs
ON Accounts FOR UPDATE AS
	INSERT INTO NotificationEmails(Recipient, [Subject], Body)
	SELECT 
		  i.Id
		  , CONCAT('Balance change for account: ',i.Id)
		  ,CONCAT('On ',GETDATE(),' your balance was changed from ',d.Balance,' to ',i.Balance,'.')
	FROM inserted AS i
	JOIN deleted AS d
	ON i.Id = d.Id
GO
UPDATE Accounts
SET Balance += 100
WHERE Id IN (1,6,8)
SELECT * FROM NotificationEmails
GO

--Problem 03
GO

GO
CREATE OR ALTER PROC usp_DepositMoney(@accountId INT, @moneyamount DECIMAL(18,4))
AS 
BEGIN		
	 IF @moneyamount < 0 OR LEN(PARSENAME(@moneyamount,2)) > 4
		BEGIN		
			RETURN
		END
		
	 UPDATE Accounts
	 SET Balance+=@moneyamount
	 WHERE Id = @accountId	
END
GO
--Problem 04
CREATE OR ALTER PROC usp_WithdrawMoney  @accountId INT, @moneyamount DECIMAL(18,4)
AS 
BEGIN		
	 IF @moneyamount < 0 OR LEN(PARSENAME(@moneyamount,2)) > 4
		BEGIN		
			RETURN
		END
		
	 UPDATE Accounts
	 SET Balance-=@moneyamount
	 WHERE Id = @accountId	
END
GO

--Problem 05

CREATE OR ALTER PROC usp_TransferMoney (@senderId INT, @receiverId INT, @amount DECIMAL(18,4))
AS
BEGIN
	BEGIN TRANSACTION 
	UPDATE Accounts
	SET Balance -=@amount
	WHERE Id = @senderId
	UPDATE Accounts
	SET Balance +=@amount
	WHERE Id = @receiverId
	IF @amount < 0 OR LEN(PARSENAME(@amount,2)) > 4	
	BEGIN
		ROLLBACK
		RETURN
	END
	COMMIT
END
GO

EXEC usp_TransferMoney 1, 5 ,5000
GO
--Problem 07
USE Diablo
GO

BEGIN TRANSACTION

SELECT * FROM Users
WHERE Username = 'Stamat'

GO
USE SoftUni
GO
--Problem 07
CREATE OR ALTER PROC usp_AssignProject(@emloyeeId INT, @projectID INT) 
AS
BEGIN
	BEGIN TRANSACTION
	DECLARE @countproject INT = 0	 	
	INSERT INTO EmployeesProjects(EmployeeID,ProjectID)
	VALUES (@emloyeeId, @projectID)
	SET @countproject = (SELECT COUNT(*) FROM EmployeesProjects
						  WHERE EmployeeID = @emloyeeId)
	IF @countproject > 3
	BEGIN	
			
			ROLLBACK
			RAISERROR ('The employee has too many projects!', 16, 1)
			RETURN
	END

	COMMIT 
END
GO
EXEC usp_AssignProject 2 , 44
SELECT * FROM EmployeesProjects
GO
--Problem 09
CREATE TABLE Deleted_Employees(	   
	   EmployeeId INT PRIMARY KEY IDENTITY
	  ,FirstName VARCHAR(50) NOT NULL
	  ,LastName VARCHAR(50) NOT NULL
	  ,MiddleName VARCHAR(50) 
	  ,JobTitle VARCHAR(50) NOT NULL
	  ,DepartmentId INT NOT NULL
	  ,Salary Money NOT NULL
)
GO

CREATE OR ALTER TRIGGER tr_Deleted_Employees
ON Employees FOR DELETE
AS	
	INSERT INTO Deleted_Employees(FirstName,LastName,MiddleName,JobTitle,DepartmentId,Salary)
	SELECT 		   
		   FirstName
		  ,LastName
		  ,MiddleName
		  ,JobTitle
		  ,DepartmentID
		  ,Salary
	FROM deleted 
GO
