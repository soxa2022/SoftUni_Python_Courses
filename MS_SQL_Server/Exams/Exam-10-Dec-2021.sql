CREATE DATABASE Airport
GO
USE Airport
GO


--01
CREATE TABLE Passengers(
	Id INT PRIMARY KEY IDENTITY,
	FullName VARCHAR(100) NOT NULL UNIQUE,
	Email VARCHAR(50) NOT NULL UNIQUE,
)

CREATE TABLE Pilots(
	Id INT PRIMARY KEY IDENTITY,
	FirstName VARCHAR(30) NOT NULL UNIQUE,
	LastName VARCHAR(30) NOT NULL UNIQUE,
	Age TINYINT NOT NULL CHECK(Age BETWEEN 21 AND 62),
	Rating FLOAT CHECK(Rating BETWEEN 0.0 AND 10.0)
)	

CREATE TABLE AircraftTypes(
	Id INT PRIMARY KEY IDENTITY,
	TypeName VARCHAR(30) NOT NULL UNIQUE
)

CREATE TABLE Aircraft(
	Id INT PRIMARY KEY IDENTITY,
	Manufacturer VARCHAR(25) NOT NULL,
	Model VARCHAR(30) NOT NULL,
	[Year] INT NOT NULL,
	FlightHours INT ,
	Condition CHAR(1) NOT NULL,
	TypeId INT NOT NULL FOREIGN KEY REFERENCES AircraftTypes(Id) 
)

CREATE TABLE PilotsAircraft(
	AircraftId INT NOT NULL FOREIGN KEY REFERENCES Aircraft(Id),
	PilotId INT NOT NULL FOREIGN KEY REFERENCES Pilots(Id),
	PRIMARY KEY (AircraftId, PilotId)
)

CREATE TABLE Airports(
	Id INT PRIMARY KEY IDENTITY,
	AirportName VARCHAR(70) NOT NULL UNIQUE,
	Country VARCHAR(100) NOT NULL UNIQUE,
)

CREATE TABLE FlightDestinations(
	Id INT PRIMARY KEY IDENTITY,
	AirportId INT NOT NULL FOREIGN KEY REFERENCES Airports(Id),
	[Start] DateTime NOT NULL,
	AircraftId INT NOT NULL FOREIGN KEY REFERENCES Aircraft(Id),
	PassengerId INT NOT NULL FOREIGN KEY REFERENCES Passengers(Id),
	TicketPrice DECIMAL(18,2) NOT NULL DEFAULT 15
)
--02
INSERT INTO Passengers(FullName,Email)
SELECT
	CONCAT_WS(' ',FirstName,LastName) AS FullName,
	CONCAT_WS('',FirstName,LastName,'@','gmail.com' ) AS Email
FROM Pilots
WHERE id BETWEEN 5 AND 15
--03
UPDATE Aircraft
SET Condition = 'A'
WHERE (Condition = 'B' OR Condition = 'C') 
		AND (FlightHours IS NULL OR FlightHours BETWEEN 0 AND 100) 
		AND ([Year] >= 2013)
--04
DELETE FlightDestinations
WHERE PassengerId IN (SELECT Id
FROM Passengers
WHERE LEN(FullName) BETWEEN 0 AND 10)

DELETE Passengers
WHERE LEN(FullName) BETWEEN 0 AND 10
--05
SELECT 
	  Manufacturer
	  ,Model
	  ,FlightHours
	  ,Condition
FROM Aircraft
ORDER BY FlightHours DESC
--06
SELECT	
	   p.FirstName
	  ,p.LastName
	  ,a.Manufacturer
	  ,a.Model
	  ,a.FlightHours
FROM Pilots AS p
JOIN PilotsAircraft AS pa
ON p.Id = pa.PilotId
JOIN Aircraft AS a
ON a.Id = pa.AircraftId
WHERE a.FlightHours IS NOT NULL AND a.FlightHours < 304
ORDER BY a.FlightHours DESC, p.FirstName

--07
SELECT TOP 20
	   fd.Id
	  ,fd.[Start]
	  ,p.FullName
	  ,a.AirportName
	  ,fd.TicketPrice
FROM FlightDestinations AS fd
JOIN Passengers AS p
ON p.Id = fd.PassengerId
JOIN Airports AS a
ON a.Id = fd.AirportId
WHERE DAY([Start]) % 2 = 0
ORDER BY fd.TicketPrice DESC,a.AirportName

--08
SELECT 
	 a.Id AS AircraftId
	 ,a.Manufacturer
	 ,a.FlightHours
	 ,fd.[Count] AS FlightDestinationsCount
	 ,fd.AvgPrice
FROM Aircraft AS a
JOIN
(SELECT 
	  AircraftId
	  ,COUNT(AircraftId) AS [Count]
	  ,ROUND(AVG(TicketPrice),2) AS AvgPrice
FROM FlightDestinations
GROUP BY AircraftId
HAVING COUNT(AircraftId) > 1) AS fd
ON a.Id = fd.AircraftId
ORDER BY fd.[Count] DESC,a.Id
--09
SELECT 
	  p.FullName 
	 ,fd.CountOfAircraft
	 ,fd.TotalPayed
FROM Passengers AS p
JOIN
(SELECT
	   PassengerId
	  ,COUNT(AircraftId) AS CountOfAircraft
	  ,SUM(TicketPrice) AS TotalPayed
FROM FlightDestinations
GROUP BY PassengerId
HAVING COUNT(AircraftId) > 1
) AS fd
ON fd.PassengerId = p.Id
WHERE SUBSTRING(p.FullName,2,1) = 'a'
ORDER BY p.FullName
--10
SELECT 
	  a.AirportName
	  ,fd.[Start] AS DayTime
	  ,fd.TicketPrice
	  ,p.FullName
	  ,ar.Manufacturer
	  ,ar.Model
FROM FlightDestinations AS fd
JOIN Passengers AS p
ON fd.PassengerId = p.Id
JOIN Airports as a
ON fd.AirportId = a.Id
JOIN Aircraft AS ar
ON ar.Id = fd.AircraftId
WHERE (DATEPART(Hour,[Start]) * 60 + DATEPART(MINUTE,[Start])) BETWEEN 360 AND 1200 
			AND fd.TicketPrice > 2500
ORDER BY ar.Model
GO
-- 11
CREATE OR ALTER FUNCTION udf_FlightDestinationsByEmail(@email varchar(50)) 
RETURNS INT AS
BEGIN 
	RETURN (SELECT 
				  COUNT(*)
			FROM Passengers AS p
			JOIN FlightDestinations AS fd
			ON p.Id = fd.PassengerId
			WHERE p.Email = @email)
END 
GO

--12
CREATE OR ALTER PROC usp_SearchByAirportName(@airportName VARCHAR(70))
AS
BEGIN
	 SELECT 
			 ap.AirportName
			,p.FullName
			, CASE 
				WHEN fd.TicketPrice BETWEEN 0 AND 400 THEN 'Low'
				WHEN fd.TicketPrice BETWEEN 401 AND 1500 THEN 'Medium'
				WHEN fd.TicketPrice > 1500 THEN 'High'			
			  END AS LevelOfTickerPrice		
			,a.Manufacturer
			,a.Condition
			,act.TypeName
	 FROM Passengers AS p
	 JOIN FlightDestinations AS fd
	 ON fd.PassengerId = p.id
	 JOIN Aircraft as a
	 ON a.Id = fd.AircraftId
	 JOIN Airports AS ap
	 ON fd.AirportId= ap.Id
	 JOIN AircraftTypes AS act
	 ON act.Id = a.TypeId
	 WHERE ap.AirportName = @airportName
	 ORDER BY a.Manufacturer, p.FullName
END
GO
EXEC usp_SearchByAirportName 'Sir Seretse Khama International Airport'