CREATE TABLE Teachers(
		TeacherID INT PRIMARY KEY IDENTITY (101,1),
		[Name] VARCHAR(50) NOT NULL,
		ManagerID INT 
		
)

INSERT INTO Teachers([Name],ManagerID)
	VALUES ('John',NULL),
		   ('Maya',106),
		   ('Silvia',106),
		   ('Ted',105),
		   ('Maya',101),
		   ('Maya',101)
			
ALTER TABLE Teachers
ADD CONSTRAINT FK_ManagerID FOREIGN KEY (ManagerID) REFERENCES Teachers


--CREATE TABLE Teachers(
--		TeacherID INT PRIMARY KEY IDENTITY (101,1),
--		[Name] VARCHAR(50) NOT NULL,
--		ManagerID INT,
--		CONSTRAINT FK_ManagerID FOREIGN KEY (ManagerID) REFERENCES Teachers
		
--)

--INSERT INTO Teachers([Name],ManagerID)
--	VALUES ('John',NULL),
--		   ('Maya',106),
--		   ('Silvia',106),
--		   ('Ted',105),
--		   ('Maya',101),
--		   ('Maya',101)