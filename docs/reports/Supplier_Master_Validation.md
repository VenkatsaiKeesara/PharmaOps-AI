# Suppliers_Master Validation Documentation

## Project

PharmaOps AI – AI-Powered Pharmacy Inventory & Drug Waste Optimization Platform

---

# Validation Script

python/validation/09_validate_suppliers.py

---

# Objective

The purpose of validation is to verify that the generated supplier dataset satisfies all business rules before loading it into the analytics database.

---

# Validation Process

The validation script performs the following checks.

---

## 1 Dataset Overview

Displays

- Number of Records
- Number of Columns
- Memory Usage
- Dataset Preview

---

## 2 Schema Validation

Verifies

Expected Columns

Expected Column Order

Primary Key

---

## 3 Data Type Validation

Checks

Text Columns

Numeric Columns

Date Columns

---

## 4 Missing Value Validation

Ensures

No missing values exist.

---

## 5 Duplicate Validation

Checks

Duplicate Supplier_ID

Duplicate Supplier_Name

Duplicate Contact_Email

Duplicate Contact_Number

Duplicate GST_Number

---

## 6 Lead Time Validation

Allowed Range

Manufacturer

7–20

Distributor

3–10

Wholesaler

2–7

---

## 7 Rating Validation

Manufacturer

4.2–5.0

Distributor

3.8–4.8

Wholesaler

3.5–4.6

---

## 8 Supplier Category Validation

Allowed Values

Domestic

International

---

## 9 Preferred Supplier Validation

Allowed Values

Yes

No

---

## 10 Active Status Validation

Allowed Values

Active

Inactive

---

## 11 Contract Date Validation

Checks

Start Date

Before End Date

Contract Duration

Between

3

and

5 Years

---

## 12 GST Validation

Checks

GST Format

State Code

Uniqueness

---

## 13 Contact Number Validation

Checks

10 Digits

Unique

Numeric

---

## 14 Email Validation

Checks

Valid Email Format

Unique Email

---

## 15 Data Quality Score

Quality Metrics

Completeness

Uniqueness

Validity

Consistency

Business Rule Compliance

---

# Expected Validation Output

Example

==================================================

SUPPLIERS MASTER VALIDATION REPORT

==================================================

Records

75

Columns

15

Missing Values

0

Duplicate Supplier_ID

0

Duplicate Supplier_Name

0

Duplicate Emails

0

Duplicate Phones

0

Duplicate GST

0

Lead Time Validation

PASS

Rating Validation

PASS

Contract Date Validation

PASS

Email Validation

PASS

GST Validation

PASS

Business Rule Validation

PASS

Overall Data Quality Score

100/100

Dataset Status

APPROVED

==================================================

---

# Validation Outcome

A dataset is approved only if

✔ No missing values

✔ No duplicate primary keys

✔ No duplicate business identifiers

✔ Valid data types

✔ Valid lead times

✔ Valid ratings

✔ Valid contract dates

✔ Valid GST numbers

✔ Business Rule Compliance

---

# Next Step

After successful validation, the dataset is approved for

Database Loading

Inventory Generation

Procurement Dataset

Power BI Dashboard

SQL Analytics

Python Analytics

AI Recommendation Engine