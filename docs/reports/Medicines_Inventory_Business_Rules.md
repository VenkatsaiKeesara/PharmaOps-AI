# Medicines Inventory Dataset Business Rules

## Project
PharmaOps AI – AI-Powered Pharmacy Inventory & Drug Waste Optimization Platform

---

# Dataset Name

Medicines_Inventory.csv

---

# Dataset Description

The Medicines Inventory dataset maintains the current inventory of medicines available across pharmacy warehouses. It records stock quantities, pricing, storage requirements, manufacturing details, expiry information, and inventory status. This dataset serves as the central inventory management table and supports stock monitoring, reorder analysis, expiry tracking, supplier performance, and AI-driven inventory optimization.

---

# Primary Key

Inventory_ID

Format:

INV000001

---

# Business Rules

## BR-001 : Unique Inventory ID

Every inventory record must contain a unique Inventory_ID.

Example:

INV000001

INV000002

---

## BR-002 : Medicine Reference

Each inventory record must contain a Medicine_ID following the standard format.

Example:

MED000001

---

## BR-003 : Supplier Reference

Each inventory record must contain a Supplier_ID following the standard format.

Example:

SUP0001

---

## BR-004 : Unique Batch Number

Every medicine batch must have a unique Batch_Number.

Example:

BAT240001

BAT240002

---

## BR-005 : Manufacturing Date

Manufacturing_Date cannot be in the future.

---

## BR-006 : Expiry Date

Expiry_Date must always be later than Manufacturing_Date.

The expiry period should range between 12 and 36 months.

---

## BR-007 : Quantity in Stock

Quantity_In_Stock cannot be negative.

Allowed Range:

0 – 1000 Units

---

## BR-008 : Unit Cost

Unit_Cost must always be greater than zero.

Allowed Range:

₹5 – ₹600

---

## BR-009 : Selling Price

Selling_Price must always be greater than Unit_Cost.

Recommended markup:

20% – 40%

---

## BR-010 : Reorder Level

Reorder_Level represents the minimum quantity before replenishment.

Allowed Range:

25 – 200 Units

---

## BR-011 : Storage Temperature

Allowed values:

• Room Temperature

• Refrigerated (2–8°C)

• Frozen (-20°C)

---

## BR-012 : Warehouse Location

Allowed warehouse codes:

WH-A

WH-B

WH-C

WH-D

WH-E

---

## BR-013 : Stock Status

Stock_Status must be calculated.

Business Logic:

If Quantity_In_Stock = 0

→ Out of Stock

If Quantity_In_Stock ≤ Reorder_Level

→ Low Stock

Otherwise

→ In Stock

---

## BR-014 : Last Restock Date

Last_Restock_Date must always occur after Manufacturing_Date and before the current date.

---

## BR-015 : Missing Values

No missing values are allowed.

---

## BR-016 : Duplicate Records

Duplicate Inventory_ID values are not allowed.

Duplicate Batch_Number values are not allowed.

---

# Expected Dataset Size

Approximately 5,000 Records

---

# Output File

data/synthetic/Medicines_Inventory.csv

---

# Validation Requirements

The validation script must verify:

• Dataset structure

• Required columns

• Missing values

• Duplicate Inventory_ID

• Duplicate Batch_Number

• Date validation

• Cost validation

• Selling price validation

• Quantity validation

• Reorder level validation

• Storage temperature validation

• Warehouse validation

• Stock status calculation

• Final dataset summary

---

Dataset Version

Version 1.0