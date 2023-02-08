CREATE DATABASE CigarShop
GO
USE CigarShop
GO
--01
CREATE TABLE Sizes(
	 Id INT PRIMARY KEY IDENTITY
	,Length INT NOT NULL CHECK(Length BETWEEN 10 AND 25)
	,RingRange DECIMAL(4,2) NOT NULL CHECK(RingRange BETWEEN 1.5 AND 7.5)
)

CREATE TABLE Tastes(
	 Id INT PRIMARY KEY IDENTITY
	,TasteType VARCHAR(20) NOT NULL
	,TasteStrength VARCHAR(15) NOT NULL
	,ImageURL NVARCHAR(100) NOT NULL
)

CREATE TABLE Brands(
	  Id INT PRIMARY KEY IDENTITY
	 ,BrandName VARCHAR(30) NOT NULL UNIQUE
	 ,BrandDescription VARCHAR(MAX)
)

CREATE TABLE Cigars(
	   Id INT PRIMARY KEY IDENTITY
	  ,CigarName VARCHAR(80) NOT NULL
	  ,BrandId INT NOT NULL FOREIGN KEY REFERENCES Brands(Id)
	  ,TastId INT NOT NULL FOREIGN KEY REFERENCES Tastes(Id)
	  ,SizeId INT NOT NULL FOREIGN KEY REFERENCES Sizes(Id)
	  ,PriceForSingleCigar DECIMAL(10,2) NOT NULL
	  ,ImageURL NVARCHAR(100) NOT NULL
)

CREATE TABLE Addresses(
	   Id INT PRIMARY KEY IDENTITY
	  ,Town VARCHAR(30) NOT NULL
	  ,Country NVARCHAR(30) NOT NULL
	  ,Streat NVARCHAR(100) NOT NULL
	  ,ZIP VARCHAR(20) NOT NULL
)

CREATE TABLE Clients(
	   Id INT PRIMARY KEY IDENTITY
	  ,FirstName NVARCHAR(30) NOT NULL
	  ,LastName NVARCHAR(30) NOT NULL
	  ,Email NVARCHAR(50) NOT NULL
	  ,AddressId INT NOT NULL FOREIGN KEY REFERENCES Addresses(Id)
)

CREATE TABLE ClientsCigars(
	   ClientId INT NOT NULL FOREIGN KEY REFERENCES Clients(Id)
	  ,CigarId INT NOT NULL FOREIGN KEY REFERENCES Cigars(Id)
	  ,PRIMARY KEY (ClientId,CigarID)
)
GO
--02
INSERT INTO Cigars(CigarName,BrandId,TastId,SizeId,PriceForSingleCigar,ImageURL)
VALUES ('COHIBA ROBUSTO', 9,1,5,15.50, 'cohiba-robusto-stick_18.jpg'),
	   ('COHIBA SIGLO I', 9,1,10,410.00, 'cohiba-siglo-i-stick_12.jpg'),
	   ('HOYO DE MONTERREY LE HOYO DU MAIRE',14,5,11,7.50, 'hoyo-du-maire-stick_17.jpg'),
	   ('HOYO DE MONTERREY LE HOYO DE SAN JUAN',14,4,15,32.00, 'hoyo-de-san-juan-stick_20.jpg'),
	   ('TRINIDAD COLONIALES',2,3,8,85.21, 'trinidad-coloniales-stick_30.jpg')

INSERT INTO Addresses(Town,Country,Streat,ZIP)
VALUES ('Sofia','Bulgaria', '18 Bul. Vasil levski', 1000),
	   ('Athens','Greece', '4342 McDonald Avenue', 10435),
	   ('Zagreb','Croatia', '4333 Lauren Drive', 10000)
	   
GO
--03
UPDATE Cigars
SET PriceForSingleCigar *= 1.20
WHERE TastId IN (SELECT Id FROM Tastes
					WHERE TasteType = 'Spicy')
UPDATE Brands
SET BrandDescription = 'New description'
WHERE BrandDescription IS NULL
GO

--04
DELETE 
FROM Clients
WHERE AddressId IN (SELECT Id FROM Addresses
					WHERE LEFT(Country,1) = 'C')

DELETE 
FROM Addresses
WHERE LEFT(Country,1) = 'C'

--05
SELECT
	CigarName,
	PriceForSingleCigar,
	ImageURL
FROM Cigars
ORDER BY PriceForSingleCigar,CigarName DESC
--06
SELECT 
	  c.Id,
	  c.CigarName,
	  c.PriceForSingleCigar,
	  t.TasteType,
	  t.TasteStrength
FROM Cigars AS c
JOIN Tastes AS t
ON c.TastId = t.Id
WHERE t.TasteType IN  ('Earthy','Woody')
ORDER BY PriceForSingleCigar DESC

--07
SELECT
	   c.Id
      ,CONCAT(c.FirstName,' ',c.LastName) AS ClientName
	  ,c.Email
FROM Clients AS c
LEFT JOIN ClientsCigars AS cc
ON c.Id = cc.ClientId
WHERE cc.CigarId is NULL
ORDER BY ClientName
--08
SELECT TOP 5
		 c.CigarName
		,c.PriceForSingleCigar
		,c.ImageURL
FROM Cigars AS c
JOIN Sizes AS s
ON c.SizeId = s.Id
WHERE s.[Length] >= 12 AND (c.CigarName LIKE '%ci%' OR c.PriceForSingleCigar > 50) AND s.RingRange > 2.55
ORDER BY c.CigarName, c.PriceForSingleCigar DESC
--09
SELECT  		
	  CONCAT(cs.FirstName,' ',cs.LastName) AS FullName
	 ,a.Country
	 ,a.ZIP
	 ,CONCAT('$',MAX(c.PriceForSingleCigar)) AS CigarPrice
FROM Cigars AS c
JOIN ClientsCigars AS cc
ON c.Id = cc.CigarId
JOIN Clients AS cs
ON cc.ClientId = cs.Id
JOIN Addresses AS a
ON a.Id = cs.AddressId
WHERE ISNUMERIC(a.ZIP) = 1
GROUP BY cs.FirstName,cs.LastName,a.Country,a.ZIP
ORDER BY FullName

--10
SELECT  		
	  cs.LastName
	  ,AVG(s.[Length]) AS CiagrLength
	  ,CEILING(AVG(s.RingRange)) AS CiagrRingRange
FROM Clients AS cs
JOIN ClientsCigars AS cc
ON cc.ClientId = cs.Id
JOIN Cigars AS c
ON c.Id = cc.CigarId
JOIN Sizes AS s
ON s.Id = c.SizeId
GROUP BY cs.LastName
ORDER BY CiagrLength DESC

--11
GO
CREATE OR ALTER FUNCTION udf_ClientWithCigars(@name NVARCHAR(30)) 
RETURNS INT AS
BEGIN
	RETURN
			(SELECT 
				COUNT(*)  
			FROM Cigars AS c
			JOIN ClientsCigars AS cc
			ON c.Id = cc.CigarId
			JOIN Clients AS cs
			ON cc.ClientId = cs.Id
			WHERE cs.FirstName = @name)
END 
GO

CREATE OR ALTER PROC usp_SearchByTaste(@taste VARCHAR(20))
AS
	BEGIN
		SELECT 
			   c.CigarName
			  ,CONCAT('$',c.PriceForSingleCigar) AS Price
			  ,t.TasteType
			  ,b.BrandName
			  ,CONCAT(s.[Length],' cm') AS CigarLength
			  ,CONCAT(s.[RingRange],' cm') AS CigarRingRange
		FROM Cigars AS c
		JOIN Tastes AS t
		ON c.TastId = t.Id
		JOIN Brands AS b
		ON b.Id = c.BrandId
		JOIN Sizes AS s
		ON s.Id = c.SizeId
		WHERE t.TasteType = @taste
		ORDER BY CigarLength, CigarRingRange DESC
	END
GO
EXEC usp_SearchByTaste 'Woody'

