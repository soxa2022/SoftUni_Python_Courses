CREATE DATABASE NationalTouristSitesOfBulgaria
GO
USE NationalTouristSitesOfBulgaria
GO

CREATE TABLE Categories(
	Id INT PRIMARY KEY IDENTITY,
	[Name] VARCHAR(50) NOT NULL
)

CREATE TABLE Locations(
	Id INT PRIMARY KEY IDENTITY,
	[Name] VARCHAR(50) NOT NULL,
	Municipality VARCHAR(50),
	Province VARCHAR(50)
)

CREATE TABLE Sites(
	Id INT PRIMARY KEY IDENTITY,
	[Name] VARCHAR(100) NOT NULL,
	LocationId INT NOT NULL FOREIGN KEY REFERENCES Locations(Id) ,
	CategoryId INT NOT NULL FOREIGN KEY REFERENCES Categories(Id) ,
	Establishment VARCHAR(15)
)
CREATE TABLE Tourists(
	Id INT PRIMARY KEY IDENTITY,
	[Name] VARCHAR(50) NOT NULL,
	Age INT NOT NULL CHECK(Age BETWEEN 0 AND 120),	
	PhoneNumber VARCHAR(20) NOT NULL,
	Nationality VARCHAR(30) NOT NULL,
	Reward VARCHAR(20) 
)
CREATE TABLE SitesTourists(
	TouristId INT FOREIGN KEY REFERENCES Tourists(Id) NOT NULL,
	SiteId INT FOREIGN KEY REFERENCES Sites(Id) NOT NULL,
	PRIMARY KEY (TouristId,SiteId)
)
CREATE TABLE BonusPrizes(
	Id INT PRIMARY KEY IDENTITY,
	[Name] VARCHAR(50) NOT NULL	
)
CREATE TABLE TouristsBonusPrizes(
	TouristId INT FOREIGN KEY REFERENCES Tourists(Id) NOT NULL,
	BonusPrizeId INT FOREIGN KEY REFERENCES BonusPrizes(Id) NOT NULL,
	PRIMARY KEY (TouristId,BonusPrizeId)
)
GO

INSERT INTO Tourists([Name],Age,PhoneNumber,Nationality,Reward)
VALUES ('Borislava Kazakova', 52, '+359896354244','Bulgaria',NULL),
	   ('Peter Bosh', 48, '+447911844141','Bulgaria',NULL),
	   ('Martin Smith', 29, '+353863818592','Ireland','Bronze badge'),
	   ('Svilen Dobrev', 49, '+359986584786','Bulgaria','Silver badge'),
	   ('Kremena Popova', 38, '+359893298604','Bulgaria',NULL)

INSERT INTO Sites([Name],LocationId,CategoryId,Establishment)
VALUES ('Ustra fortress',90, 7,'X'),
	   ('Karlanovo Pyramids',65, 7,NULL),
	   ('The Tomb of Tsar Sevt',63, 8,'V BC'),
	   ('Sinite Kamani Natural Park',17, 1, NULL),
	   ('St. Petka of Bulgaria – Rupite',92, 6,'1994')
GO
--03
UPDATE Sites
SET Establishment = '(not defined)'
WHERE Establishment IS NULL

--04
DELETE TouristsBonusPrizes
WHERE BonusPrizeId IN (SELECT Id FROM BonusPrizes
						WHERE [Name] = 'Sleeping bag')

DELETE BonusPrizes
WHERE [Name] = 'Sleeping bag'
--05
SELECT 
	  [Name]
	  ,Age
	  ,PhoneNumber
	  ,Nationality
FROM Tourists
ORDER BY Nationality,Age DESC ,[Name]
--06
SELECT 
	  s.[Name]
	  ,l.[Name]
	  ,s.Establishment
	  ,c.[Name]
FROM Sites AS s
JOIN Locations AS l 
ON s.LocationId = l.Id
JOIN Categories AS c
ON c.Id = s.CategoryId
ORDER BY c.[Name] DESC, l.[Name],s.[Name]
--07
SELECT	
		l.Province	   
	   ,l.Municipality
	   ,l.[Name] AS [Location]
	   ,s.CountOfSites
FROM Locations AS l
JOIN
	(SELECT 
		   LocationId
		   ,COUNT(LocationId) AS CountOfSites
	FROM Sites
	GROUP BY LocationId) AS s
ON s.LocationId = l.Id
WHERE l.Province = 'Sofia'
ORDER BY s.CountOfSites DESC, l.[Name]
--08
SELECT 
	  s.[Name] AS [Site]
	  ,l.[Name] AS [Location]
	  ,l.Municipality
	  ,l.Province
	  ,s.Establishment
FROM Sites AS s
JOIN Locations AS l
ON s.LocationId = l.Id
WHERE LEFT(s.[Name],1) NOT IN ('B','M','D' ) AND s.Establishment LIKE '%BC'
ORDER BY [Site]
--09
SELECT 
	  t.[Name]
	  ,t.Age
	  ,t.PhoneNumber
	  ,t.Nationality
	  ,ISNULL(bp.[Name],'(no bonus prize)') AS Reward
FROM Tourists AS t
LEFT JOIN TouristsBonusPrizes AS tbp
ON t.id = tbp.TouristId
LEFT JOIN BonusPrizes AS bp
ON tbp.BonusPrizeId = bp.Id
ORDER BY t.[Name]
--10
SELECT 
	   SUBSTRING(t.[Name], CHARINDEX(' ',t.[Name],1) + 1, LEN(t.[Name])) AS LastName
	  ,t.Nationality
	  ,t.Age
	  ,t.PhoneNumber	  
FROM Tourists AS t
JOIN SitesTourists AS st
ON st.TouristId = t.Id
JOIN Sites AS s
ON s.Id = st.SiteId
JOIN Categories AS c
ON c.Id = s.CategoryId
WHERE c.Name = 'History and archaeology'
GROUP BY t.[Name],t.Nationality,t.Age,t.PhoneNumber
ORDER BY LastName

--11
GO
CREATE FUNCTION udf_GetTouristsCountOnATouristSite (@Site VARCHAR(100))
RETURNS INT AS
	BEGIN 
	RETURN (SELECT 
			   COUNT(*) 
		FROM Tourists AS t
		JOIN SitesTourists AS st
		ON t.Id = st.TouristId
		JOIN Sites AS s
		ON s.Id = st.SiteId
		WHERE s.[Name] = @Site)
	END
GO

--12

CREATE OR ALTER PROC usp_AnnualRewardLottery(@TouristName VARCHAR(50)) AS
BEGIN
		SELECT 
			   t.[Name]
			   , CASE
					 WHEN COUNT(t.Id) >= 100 THEN 'Gold badge'
					 WHEN COUNT(t.Id) >= 50 THEN 'Silver badge'
					 WHEN COUNT(t.Id) >= 25 THEN 'Bronze badge'
					 ELSE NULL
				 END  AS  Reward
		FROM Tourists AS t
		JOIN SitesTourists AS st
		ON t.Id = st.TouristId
		WHERE t.[Name] = @TouristName
		GROUP BY t.[Name],t.Id
END
GO
			
		
