# 📦 Inventory Analytics

## Dashboard Name

Inventory Analytics

---

# Objective

The Inventory Analytics dashboard provides detailed insights into pharmacy inventory levels, stock availability, inventory aging, stock coverage, and expiry risk. It helps inventory managers maintain optimal stock levels while minimizing shortages and excess inventory.

---

# Target Audience

- Inventory Manager
- Pharmacy Manager
- Operations Manager
- Supply Chain Team
- Business Analyst

---

# Business Problem

Poor inventory management can lead to stock shortages, overstocking, expired medicines, and unnecessary inventory holding costs. This dashboard enables proactive inventory monitoring and timely replenishment decisions.

---

# Business Questions

1. How much inventory is currently available?
2. Which medicines are running low?
3. Which medicines are overstocked?
4. Which medicines are out of stock?
5. Which medicines are nearing expiry?
6. What is the average inventory age?
7. How many days remain before inventory expires?
8. Is the current inventory coverage sufficient?

---

# KPIs Implemented

| KPI | Business Purpose |
|------|------------------|
| INV_Total Quantity In Stock | Calculates the total available inventory quantity. |
| INV_Average Days to Expiry | Measures the average remaining shelf life of inventory. |
| INV_Average Inventory Age | Measures the average age of inventory in storage. |
| INV_Low Stock Count | Counts medicines below the reorder level. |
| INV_Overstock Count | Counts medicines with excess inventory. |
| INV_Out of Stock Count | Counts medicines currently unavailable. |
| INV_Near Expiry Count | Counts medicines approaching expiry. |
| INV_Average Stock Coverage Ratio | Measures average inventory coverage relative to demand. |

---

# DAX Measures Created

| Measure | Aggregation |
|----------|-------------|
| INV_Total Quantity In Stock | SUM |
| INV_Average Days to Expiry | AVERAGE |
| INV_Average Inventory Age | AVERAGE |
| INV_Low Stock Count | SUM |
| INV_Overstock Count | SUM |
| INV_Out of Stock Count | SUM |
| INV_Near Expiry Count | SUM |
| INV_Average Stock Coverage Ratio | AVERAGE |

---

# Expected Visuals

The dashboard is planned to include:

- KPI Cards
- Clustered Bar Chart
- Stacked Column Chart
- Line Chart
- Matrix/Table
- Inventory Status Distribution
- ABC Analysis
- Inventory Health Visualization

*(Visuals will be finalized during dashboard design.)*

---

# Planned Filters

- Date
- Medicine
- Category
- Supplier
- ABC Class
- Inventory Criticality

---

# Expected Insights

The dashboard should help identify:

- Current inventory availability.
- Medicines requiring immediate replenishment.
- Overstock situations.
- Out-of-stock medicines.
- Medicines nearing expiry.
- Inventory aging patterns.
- Overall inventory efficiency.

---

# Business Decisions Supported

- Inventory replenishment planning.
- Stock optimization.
- Warehouse management.
- Inventory investment decisions.
- Expiry risk reduction.
- Inventory health improvement.

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

- Executive Overview

Next Page

- Sales Analytics

---

# Development Status

| Module | Status |
|---------|--------|
| Data Model | ✅ Completed |
| Relationships | ✅ Completed |
| Inventory KPIs | ✅ Completed |
| DAX Measures | ✅ Completed |
| Visual Design | ⏳ Pending |
| Dashboard Development | ⏳ Pending |
| Testing | ⏳ Pending |

---

# Future Enhancements

- Inventory forecasting.
- Dynamic reorder recommendations.
- Inventory turnover analysis.
- Safety stock monitoring.
- Automated stock alerts.

---

# Notes

This dashboard focuses on inventory optimization and operational monitoring, enabling proactive inventory management and reducing stock-related risks.

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