-- ============================================================
-- Stored Procedure 1: Get Inventory by Category
-- ============================================================
-- Business Purpose:
-- Retrieves all inventory records belonging to a specified
-- medicine category. This procedure helps inventory managers
-- analyze stock availability within a selected category.
--
-- Business Benefits:
-- • Supports category-wise inventory analysis.
-- • Simplifies inventory reporting.
-- • Eliminates repetitive SQL filtering.
-- • Assists inventory planning.
-- ============================================================

DROP PROCEDURE IF EXISTS sp_GetInventoryByCategory;

DELIMITER $$

CREATE PROCEDURE sp_GetInventoryByCategory(

    IN p_Category_ID VARCHAR(20)

)

BEGIN

SELECT

    c.Category_ID,
    c.Category_Name,
    m.Generic_Name,
    m.Brand_Name,
    i.Batch_Number,
    i.Quantity_In_Stock,
    i.Unit_Cost,
    i.Selling_Price,
    i.Stock_Status

FROM Medicines_Inventory i

INNER JOIN Medicines_Master m
ON i.Medicine_ID = m.Medicine_ID

INNER JOIN Category_Master c
ON m.Category_ID = c.Category_ID

WHERE c.Category_ID = p_Category_ID

ORDER BY m.Generic_Name;

END $$

DELIMITER ;

-- ============================================================
-- Stored Procedure 2: Get Supplier Inventory
-- ============================================================
-- Business Purpose:
-- Retrieves all medicines supplied by a specific supplier
-- along with their inventory details.
--
-- Business Benefits:
-- • Supports supplier performance analysis.
-- • Simplifies procurement reporting.
-- • Tracks supplier inventory contribution.
-- • Assists purchasing decisions.
-- ============================================================

DROP PROCEDURE IF EXISTS sp_GetSupplierInventory;

DELIMITER $$

CREATE PROCEDURE sp_GetSupplierInventory(

    IN p_Supplier_ID VARCHAR(20)

)

BEGIN

SELECT

    s.Supplier_ID,
    s.Supplier_Name,
    s.Supplier_Category,
    m.Generic_Name,
    m.Brand_Name,
    i.Batch_Number,
    i.Quantity_In_Stock,
    i.Unit_Cost,
    i.Selling_Price,
    i.Stock_Status,
    i.Expiry_Date

FROM Medicines_Inventory i

INNER JOIN Suppliers_Master s
ON i.Supplier_ID = s.Supplier_ID

INNER JOIN Medicines_Master m
ON i.Medicine_ID = m.Medicine_ID

WHERE s.Supplier_ID = p_Supplier_ID

ORDER BY m.Generic_Name;

END $$

DELIMITER ;


-- ============================================================
-- Stored Procedure 3: Get Low Stock Medicines
-- ============================================================
-- Business Purpose:
-- Retrieves medicines whose available quantity is less than
-- or equal to the reorder level.
--
-- Business Benefits:
-- • Prevents stock shortages.
-- • Supports inventory replenishment.
-- • Improves medicine availability.
-- • Enables proactive procurement.
-- ============================================================

DELIMITER $$

CREATE PROCEDURE sp_GetLowStockMedicines()

BEGIN

SELECT

    m.Generic_Name,
    m.Brand_Name,
    i.Batch_Number,
    i.Quantity_In_Stock,
    i.Reorder_Level,
    i.Stock_Status

FROM Medicines_Inventory i

INNER JOIN Medicines_Master m
ON i.Medicine_ID = m.Medicine_ID

WHERE i.Quantity_In_Stock <= i.Reorder_Level

ORDER BY i.Quantity_In_Stock;

END $$

DELIMITER ;


-- ============================================================
-- Stored Procedure 4: Get Near Expiry Medicines
-- ============================================================
-- Business Purpose:
-- Retrieves medicines that will expire within a specified
-- number of days to support timely stock rotation.
--
-- Business Benefits:
-- • Reduces medicine wastage.
-- • Supports FEFO implementation.
-- • Improves inventory planning.
-- • Minimizes financial loss.
-- ============================================================

DELIMITER $$

CREATE PROCEDURE sp_GetNearExpiryMedicines(

    IN p_Days INT

)

BEGIN

SELECT

    m.Generic_Name,
    m.Brand_Name,
    i.Batch_Number,
    i.Quantity_In_Stock,
    i.Expiry_Date,
    DATEDIFF(i.Expiry_Date,CURDATE()) AS Days_Remaining

FROM Medicines_Inventory i

INNER JOIN Medicines_Master m
ON i.Medicine_ID = m.Medicine_ID

WHERE i.Expiry_Date
BETWEEN CURDATE()
AND DATE_ADD(CURDATE(),INTERVAL p_Days DAY)

ORDER BY i.Expiry_Date;

END $$

DELIMITER ;

-- ============================================================
-- Stored Procedure 5: Get Sales Report Between Dates
-- ============================================================
-- Business Purpose:
-- Retrieves all completed sales transactions within a specified
-- date range. This procedure supports sales reporting,
-- revenue analysis, and period-wise business performance.
--
-- Business Benefits:
-- • Supports custom sales reporting.
-- • Simplifies period-wise analysis.
-- • Enables revenue tracking.
-- • Assists management decision-making.
-- ============================================================

DELIMITER $$

CREATE PROCEDURE sp_GetSalesReportByDate(

    IN p_Start_Date DATE,
    IN p_End_Date DATE

)

BEGIN

SELECT

    st.Transaction_ID,
    st.Invoice_Number,
    st.Transaction_Date,
    m.Generic_Name,
    st.Quantity_Sold,
    st.Unit_Selling_Price,
    st.Discount_Percentage,
    st.Total_Amount,
    st.Payment_Method,
    st.Customer_Type

FROM Sales_Transactions st

INNER JOIN Medicines_Master m
ON st.Medicine_ID = m.Medicine_ID

WHERE st.Transaction_Date
BETWEEN p_Start_Date
AND p_End_Date

ORDER BY st.Transaction_Date;

END $$

DELIMITER ;

-- ============================================================
-- Stored Procedure 6: Get Category Sales Summary
-- ============================================================
-- Business Purpose:
-- Generates category-wise sales performance by calculating
-- total transactions, quantity sold, and revenue generated
-- for each medicine category.
--
-- Business Benefits:
-- • Supports category performance analysis.
-- • Identifies high-performing categories.
-- • Simplifies revenue reporting.
-- • Supports executive dashboards.
-- ============================================================

DROP PROCEDURE IF EXISTS sp_GetCategorySalesSummary;

DELIMITER $$

CREATE PROCEDURE sp_GetCategorySalesSummary()

BEGIN

    SELECT

        c.Category_Name,

        COUNT(st.Transaction_ID) AS Total_Transactions,

        SUM(st.Quantity_Sold) AS Total_Quantity_Sold,

        ROUND(SUM(st.Total_Amount), 2) AS Total_Revenue

    FROM Sales_Transactions st

    INNER JOIN Medicines_Master m
        ON st.Medicine_ID = m.Medicine_ID

    INNER JOIN Category_Master c
        ON m.Category_ID = c.Category_ID

    GROUP BY
        c.Category_Name

    ORDER BY
        Total_Revenue DESC;

END $$

DELIMITER ;
-- ============================================================
-- Stored Procedure 7: Get Waste Analysis Report
-- ============================================================
-- Business Purpose:
-- Generates waste analysis for a specified date range by
-- summarizing medicine waste quantities and financial losses.
--
-- Business Benefits:
-- • Supports waste monitoring.
-- • Identifies high-loss medicines.
-- • Improves inventory planning.
-- • Assists regulatory reporting.
-- ============================================================

DELIMITER $$

CREATE PROCEDURE sp_GetWasteAnalysis(

    IN p_Start_Date DATE,
    IN p_End_Date DATE

)

BEGIN

SELECT

    m.Generic_Name,

    COUNT(w.Waste_Record_ID) AS Waste_Records,

    SUM(w.Quantity_Wasted) AS Total_Quantity_Wasted,

    ROUND(SUM(w.Total_Waste_Value),2) AS Total_Waste_Value

FROM Waste_Records w

INNER JOIN Medicines_Master m
ON w.Medicine_ID = m.Medicine_ID

WHERE w.Waste_Date
BETWEEN p_Start_Date
AND p_End_Date

GROUP BY m.Generic_Name

ORDER BY Total_Waste_Value DESC;

END $$

DELIMITER ;

-- ============================================================
-- Stored Procedure 8: Pharmacy Executive Dashboard KPIs
-- ============================================================
-- Business Purpose:
-- Generates key business performance indicators required for
-- executive reporting and dashboard visualization.
--
-- Business Benefits:
-- • Provides overall business summary.
-- • Supports executive decision-making.
-- • Eliminates multiple KPI queries.
-- • Improves reporting efficiency.
-- ============================================================

DELIMITER $$

CREATE PROCEDURE sp_GetExecutiveDashboardKPIs()

BEGIN

SELECT

    (SELECT COUNT(*) FROM Medicines_Master) AS Total_Medicines,

    (SELECT COUNT(*) FROM Suppliers_Master) AS Total_Suppliers,

    (SELECT COUNT(*) FROM Medicines_Inventory) AS Inventory_Records,

    (SELECT COUNT(*) FROM Sales_Transactions) AS Total_Transactions,

    (SELECT ROUND(SUM(Total_Amount),2)
     FROM Sales_Transactions) AS Total_Revenue,

    (SELECT ROUND(SUM(Quantity_In_Stock * Unit_Cost),2)
     FROM Medicines_Inventory) AS Inventory_Value,

    (SELECT ROUND(SUM(Total_Waste_Value),2)
     FROM Waste_Records) AS Total_Waste_Cost;

END $$

DELIMITER ;


CALL sp_GetInventoryByCategory('CAT001');

CALL sp_GetSupplierInventory('SUP001');

CALL sp_GetLowStockMedicines();

CALL sp_GetNearExpiryMedicines(90);

CALL sp_GetSalesReportByDate('2024-01-01','2026-12-31');

CALL sp_GetCategorySalesSummary();

CALL sp_GetWasteAnalysis('2024-01-01','2026-12-31');

CALL sp_GetExecutiveDashboardKPIs();