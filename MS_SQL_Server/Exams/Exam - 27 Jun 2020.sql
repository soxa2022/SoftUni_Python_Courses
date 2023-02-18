CREATE DATABASE WMS
GO
USE WMS
GO


--01
create table Clients(
	ClientId INT PRIMARY KEY IDENTITY,
	FirstName VARCHAR(50) NOT NULL,
	LastName VARCHAR(50) NOT NULL,
	Phone VARCHAR(12) CHECK(LEN(Phone) = 12) NOT NULL
)

create table Mechanics(
	MechanicId INT PRIMARY KEY IDENTITY,
	FirstName VARCHAR(50) NOT NULL,
	LastName VARCHAR(50) NOT NULL,
	[Address] VARCHAR(255) NOT NULL
)

create table Models(
	ModelId INT PRIMARY KEY IDENTITY,
	[Name] VARCHAR(50) Unique NOT NULL
) 


create table Jobs(
	JobId INT PRIMARY KEY IDENTITY,
	ModelId INT FOREIGN KEY REFERENCES Models(ModelId) NOT NULL,
	[Status] VARCHAR(11) CHECK([Status] IN ('Pending', 'In Progress','Finished')) DEFAULT 'Pending'  NOT NULL,
	ClientId INT FOREIGN KEY REFERENCES Clients(ClientId) NOT NULL,
	MechanicId INT FOREIGN KEY REFERENCES Mechanics(MechanicId),
	IssueDate DATE NOT NULL,
	FinishDate DATE
)



create table Orders(
	OrderId INT PRIMARY KEY IDENTITY,
	JobId INT Foreign key References Jobs(JobId) NOT NULL,
	IssueDate DATE ,
	Delivered BIT Default 0
)

create table Vendors(
	VendorId INT PRIMARY KEY IDENTITY,
	[Name] VARCHAR(50) NOT NULL UNIQUE
)

create table Parts(
	PartId INT PRIMARY KEY IDENTITY,
	SerialNumber  VARCHAR(50) UNIQUE NOT NULL,
	[Description] VARCHAR(255),
	Price Money CHECK (Price > 0 and Price <10000) NOT NULL,
	VendorId INT Foreign Key References Vendors(VendorId) NOT NULL,
	StockQty INT CHECK (StockQty >= 0) DEFAULT 0
)
create table OrderParts(
	OrderId INT Foreign Key References Orders(OrderId) NOT NULL,
	PartId INT Foreign Key References Parts(PartId) NOT NULL,
	Primary key (OrderId, PartId),
	Quantity INT NOT NULL CHECK (Quantity >= 1) Default 1
)

create table PartsNeeded(
	JobId INT Foreign Key References Jobs(JobId) NOT NULL,
	PartId INT Foreign Key References Parts(PartId) NOT NULL,
	Primary key (JobId, PartId),
	Quantity INT NOT NULL CHECK (Quantity >= 1) Default 1
)
--02
Insert into Clients(FirstName,LastName,Phone)
VALUES ('Teri',	'Ennaco'	,'570-889-5187'),
		('Merlyn',	'Lawler',	'201-588-7810'),
		('Georgene',	'Montezuma'	,'925-615-5185'),
		('Jettie',	'Mconnell',	'908-802-3564'),
		('Lemuel',	'Latzke'	,'631-748-6479'),
		('Melodie',	'Knipp',	'805-690-1682'),
		('Candida'	,'Corbley'	,'908-275-8357')
Insert into Parts(SerialNumber,[Description],Price,VendorId)
Values ('WP8182119',	'Door Boot Seal',	117.86	,2),
		('W10780048',	'Suspension Rod',	42.81,	1),
		('W10841140','Silicone Adhesive' ,	6.77	,4),
		('WPY055980',	'High Temperature Adhesive',13.94	,3)

--03
Update Jobs
SET MechanicId = (Select MechanicId from Mechanics
												Where FirstName = 'Ryan')
Where [Status] = 'Pending' 
Update Jobs
SET [Status] = 'In Progress'
Where [Status] = 'Pending' 

--04
Delete from OrderParts
Where OrderId = 19

Delete from Orders
Where OrderId = 19

--05
Select 
	CONCAT(m.FirstName,' ', m.LastName) AS Mechanic,
	j.[Status],
	j.IssueDate

from Jobs AS j
JOIN Mechanics AS m ON j.MechanicId = m.MechanicId
Order by j.MechanicId,j.IssueDate, j.JobId

--06
Select  
		CONCAT(c.FirstName,' ',c.LastName) AS Client,
		DATEDIFF(DAY,j.IssueDate,'2017-04-24') AS [Days going],
		j.[Status]
from Jobs AS j
join Clients as c 
ON j.ClientId = c.ClientId
WHERE j.[Status] <> 'Finished'
ORDER BY [Days going] DESC

--07
SELECT 
		CONCAT(m.FirstName,' ', m.LastName) AS Mechanic,
		AVG(DATEDIFF(DAY, j.IssueDate,j.FinishDate)) AS [Average Days]

FROM Mechanics AS m
JOIN Jobs AS j ON m.MechanicId = j.MechanicId 
Where j.FinishDate IS NOT NULL
GROUP BY m.FirstName,m.LastName, m.MechanicId
ORDER BY m.MechanicId

--08

SELECT
		CONCAT(FirstName, ' ',LastName) AS Available
FROM Mechanics 
WHERE MechanicId NOT IN (SELECT MechanicId FROM Jobs
WHERE FinishDate IS NULL AND MechanicId IS NOT NULL
GROUP BY MechanicId )
ORDER BY MechanicId

--09
SELECT 
	    j.JobId,
		ISNULL(SUM(op.Quantity * p.Price),0) AS Total
FROM Jobs AS j
LEFT JOIN Orders AS o ON j.JobId = o.JobId
LEFT JOIN OrderParts AS op ON op.OrderId = o.OrderId
LEFT JOIN Parts AS p ON p.PartId = op.PartId
WHERE [Status] = 'Finished'
GROUP BY j.JobId
ORDER BY Total DESC, j.JobId

--10

SELECT 
p.PartId,
p.Description, 
pn.Quantity AS [Required],
p.StockQty AS [In Stock],
IIF(o.Delivered = 0, op.Quantity, 0) AS Ordered
FROM Parts AS p
LEFT JOIN PartsNeeded AS pn
ON p.PartId = pn.PartId
LEFT JOIN OrderParts AS op
ON pn.PartId = op.PartId
LEFT JOIN Jobs AS j
ON pn.JobId = j.JobId
LEFT JOIN Orders AS o
ON j.JobId = o.JobId
WHERE j.Status <> 'Finished' AND 
p.StockQty + IIF(o.Delivered = 0, op.Quantity,0) < pn.Quantity 
ORDER BY p.PartId
--11

GO
CREATE OR ALTER PROC usp_PlaceOrder(@jobid int, @part_number varchar(50),@quantity int)
AS 
BEGIN
		DECLARE @is_finished varchar(30) ,@is_found int, @is_exist int
		SET @is_finished = (SELECT [Status] FROM Jobs Where JobId = @jobid)
		SET @is_found = (SELECT COUNT(JobId) FROM Jobs Where JobId = @jobid ) 
		SET @is_exist  = (SELECT COUNT(SerialNumber) FROM Parts Where SerialNumber = @part_number )
		
		IF @is_finished = 'Finished'			
			THROW 50011, 'This job is not active!', 1
			
		IF @quantity <= 0
			THROW 50012, 'Part quantity must be more than zero!', 1
				
		IF  @is_found = 0
			THROW 50013, 'Job not found!', 1
			
		IF  @is_exist = 0
			THROW 50014, 'Part not found!', 1
			
		
		SET @is_exist  = (SELECT COUNT(OrderId) FROM Orders WHERE JobId = @jobId AND IssueDate IS NULL)
		IF  @is_exist = 0
			INSERT INTO Orders(JobId,IssueDate,Delivered)
			Values (@jobid,NULL,0)
		
		DECLARE @partid int, @orderid int , @partqiantity int
		SET @partid = (SELECT PartId FROM Parts WHERE SerialNumber = @part_number)
		SET @orderid = (SELECT OrderId FROM Orders WHERE JobId = @jobid AND IssueDate IS NULL)
		SET @partqiantity = (SELECT Quantity FROM OrderParts WHERE PartId = @partid AND OrderId = @orderid)

		IF @partqiantity IS NULL
			INSERT INTO OrderParts(OrderId,PartId,Quantity)
			VALUES (@orderid,@partid,@quantity)

		
		ELSE 
			UPDATE OrderParts
			SET Quantity += @quantity
			WHERE PartId = @partid AND OrderId = @orderid
	
			
END

DECLARE @err_msg AS NVARCHAR(MAX);
BEGIN TRY
  EXEC usp_PlaceOrder 1, 'ZeroQuantity', 0
END TRY

BEGIN CATCH
  SET @err_msg = ERROR_MESSAGE();
  SELECT @err_msg
END CATCH
GO
-- 12
CREATE OR ALTER FUNCTION udf_GetCost(@jobsid int) 
RETURNS DECIMAL(18,2) AS
BEGIN
		DECLARE @result DECIMAL(18,2) = 0
		SET @result = (SELECT 
				ISNULL(SUM(p.Price  * op.Quantity),0)
				FROM  Jobs AS j
			    JOIN Orders AS o ON j.JobId = o.JobId
			    JOIN OrderParts AS op ON op.OrderId = o.OrderId
			    JOIN Parts AS p ON p.PartId = op.PartId
			    WHERE j.JobId = @jobsid)
		RETURN @result
END
GO
SELECT dbo.udf_GetCost(3)