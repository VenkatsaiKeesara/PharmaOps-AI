# Sales Transactions Dataset Business Rules

## Project

PharmaOps AI – AI-Powered Pharmacy Inventory & Drug Waste Optimization Platform

---

# Dataset Name

Sales_Transactions.csv

---

# Dataset Description

The Sales Transactions dataset records every medicine sale processed across pharmacy branches. It captures transaction details including medicines sold, branch information, billing amount, discounts, payment methods, customer type, prescription requirements, pharmacists, and transaction status. This dataset supports revenue analysis, customer behavior analysis, inventory consumption tracking, business intelligence dashboards, and AI-powered sales forecasting.

---

# Primary Key

Transaction_ID

Format:

TXN000001

---

# Business Rules

## BR-001 : Unique Transaction ID

Every sales transaction must have a unique Transaction_ID.

Example:

TXN000001

---

## BR-002 : Unique Invoice Number

Each transaction must have a unique Invoice_Number.

Format:

INV2026000001

---

## BR-003 : Medicine Reference

Each transaction must reference a valid Medicine_ID from Medicines_Master.

Example:

MED000001

---

## BR-004 : Branch Reference

Each transaction must belong to a valid pharmacy branch.

Allowed values:

BR001

BR002

BR003

BR004

BR005

---

## BR-005 : Transaction Date

Transaction_Date must:

- Not be in the future
- Fall within the last two years

---

## BR-006 : Sale Time

Sale_Time must fall within pharmacy operating hours.

Allowed Time:

08:00 AM

to

10:00 PM

---

## BR-007 : Quantity Sold

Quantity_Sold must be between:

1 and 10 Units

Weighted distribution should favor smaller purchases.

---

## BR-008 : Unit Selling Price

Unit_Selling_Price must be between:

₹10 and ₹1200

---

## BR-009 : Discount Percentage

Allowed values:

0%

5%

10%

15%

20%

Most transactions should have either no discount or a 5% discount.

---

## BR-010 : Total Amount

Total_Amount must be calculated as:

Quantity_Sold × Unit_Selling_Price

Minus Discount Percentage

Rounded to two decimal places.

---

## BR-011 : Payment Method

Allowed values:

Cash

UPI

Card

Insurance

UPI should be the most frequently used payment method.

---

## BR-012 : Customer Type

Allowed values:

Walk-in

Member

Online

Walk-in customers should represent the majority of transactions.

---

## BR-013 : Prescription Required

Allowed values:

Yes

No

Most transactions should not require a prescription.

---

## BR-014 : Pharmacist

Each transaction must be handled by one pharmacist.

Allowed IDs:

PH001

to

PH015

---

## BR-015 : Transaction Status

Allowed values:

Completed

Returned

Cancelled

Most transactions should be Completed.

---

## BR-016 : Missing Values

No missing values are allowed in the dataset.

---

## BR-017 : Duplicate Records

Duplicate Transaction_ID values are not allowed.

Duplicate Invoice_Number values are not allowed.

---

# Expected Dataset Size

Approximately 10,000 Records

---

# Output File

data/synthetic/Sales_Transactions.csv

---

# Validation Requirements

The validation script must verify:

- Dataset structure
- Required columns
- Missing values
- Duplicate Transaction_ID
- Duplicate Invoice_Number
- Transaction_ID format
- Invoice_Number format
- Medicine_ID format
- Branch_ID validation
- Transaction_Date validation
- Sale_Time validation
- Quantity_Sold validation
- Unit_Selling_Price validation
- Discount_Percentage validation
- Total_Amount calculation
- Payment_Method validation
- Customer_Type validation
- Prescription_Required validation
- Pharmacist_ID validation
- Transaction_Status validation
- Dataset summary
- Final PASS / FAIL status

---

# Expected Columns

1. Transaction_ID
2. Invoice_Number
3. Medicine_ID
4. Branch_ID
5. Transaction_Date
6. Sale_Time
7. Quantity_Sold
8. Unit_Selling_Price
9. Discount_Percentage
10. Total_Amount
11. Payment_Method
12. Customer_Type
13. Prescription_Required
14. Pharmacist_ID
15. Transaction_Status

---

# Dataset Version

Version 1.0