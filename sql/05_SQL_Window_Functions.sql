-- ============================================================
-- Window Function 1: Rank Medicines by Revenue
-- ============================================================
-- Business Purpose:
-- Ranks medicines based on total revenue generated from sales.
--
-- Business Benefits:
-- • Identifies top revenue-generating medicines.
-- • Supports sales strategy.
-- • Helps inventory prioritization.
-- ============================================================

SELECT

    m.Generic_Name,

    SUM(st.Total_Amount) AS Total_Revenue,

    RANK() OVER (
        ORDER BY SUM(st.Total_Amount) DESC
    ) AS Revenue_Rank

FROM Sales_Transactions st

JOIN Medicines_Master m
ON st.Medicine_ID = m.Medicine_ID

GROUP BY
    m.Generic_Name;
    
    
-- ============================================================
-- Window Function 2: Category Revenue Ranking
-- ============================================================

SELECT

    c.Category_Name,

    SUM(st.Total_Amount) AS Revenue,

    DENSE_RANK() OVER(

        ORDER BY SUM(st.Total_Amount) DESC

    ) AS Category_Rank

FROM Sales_Transactions st

JOIN Medicines_Master m
ON st.Medicine_ID=m.Medicine_ID

JOIN Category_Master c
ON m.Category_ID=c.Category_ID

GROUP BY
c.Category_Name;


-- ============================================================
-- Window Function 3: Running Monthly Revenue
-- ============================================================

SELECT

DATE_FORMAT(Transaction_Date,'%Y-%m') AS Sales_Month,

SUM(Total_Amount) AS Monthly_Revenue,

SUM(SUM(Total_Amount))
OVER(

ORDER BY DATE_FORMAT(Transaction_Date,'%Y-%m')

) AS Running_Revenue

FROM Sales_Transactions

GROUP BY
DATE_FORMAT(Transaction_Date,'%Y-%m');


-- ============================================================
-- Window Function 4: Compare Monthly Revenue
-- ============================================================

SELECT

Sales_Month,

Monthly_Revenue,

LAG(Monthly_Revenue)
OVER(
ORDER BY Sales_Month
) AS Previous_Month

FROM(

SELECT

DATE_FORMAT(Transaction_Date,'%Y-%m') Sales_Month,

SUM(Total_Amount) Monthly_Revenue

FROM Sales_Transactions

GROUP BY DATE_FORMAT(Transaction_Date,'%Y-%m')

)x;

-- ============================================================
-- Window Function 5: Next Month Revenue
-- ============================================================

SELECT

Sales_Month,

Monthly_Revenue,

LEAD(Monthly_Revenue)
OVER(
ORDER BY Sales_Month
) AS Next_Month

FROM(

SELECT

DATE_FORMAT(Transaction_Date,'%Y-%m') Sales_Month,

SUM(Total_Amount) Monthly_Revenue

FROM Sales_Transactions

GROUP BY DATE_FORMAT(Transaction_Date,'%Y-%m')

)x;

-- ============================================================
-- Window Function 6: Revenue Contribution
-- ============================================================

SELECT

m.Generic_Name,

SUM(st.Total_Amount) Revenue,

ROUND(

100*SUM(st.Total_Amount)

/

SUM(SUM(st.Total_Amount))
OVER(),

2

) AS Revenue_Percentage

FROM Sales_Transactions st

JOIN Medicines_Master m
ON st.Medicine_ID=m.Medicine_ID

GROUP BY
m.Generic_Name;

-- ============================================================
-- Window Function 7: Supplier Inventory Ranking
-- ============================================================

SELECT

s.Supplier_Name,

SUM(i.Quantity_In_Stock*i.Unit_Cost) Inventory_Value,

ROW_NUMBER()
OVER(

ORDER BY SUM(i.Quantity_In_Stock*i.Unit_Cost) DESC

) Supplier_Rank

FROM Medicines_Inventory i

JOIN Suppliers_Master s
ON i.Supplier_ID=s.Supplier_ID

GROUP BY
s.Supplier_Name;


-- ============================================================
-- Window Function 8: Running Waste Cost
-- ============================================================

SELECT

Waste_Date,

SUM(Total_Waste_Value) Daily_Waste,

SUM(SUM(Total_Waste_Value))
OVER(

ORDER BY Waste_Date

) Running_Waste

FROM Waste_Records

GROUP BY
Waste_Date;


-- ============================================================
-- Window Function 9: Top Medicine Per Category
-- ============================================================

SELECT *

FROM(

SELECT

c.Category_Name,

m.Generic_Name,

SUM(st.Total_Amount) Revenue,

ROW_NUMBER()
OVER(

PARTITION BY c.Category_Name

ORDER BY SUM(st.Total_Amount) DESC

) rn

FROM Sales_Transactions st

JOIN Medicines_Master m
ON st.Medicine_ID=m.Medicine_ID

JOIN Category_Master c
ON m.Category_ID=c.Category_ID

GROUP BY

c.Category_Name,

m.Generic_Name

)x

WHERE rn=1;

-- ============================================================
-- Window Function 10: 3-Month Moving Average Revenue
-- ============================================================

SELECT

Sales_Month,

Monthly_Revenue,

AVG(Monthly_Revenue)
OVER(

ORDER BY Sales_Month

ROWS BETWEEN 2 PRECEDING

AND CURRENT ROW

) Moving_Average

FROM(

SELECT

DATE_FORMAT(Transaction_Date,'%Y-%m') Sales_Month,

SUM(Total_Amount) Monthly_Revenue

FROM Sales_Transactions

GROUP BY DATE_FORMAT(Transaction_Date,'%Y-%m')

)x;