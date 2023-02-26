CREATE DATABASE Boardgames
Go
USE Boardgames
GO
--01
CREATE TABLE Categories(
	Id INT PRIMARY KEY IDENTITY,
	 [Name] VARCHAR(50) NOT NULL,
)

CREATE TABLE Addresses(
	Id INT PRIMARY KEY IDENTITY,
	StreetName NVARCHAR(100) NOT NULL,
	StreetNumber INT NOT NULL,
	Town VARCHAR(30) NOT NULL,
	Country VARCHAR(50) NOT NULL,
	ZIP INT NOT NULL
)

CREATE TABLE Publishers(
	Id INT PRIMARY KEY IDENTITY,
	[Name] VARCHAR(30) NOT NULL UNIQUE,
	AddressId INT FOREIGN KEY REFERENCES Addresses(Id) NOT NULL,
	Website NVARCHAR(40)  NULL,
	Phone NVARCHAR(20)  NULL
)

CREATE TABLE PlayersRanges(
	Id INT PRIMARY KEY IDENTITY,
	PlayersMin INT NOT NULL,
	PlayersMax INT NOT NULL
)
CREATE TABLE Boardgames(
	Id INT PRIMARY KEY IDENTITY,
	[Name] NVARCHAR(30) NOT NULL,
	YearPublished INT NOT NULL,
	Rating DECIMAL(8,2) NOT NULL,
	CategoryId INT FOREIGN KEY REFERENCES Categories(Id) NOT NULL,
	PublisherId INT FOREIGN KEY REFERENCES Publishers(Id) NOT NULL,
	PlayersRangeId INT FOREIGN KEY REFERENCES PlayersRanges(Id) NOT NULL
)
CREATE TABLE Creators(
	Id INT PRIMARY KEY IDENTITY, 
	FirstName NVARCHAR(30) NOT NULL,
	LastName NVARCHAR(30) NOT NULL,
	Email NVARCHAR(30) NOT NULL,
)

CREATE TABLE CreatorsBoardgames(
	 CreatorId INT FOREIGN KEY REFERENCES Creators(Id) NOT NULL,
	BoardgameId INT FOREIGN KEY REFERENCES Boardgames(Id) NOT NULL,
	PRIMARY KEY (CreatorId,BoardgameId)	
)

-- 02
INSERT INTO [dbo].Boardgames([Name],YearPublished,Rating,CategoryId,PublisherId,PlayersRangeId)
VALUES  ('Deep Blue',2019, 5.67, 1, 15, 7),
		('Paris',2016, 9.78, 7, 1, 5),
		('Catan: Starfarers',2021, 9.87, 7, 13, 6),
		('Bleeding Kansas',2020, 3.25, 3, 7, 4),
		('One Small Step',2019, 5.75, 5, 9, 2)
	
	   	  
INSERT INTO Publishers([Name], AddressId, Website, Phone)
VALUES  ('Agman Games',5 ,'www.agmangames.com','+16546135542'),		
		('Amethyst Games',7 ,'www.amethystgames.com','+15558889992'),
		('BattleBooks', 13,'www.battlebooks.com','+12345678907')


--03
UPDATE PlayersRanges
SET PlayersMax += 1
WHERE PlayersMax = 2 AND PlayersMin = 2


UPDATE Boardgames
SET [Name] += 'V2'
WHERE  YearPublished >= 2020

--04


DELETE FROM CreatorsBoardgames
WHERE BoardgameId IN (
SELECT Id FROM Boardgames
WHERE PublisherId = 1)

DELETE FROM Boardgames
WHERE PublisherId = 1

DELETE
FROM Publishers
WHERE AddressId = 5

DELETE 
Addresses
WHERE Id IN (SELECT Id FROM Addresses
						WHERE  LEFT(Town,1) = 'L')





--05
SELECT [Name], Rating FROM Boardgames
Order by YearPublished, [Name] desc
		

--06
 SELECT 
			b.Id,b.[Name],b.YearPublished,c.[Name]
 FROM Boardgames AS b
 JOIN Categories AS c
 ON b.CategoryId = c.Id
 WHERE c.[Name] in ('Strategy Games','Wargames')
 ORDER BY b.YearPublished DESC



-- 07
SELECT c.Id,
		CONCAT(c.FirstName,' ',LastName ) AS CreatorName,
		c.Email
from Creators As c
LEFT JOIN CreatorsBoardgames AS cb ON c.Id = cb.CreatorId
WHERE  CreatorId IS NULL
ORDER BY CreatorName


-- 08
SELECT TOP 5
		b.[Name],
		b.Rating,
		c.[Name]
FROM Boardgames AS b
JOIN PlayersRanges AS p ON b.PlayersRangeId = p.Id
JOIN Categories AS c ON c.Id = b.CategoryId
WHERE (b.[Name] LIKE '%a%' AND Rating > 7.00 ) OR (Rating > 7.50 AND (p.PlayersMin = 2 AND p.PlayersMax = 5))
ORDER BY b.[Name], Rating DESC

-- 09

SELECT 
	CONCAT(c.FirstName,' ', c.LastName) As FullName,
	c.Email,
	MAX(b.Rating) AS Rating
FROM Creators AS c
JOIN CreatorsBoardgames AS cb ON cb.CreatorId = c.Id
JOIN Boardgames AS b ON b.Id = cb.BoardgameId
WHERE c.Email LIKE '%com'
GROUP BY c.FirstName,c.LastName, c.Email
ORDER BY FullName

--	10
SELECT 
	c.LastName,
	CEILING(AVG(Rating)) AS AverageRating,
	p.[Name]
FROM Creators AS c
JOIN CreatorsBoardgames AS cb ON cb.CreatorId = c.Id
JOIN Boardgames AS b ON b.Id = cb.BoardgameId
JOIN Publishers AS p ON p.Id = b.PublisherId
WHERE p.[Name] = 'Stonemaier Games'
GROUP BY c.LastName, p.[Name]
ORDER BY AVG(Rating) DESC;


--11
GO

CREATE OR ALTER FUNCTION udf_CreatorWithBoardgames (@name NVARCHAR(30))
RETURNS INT AS	
	BEGIN 
		  DECLARE @result INT = 0
		  SET @result = (SELECT 
						COUNT(*)
					FROM Creators AS c
					JOIN CreatorsBoardgames AS cb ON cb.CreatorId = c.Id
					JOIN Boardgames AS b ON b.Id = cb.BoardgameId
					WHERE c.FirstName = @name)

			
				RETURN @result
	END
GO
SELECT dbo.udf_CreatorWithBoardgames('Bruno')



GO

-- 12
CREATE OR ALTER PROC usp_SearchByCategory(@category VARCHAR (30))
AS
	BEGIN
		SELECT 
				b.[Name],
				b.YearPublished,
				b.Rating,
				c.[Name] AS CategoryName,
				p.[Name] AS PublisherName,
				CONCAT(pr.PlayersMin,' ','people') AS MinPlayers,
				CONCAT(pr.PlayersMax,' ','people')  AS MaxPlayers
		FROM Boardgames AS b
		JOIN Categories AS c ON b.CategoryId = c.Id
		JOIN Publishers AS p ON p.Id = b.PublisherId
		JOIN PlayersRanges AS pr ON pr.Id = b.PlayersRangeId
		WHERE c.[Name] = @category
		ORDER BY PublisherName, b.YearPublished DESC
				
	END
GO
EXEC usp_SearchByCategory 'Wargames'
GO

SELECT 
		b.[Name],
		b.YearPublished,
		b.Rating,
		c.[Name] AS CategoryName,
		p.[Name] AS PublisherName,
		CONCAT(pr.PlayersMin,' ','people') AS MinPlayers,
		CONCAT(pr.PlayersMax,' ','people')  AS MaxPlayers
FROM Boardgames AS b
JOIN Categories AS c ON b.CategoryId = c.Id
JOIN Publishers AS p ON p.Id = b.PublisherId
JOIN PlayersRanges AS pr ON pr.Id = b.PlayersRangeId
WHERE c.[Name] = 'Wargames'
ORDER BY PublisherName, b.YearPublished DESC