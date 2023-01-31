USE Gringotts
GO
SELECT * FROM WizzardDeposits

-- Problem 01
SELECT 
      COUNT(*) AS [Count] 
FROM WizzardDeposits

-- Problem 02
SELECT MAX(MagicWandSize) AS [LongestMagicWand]
FROM WizzardDeposits

-- Problem 03
SELECT 
      w.DepositGroup
      ,MAX(w.MagicWandSize) AS [LongestMagicWand]
FROM WizzardDeposits AS w
GROUP BY w.DepositGroup

--Problem 04
SELECT TOP 2
      w.DepositGroup       
FROM WizzardDeposits AS w
GROUP BY w.DepositGroup
ORDER BY AVG(w.MagicWandSize)

-- Problem 05
SELECT 
      w.DepositGroup
      , SUM(w.DepositAmount) AS [TotalSum]
FROM WizzardDeposits AS w
GROUP BY w.DepositGroup

-- Problem 06
SELECT 
    DepositGroup
    ,TotalSum
FROM
    (SELECT 
            w.MagicWandCreator
            ,w.DepositGroup
            , SUM(w.DepositAmount) AS [TotalSum]
    FROM WizzardDeposits AS w
    GROUP BY w.DepositGroup,w.MagicWandCreator) AS [Subquery]
WHERE MagicWandCreator = 'Ollivander family'

-- Problem 07
SELECT 
    DepositGroup
    ,TotalSum
FROM
    (
        SELECT 
            w.MagicWandCreator
            ,w.DepositGroup
            , SUM(w.DepositAmount) AS [TotalSum]
    FROM WizzardDeposits AS w
    GROUP BY w.DepositGroup,w.MagicWandCreator
    HAVING SUM(w.DepositAmount) < 150000
    ) AS [Subquery]
WHERE MagicWandCreator = 'Ollivander family'
ORDER BY TotalSum DESC



SELECT            
       w.DepositGroup
       , SUM(w.DepositAmount) AS [TotalSum]
FROM WizzardDeposits AS w
WHERE w.MagicWandCreator = 'Ollivander family'
GROUP BY w.DepositGroup,w.MagicWandCreator
HAVING SUM(w.DepositAmount) < 150000
ORDER BY TotalSum DESC


-- Problem 08
SELECT 
      DepositGroup
      ,MagicWandCreator
      ,MIN(DepositCharge) AS [MinDepositCharge]
FROM WizzardDeposits
GROUP BY DepositGroup,MagicWandCreator 
ORDER BY MagicWandCreator,DepositGroup

-- Problem 09
SELECT
        AgeGroup
        , SUM(WizardCount) AS [WizardCount]
FROM
    (SELECT 
        CASE
        WHEN Age <= 10 THEN '[0-10]'
        WHEN Age > 10 AND Age <= 20 THEN '[11-20]'
        WHEN Age > 20 AND Age <= 30 THEN '[21-30]'
        WHEN Age > 30 AND Age <= 40 THEN '[31-40]'
        WHEN Age > 40 AND Age <= 50 THEN '[41-50]'
        WHEN Age > 50 AND Age <= 60 THEN '[51-60]'
        ELSE '[61+]'
        END AS AgeGroup
        ,Count(*) AS [WizardCount]
    FROM WizzardDeposits 
    GROUP BY Age) AS Subquery
GROUP BY AgeGroup

SELECT
        AgeGroup
        , COUNT(*) AS [WizardCount]
FROM
    (SELECT 
        CASE
        WHEN Age <= 10 THEN '[0-10]'
        WHEN Age > 10 AND Age <= 20 THEN '[11-20]'
        WHEN Age > 20 AND Age <= 30 THEN '[21-30]'
        WHEN Age > 30 AND Age <= 40 THEN '[31-40]'
        WHEN Age > 40 AND Age <= 50 THEN '[41-50]'
        WHEN Age > 50 AND Age <= 60 THEN '[51-60]'
        ELSE '[61+]'
        END AS AgeGroup
        
    FROM WizzardDeposits 
    ) AS Subquery
GROUP BY AgeGroup




-- Problem 10
SELECT DISTINCT
     LEFT(w.FirstName,1) AS FirstLetter
FROM WizzardDeposits as w
WHERE DepositGroup = 'Troll Chest'
GROUP BY LEFT(w.FirstName,1)
ORDER BY FirstLetter



-- Problem 11
SELECT
       w.DepositGroup
       ,w.IsDepositExpired
       , AVG(w.DepositInterest) AS [AverageInterest]
FROM WizzardDeposits AS w
WHERE w.DepositStartDate > '01/01/1985'
GROUP BY w.DepositGroup,w.IsDepositExpired
ORDER BY w.DepositGroup DESC,w.IsDepositExpired

-- Problem 12

SELECT SUM(w.[Difference]) AS [SumDifference] 

FROM

	(SELECT 
		   w1.FirstName AS [Host Wizard]
		  ,w1.DepositAmount AS [Host Wizard Deposit]
		  ,w2.FirstName AS [Guest Wizard]
		  ,w2.DepositAmount AS [Guest Wizard Deposit]
		  ,w1.DepositAmount - w2.DepositAmount AS [Difference]
	FROM WizzardDeposits AS w1
	JOIN  WizzardDeposits AS w2
	ON w1.Id + 1 = w2.id ) AS w

SELECT SUM([Difference])
    AS [SumDifference]
  FROM (
                SELECT [FirstName]
                    AS [Host Wizard],
                       [DepositAmount]     
                    AS [Host Wizard Deposit],
                       LEAD([FirstName]) OVER(ORDER BY [Id])
                    AS [Guest Wizard],
                       LEAD([DepositAmount]) OVER(ORDER BY [Id])
                    AS [Guest Wizard Deposit],
                       [DepositAmount] - LEAD([DepositAmount]) OVER(ORDER BY [Id])
                    AS [Difference]
                  FROM [WizzardDeposits]
       ) AS [DifferenceSubQuery]



-- Problem 13
USE SoftUni
GO
SELECT 
      e.DepartmentID 
      ,SUM(e.Salary) AS TotalSalary   
FROM Employees as e
GROUP BY e.DepartmentID
ORDER BY e.DepartmentID

-- Problem 14
SELECT 
      e.DepartmentID 
      ,MIN(e.Salary) AS MinimumSalary   
FROM Employees as e
WHERE e.DepartmentID IN (2, 5, 7) AND e.HireDate > '01/01/2000'
GROUP BY e.DepartmentID
ORDER BY e.DepartmentID

-- Problem 15

SELECT * INTO NewTable 
FROM Employees
WHERE Salary > 30000

DELETE FROM NewTable
WHERE ManagerID = 42

UPDATE NewTable
SET Salary += 5000
WHERE DepartmentID = 1

SELECT
       n.DepartmentID
       ,AVG(n.Salary) 
FROM NewTable AS n
GROUP BY n.DepartmentID


--Problem 16
SELECT 
      e.DepartmentID 
      ,MAX(e.Salary) AS MaxSalary   
FROM Employees as e
GROUP BY e.DepartmentID
HAVING MAX(e.Salary) NOT BETWEEN 30000 AND 70000

-- Problem 17 
SELECT 
      COUNT(e.Salary) AS Count   
FROM Employees as e
WHERE e.ManagerID IS NULL

-- Problem 18

SELECT 
      Subquery.DepartmentID
      ,Subquery.Salary
FROM
(
      SELECT 
            e.DepartmentID
            ,e.Salary
            ,DENSE_RANK() OVER (PARTITION BY e.DepartmentID ORDER BY E.Salary DESC ) AS [Rank]
            
      FROM  Employees AS e
      GROUP BY e.DepartmentID,e.Salary
)     AS Subquery 
WHERE Subquery.Rank = 3

SELECT 
DISTINCT [DepartmentID],
         [Salary]
      AS [ThirdHighestSalary]
    FROM (
              SELECT [DepartmentID],
                     [Salary],
                     DENSE_RANK() OVER(PARTITION BY [DepartmentID] ORDER BY [Salary] DESC)
                  AS [SalaryRank]
                FROM [Employees]
         )
      AS [SalaryRankingSuquery]
   WHERE [SalaryRank] = 3

-- Problem 19

SELECT TOP 10
     em.FirstName
     ,em.LastName
     ,em.DepartmentID     
FROM Employees AS em
JOIN    (
        SELECT 
            e.DepartmentID
            ,AVG(e.Salary) AS AvgSalary
        FROM Employees AS e
        GROUP BY e.DepartmentID
        )   AS q
        ON q.DepartmentID = em.DepartmentID 
WHERE em.Salary > q.AvgSalary
ORDER BY em.DepartmentID

  SELECT 
TOP (10) [e].[FirstName],
         [e].[LastName],
         [e].[DepartmentID]
    FROM [Employees]
      AS [e]
   WHERE [e].[Salary] > (
                              SELECT AVG([Salary])
                                  AS [AverageSalary]
                                FROM [Employees]
                                  AS [eSub]
                               WHERE [eSub].[DepartmentID] = [e].[DepartmentID]
                            GROUP BY [DepartmentID]
                         )
ORDER BY [e].[DepartmentID]


-- Instead of delete in real world
ALTER TABLE [NewTable]
        ADD [IsDeleted] BIT DEFAULT(0) NOT NULL
 
-- Select all non-deleted employees
SELECT *
  FROM [NewTable]
 WHERE [IsDeleted] = 0
 
-- Delete all with ManagerID 3
UPDATE [NewTable]
   SET [IsDeleted] = 1
 WHERE [ManagerID] = 3