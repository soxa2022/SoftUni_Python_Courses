CREATE DATABASE Movies
GO
USE Movies
-- •	Directors (Id, DirectorName, Notes)
-- •	Genres (Id, GenreName, Notes)
-- •	Categories (Id, CategoryName, Notes)
-- •	Movies (Id, Title, DirectorId, CopyrightYear, Length, GenreId, CategoryId, Rating, Notes)


CREATE TABLE Directors(
    Id INT NOT NULL PRIMARY KEY IDENTITY,
    DirectorName NVARCHAR(50) NOT NULL,
    Notes NVARCHAR(MAX)
)

CREATE TABLE Genres(
    Id INT NOT NULL PRIMARY KEY IDENTITY,
    GenreName NVARCHAR(50) NOT NULL,
    Notes NVARCHAR(MAX)
)

CREATE TABLE Categories(
    Id INT NOT NULL PRIMARY KEY IDENTITY,
    CategoryName NVARCHAR(50) NOT NULL,
    Notes NVARCHAR(MAX)
)

CREATE TABLE Movies(
    Id INT NOT NULL PRIMARY KEY IDENTITY,
    Title NVARCHAR(50) NOT NULL,
    DirectorId INT NOT NULL FOREIGN KEY REFERENCES Directors(Id),
    CopyrightYear SMALLINT,
    [Length] SMALLINT,
    GenreId INT NOT NULL FOREIGN KEY REFERENCES Genres(Id),
    CategoryId INT NOT NULL FOREIGN KEY REFERENCES Categories(Id),
    Rating TINYINT,    
    Notes NVARCHAR(MAX)
)

INSERT INTO Directors(DirectorName,Notes)
    VALUES ('Peter', NULL),
            ('Pete', NULL),
            ('Peer', NULL),
            ('Petr', NULL),
            ('Pet', NULL)

INSERT INTO Genres(GenreName,Notes)
    VALUES ('Action', NULL),
            ('Comedy', NULL),
            ('Horor', NULL),
            ('Drama', NULL),
            ('Action', NULL)

INSERT INTO Categories(CategoryName,Notes)
    VALUES ('Fantasy', NULL),
            ('Teen', NULL),
            ('Thriller', NULL),
            ('Thriller', NULL),
            ('Fantasy', NULL)

INSERT INTO Movies(Title, DirectorId, CopyrightYear,[Length], GenreId, CategoryId, Rating, Notes)
    VALUES ('Matrix',1, 2000, 195,1,1, 5, NULL),
            ('Wolfteen',2, 1998, 95,2,2, 4, NULL),
            ('Adams',3, 1993, 90,3,3, 5, NULL),
            ('DOOM',4, 2002, 100,4,4, 4, NULL),
            ('Matrix II', 5,2005, 200,5,5, 6, NULL)



            



