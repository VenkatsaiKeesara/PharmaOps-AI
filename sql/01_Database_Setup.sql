CREATE DATABASE PharmaOps_AI;
USE PharmaOps_AI;
SELECT DATABASE();
CREATE TABLE Category_Master (
    Category_ID VARCHAR(20) PRIMARY KEY,
    Category_Name VARCHAR(100) NOT NULL
);
ALTER TABLE Category_Master
ADD COLUMN Description VARCHAR(255);
SHOW TABLES;
DESCRIBE Category_Master;

CREATE TABLE Suppliers_Master (
    Supplier_ID VARCHAR(20) PRIMARY KEY,
    Supplier_Name VARCHAR(255) NOT NULL,
    Supplier_Type VARCHAR(100),
    Supplier_Category VARCHAR(100),
    Preferred_Supplier VARCHAR(10),
    City VARCHAR(100),
    State VARCHAR(100),
    Contact_Email VARCHAR(255),
    Contact_Number VARCHAR(20),
    Lead_Time_Days INT,
    Supplier_Rating DECIMAL(2,1),
    Active_Status VARCHAR(20),
    Contract_Start_Date DATE,
    Contract_End_Date DATE,
    GST_Number VARCHAR(20)
);
SHOW TABLES;
DESCRIBE Suppliers_Master;

-- Create Medicines_Master table to store the master details of all medicines.
CREATE TABLE Medicines_Master (
    Medicine_ID VARCHAR(20) PRIMARY KEY,
    Product_NDC VARCHAR(30),
    Generic_Name VARCHAR(255) NOT NULL,
    Brand_Name VARCHAR(255),
    Manufacturer VARCHAR(255),
    Active_Ingredient TEXT,
    Strength VARCHAR(100),
    Dosage_Form VARCHAR(100),
    Route VARCHAR(100),
    Pharm_Class TEXT,
    Category_ID VARCHAR(20),

    CONSTRAINT FK_Medicine_Category
        FOREIGN KEY (Category_ID)
        REFERENCES Category_Master(Category_ID)
);
DESCRIBE Medicines_Master;
SHOW TABLES;

-- Create Medicines_Inventory table to store medicine stock and inventory details.
CREATE TABLE Medicines_Inventory (
    Inventory_ID VARCHAR(20) PRIMARY KEY,
    Medicine_ID VARCHAR(20) NOT NULL,
    Supplier_ID VARCHAR(20) NOT NULL,
    Batch_Number VARCHAR(50) NOT NULL,
    Manufacturing_Date DATE NOT NULL,
    Expiry_Date DATE NOT NULL,
    Quantity_In_Stock INT NOT NULL,
    Unit_Cost DECIMAL(10,2) NOT NULL,
    Selling_Price DECIMAL(10,2) NOT NULL,
    Reorder_Level INT NOT NULL,
    Storage_Temperature VARCHAR(50),
    Warehouse_Location VARCHAR(100),
    Stock_Status VARCHAR(30),
    Last_Restock_Date DATE,

    CONSTRAINT FK_Inventory_Medicine
        FOREIGN KEY (Medicine_ID)
        REFERENCES Medicines_Master(Medicine_ID),

    CONSTRAINT FK_Inventory_Supplier
        FOREIGN KEY (Supplier_ID)
        REFERENCES Suppliers_Master(Supplier_ID)
);

DESCRIBE Medicines_Inventory;

-- Create Purchase_Orders table to store medicine procurement and purchase details.
CREATE TABLE Purchase_Orders (
    Purchase_Order_ID VARCHAR(20) PRIMARY KEY,
    Medicine_ID VARCHAR(20) NOT NULL,
    Supplier_ID VARCHAR(20) NOT NULL,
    Order_Date DATE NOT NULL,
    Expected_Delivery_Date DATE NOT NULL,
    Actual_Delivery_Date DATE,
    Quantity_Ordered INT NOT NULL,
    Unit_Purchase_Cost DECIMAL(10,2) NOT NULL,
    Total_Order_Value DECIMAL(12,2) NOT NULL,
    Payment_Method VARCHAR(50),
    Payment_Status VARCHAR(30),
    Order_Status VARCHAR(30),
    Warehouse_Location VARCHAR(100),
    Procurement_Manager VARCHAR(100),

    CONSTRAINT FK_Purchase_Medicine
        FOREIGN KEY (Medicine_ID)
        REFERENCES Medicines_Master(Medicine_ID),

    CONSTRAINT FK_Purchase_Supplier
        FOREIGN KEY (Supplier_ID)
        REFERENCES Suppliers_Master(Supplier_ID)
);
DESCRIBE Purchase_Orders;

-- Create Sales_Transactions table to store medicine sales records.
CREATE TABLE Sales_Transactions (
    Transaction_ID VARCHAR(20) PRIMARY KEY,
    Invoice_Number VARCHAR(20) NOT NULL,
    Medicine_ID VARCHAR(20) NOT NULL,
    Branch_ID VARCHAR(20) NOT NULL,
    Transaction_Date DATE NOT NULL,
    Sale_Time TIME NOT NULL,
    Quantity_Sold INT NOT NULL,
    Unit_Selling_Price DECIMAL(10,2) NOT NULL,
    Discount_Percentage DECIMAL(5,2),
    Total_Amount DECIMAL(12,2) NOT NULL,
    Payment_Method VARCHAR(50),
    Customer_Type VARCHAR(50),
    Prescription_Required VARCHAR(10),
    Pharmacist_ID VARCHAR(20),
    Transaction_Status VARCHAR(30),

    CONSTRAINT FK_Sales_Medicine
        FOREIGN KEY (Medicine_ID)
        REFERENCES Medicines_Master(Medicine_ID)
);
DESCRIBE Sales_Transactions;

-- Create Waste_Records table to store expired, damaged, and discarded medicine records.
CREATE TABLE Waste_Records (
    Waste_Record_ID VARCHAR(20) PRIMARY KEY,
    Inventory_ID VARCHAR(20) NOT NULL,
    Medicine_ID VARCHAR(20) NOT NULL,
    Batch_Number VARCHAR(50) NOT NULL,
    Waste_Date DATE NOT NULL,
    Expiry_Date DATE NOT NULL,
    Quantity_Wasted INT NOT NULL,
    Unit_Cost DECIMAL(10,2) NOT NULL,
    Total_Waste_Value DECIMAL(12,2) NOT NULL,
    Waste_Reason VARCHAR(100),
    Disposal_Method VARCHAR(100),
    Disposal_Status VARCHAR(50),
    Reported_By VARCHAR(100),
    Warehouse_Location VARCHAR(100),
    Remarks VARCHAR(255),

    CONSTRAINT FK_Waste_Inventory
        FOREIGN KEY (Inventory_ID)
        REFERENCES Medicines_Inventory(Inventory_ID),

    CONSTRAINT FK_Waste_Medicine
        FOREIGN KEY (Medicine_ID)
        REFERENCES Medicines_Master(Medicine_ID)
);
DESCRIBE Waste_Records;



-- after importing data
-- Check the number of records imported.

SELECT COUNT(*) FROM Category_Master;
SELECT COUNT(*) FROM Suppliers_Master;
SELECT COUNT(*) FROM Medicines_Master;
SELECT COUNT(*) FROM Medicines_Inventory;
SELECT COUNT(*) FROM Purchase_Orders;
SELECT COUNT(*) FROM Sales_Transactions;
SELECT COUNT(*) FROM Waste_Records;

SELECT COUNT(*) AS Total_Medicines
FROM Medicines_Master;

SELECT MIN(Medicine_ID) AS First_ID,
       MAX(Medicine_ID) AS Last_ID
FROM Medicines_Master;



SELECT DISTINCT m.Category_ID
FROM Medicines_Master m
LEFT JOIN Category_Master c
ON m.Category_ID = c.Category_ID
WHERE c.Category_ID IS NULL;

SELECT *
FROM Category_Master;

SHOW WARNINGS;

SELECT COUNT(*) AS Total_Medicines
FROM Medicines_Master;

SELECT COUNT(DISTINCT Medicine_ID) AS Unique_Medicines
FROM Medicines_Master;

SELECT COUNT(*)
FROM Medicines_Master
WHERE Category_ID = 'CAT011';

SHOW CREATE TABLE Medicines_Master;
SELECT COUNT(*)
FROM Category_Master;

SELECT
    MAX(LENGTH(Manufacturer)) AS Max_Manufacturer_Length,
    MAX(LENGTH(Generic_Name)) AS Max_Generic_Name_Length,
    MAX(LENGTH(Brand_Name)) AS Max_Brand_Name_Length,
    MAX(LENGTH(Strength)) AS Max_Strength_Length,
    MAX(LENGTH(Dosage_Form)) AS Max_Dosage_Form_Length,
    MAX(LENGTH(Route)) AS Max_Route_Length
FROM Medicines_Master;

SHOW VARIABLES LIKE 'local_infile';

SELECT VERSION();

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE Medicines_Master;
SET FOREIGN_KEY_CHECKS = 1;
SELECT COUNT(*) AS Total_Rows
FROM Medicines_Master;



USE PharmaOps_AI;

SHOW VARIABLES LIKE 'secure_file_priv';

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Medicines_Master_Final.csv'
INTO TABLE Medicines_Master
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(
    Medicine_ID,
    Product_NDC,
    Generic_Name,
    Brand_Name,
    Manufacturer,
    Active_Ingredient,
    Strength,
    Dosage_Form,
    Route,
    Pharm_Class,
    Category_ID
);

ALTER TABLE Medicines_Master
MODIFY COLUMN Generic_Name VARCHAR(600) NOT NULL,
MODIFY COLUMN Brand_Name VARCHAR(400);

DESCRIBE Medicines_Master;

SELECT COUNT(*) AS Total_Rows
FROM Medicines_Master;

SELECT COUNT(*) AS Total_Rows
FROM Medicines_Master;

SELECT COUNT(*) AS Duplicate_MedicineIDs
FROM (
    SELECT Medicine_ID
    FROM Medicines_Master
    GROUP BY Medicine_ID
    HAVING COUNT(*) > 1
) AS DuplicateCheck;

SELECT COUNT(*) AS Null_MedicineIDs
FROM Medicines_Master
WHERE Medicine_ID IS NULL;

SELECT *
FROM Medicines_Master
LIMIT 5;

-- reconnect foreginnkeys 

SELECT COUNT(*) AS Inventory_Rows
FROM Medicines_Inventory;

SELECT COUNT(*) AS Purchase_Order_Rows
FROM Purchase_Orders;

SELECT COUNT(*) AS Sales_Transaction_Rows
FROM Sales_Transactions;

SELECT COUNT(*) AS Waste_Record_Rows
FROM Waste_Records;

SELECT COUNT(*) AS Invalid_Inventory_Medicines
FROM Medicines_Inventory i
LEFT JOIN Medicines_Master m
ON i.Medicine_ID = m.Medicine_ID
WHERE m.Medicine_ID IS NULL;

SELECT COUNT(*) AS Invalid_PO_Medicines
FROM Purchase_Orders p
LEFT JOIN Medicines_Master m
ON p.Medicine_ID = m.Medicine_ID
WHERE m.Medicine_ID IS NULL;

SELECT COUNT(*) AS Invalid_Sales_Medicines
FROM Sales_Transactions s
LEFT JOIN Medicines_Master m
ON s.Medicine_ID = m.Medicine_ID
WHERE m.Medicine_ID IS NULL;

SELECT COUNT(*) AS Invalid_Waste_Medicines
FROM Waste_Records w
LEFT JOIN Medicines_Master m
ON w.Medicine_ID = m.Medicine_ID
WHERE m.Medicine_ID IS NULL;