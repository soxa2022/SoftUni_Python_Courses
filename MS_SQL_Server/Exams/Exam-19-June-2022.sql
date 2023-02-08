CREATE DATABASE  Zoo
Go
USE Zoo
GO

CREATE TABLE Owners(
	Id INT PRIMARY KEY IDENTITY,
	[Name] VARCHAR(50) NOT NULL,
	PhoneNumber VARCHAR(15) NOT NULL,
	[Address] VARCHAR(50)
)

CREATE TABLE AnimalTypes(
	Id INT PRIMARY KEY IDENTITY,
	AnimalType VARCHAR(30) NOT NULL,
)

CREATE TABLE Cages(
	Id INT PRIMARY KEY IDENTITY,
	AnimalTypeId INT FOREIGN KEY REFERENCES AnimalTypes(Id) NOT NULL,
)

CREATE TABLE Animals(
	Id INT PRIMARY KEY IDENTITY,
	[Name] VARCHAR(30) NOT NULL,
	BirthDate DATE NOT NULL,
	OwnerId INT FOREIGN KEY REFERENCES Owners(Id),
	AnimalTypeId INT FOREIGN KEY REFERENCES AnimalTypes(Id) NOT NULL
)
CREATE TABLE AnimalsCages(
	CageId INT FOREIGN KEY REFERENCES Cages(Id),
	AnimalId INT FOREIGN KEY REFERENCES Animals(Id)
	PRIMARY KEY (CageId,AnimalId)
)
CREATE TABLE VolunteersDepartments(
	Id INT PRIMARY KEY IDENTITY, 
	DepartmentName VARCHAR(30) NOT NULL
)

CREATE TABLE Volunteers(
	Id INT PRIMARY KEY IDENTITY,
	[Name] VARCHAR(50) NOT NULL,
	PhoneNumber VARCHAR(15) NOT NULL,
	[Address] VARCHAR(50),
	AnimalId INT FOREIGN KEY REFERENCES Animals(Id),
	DepartmentId INT FOREIGN KEY REFERENCES VolunteersDepartments(Id) NOT NULL
)

-- INSERT
INSERT INTO Volunteers([Name],PhoneNumber,[Address],AnimalId,DepartmentId)
VALUES  ('Anita Kostova','0896365412','Sofia, 5 Rosa str.',15,1),
		('Dimitur Stoev','0877564223',NULL ,42 ,4),
		('Kalina Evtimova','0896321112','Silistra, 21 Breza str.',9,7),
		('Stoyan Tomov','0898564100','Montana, 1 Bor str.',18,8),
		('Boryana Mileva','0888112233',NULL,31,5)

INSERT INTO Animals([Name],BirthDate,OwnerId,AnimalTypeId)
VALUES  ('Giraffe','2018-09-21',21,1),		
		('Harpy Eagle','2015-04-17',15,3),
		('Hamadryas Baboon','2017-11-02',NULL,1),
		('Tuatara','2021-06-30',2,4)

--UPDATE
UPDATE Animals
SET OwnerId = (SELECT Id FROM Owners
				WHERE [Name] = 'Kaloqn Stoqnov')
WHERE OwnerId IS NULL

--DELETE
DELETE Volunteers
WHERE DepartmentId = (SELECT DepartmentId FROM VolunteersDepartments
						WHERE DepartmentName = 'Education program assistant' )
DELETE VolunteersDepartments
WHERE DepartmentName = 'Education program assistant'
--Volunteers

SELECT 
		[Name]
		,PhoneNumber
		,[Address]
		,AnimalId
		,DepartmentId
FROM Volunteers
ORDER BY [Name],AnimalId,DepartmentId
--Animal Data
SELECT 
	  [Name]
	  ,ant.AnimalType
	  ,FORMAT(BirthDate,'dd.MM.yyyy') AS BirthDate
	  
FROM Animals AS a
JOIN AnimalTypes AS ant ON a.AnimalTypeId = ant.Id
ORDER BY [Name]

-- Owners and Their Animals 
SELECT TOP 5
	o.[Name]
	,oa.CountOfAnimals 
FROM (
	SELECT 
		  OwnerId,
		  COUNT(*) AS CountOfAnimals
	FROM Animals
	GROUP BY OwnerId
	) AS oa
JOIN Owners AS o ON oa.OwnerId = o.id
ORDER BY oa.CountOfAnimals DESC, o.[Name]
-- Owners, Animals and Cages
SELECT 
	  CONCAT_WS('-',o.[Name],sq.[Name]) AS OwnersAnimals
	  ,PhoneNumber
	  ,CageId
FROM Owners AS o
JOIN
(SELECT [Name], OwnerId, Id FROM Animals
WHERE AnimalTypeId IN (SELECT id FROM AnimalTypes
						WHERE AnimalType = 'Mammals') ) AS sq
ON o.Id = sq.OwnerId
JOIN AnimalsCages AS ac ON ac.AnimalId = sq.id
ORDER BY o.[Name],sq.[Name] DESC

-- Volunteers in Sofia

SELECT 
		[Name]
		,PhoneNumber
		,TRIM(SUBSTRING(TRIM([Address]),CHARINDEX('Sofia',[Address])+ LEN('Sofia')+1,LEN([Address]))) AS [Address]		  
FROM Volunteers
WHERE [Address] LIKE '%Sofia%' AND DepartmentID IN ( SELECT Id FROM VolunteersDepartments
													WHERE DepartmentName = 'Education program assistant'
													)
ORDER BY [Name]

--	Animals for Adoption
SELECT
	  a.[Name]
	  ,YEAR(a.BirthDate) AS BirthYear
	  ,ant.AnimalType
FROM Animals AS a
JOIN AnimalTypes AS ant 
ON ant.Id = a.AnimalTypeId
WHERE OwnerId IS NULL AND (YEAR('01/01/2022') - YEAR(BirthDate)) < 5 
     				  AND AnimalTypeId NOT IN (SELECT Id FROM AnimalTypes
     											WHERE AnimalType = 'Birds')
ORDER BY a.[Name]

--All Volunteers in Department
GO
CREATE OR ALTER FUNCTION udf_GetVolunteersCountFromADepartment (@VolunteersDepartment VARCHAR(50))
RETURNS INT AS	
	BEGIN
	RETURN
		 (SELECT COUNT(*)			
		 FROM Volunteers
		 AS v
		 JOIN VolunteersDepartments AS vd
		 ON v.DepartmentId = vd.Id
		 WHERE vd.DepartmentName = @VolunteersDepartment)
	END
GO
-- Animals with Owner or Not
CREATE OR ALTER PROC usp_AnimalsWithOwnersOrNot(@AnimalName VARCHAR (30))
AS
	BEGIN
		SELECT 
				a.[Name],
				IIF(o.[Name] IS NULL, 'For adoption',o.[Name]) AS OwnersName
		FROM Owners AS o
		RIGHT JOIN Animals AS a
		ON a.OwnerId = o.Id
		WHERE a.[Name] = @AnimalName
	END
GO
EXEC usp_AnimalsWithOwnersOrNot 'Pumpkinseed Sunfish'
EXEC usp_AnimalsWithOwnersOrNot 'Hippo'