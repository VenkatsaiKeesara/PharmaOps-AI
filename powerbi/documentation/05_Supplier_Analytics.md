# 🚚 Supplier Analytics

## Dashboard Name

Supplier Analytics

---

# Objective

The Supplier Analytics dashboard evaluates supplier performance, delivery efficiency, reliability, and supplier-related operational risks. It helps procurement teams identify high-performing suppliers, monitor lead times, and improve purchasing decisions.

---

# Target Audience

- Procurement Manager
- Supply Chain Manager
- Inventory Manager
- Operations Manager
- Business Analyst

---

# Business Problem

Supplier performance directly impacts inventory availability, medicine procurement, and customer satisfaction. Delayed deliveries or unreliable suppliers can lead to stock shortages, increased operational costs, and reduced business performance.

---

# Business Questions

1. What is the average supplier rating?
2. What is the average supplier lead time?
3. How well are suppliers performing?
4. How many suppliers are classified as high risk?
5. How many active suppliers are currently available?

---

# KPIs Implemented

| KPI | Business Purpose |
|------|------------------|
| SUP_Average Supplier Rating | Measures supplier quality and reliability. |
| SUP_Average Lead Time | Measures average delivery time. |
| SUP_Average Supplier Performance Index | Evaluates supplier operational performance. |
| SUP_High Risk Suppliers | Counts suppliers categorized as high risk. |
| SUP_Total Active Suppliers | Counts currently active suppliers. |

---

# DAX Measures Created

| Measure | Aggregation |
|----------|-------------|
| SUP_Average Supplier Rating | AVERAGE |
| SUP_Average Lead Time | AVERAGE |
| SUP_Average Supplier Performance Index | AVERAGE |
| SUP_High Risk Suppliers | CALCULATE + DISTINCTCOUNT |
| SUP_Total Active Suppliers | CALCULATE + DISTINCTCOUNT |

---

# Expected Visuals

- KPI Cards
- Supplier Rating Distribution
- Lead Time Comparison
- Supplier Performance Ranking
- High Risk Supplier Analysis
- Active Supplier Summary
- Matrix/Table

*(Visuals will be finalized during dashboard development.)*

---

# Planned Filters

- Supplier
- Category
- Medicine
- Date
- Supplier Category
- State

---

# Expected Insights

The dashboard should help identify:

- Best-performing suppliers.
- Suppliers with long lead times.
- High-risk suppliers.
- Active supplier coverage.
- Procurement improvement opportunities.

---

# Business Decisions Supported

- Supplier selection.
- Procurement optimization.
- Vendor performance evaluation.
- Lead time reduction.
- Supplier risk management.

---

# Data Sources

### Fact Table

- Fact_Medicine_Performance

### Dimension Tables

- Dim_Supplier
- Dim_Medicine
- Dim_Category
- Dim_Date

---

# Dashboard Navigation

Previous Page

- Waste & Expiry Analytics

Next Page

- AI Recommendation Center

---

# Development Status

| Module | Status |
|---------|--------|
| Data Model | ✅ Completed |
| Relationships | ✅ Completed |
| Supplier KPIs | ✅ Completed |
| DAX Measures | ✅ Completed |
| Visual Design | ⏳ Pending |
| Dashboard Development | ⏳ Pending |
| Testing | ⏳ Pending |

---

# Future Enhancements

- Supplier scorecards.
- Lead time trend analysis.
- Supplier benchmarking.
- AI procurement recommendations.
- Supplier contract analysis.

---

# Notes

This dashboard provides procurement teams with actionable supplier insights to improve purchasing efficiency and reduce operational risks.

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