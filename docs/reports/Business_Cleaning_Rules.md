# Business Cleaning Rules

## Project Information

| Field | Value |
|-------|-------|
| Project | PharmaOps AI – Pharmacy Inventory & Drug Waste Optimization |
| Module | 03_clean_medicines.py |
| Version | 1.0 |
| Author | Venkatsai Keesara |
| Date | July 2026 |
| Dataset | FDA National Drug Code (NDC) Directory |

---

# Purpose

This document defines the business rules used to clean, standardize, validate, and transform the FDA NDC dataset into a production-ready medicine master dataset.

The purpose of these rules is to ensure that the final dataset is suitable for:

- Pharmacy Inventory Analytics
- Procurement Analytics
- Drug Waste Analysis
- Inventory Optimization
- Executive Dashboards
- AI-powered Business Recommendations

These rules are implemented in the ETL pipeline through the `03_clean_medicines.py` script.

---

# Business Cleaning Rules

# Business Cleaning Rules

## Project Information

| Field | Value |
|-------|-------|
| Project | PharmaOps AI – Pharmacy Inventory & Drug Waste Optimization |
| Module | 03_clean_medicines.py |
| Version | 1.0 |
| Author | Venkatsai Keesara |
| Dataset | FDA National Drug Code (NDC) Directory |

---

# Purpose

This document defines the business rules used to clean, standardize, validate, and transform the FDA National Drug Code (NDC) dataset into a production-ready medicine master dataset.

The cleaned dataset will be used for:

- Pharmacy Inventory Analytics
- Procurement Analytics
- Drug Waste Analysis
- Executive Dashboards
- AI-powered Decision Support
- Inventory Optimization

These rules will be implemented in the ETL pipeline through `03_clean_medicines.py`.

---

# Business Cleaning Rules

---

## BR-001 – Filter Product Types

### Objective
Retain only products relevant to hospital and pharmacy inventory management.

### Keep
- HUMAN PRESCRIPTION DRUG
- HUMAN OTC DRUG
- VACCINE

### Remove
- BULK INGREDIENT
- DRUG FOR FURTHER PROCESSING
- NON-STANDARDIZED ALLERGENIC
- STANDARDIZED ALLERGENIC
- CELLULAR THERAPY
- LICENSED VACCINE BULK INTERMEDIATE
- PLASMA DERIVATIVE

### Business Justification
Hospitals and retail pharmacies manage finished medicines, not pharmaceutical manufacturing materials or intermediate products.

### Expected Impact
Reduce dataset size while keeping only inventory-relevant medicines.

---

## BR-002 – Remove Records with Missing Generic Name

### Objective
Ensure every medicine has a valid generic name.

### Condition
Generic_Name is NULL.

### Action
Remove the record.

### Business Justification
Generic Name is the primary identifier used throughout inventory, procurement and analytics.

### Expected Impact
Remove only a very small number of invalid records.

---

## BR-003 – Handle Missing Brand Names

### Objective
Standardize medicines without commercial brand names.

### Condition
Brand_Name is NULL.

### Action
Replace Brand_Name with Generic_Name.

### Business Justification
Many generic medicines are marketed without a registered brand.

---

## BR-004 – Handle Missing Route

### Objective
Maintain complete records.

### Condition
Route is NULL.

### Action
Replace with

UNKNOWN

### Business Justification
Route information is useful but not mandatory for inventory management.

---

## BR-005 – Handle Missing Pharmacological Class

### Objective
Maintain complete medicine records.

### Condition
Pharm_Class is NULL.

### Action
Replace with

UNKNOWN

### Business Justification
Medicine categories will later be assigned using business mapping and AI-assisted categorization.

---

## BR-006 – Standardize Text Formatting

### Objective
Improve consistency across the dataset.

### Convert to Title Case

- Generic_Name
- Brand_Name
- Manufacturer

### Convert to Upper Case

- Dosage_Form
- Route
- Marketing_Category
- Product_Type

### Business Justification
Consistent formatting improves SQL querying, filtering, reporting and dashboard readability.

---

## BR-007 – Remove Duplicate Medicine IDs

### Objective
Ensure every medicine has a unique internal identifier.

### Condition
Duplicate Medicine_ID.

### Action
Remove duplicate records.

### Business Justification
Medicine_ID is the primary key of the master dataset.

---

## BR-008 – Resolve Duplicate Product NDC

### Objective
Ensure one master record per FDA Product NDC.

### Condition
Duplicate Product_NDC.

### Action
Keep the first occurrence and remove subsequent duplicates.

### Business Justification
Duplicate NDCs usually represent repeated FDA listings rather than unique medicines.

---

## BR-009 – Remove Unsupported Marketing Categories

### Remove

- EXPORT ONLY
- EMERGENCY USE AUTHORIZATION

### Keep

- ANDA
- NDA
- BLA
- OTC MONOGRAPH DRUG
- NDA AUTHORIZED GENERIC
- UNAPPROVED DRUG OTHER
- OTC MONOGRAPH FINAL
- OTC MONOGRAPH NOT FINAL

### Business Justification
Only products intended for routine pharmacy operations are required.

---

## BR-010 – Preserve Combination Medicines

### Examples

- Amoxicillin + Clavulanate
- Losartan + Hydrochlorothiazide

### Action
Keep combination medicines exactly as provided.

### Business Justification
Combination medicines are stocked and dispensed as single inventory items.

---

## BR-011 – Preserve Dosage Forms

### Action

Do NOT merge dosage forms such as

- TABLET
- TABLET, FILM COATED
- TABLET, COATED
- TABLET, EXTENDED RELEASE

### Business Justification
Each dosage form represents a clinically different product.

---

## BR-012 – Preserve Manufacturer Names

### Action

Keep FDA manufacturer names exactly as provided.

### Business Justification

Avoid introducing inconsistencies through manual manufacturer normalization.

---

## BR-013 – Remove Records Missing Both Active Ingredient and Strength

### Condition

Active_Ingredient = NULL

AND

Strength = NULL

### Action

Remove record.

### Business Justification

Medicines without both fields cannot be reliably identified.

---

## BR-014 – Standardize Date Format

### Current Format

YYYYMMDD

### Convert To

YYYY-MM-DD

### Example

20190626

↓

2019-06-26

### Business Justification

Improves SQL compatibility, Power BI reporting and date calculations.

---

## BR-015 – Final Dataset Validation

Before exporting the cleaned dataset, validate the following:

- No missing Generic_Name
- No duplicate Medicine_ID
- No duplicate Product_NDC
- Product_Type contains only approved values
- Dates are standardized
- Required columns exist
- Dataset passes all cleaning rules

### Output

Medicines_Master_Clean.csv

---

# Cleaning Pipeline

FDA NDC JSON

↓

01_extract_fda_dataset.py

↓

Medicines_Master_Raw.csv

↓

02_data_profiling.py

↓

Business Cleaning Rules

↓

03_clean_medicines.py

↓

Medicines_Master_Clean.csv

↓

04_create_final_master.py

↓

Medicines_Master_Final.csv