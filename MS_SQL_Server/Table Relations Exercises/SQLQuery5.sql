CREATE DATABASE [Online Store Database]
GO
USE [Online Store Database]
GO
CREATE TABLE Cities(
    CityID INT PRIMARY KEY ,
    [Name] VARCHAR(50) NOT NULL
)

CREATE TABLE ItemTypes(
    ItemTypeID INT PRIMARY KEY,
    [Name] VARCHAR(50) NOT NULL
)

CREATE TABLE Customers(    
    CustomerID INT NOT NULL PRIMARY KEY,
    [Name] VARCHAR(50) NOT NULL,
    Birthday DATE NOT NULL,
    CityID INT NOT NULL ,
    CONSTRAINT FK_CItiesID FOREIGN KEY(CityID) REFERENCES Cities(CityID)
)

CREATE TABLE Items(
    ItemID INT PRIMARY KEY,
    [Name] VARCHAR(50) NOT NULL,
    ItemTypeID INT NOT NULL FOREIGN KEY REFERENCES ItemTypes(ItemTypeID)
)


CREATE TABLE Orders(
    OrderID INT NOT NULL PRIMARY KEY,
    CustomerID INT NOT NULL FOREIGN KEY REFERENCES Customers(CustomerID)
)

CREATE TABLE OrderItems(
    OrderID INT NOT NULL,
    ItemID INT NOT NULL,
    CONSTRAINT PK_OrderID_ItemID PRIMARY KEY(OrderID,ItemID),
    CONSTRAINT FK_OrderID FOREIGN KEY(OrderID) REFERENCES Orders(OrderID),
    CONSTRAINT FK_ItemID FOREIGN KEY(ItemID) REFERENCES Items(ItemID)
)
