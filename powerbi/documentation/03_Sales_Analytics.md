# 💰 Sales Analytics

## Dashboard Name

Sales Analytics

---

# Objective

The Sales Analytics dashboard provides insights into pharmacy sales performance, revenue generation, profitability, and pricing efficiency. It helps business users evaluate sales trends and identify opportunities to maximize revenue and profit.

---

# Target Audience

- CEO
- Sales Manager
- Pharmacy Manager
- Business Analyst
- Finance Team

---

# Business Problem

Pharmacies need a clear understanding of revenue generation, sales performance, pricing efficiency, and profitability to make informed business decisions. This dashboard consolidates key sales KPIs into one analytical view.

---

# Business Questions

1. How much revenue has been generated?
2. What is the total quantity of medicines sold?
3. What is the average revenue earned per transaction?
4. What is the average revenue earned per unit sold?
5. What is the total potential sales value?
6. What is the average profit earned per unit?
7. How well are medicines performing in terms of sales?
8. What is the average markup percentage?

---

# KPIs Implemented

| KPI | Business Purpose |
|------|------------------|
| SAL_Total Quantity Sold | Calculates total units sold. |
| SAL_Total Revenue | Calculates total revenue generated. |
| SAL_Average Revenue per Transaction | Measures average revenue per transaction. |
| SAL_Average Revenue per Unit | Measures average revenue generated per unit sold. |
| SAL_Total Potential Sales Value | Calculates maximum potential sales value. |
| SAL_Average Profit per Unit | Measures average profit earned per unit. |
| SAL_Average Sales Performance Score | Evaluates overall sales performance. |
| SAL_Average Markup Percentage | Measures average pricing markup. |

---

# DAX Measures Created

| Measure | Aggregation |
|----------|-------------|
| SAL_Total Quantity Sold | SUM |
| SAL_Total Revenue | SUM |
| SAL_Average Revenue per Transaction | AVERAGE |
| SAL_Average Revenue per Unit | AVERAGE |
| SAL_Total Potential Sales Value | SUM |
| SAL_Average Profit per Unit | AVERAGE |
| SAL_Average Sales Performance Score | AVERAGE |
| SAL_Average Markup Percentage | AVERAGE |

---

# Expected Visuals

- KPI Cards
- Revenue Trend
- Sales by Category
- Sales by Medicine
- Profitability Analysis
- Revenue Distribution
- Top Performing Medicines
- Sales Performance Matrix

*(Visuals will be finalized during dashboard development.)*

---

# Planned Filters

- Date
- Medicine
- Category
- Supplier
- ABC Class
- Movement Type

---

# Expected Insights

The dashboard should help identify:

- Overall revenue performance.
- Sales volume.
- High-performing medicines.
- Revenue efficiency.
- Profitability trends.
- Pricing effectiveness.
- Sales opportunities.

---

# Business Decisions Supported

- Pricing strategy.
- Revenue optimization.
- Product performance evaluation.
- Sales planning.
- Profitability improvement.
- Business growth initiatives.

---

# Data Sources

### Fact Table

- Fact_Medicine_Performance

### Dimension Tables

- Dim_Medicine
- Dim_Category
- Dim_Supplier
- Dim_Date

---

# Dashboard Navigation

Previous Page

- Inventory Analytics

Next Page

- Waste & Expiry Analytics

---

# Development Status

| Module | Status |
|---------|--------|
| Data Model | ✅ Completed |
| Relationships | ✅ Completed |
| Sales KPIs | ✅ Completed |
| DAX Measures | ✅ Completed |
| Visual Design | ⏳ Pending |
| Dashboard Development | ⏳ Pending |
| Testing | ⏳ Pending |

---

# Future Enhancements

- Monthly sales trends.
- Product growth analysis.
- Revenue forecasting.
- Customer purchase behavior.
- Sales target tracking.

---

# Notes

This dashboard focuses on revenue generation, sales efficiency, and profitability to support strategic business growth.

---

# Page Completion Checklist

- [x] Business Questions Defined
- [x] KPIs Identified
- [x] DAX Measures Created
- [ ] Visuals Designed
- [ ] Theme Applied
- [ ] Navigation Added
- [ ] Tooltips Configured
- [ ] Testing Completed
- [ ] Screenshots Captured
- [ ] Documentation Completed