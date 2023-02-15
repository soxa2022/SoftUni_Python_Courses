USE DIABLO
GO
--01
SELECT 
	  s.[Email Provider]
	  ,COUNT([Email Provider]) AS [Number Of Users]
FROM
		(SELECT
			 Substring(Email,CHARINDEX('@',Email,1)+1,len(Email)) AS [Email Provider]
		FROM Users) AS s
GROUP BY s.[Email Provider]
ORDER BY [Number Of Users] desc, s.[Email Provider];

--02
SELECT 
	    g.[Name]
	   ,gt.[Name]
	   ,u.Username
	   ,ug.[Level]
	   ,ug.Cash
	   ,c.[Name]
FROM Users AS u
JOIN UsersGames AS ug
ON u.Id = ug.UserId
JOIN Games AS g
ON g.Id = ug.GameId
JOIN GameTypes AS gt
ON gt.Id = g.GameTypeId
JOIN Characters AS c
ON c.Id = ug.CharacterId
ORDER BY ug.[Level] DESC, u.Username, g.[Name];
--03
SELECT 
	   u.Username
	   ,g.[Name]
	   ,COUNT(i.Id) AS [Items Count]
	   ,SUM(i.Price) AS [Items Price]
FROM Users AS u
JOIN UsersGames AS ug
ON u.Id = ug.UserId
JOIN Games AS g
ON g.Id = ug.GameId
JOIN UserGameItems AS ugi
ON ug.Id = ugi.UserGameId
JOIN Items AS i
ON i.Id = ugi.ItemId
GROUP BY u.Username,g.[Name]
HAVING COUNT(i.Id) >= 10
ORDER BY [Items Count] DESC, [Items Price] DESC, u.Username;

--04

SELECT 
		u.Username, 
		g.[Name] as Game, 
		MAX(ch.[Name]) as [Character],
		SUM(s.Strength) + MAX(bs.Strength) + MAX(chs.Strength) as Strength,
		SUM(s.Defence) + MAX(bs.Defence) + MAX(chs.Defence) as Defence,
		SUM(s.Speed) + MAX(bs.Speed) + MAX(chs.Speed) as Speed,
		SUM(s.Mind) + MAX(bs.Mind) + MAX(chs.Mind) as Mind,
		SUM(s.Luck) + MAX(bs.Luck) + MAX(chs.Luck) as luck
	FROM Users AS u
		JOIN UsersGames ug ON u.id = ug.UserId
		JOIN Games g ON ug.GameId = g.Id
		JOIN GameTypes gt ON g.GameTypeId = gt.Id
		JOIN UserGameItems ugi ON ug.Id = ugi.UserGameId
		JOIN items i ON ugi.ItemId = i.Id
		JOIN [Statistics] s ON i.StatisticId = s.Id
		JOIN [Statistics] bs ON gt.BonusStatsId = bs.Id
		JOIN Characters ch ON ug.CharacterId = ch.Id
		JOIN [Statistics] chs ON ch.StatisticId = chs.Id
	GROUP BY u.Username, g.[Name]
	ORDER BY Strength DESC, Defence DESC, Speed DESC, Mind DESC, Luck DESC

GO


--05
SELECT 
		 [Name]
		,Price
		,MinLevel
		,Strength
		,Defence
		,Speed
		,Luck
		,Mind
FROM Items AS i
JOIN [Statistics] AS s ON s.Id = i.StatisticId
WHERE s.Mind > (SELECT AVG(Mind)  FROM [Statistics])					 
                AND s.Luck > (SELECT AVG(Luck) FROM [Statistics]) 
				AND s.Speed > (SELECT AVG(Speed)  FROM [Statistics])
ORDER BY [Name];

--06
SELECT 
		 i.[Name] AS Item
		,i.Price
		,i.MinLevel
		,gt.[Name] AS [Forbidden Game Type]
FROM Items AS i
LEFT JOIN GameTypeForbiddenItems AS gti ON i.Id = gti.ItemId
LEFT JOIN GameTypes AS gt ON gt.Id = gti.GameTypeId
ORDER BY gt.[Name] DESC, i.[Name]
Use Diablo
GO

--07
GO
WIth new_cte (itemsids,usersIDs) AS 
		(SELECT * from
		(SELECT id AS itemsids FROM Items 
			WHERE [Name] in ('Blackguard', 'Bottomless Potion of Amplification', 'Eye of Etlich (Diablo III)', 'Gem of Efficacious Toxin', 'Golden Gorget of Leoric','Hellfire Amulet')) AS A,
		(SELECT id AS usersIDs FROM UsersGames 
			WHERE UserId = (select id from Users WHERE Username = 'Alex') AND GameId =(select id from Games WHERE [Name] = 'Edinburgh')) AS B)
		
INSERT INTO UserGameItems
SELECT * from new_cte
		
UPDATE UsersGames
SET Cash -= (SELECT SUM(Price) FROM Items
				WHERE [Name] in ('Blackguard', 'Bottomless Potion of Amplification', 'Eye of Etlich (Diablo III)', 'Gem of Efficacious Toxin', 'Golden Gorget of Leoric','Hellfire Amulet'))
WHERE UserId = (select id from Users WHERE Username = 'Alex') AND GameId =(select id from Games WHERE [Name] = 'Edinburgh')

SELECT	
	   u.Username,
	   g.[Name],
	   ug.Cash,
	   i.[Name]
FROM Games AS g
JOIN UsersGames AS ug ON g.Id = ug.GameId
JOIN Users AS u ON u.Id = ug.UserId
JOIN UserGameItems AS ugi ON ugi.UserGameId = ug.Id
JOIN Items AS i ON i.Id = ugi.ItemId
WHERE g.[Name] = 'Edinburgh'
Order BY i.[Name]
GO
--08
USE Geography
GO
SELECT 
	  p.PeakName,
	  m.MountainRange AS Mountain,
	  p.Elevation
FROM Mountains AS m
JOIN Peaks AS p ON p.MountainId = m.Id
ORDER BY p.Elevation DESC, p.PeakName

-- 09
SELECT 
	  p.PeakName,
	  m.MountainRange AS Mountain,
	  c.CountryName,
	  co.ContinentName
FROM Mountains AS m
JOIN Peaks AS p ON p.MountainId = m.Id
JOIN MountainsCountries AS mc ON mc.MountainId = m.Id
JOIN Countries AS c ON c.CountryCode = mc.CountryCode
JOIN Continents AS co ON co.ContinentCode = c.ContinentCode
ORDER BY  p.PeakName , c.CountryName

--10
SELECT 
	  c.CountryName,
	  co.ContinentName,
	  COUNT(r.RiverName) AS RiversCount,
	  COALESCE(SUM(r.[Length]),0) AS TotalLength
--	  ISNULL(SUM(r.[Length]),0) AS TotalLength
FROM Continents AS co
LEFT JOIN Countries AS c ON c.ContinentCode = co.ContinentCode
LEFT JOIN CountriesRivers AS cr ON c.CountryCode = cr.CountryCode
LEFT JOIN Rivers AS r ON r.Id = cr.RiverId
GROUP BY c.CountryName,co.ContinentName
ORDER BY RiversCount DESC, TotalLength DESC, c.CountryName

--11
SELECT
		cu.CurrencyCode ,
		cu.[Description] AS Currency,
		Count(c.CountryName) AS NumberOfCountries
FROM Countries AS c
RIGHT JOIN Currencies AS cu ON c.CurrencyCode = cu.CurrencyCode
GROUP BY cu.CurrencyCode, cu.[Description]
ORDER BY NumberOfCountries DESC, Currency

--12
SELECT 
       co.ContinentName,
	   SUM(c.AreaInSqKm) AS CountriesArea,
	   SUM(CAST(c.Population AS BIGINT)) AS CountriesPopulation
FROM Continents AS co
LEFT JOIN Countries AS c ON c.ContinentCode= co.ContinentCode
GROUP BY co.ContinentName
ORDER BY CountriesPopulation DESC

-- 13

BEGIN TRAN
CREATE TABLE Monasteries(
	   Id INT PRIMARY KEY IDENTITY,
	   [Name] VARCHAR(80) NOT NULL,
	   CountryCode CHAR(2) NOT NULL FOREIGN KEY REFERENCES Countries(CountryCode)
)
INSERT INTO Monasteries(Name, CountryCode) VALUES
('Rila Monastery “St. Ivan of Rila”', 'BG'), 
('Bachkovo Monastery “Virgin Mary”', 'BG'),
('Troyan Monastery “Holy Mother''s Assumption”', 'BG'),
('Kopan Monastery', 'NP'),
('Thrangu Tashi Yangtse Monastery', 'NP'),
('Shechen Tennyi Dargyeling Monastery', 'NP'),
('Benchen Monastery', 'NP'),
('Southern Shaolin Monastery', 'CN'),
('Dabei Monastery', 'CN'),
('Wa Sau Toi', 'CN'),
('Lhunshigyia Monastery', 'CN'),
('Rakya Monastery', 'CN'),
('Monasteries of Meteora', 'GR'),
('The Holy Monastery of Stavronikita', 'GR'),
('Taung Kalat Monastery', 'MM'),
('Pa-Auk Forest Monastery', 'MM'),
('Taktsang Palphug Monastery', 'BT'),
('Sümela Monastery', 'TR')

ALTER TABLE Countries
ADD IsDeleted BIT DEFAULT 0 NOT NULL

UPDATE Countries
SET IsDeleted = 1
WHERE CountryCode IN (SELECT 
					  CountryCode					  
				FROM CountriesRivers 
				GROUP BY CountryCode
				HAVING COUNT(RiverId) > 3)
SELECT 
	   m.[Name] AS Monastery,
	   c.CountryName AS Country
FROM Countries AS c
JOIN Monasteries AS m ON c.CountryCode = m.CountryCode
WHERE c.IsDeleted = 0
ORDER BY m.[Name]

ROLLBACK TRAN
COMMIT TRAN
GO

--14
BEGIN TRAN

UPDATE Countries
SET CountryName = 'Burma'
WHERE CountryName = 'Myanmar'

INSERT INTO Monasteries([Name],CountryCode)
VALUES ('Hanga Abbey', (SELECT CountryCode FROM Countries
							WHERE CountryName = 'Tanzania'))

INSERT INTO Monasteries([Name],CountryCode)
VALUES ('Myin-Tin-Daik', (SELECT CountryCode FROM Countries
							WHERE CountryName = 'Myanmar'))

SELECT  
		co.ContinentName,
		c.CountryName,
	    COUNT(m.[Name]) AS MonasteriesCount
FROM Countries AS c
LEFT JOIN Continents AS co ON c.ContinentCode = co.ContinentCode
LEFT JOIN Monasteries AS m ON m.CountryCode = c.CountryCode
WHERE c.IsDeleted = 0
GROUP BY co.ContinentName,c.CountryName
ORDER BY MonasteriesCount DESC, c.CountryName


ROLLBACK TRAN
COMMIT TRAN
