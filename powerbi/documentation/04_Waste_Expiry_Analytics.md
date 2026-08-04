# 🗑️ Waste & Expiry Analytics

## Dashboard Name

Waste & Expiry Analytics

---

# Objective

The Waste & Expiry Analytics dashboard monitors medicine waste, expiry risks, and financial losses caused by expired or damaged inventory. It enables pharmacy managers to reduce waste, optimize inventory rotation, and improve operational efficiency.

---

# Target Audience

- Pharmacy Manager
- Inventory Manager
- Operations Manager
- Business Analyst
- Executive Management

---

# Business Problem

Medicine expiry and inventory waste directly impact profitability and operational efficiency. This dashboard helps identify waste patterns, monitor expiry risks, and support proactive inventory management.

---

# Business Questions

1. How many medicines have been wasted?
2. What is the total financial loss due to waste?
3. What is the average waste percentage?
4. What is the average waste cost ratio?
5. How many days remain before medicines expire?
6. How many medicines are nearing expiry?
7. What is the overall waste risk?
8. What is the executive risk associated with waste?

---

# KPIs Implemented

| KPI | Business Purpose |
|------|------------------|
| WST_Total Waste Quantity | Calculates total quantity of medicines wasted. |
| WST_Total Waste Value | Calculates total financial loss due to waste. |
| WST_Average Waste Percentage | Measures average waste percentage. |
| WST_Average Waste Cost Ratio | Measures waste cost relative to inventory value. |
| WST_Average Days to Expiry | Measures remaining shelf life. |
| WST_Near Expiry Count | Counts medicines approaching expiry. |
| WST_Average Waste Risk | Measures average waste risk score. |
| WST_Average Executive Risk Score | Measures operational risk from waste and expiry. |

---

# DAX Measures Created

| Measure | Aggregation |
|----------|-------------|
| WST_Total Waste Quantity | SUM |
| WST_Total Waste Value | SUM |
| WST_Average Waste Percentage | AVERAGE |
| WST_Average Waste Cost Ratio | AVERAGE |
| WST_Average Days to Expiry | AVERAGE |
| WST_Near Expiry Count | SUM |
| WST_Average Waste Risk | AVERAGE |
| WST_Average Executive Risk Score | AVERAGE |

---

# Expected Visuals

- KPI Cards
- Waste Trend
- Waste by Category
- Waste by Medicine
- Expiry Distribution
- Waste Risk Analysis
- Matrix/Table
- Executive Summary

*(Visuals will be finalized during dashboard development.)*

---

# Planned Filters

- Date
- Medicine
- Category
- Supplier
- Waste Risk
- ABC Class

---

# Expected Insights

The dashboard should help identify:

- Financial impact of medicine waste.
- High-risk medicines.
- Expiry trends.
- Waste patterns.
- Operational risks.
- Waste reduction opportunities.

---

# Business Decisions Supported

- Waste reduction planning.
- Inventory rotation.
- Expiry management.
- Procurement optimization.
- Cost reduction.
- Operational improvement.

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

- Sales Analytics

Next Page

- Supplier Analytics

---

# Development Status

| Module | Status |
|---------|--------|
| Data Model | ✅ Completed |
| Relationships | ✅ Completed |
| Waste KPIs | ✅ Completed |
| DAX Measures | ✅ Completed |
| Visual Design | ⏳ Pending |
| Dashboard Development | ⏳ Pending |
| Testing | ⏳ Pending |

---

# Future Enhancements

- Waste forecasting.
- Expiry prediction.
- AI waste recommendations.
- Automatic clearance alerts.
- Seasonal waste analysis.

---

# Notes

This dashboard focuses on minimizing inventory waste and reducing financial losses through proactive expiry and waste monitoring.

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