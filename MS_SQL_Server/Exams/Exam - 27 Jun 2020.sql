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
