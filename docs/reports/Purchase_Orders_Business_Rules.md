# Purchase Orders Dataset Business Rules

## Project

PharmaOps AI – AI-Powered Pharmacy Inventory & Drug Waste Optimization Platform

---

# Dataset Name

Purchase_Orders.csv

---

# Dataset Description

The Purchase Orders dataset records all medicine procurement transactions made by the pharmacy from approved suppliers. It tracks order dates, supplier information, delivery schedules, procurement costs, payment status, warehouse allocation, and procurement managers. This dataset supports procurement analysis, supplier performance evaluation, inventory replenishment, and financial reporting.

---

# Primary Key

Purchase_Order_ID

Format:

PO000001

---

# Business Rules

## BR-001 : Unique Purchase Order ID

Every purchase order must have a unique Purchase_Order_ID.

Example:

PO000001

---

## BR-002 : Medicine Reference

Each order must reference a valid Medicine_ID.

Example:

MED000001

---

## BR-003 : Supplier Reference

Each order must reference a valid Supplier_ID.

Example:

SUP0001

---

## BR-004 : Order Date

Order_Date cannot be in the future.

---

## BR-005 : Expected Delivery Date

Expected_Delivery_Date must always be on or after Order_Date.

---

## BR-006 : Actual Delivery Date

For delivered orders, Actual_Delivery_Date must be on or after Order_Date.

Cancelled orders must not have an Actual_Delivery_Date.

---

## BR-007 : Quantity Ordered

Allowed Range:

50 – 2000 Units

---

## BR-008 : Unit Purchase Cost

Allowed Range:

₹5 – ₹600

---

## BR-009 : Total Order Value

Total_Order_Value = Quantity_Ordered × Unit_Purchase_Cost

---

## BR-010 : Payment Method

Allowed values:

• Bank Transfer

• UPI

• Credit

---

## BR-011 : Payment Status

Allowed values:

• Paid

• Pending

• Partial

---

## BR-012 : Order Status

Allowed values:

• Delivered

• Pending

• Cancelled

---

## BR-013 : Warehouse Location

Allowed warehouse codes:

WH-A

WH-B

WH-C

WH-D

WH-E

---

## BR-014 : Procurement Manager

Each purchase order must be assigned to one procurement manager.

---

## BR-015 : Missing Values

No missing values are allowed except Actual_Delivery_Date for Cancelled or Pending orders.

---

## BR-016 : Duplicate Records

Duplicate Purchase_Order_ID values are not allowed.

---

# Expected Dataset Size

Approximately 3,000 Records

---

# Output File

data/synthetic/Purchase_Orders.csv

---

# Validation Requirements

The validation script must verify:

• Dataset structure

• Required columns

• Missing values

• Duplicate Purchase_Order_ID

• Date validations

• Quantity validation

• Cost validation

• Total order value calculation

• Payment method validation

• Payment status validation

• Order status validation

• Warehouse validation

• Final dataset summary

---

Dataset Version

Version 1.0