-- ============================================================
-- Query 1: Pharmacy Business Overview
-- ============================================================
-- Business Question:
-- What is the overall operational scale of the pharmacy?
--
-- Business Objective:
-- Provide a high-level summary of the pharmacy database by
-- displaying the total medicines, suppliers, inventory,
-- purchase orders, sales transactions, and waste records.
-- ============================================================

SELECT
    (SELECT COUNT(*) FROM Medicines_Master) AS Total_Medicines,
    (SELECT COUNT(*) FROM Suppliers_Master) AS Total_Suppliers,
    (SELECT COUNT(*) FROM Medicines_Inventory) AS Total_Inventory_Records,
    (SELECT COUNT(*) FROM Purchase_Orders) AS Total_Purchase_Orders,
    (SELECT COUNT(*) FROM Sales_Transactions) AS Total_Sales_Transactions,
    (SELECT COUNT(*) FROM Waste_Records) AS Total_Waste_Records;

-- ============================================================
-- Query 2: Medicine Distribution by Category
-- ============================================================
-- Business Question:
-- Which medicine categories contain the highest number of
-- medicines in the pharmacy?
--
-- Business Objective:
-- Identify the distribution of medicines across different
-- categories to understand inventory composition and support
-- category-wise inventory planning.
-- ============================================================

SELECT
    c.Category_Name,
    COUNT(m.Medicine_ID) AS Total_Medicines
FROM Medicines_Master m
JOIN Category_Master c
    ON m.Category_ID = c.Category_ID
GROUP BY c.Category_Name
ORDER BY Total_Medicines DESC;


-- ============================================================
-- Query 3: Top Suppliers by Inventory Portfolio
-- ============================================================
-- Business Question:
-- Which suppliers currently supply the highest number of
-- inventory records in the pharmacy?
--
-- Business Objective:
-- Identify the suppliers contributing the largest inventory
-- portfolio to understand supplier dependence and inventory
-- distribution.
-- ============================================================

SELECT
    s.Supplier_Name,
    COUNT(i.Inventory_ID) AS Total_Inventory_Items
FROM Suppliers_Master s
JOIN Medicines_Inventory i
    ON s.Supplier_ID = i.Supplier_ID
GROUP BY s.Supplier_Name
ORDER BY Total_Inventory_Items DESC;


-- ============================================================
-- Query 4: Inventory Stock Status
-- ============================================================
-- Business Question:
-- What is the current inventory stock status of medicines?
--
-- Business Objective:
-- Categorize inventory into In Stock, Low Stock, and Out of
-- Stock based on available quantities to support inventory
-- monitoring and replenishment planning.
-- ============================================================

SELECT
    CASE
        WHEN Quantity_In_Stock = 0 THEN 'Out of Stock'
        WHEN Quantity_In_Stock <= Reorder_Level THEN 'Low Stock'
        ELSE 'In Stock'
    END AS Stock_Status,
    COUNT(*) AS Total_Inventory_Items
FROM Medicines_Inventory
GROUP BY
    CASE
        WHEN Quantity_In_Stock = 0 THEN 'Out of Stock'
        WHEN Quantity_In_Stock <= Reorder_Level THEN 'Low Stock'
        ELSE 'In Stock'
    END
ORDER BY Total_Inventory_Items DESC;

-- ============================================================
-- Query 5: Purchase Orders by Status
-- ============================================================
-- Business Question:
-- What is the distribution of purchase orders across different
-- order statuses?
--
-- Business Objective:
-- Analyze procurement activities by identifying the number
-- of purchase orders that are Pending, Delivered, Cancelled,
-- or In Transit.
-- ============================================================

SELECT
    Order_Status,
    COUNT(*) AS Total_Orders
FROM Purchase_Orders
GROUP BY Order_Status
ORDER BY Total_Orders DESC;

DESC Medicines_Master;
DESC Medicines_Inventory;
DESC Suppliers_Master;

-- ============================================================
-- Query 6: Inventory Value by Medicine Category
-- ============================================================
-- Business Question:
-- Which medicine categories contribute the highest inventory
-- value in the pharmacy?
--
-- Business Objective:
-- Calculate the total inventory value for each medicine
-- category to identify high-value inventory and support
-- financial planning.
-- ============================================================

SELECT
    c.Category_Name,
    ROUND(SUM(i.Quantity_In_Stock * i.Unit_Cost), 2) AS Inventory_Value
FROM Medicines_Inventory i
JOIN Medicines_Master m
    ON i.Medicine_ID = m.Medicine_ID
JOIN Category_Master c
    ON m.Category_ID = c.Category_ID
GROUP BY c.Category_Name
ORDER BY Inventory_Value DESC;

-- ============================================================
-- Query 7: Medicines Below Reorder Level
-- ============================================================
-- Business Question:
-- Which medicines require immediate replenishment?
--
-- Business Objective:
-- Identify medicines whose stock quantity is less than or
-- equal to the reorder level to avoid stock shortages.
-- ============================================================

SELECT
    i.Inventory_ID,
    m.Generic_Name,
    i.Quantity_In_Stock,
    i.Reorder_Level,
    s.Supplier_Name
FROM Medicines_Inventory i
JOIN Medicines_Master m
    ON i.Medicine_ID = m.Medicine_ID
JOIN Suppliers_Master s
    ON i.Supplier_ID = s.Supplier_ID
WHERE i.Quantity_In_Stock <= i.Reorder_Level
ORDER BY i.Quantity_In_Stock ASC;

-- ============================================================
-- Query 8: Medicines Near Expiry
-- ============================================================
-- Business Question:
-- Which medicines are nearing their expiry date?
--
-- Business Objective:
-- Identify medicines expiring within the next 90 days so the
-- pharmacy can prioritize sales or take preventive actions.
-- ============================================================

SELECT
    i.Inventory_ID,
    m.Generic_Name,
    i.Batch_Number,
    i.Expiry_Date,
    DATEDIFF(i.Expiry_Date, CURDATE()) AS Days_Remaining
FROM Medicines_Inventory i
JOIN Medicines_Master m
    ON i.Medicine_ID = m.Medicine_ID
WHERE i.Expiry_Date BETWEEN CURDATE()
                        AND DATE_ADD(CURDATE(), INTERVAL 90 DAY)
ORDER BY i.Expiry_Date;

-- ============================================================
-- Query 9: Top 10 Highest Value Inventory Items
-- ============================================================
-- Business Question:
-- Which inventory items have the highest monetary value?
--
-- Business Objective:
-- Identify the most valuable inventory items based on stock
-- quantity and unit cost to support inventory control and
-- financial risk management.
-- ============================================================

SELECT
    m.Generic_Name,
    i.Batch_Number,
    i.Quantity_In_Stock,
    i.Unit_Cost,
    ROUND(i.Quantity_In_Stock * i.Unit_Cost, 2) AS Inventory_Value
FROM Medicines_Inventory i
JOIN Medicines_Master m
    ON i.Medicine_ID = m.Medicine_ID
ORDER BY Inventory_Value DESC
LIMIT 10;

- ============================================================
-- Query 10: Top Rated Suppliers
-- ============================================================
-- Business Question:
-- Which suppliers have the highest performance ratings?
--
-- Business Objective:
-- Identify the best-performing suppliers based on their
-- supplier ratings to support procurement decisions.
-- ============================================================

SELECT
    Supplier_Name,
    Supplier_Category,
    Supplier_Rating
FROM Suppliers_Master
WHERE Supplier_Rating IS NOT NULL
ORDER BY Supplier_Rating DESC, Supplier_Name;

-- ============================================================
-- Query 11: Average Lead Time by Supplier Category
-- ============================================================
-- Business Question:
-- Which supplier categories have the shortest and longest
-- average lead times?
--
-- Business Objective:
-- Measure supplier responsiveness by comparing average
-- delivery lead times across supplier categories.
-- ============================================================

SELECT
    Supplier_Category,
    ROUND(AVG(Lead_Time_Days),2) AS Average_Lead_Time_Days
FROM Suppliers_Master
GROUP BY Supplier_Category
ORDER BY Average_Lead_Time_Days;

-- ============================================================
-- Query 12: Preferred vs Non-Preferred Suppliers
-- ============================================================
-- Business Question:
-- How many suppliers are marked as preferred compared to
-- non-preferred suppliers?
--
-- Business Objective:
-- Analyze the supplier base to understand the proportion
-- of preferred suppliers used by the pharmacy.
-- ============================================================

SELECT
    Preferred_Supplier,
    COUNT(*) AS Total_Suppliers
FROM Suppliers_Master
GROUP BY Preferred_Supplier;

-- ============================================================
-- Query 13: Inventory Value by Supplier
-- ============================================================
-- Business Question:
-- Which suppliers contribute the highest inventory value?
--
-- Business Objective:
-- Calculate the total inventory value supplied by each
-- supplier to identify high-value procurement partners.
-- ============================================================

SELECT
    s.Supplier_Name,
    ROUND(SUM(i.Quantity_In_Stock * i.Unit_Cost),2) AS Inventory_Value
FROM Suppliers_Master s
JOIN Medicines_Inventory i
    ON s.Supplier_ID = i.Supplier_ID
GROUP BY s.Supplier_Name
ORDER BY Inventory_Value DESC;

-- ============================================================
-- Query 14: Top 10 Selling Medicines
-- ============================================================
-- Business Question:
-- Which medicines are sold the most based on quantity?
--
-- Business Objective:
-- Identify the highest-selling medicines to understand
-- customer demand and optimize inventory planning.
-- ============================================================

SELECT
    m.Generic_Name,
    SUM(s.Quantity_Sold) AS Total_Quantity_Sold
FROM Sales_Transactions s
JOIN Medicines_Master m
    ON s.Medicine_ID = m.Medicine_ID
GROUP BY m.Generic_Name
ORDER BY Total_Quantity_Sold DESC
LIMIT 10;

-- ============================================================
-- Query 15: Revenue by Medicine Category
-- ============================================================
-- Business Question:
-- Which medicine categories generate the highest sales revenue?
--
-- Business Objective:
-- Calculate total revenue generated by each medicine category
-- to identify the most profitable therapeutic segments.
-- ============================================================

SELECT
    c.Category_Name,
    ROUND(SUM(s.Total_Amount),2) AS Total_Revenue
FROM Sales_Transactions s
JOIN Medicines_Master m
    ON s.Medicine_ID = m.Medicine_ID
JOIN Category_Master c
    ON m.Category_ID = c.Category_ID
GROUP BY c.Category_Name
ORDER BY Total_Revenue DESC;


-- ============================================================
-- Query 16: Monthly Sales Performance
-- ============================================================
-- Business Question:
-- How do sales transactions and revenue vary by month?
--
-- Business Objective:
-- Analyze monthly sales performance to identify business
-- trends, seasonality, and revenue growth patterns.
-- ============================================================

SELECT
    DATE_FORMAT(Transaction_Date,'%Y-%m') AS Sales_Month,
    COUNT(*) AS Total_Transactions,
    SUM(Quantity_Sold) AS Total_Quantity_Sold,
    ROUND(SUM(Total_Amount),2) AS Total_Revenue
FROM Sales_Transactions
GROUP BY DATE_FORMAT(Transaction_Date,'%Y-%m')
ORDER BY Sales_Month;

-- ============================================================
-- Query 17: Sales Analysis by Payment Method
-- ============================================================
-- Business Question:
-- Which payment methods are most frequently used by customers?
--
-- Business Objective:
-- Analyze customer payment preferences to improve payment
-- services and support financial planning.
-- ============================================================

SELECT
    Payment_Method,
    COUNT(*) AS Total_Transactions,
    SUM(Quantity_Sold) AS Total_Quantity_Sold,
    ROUND(SUM(Total_Amount),2) AS Total_Revenue
FROM Sales_Transactions
GROUP BY Payment_Method
ORDER BY Total_Revenue DESC;


DESC Waste_Records;
-- ============================================================
-- Query 18: Top 10 Medicines with Highest Waste Quantity
-- ============================================================
-- Business Question:
-- Which medicines have the highest quantity of waste?
--
-- Business Objective:
-- Identify medicines with the highest wastage to reduce
-- inventory losses and improve stock management.
-- ============================================================

SELECT
    m.Generic_Name,
    SUM(w.Quantity_Wasted) AS Total_Quantity_Wasted
FROM Waste_Records w
JOIN Medicines_Master m
    ON w.Medicine_ID = m.Medicine_ID
GROUP BY m.Generic_Name
ORDER BY Total_Quantity_Wasted DESC
LIMIT 10;

-- ============================================================
-- Query 19: Total Waste Cost by Category
-- ============================================================
-- Business Question:
-- Which medicine categories incur the highest financial loss
-- due to waste?
--
-- Business Objective:
-- Calculate the total waste value across medicine categories
-- to identify areas with the greatest inventory loss.
-- ============================================================

SELECT
    c.Category_Name,
    ROUND(SUM(w.Total_Waste_Value),2) AS Total_Waste_Cost
FROM Waste_Records w
JOIN Medicines_Master m
    ON w.Medicine_ID = m.Medicine_ID
JOIN Category_Master c
    ON m.Category_ID = c.Category_ID
GROUP BY c.Category_Name
ORDER BY Total_Waste_Cost DESC;

-- ============================================================
-- Query 20: Waste Analysis by Reason
-- ============================================================
-- Business Question:
-- What are the primary reasons for medicine waste?
--
-- Business Objective:
-- Analyze waste reasons to identify operational issues
-- and improve inventory management.
-- ============================================================

SELECT
    Waste_Reason,
    COUNT(*) AS Total_Records,
    SUM(Quantity_Wasted) AS Total_Quantity_Wasted,
    ROUND(SUM(Total_Waste_Value),2) AS Total_Waste_Cost
FROM Waste_Records
GROUP BY Waste_Reason
ORDER BY Total_Waste_Cost DESC;

-- ============================================================
-- Query 21: Waste Analysis by Disposal Method
-- ============================================================
-- Business Question:
-- Which disposal methods are used most frequently for
-- pharmaceutical waste?
--
-- Business Objective:
-- Analyze disposal practices to ensure regulatory compliance
-- and sustainable waste management.
-- ============================================================

SELECT
    Disposal_Method,
    COUNT(*) AS Total_Records,
    SUM(Quantity_Wasted) AS Total_Quantity_Wasted,
    ROUND(SUM(Total_Waste_Value),2) AS Total_Waste_Cost
FROM Waste_Records
GROUP BY Disposal_Method
ORDER BY Total_Waste_Cost DESC;

-- ============================================================
-- Query 22: Top 10 Most Profitable Medicines
-- ============================================================
-- Business Question:
-- Which medicines generate the highest total sales revenue?
--
-- Business Objective:
-- Identify the most profitable medicines to support
-- pricing strategies, inventory planning, and marketing.
-- ============================================================

SELECT
    m.Generic_Name,
    ROUND(SUM(s.Total_Amount),2) AS Total_Revenue,
    SUM(s.Quantity_Sold) AS Total_Quantity_Sold
FROM Sales_Transactions s
JOIN Medicines_Master m
    ON s.Medicine_ID = m.Medicine_ID
GROUP BY m.Generic_Name
ORDER BY Total_Revenue DESC
LIMIT 10;

-- ============================================================
-- Query 23: Branch-wise Revenue Analysis
-- ============================================================
-- Business Question:
-- Which pharmacy branches generate the highest revenue?
--
-- Business Objective:
-- Compare branch performance based on sales revenue
-- and transaction volume.
-- ============================================================

SELECT
    Branch_ID,
    COUNT(Transaction_ID) AS Total_Transactions,
    SUM(Quantity_Sold) AS Total_Items_Sold,
    ROUND(SUM(Total_Amount),2) AS Total_Revenue
FROM Sales_Transactions
GROUP BY Branch_ID
ORDER BY Total_Revenue DESC;

-- ============================================================
-- Query 24: Customer Type Sales Analysis
-- ============================================================
-- Business Question:
-- How does sales performance vary across customer types?
--
-- Business Objective:
-- Analyze customer segments based on revenue and
-- purchasing behavior.
-- ============================================================

SELECT
    Customer_Type,
    COUNT(Transaction_ID) AS Total_Transactions,
    SUM(Quantity_Sold) AS Total_Quantity_Sold,
    ROUND(SUM(Total_Amount),2) AS Total_Revenue,
    ROUND(AVG(Total_Amount),2) AS Average_Bill_Value
FROM Sales_Transactions
GROUP BY Customer_Type
ORDER BY Total_Revenue DESC;

-- ============================================================
-- Query 25: Executive Business KPI Dashboard
-- ============================================================
-- Business Question:
-- What are the overall business KPIs for the pharmacy?
--
-- Business Objective:
-- Provide a single dashboard query summarizing the
-- pharmacy's key operational and financial metrics.
-- ============================================================

SELECT
    (SELECT COUNT(*) FROM Medicines_Master) AS Total_Medicines,
    (SELECT COUNT(*) FROM Suppliers_Master) AS Total_Suppliers,
    (SELECT COUNT(*) FROM Medicines_Inventory) AS Inventory_Records,
    (SELECT COUNT(*) FROM Sales_Transactions) AS Total_Transactions,
    (SELECT ROUND(SUM(Total_Amount),2) FROM Sales_Transactions) AS Total_Revenue,
    (SELECT ROUND(SUM(Quantity_In_Stock * Unit_Cost),2)
        FROM Medicines_Inventory) AS Inventory_Value,
    (SELECT ROUND(SUM(w.Waste_Quantity * i.Unit_Cost),2)
        FROM Waste_Records w
        JOIN Medicines_Inventory i
            ON w.Inventory_ID = i.Inventory_ID) AS Total_Waste_Cost;