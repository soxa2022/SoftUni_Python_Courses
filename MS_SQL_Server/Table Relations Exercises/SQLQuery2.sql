CREATE TABLE [Manufacturers](
	ManufacturerID INT NOT NULL,
	[Name] VARCHAR(50) NOT NULL,
	EstablishedOn DATE NOT NULL
)

CREATE TABLE [Models](
	ModelID INT NOT NULL,
	[Name] VARCHAR(50) NOT NULL,
	ManufacturerID INT NOT NULL
	
)
INSERT INTO Manufacturers(ManufacturerID,[Name],EstablishedOn)
	VALUES (1,'BMW','07/03/1916'),
		   (2,'Tesla','01/01/2003'),
		   (3,'Lada','01/05/1966')
		   
INSERT INTO Models(ModelID,[Name],ManufacturerID) 
	VALUES (101,'X1',1),	
		   (102,'i6',1),
		   (103,'Model S',2),
		   (104,'Model X',2),
		   (105,'Model 3',2),
		   (106,'Nova',3)

ALTER TABLE Models
ADD CONSTRAINT PK_ModelID PRIMARY KEY(ModelID) 

ALTER TABLE Manufacturers
ADD CONSTRAINT PK_ManufacturerID PRIMARY KEY(ManufacturerID) 

ALTER TABLE Models
ADD CONSTRAINT FK_ManufacturersModel FOREIGN KEY(ManufacturerID)  REFERENCES Manufacturers(ManufacturerID)


--CREATE TABLE [Manufacturers](
--	ManufacturerID INT PRIMARY KEY IDENTITY,
--	[Name] VARCHAR(50) NOT NULL,
--	EstablishedOn DATE NOT NULL
--)

--CREATE TABLE [Models](
--	ModelID INT PRIMARY KEY IDENTITY(101,1),
--	[Name] VARCHAR(50) NOT NULL,
--	ManufacturerID INT NOT NULL FOREIGN KEY REFERENCES Manufacturers(ManufacturerID)
--)
--INSERT INTO Manufacturers([Name],EstablishedOn)
--	VALUES ('BMW','07/03/1916'),
--		   ('Tesla','01/01/2003'),
--		   ('Lada','01/05/1966')
		   
--INSERT INTO Models([Name],ManufacturerID)
--	VALUES ('X1',1),
--		   ('i6',1),
--		   ('Model S',2),
--		   ('Model X',2),
--		   ('Model 3',2),
--		   ('Nova',3)