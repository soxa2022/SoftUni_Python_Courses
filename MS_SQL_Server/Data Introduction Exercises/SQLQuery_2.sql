CREATE TABLE Users(
    Id BIGINT  NOT NULL PRIMARY KEY IDENTITY,
    Username VARCHAR(30) NOT NULL UNIQUE,
    [Password] VARCHAR(26) NOT NULL CHECK(LEN(Password) <= 26),
    ProfilePicture VARBINARY(MAX),
    LastLoginTime   DATETIME2 NOT NULL,
    IsDeleted BIT DEFAULT 0);

INSERT INTO Users(Username,[Password],ProfilePicture,LastLoginTime)
    VALUES ('Peter', 'fho48sd', NULL, GETDATE()),
            ('Pet', 'fho423ra', NULL, GETDATE()),
            ('Petr', 'fho423a', NULL, GETDATE()),
            ('Per', '12345', NULL, GETDATE()),
            ('Peer', '145553', NULL, GETDATE());

ALTER TABLE Users
DROP CONSTRAINT PK__Users__3214EC0766E02533

ALTER TABLE Users
ADD CONSTRAINT PK_IdUsername PRIMARY KEY (Id,Username)

ALTER TABLE Users
ADD CONSTRAINT CH_lenpassword CHECK(LEN([Password]) >= 5)

ALTER TABLE Users
ADD CONSTRAINT DF_Time DEFAULT GETDATE() FOR LastLoginTime

ALTER TABLE Users
DROP PK_IdUsername

ALTER TABLE Users
ADD CONSTRAINT PK_Id PRIMARY KEY(Id)

ALTER TABLE Users
ADD CONSTRAINT CK_LenUSERNAME CHECK(LEN(Username) >= 3)

            



