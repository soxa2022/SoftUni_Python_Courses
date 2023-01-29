CREATE TABLE People(
    Id BIGINT NOT NULL PRIMARY KEY IDENTITY(1,1),
    [Name] NVARCHAR(200) NOT NULL ,
    Picture VARBINARY(MAX) ,
    Height NUMERIC(5,2),
    [Weight] NUMERIC(5,2),
    Gender CHAR(1) NOT NULL,
    Birthdate DATE NOT NULL,
    Biography NVARCHAR(MAX)
) 
INSERT INTO People([Name],Picture,Height,[Weight],Gender,Birthdate,Biography)
    VALUES ('Ivan',NULL,1.80,78.6,'m','1980-09-10',NULL),
            ('Pete',NULL,1.99,98.6,'m','1981-10-01',NULL),       
            ('Gosho',NULL,1.60,61.6,'m','1982-07-10',NULL),      
            ('Ann',NULL,1.65,58.6,'f','1984-05-14',NULL),
            ('Kalina',NULL,1.58,48.6,'f','1985-04-20',NULL)       
            
    
-- DROP TABLE People