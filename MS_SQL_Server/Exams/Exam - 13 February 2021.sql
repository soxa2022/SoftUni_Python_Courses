CREATE DATABASE Bitbucket
GO
USE Bitbucket
GO

--01
Create table Users(
		Id int primary key identity,
		Username varchar(30) Not null,
		[Password] varchar(30) Not null,
		Email varchar(50) Not null
)

Create table Repositories(
		Id int primary key identity,
		[Name] varchar(50) Not null,
)

Create table RepositoriesContributors(
		RepositoryId int foreign key references Repositories(Id) NOT NULL,
		ContributorId int foreign key references Users(Id) NOT NULL,
		Primary Key(RepositoryId,ContributorId)
)
Create table Issues(
		Id int primary key identity,
		Title varchar(255) Not null,
		IssueStatus varchar(10) Not null CHECK(LEN(IssueStatus) <= 6),
		RepositoryId int foreign key references Repositories(Id) NOT NULL,
		AssigneeId int foreign key references Users(Id) NOT NULL
)
Create table Commits(
		Id int primary key identity,
		[Message] varchar(255) Not null,
		IssueId int foreign key references Issues(Id),
		RepositoryId int foreign key references Repositories(Id) NOT NULL,
		ContributorId int foreign key references Users(Id) NOT NULL
)
Create table Files(
		Id int primary key identity,
		[Name] varchar(100) Not null,
		Size DECIMAL(18,2) Not null,
		ParentId int foreign key references Files(Id),
		CommitId int foreign key references Commits(Id) NOT NULL
)
GO
--02
INSERT INTO Files([Name],Size,ParentId,CommitId)
VALUES ('Trade.idk', 2598.0,	1, 1),
	   ('menu.net', 9238.31, 2,	2),
	   ('Administrate.soshy', 1246.93, 3, 3),
		('Controller.php',	7353.15, 4,	4),
		('Find.java', 9957.86, 5, 5),
		('Controller.json',	14034.87,	3,	6),
		('Operate.xix',	7662.92, 7, 7)

INSERT INTO Issues(Title,IssueStatus,RepositoryId,AssigneeId)
VALUES ('Critical Problem with HomeController.cs file', 'open',	1, 4),
		('Typo fix in Judge.html', 'open',	4, 3),
		('Implement documentation for UsersService.cs',	'closed', 8, 2),
        ('Unreachable code in Index.cs', 'open', 9, 8)

--03
UPDATE Issues
SET IssueStatus = 'closed'
Where AssigneeId = 6 

--04



DELETE FROM Issues
WHERE RepositoryId = (SELECT Id FROM Repositories
					WHERE [Name] = 'Softuni-Teamwork')


DELETE FROM RepositoriesContributors
WHERE RepositoryId = (SELECT Id FROM Repositories
					WHERE [Name] = 'Softuni-Teamwork')


--05


SELECT 
		Id, 
		[Message],
		RepositoryId, 
		ContributorId 
FROM Commits
ORDER BY Id, [Message],RepositoryId, ContributorId

--06
SELECT 
		id,
		[Name],
		Size
FROM Files
WHERE [Name] LIKE '%html%' AND Size > 1000
ORDER BY Size desc, id, [Name]
--07
SELECT 
	   i.Id,	
	   CONCAT(u.Username,' : ',i.Title) AS IssueAssignee
FROM Users AS u
JOIN Issues AS i ON i.AssigneeId = u.Id
ORDER BY i.Id desc, IssueAssignee 

--08

SELECT 
		Id,
		[Name],
		CONCAT(Size,'KB') AS Size
FROM Files
WHERE Id NOT IN (SELECT ParentId FROM Files WHERE ParentId IS NOT NULL) 
ORDER BY Id, [Name], Size desc

--09
SELECT TOP 5
	   r.Id,
	   r.[Name],
	   COUNT(*) AS [Commits]
FROM Repositories AS r
JOIN Commits AS c ON c.RepositoryId = r.Id
JOIN RepositoriesContributors AS rc ON rc.RepositoryId = r.Id
GROUP BY r.[Name] , r.Id
ORDER BY [Commits] desc, r.Id, r.[Name]

--10

SELECT
		u.Username,
		AVG(f.Size) AS [Size]
FROM Users AS u
JOIN Commits AS c ON c.ContributorId = u.Id
JOIN Files AS f ON f.CommitId = c.Id
GROUP BY u.Username
ORDER BY [Size] desc, u.Username

-- 11
GO

CREATE OR ALTER FUNCTION udf_AllUserCommits(@username VARCHAR(30)) 
RETURNS INT AS
BEGIN
		DECLARE @result INT = 0
		SET @result = (SELECT  	   
							   COUNT(*) 
						FROM Users AS u
						JOIN Commits AS c ON u.Id = c.ContributorId
						WHERE u.Username = @username)
		RETURN @result

END;
GO

CREATE OR ALTER PROC usp_SearchForFiles(@fileExtension VARCHAR(20)) 
AS
BEGIN
		SELECT
		Id,
		[Name],
		CONCAT(t.Size,'KB') AS [Size]
		FROM Files AS t
		WHERE [Name] LIKE CONCAT('%.',@fileExtension)
		ORDER BY t.Id,t.[Name],t.Size DESC
END;
GO
EXEC usp_SearchForFiles 'txt'

