USE PharmaOps_AI;

-- ============================================================
-- View 1: Inventory Overview
-- ============================================================
-- Business Purpose:
-- Provides a consolidated inventory view by combining medicine,
-- supplier, and inventory information. This view enables users
-- to monitor stock availability, pricing, supplier details,
-- batch information, and expiry dates from a single source.
--
-- Business Benefits:
-- • Simplifies inventory reporting.
-- • Eliminates repetitive JOIN operations.
-- • Supports dashboard development.
-- • Enables faster inventory analysis.
-- ============================================================

CREATE VIEW vw_inventory_overview AS

SELECT
    i.Inventory_ID,
    m.Medicine_ID,
    m.Generic_Name,
    m.Brand_Name,
    c.Category_Name,
    s.Supplier_Name,
    i.Batch_Number,
    i.Quantity_In_Stock,
    i.Unit_Cost,
    i.Selling_Price,
    i.Stock_Status,
    i.Expiry_Date

FROM Medicines_Inventory i

INNER JOIN Medicines_Master m
ON i.Medicine_ID = m.Medicine_ID

INNER JOIN Category_Master c
ON m.Category_ID = c.Category_ID

INNER JOIN Suppliers_Master s
ON i.Supplier_ID = s.Supplier_ID;


-- ============================================================
-- View 2: Sales Transaction Overview
-- ============================================================
-- Business Purpose:
-- Provides a unified view of sales transactions along with
-- medicine and category information for business reporting
-- and sales performance analysis.
--
-- Business Benefits:
-- • Simplifies sales reporting.
-- • Supports revenue analysis.
-- • Reduces repetitive SQL joins.
-- • Useful for Power BI dashboards.
-- ============================================================

CREATE VIEW vw_sales_overview AS

SELECT
    st.Transaction_ID,
    st.Invoice_Number,
    st.Transaction_Date,
    m.Generic_Name,
    m.Brand_Name,
    c.Category_Name,
    st.Quantity_Sold,
    st.Unit_Selling_Price,
    st.Discount_Percentage,
    st.Total_Amount,
    st.Payment_Method,
    st.Customer_Type,
    st.Transaction_Status

FROM Sales_Transactions st

INNER JOIN Medicines_Master m
ON st.Medicine_ID = m.Medicine_ID

INNER JOIN Category_Master c
ON m.Category_ID = c.Category_ID;


-- ============================================================
-- View 3: Waste Management Overview
-- ============================================================
-- Business Purpose:
-- Combines waste records with medicine and category details
-- to monitor expired, damaged, or discarded medicines and
-- evaluate their financial impact.
--
-- Business Benefits:
-- • Supports waste monitoring.
-- • Helps identify high-loss medicines.
-- • Enables regulatory reporting.
-- • Assists inventory optimization.
-- ============================================================

CREATE VIEW vw_waste_overview AS

SELECT
    w.Waste_Record_ID,
    m.Generic_Name,
    m.Brand_Name,
    c.Category_Name,
    w.Batch_Number,
    w.Waste_Date,
    w.Expiry_Date,
    w.Quantity_Wasted,
    w.Unit_Cost,
    w.Total_Waste_Value,
    w.Waste_Reason,
    w.Disposal_Method,
    w.Disposal_Status

FROM Waste_Records w

INNER JOIN Medicines_Master m
ON w.Medicine_ID = m.Medicine_ID

INNER JOIN Category_Master c
ON m.Category_ID = c.Category_ID;


-- ============================================================
-- View 4: Supplier Performance Overview
-- ============================================================
-- Business Purpose:
-- Displays supplier information required for procurement,
-- vendor evaluation, and purchasing decisions.
--
-- Business Benefits:
-- • Simplifies supplier evaluation.
-- • Supports procurement planning.
-- • Tracks supplier performance.
-- • Enables vendor comparison.
-- ============================================================

CREATE VIEW vw_supplier_performance AS

SELECT
    Supplier_ID,
    Supplier_Name,
    Supplier_Category,
    Contact_Person,
    City,
    State,
    Supplier_Rating,
    Lead_Time_Days,
    Preferred_Supplier,
    Active_Status

FROM Suppliers_Master;

-- ============================================================
-- View 5: Low Stock Medicines
-- ============================================================
-- Business Purpose:
-- Identifies medicines whose available stock has fallen
-- below the predefined reorder level. This view helps the
-- inventory team prioritize replenishment activities.
--
-- Business Benefits:
-- • Supports proactive inventory management.
-- • Prevents stock shortages.
-- • Improves medicine availability.
-- • Assists procurement planning.
-- ============================================================

CREATE VIEW vw_low_stock_medicines AS

SELECT
    i.Inventory_ID,
    m.Medicine_ID,
    m.Generic_Name,
    m.Brand_Name,
    c.Category_Name,
    s.Supplier_Name,
    i.Batch_Number,
    i.Quantity_In_Stock,
    i.Reorder_Level,
    i.Stock_Status

FROM Medicines_Inventory i

INNER JOIN Medicines_Master m
ON i.Medicine_ID = m.Medicine_ID

INNER JOIN Category_Master c
ON m.Category_ID = c.Category_ID

INNER JOIN Suppliers_Master s
ON i.Supplier_ID = s.Supplier_ID

WHERE i.Quantity_In_Stock <= i.Reorder_Level;

-- ============================================================
-- View 6: Near Expiry Medicines
-- ============================================================
-- Business Purpose:
-- Displays medicines approaching their expiry date within
-- the next 90 days, enabling timely stock rotation and
-- minimizing financial losses due to expiration.
--
-- Business Benefits:
-- • Reduces medicine wastage.
-- • Supports FEFO inventory strategy.
-- • Improves inventory planning.
-- • Enables timely promotional actions.
-- ============================================================

CREATE VIEW vw_near_expiry_medicines AS

SELECT
    i.Inventory_ID,
    m.Medicine_ID,
    m.Generic_Name,
    m.Brand_Name,
    c.Category_Name,
    i.Batch_Number,
    i.Quantity_In_Stock,
    i.Expiry_Date,
    DATEDIFF(i.Expiry_Date, CURDATE()) AS Days_To_Expiry

FROM Medicines_Inventory i

INNER JOIN Medicines_Master m
ON i.Medicine_ID = m.Medicine_ID

INNER JOIN Category_Master c
ON m.Category_ID = c.Category_ID

WHERE i.Expiry_Date
BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 90 DAY);

-- ============================================================
-- View 7: Category Inventory Summary
-- ============================================================
-- Business Purpose:
-- Provides category-wise inventory statistics including
-- total medicines, stock quantity, inventory value,
-- and average selling price for management reporting.
--
-- Business Benefits:
-- • Supports category performance analysis.
-- • Simplifies inventory reporting.
-- • Helps identify high-value categories.
-- • Enables executive decision-making.
-- ============================================================

CREATE VIEW vw_category_inventory_summary AS

SELECT

    c.Category_Name,

    COUNT(DISTINCT m.Medicine_ID) AS Total_Medicines,

    SUM(i.Quantity_In_Stock) AS Total_Stock,

    SUM(i.Quantity_In_Stock * i.Unit_Cost) AS Inventory_Value,

    ROUND(AVG(i.Selling_Price),2) AS Average_Selling_Price

FROM Category_Master c

INNER JOIN Medicines_Master m
ON c.Category_ID = m.Category_ID

INNER JOIN Medicines_Inventory i
ON m.Medicine_ID = i.Medicine_ID

GROUP BY c.Category_Name;

-- ============================================================
-- View 8: Monthly Sales Summary
-- ============================================================
-- Business Purpose:
-- Summarizes monthly sales performance by calculating
-- transaction volume, quantity sold, and revenue generated.
-- This view supports business trend analysis over time.
--
-- Business Benefits:
-- • Enables monthly sales reporting.
-- • Supports trend analysis.
-- • Tracks revenue performance.
-- • Useful for executive dashboards.
-- ============================================================

CREATE VIEW vw_monthly_sales_summary AS

SELECT

    DATE_FORMAT(Transaction_Date,'%Y-%m') AS Sales_Month,

    COUNT(Transaction_ID) AS Total_Transactions,

    SUM(Quantity_Sold) AS Total_Quantity_Sold,

    ROUND(SUM(Total_Amount),2) AS Total_Revenue,

    ROUND(AVG(Total_Amount),2) AS Average_Transaction_Value

FROM Sales_Transactions

GROUP BY DATE_FORMAT(Transaction_Date,'%Y-%m')

ORDER BY Sales_Month;


-- View 1
SELECT * FROM vw_inventory_overview;

-- View 2
SELECT * FROM vw_sales_overview;

-- View 3
SELECT * FROM vw_waste_overview;

-- View 4
SELECT * FROM vw_supplier_performance;

-- View 5
SELECT * FROM vw_low_stock_medicines;

-- View 6
SELECT * FROM vw_near_expiry_medicines;

-- View 7
SELECT * FROM vw_category_inventory_summary;

-- View 8
SELECT * FROM vw_monthly_sales_summary;