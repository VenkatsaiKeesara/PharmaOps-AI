# Waste Records Dataset Business Rules

## Project

PharmaOps AI – AI-Powered Pharmacy Inventory & Drug Waste Optimization Platform

---

# Dataset Name

Waste_Records.csv

---

# Dataset Description

The Waste Records dataset captures medicines that are removed from inventory due to expiry, damage, recalls, contamination, or overstock. It records waste quantity, financial loss, disposal methods, reporting details, and warehouse information. This dataset supports waste analysis, inventory optimization, cost reduction, compliance reporting, and AI-driven recommendations to minimize future medicine wastage.

---

# Primary Key

Waste_Record_ID

Format:

WR000001

---

# Business Rules

## BR-001 : Unique Waste Record ID

Every waste record must have a unique Waste_Record_ID.

Example:

WR000001

---

## BR-002 : Inventory Reference

Each waste record must reference a valid Inventory_ID from the Medicines_Inventory dataset.

Example:

INV000001

---

## BR-003 : Medicine Reference

Each waste record must reference a valid Medicine_ID from the Medicines_Master dataset.

Example:

MED000001

---

## BR-004 : Batch Reference

Each waste record must contain a valid Batch_Number corresponding to the inventory batch.

---

## BR-005 : Waste Date

Waste_Date must:

- Not be in the future
- Fall within the last two years

---

## BR-006 : Expiry Date

Expiry_Date must be on or before the Waste_Date for expired medicines.

For other waste reasons, Expiry_Date must still be a valid date from the inventory batch.

---

## BR-007 : Quantity Wasted

Quantity_Wasted must be between:

1 and 200 Units

---

## BR-008 : Unit Cost

Unit_Cost must be between:

₹5 and ₹600

---

## BR-009 : Total Waste Value

Total_Waste_Value must be calculated as:

Quantity_Wasted × Unit_Cost

Rounded to two decimal places.

---

## BR-010 : Waste Reason

Allowed values:

- Expired
- Damaged
- Recalled
- Contaminated
- Overstock

Suggested distribution:

- Expired → 50%
- Damaged → 20%
- Overstock → 15%
- Recalled → 10%
- Contaminated → 5%

---

## BR-011 : Disposal Method

Allowed values:

- Incineration
- Return to Supplier
- Biohazard Disposal
- Recycling

---

## BR-012 : Disposal Status

Allowed values:

- Completed
- Pending

Suggested distribution:

- Completed → 90%
- Pending → 10%

---

## BR-013 : Reported By

Each waste record must be reported by an employee.

Allowed Employee IDs:

EMP001

to

EMP020

---

## BR-014 : Warehouse Location

Allowed warehouse codes:

WH-A

WH-B

WH-C

WH-D

WH-E

---

## BR-015 : Remarks

Remarks should describe the waste event.

Examples:

- Expired during monthly audit
- Damaged during transportation
- Manufacturer recall
- Packaging contamination
- Overstock disposal

---

## BR-016 : Missing Values

No missing values are allowed.

---

## BR-017 : Duplicate Records

Duplicate Waste_Record_ID values are not allowed.

---

# Expected Dataset Size

Approximately 2,500 Records

---

# Output File

data/synthetic/Waste_Records.csv

---

# Validation Requirements

The validation script must verify:

- Dataset structure
- Required columns
- Missing values
- Duplicate Waste_Record_ID
- Waste_Record_ID format
- Inventory_ID format
- Medicine_ID format
- Batch_Number format
- Waste_Date validation
- Expiry_Date validation
- Quantity_Wasted validation
- Unit_Cost validation
- Total_Waste_Value calculation
- Waste_Reason validation
- Disposal_Method validation
- Disposal_Status validation
- Reported_By validation
- Warehouse_Location validation
- Remarks validation
- Dataset summary
- Final PASS / FAIL status

---

# Expected Columns

1. Waste_Record_ID
2. Inventory_ID
3. Medicine_ID
4. Batch_Number
5. Waste_Date
6. Expiry_Date
7. Quantity_Wasted
8. Unit_Cost
9. Total_Waste_Value
10. Waste_Reason
11. Disposal_Method
12. Disposal_Status
13. Reported_By
14. Warehouse_Location
15. Remarks

---

# Dataset Version

Version 1.0