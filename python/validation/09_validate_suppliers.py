# ==========================================================
# PharmaOps AI
# Suppliers Master Dataset Validation
# ==========================================================

import pandas as pd
import re
from pathlib import Path

# ----------------------------------------------------------
# Project Paths
# ----------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

DATASET = BASE_DIR / "data" / "synthetic" / "Suppliers_Master.csv"

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

print("=" * 65)
print("SUPPLIERS MASTER DATASET VALIDATION")
print("=" * 65)

df = pd.read_csv(DATASET)

print(f"Dataset Loaded : {DATASET.name}")
print(f"Total Records  : {len(df)}")
print(f"Total Columns  : {len(df.columns)}")
print()

# ==========================================================
# EXPECTED COLUMNS
# ==========================================================

expected_columns = [
    "Supplier_ID",
    "Supplier_Name",
    "Supplier_Type",
    "Supplier_Category",
    "Preferred_Supplier",
    "City",
    "State",
    "Contact_Email",
    "Contact_Number",
    "Lead_Time_Days",
    "Supplier_Rating",
    "Active_Status",
    "Contract_Start_Date",
    "Contract_End_Date",
    "GST_Number"
]

print("=" * 65)
print("COLUMN VALIDATION")
print("=" * 65)

missing_columns = [c for c in expected_columns if c not in df.columns]

if len(missing_columns) == 0:
    print("PASS : All required columns exist.")
else:
    print("FAIL : Missing Columns")
    for c in missing_columns:
        print(f"   - {c}")

print()

# ==========================================================
# MISSING VALUES
# ==========================================================

print("=" * 65)
print("MISSING VALUE VALIDATION")
print("=" * 65)

missing = df.isnull().sum()

if missing.sum() == 0:
    print("PASS : No Missing Values")
else:
    print("FAIL : Missing Values Found")
    print(missing[missing > 0])

print()

# ==========================================================
# DUPLICATE VALIDATION
# ==========================================================

print("=" * 65)
print("DUPLICATE VALIDATION")
print("=" * 65)

duplicate_checks = {
    "Supplier_ID": df["Supplier_ID"].duplicated().sum(),
    "Contact_Email": df["Contact_Email"].duplicated().sum(),
    "Contact_Number": df["Contact_Number"].duplicated().sum(),
    "GST_Number": df["GST_Number"].duplicated().sum()
}

for key, value in duplicate_checks.items():
    status = "PASS" if value == 0 else "FAIL"
    print(f"{status} : {key:<20} -> {value}")

print()

# ==========================================================
# SUPPLIER ID FORMAT
# ==========================================================

print("=" * 65)
print("SUPPLIER ID FORMAT")
print("=" * 65)

invalid = df[
    ~df["Supplier_ID"].astype(str).str.match(r"^SUP\d{4}$")
]

if len(invalid) == 0:
    print("PASS : Supplier IDs are valid.")
else:
    print(f"FAIL : {len(invalid)} Invalid Supplier IDs")

print()

# ==========================================================
# EMAIL VALIDATION
# ==========================================================

print("=" * 65)
print("EMAIL VALIDATION")
print("=" * 65)

email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

invalid = df[
    ~df["Contact_Email"].astype(str).str.match(email_pattern)
]

if len(invalid) == 0:
    print("PASS : Email format is valid.")
else:
    print(f"FAIL : {len(invalid)} Invalid Emails")

print()

# ==========================================================
# PHONE VALIDATION
# ==========================================================

print("=" * 65)
print("PHONE VALIDATION")
print("=" * 65)

invalid = df[
    ~df["Contact_Number"].astype(str).str.match(r"^[6-9]\d{9}$")
]

if len(invalid) == 0:
    print("PASS : Phone numbers are valid.")
else:
    print(f"FAIL : {len(invalid)} Invalid Phone Numbers")

print()

# ==========================================================
# GST VALIDATION
# ==========================================================

print("=" * 65)
print("GST VALIDATION")
print("=" * 65)

gst_pattern = r'^\d{2}[A-Z]{5}\d{4}[A-Z]1Z5$'

invalid = df[
    ~df["GST_Number"].astype(str).str.match(gst_pattern)
]

if len(invalid) == 0:
    print("PASS : GST Numbers are valid.")
else:
    print(f"FAIL : {len(invalid)} Invalid GST Numbers")

print()

# ==========================================================
# BUSINESS RULE VALIDATION
# ==========================================================

print("=" * 65)
print("BUSINESS RULE VALIDATION")
print("=" * 65)

rating = df[
    (df["Supplier_Rating"] < 0) |
    (df["Supplier_Rating"] > 5)
]

lead = df[
    df["Lead_Time_Days"] <= 0
]

preferred = df[
    ~df["Preferred_Supplier"].isin(["Yes", "No"])
]

status = df[
    ~df["Active_Status"].isin(["Active", "Inactive"])
]

start = pd.to_datetime(df["Contract_Start_Date"])
end = pd.to_datetime(df["Contract_End_Date"])

contract = df[end <= start]

checks = {
    "Supplier Rating": len(rating),
    "Lead Time": len(lead),
    "Preferred Supplier": len(preferred),
    "Active Status": len(status),
    "Contract Dates": len(contract)
}

for key, value in checks.items():

    result = "PASS" if value == 0 else "FAIL"

    print(f"{result} : {key:<22} -> {value}")

print()

# ==========================================================
# DATA SUMMARY
# ==========================================================

print("=" * 65)
print("DATA SUMMARY")
print("=" * 65)

print("\nSupplier Type Distribution")
print(df["Supplier_Type"].value_counts())

print("\nSupplier Category Distribution")
print(df["Supplier_Category"].value_counts())

print("\nPreferred Supplier Distribution")
print(df["Preferred_Supplier"].value_counts())

print("\nActive Status Distribution")
print(df["Active_Status"].value_counts())

print("\nLead Time Statistics")
print(df["Lead_Time_Days"].describe())

print("\nSupplier Rating Statistics")
print(df["Supplier_Rating"].describe())

print()

# ==========================================================
# FINAL RESULT
# ==========================================================

total_errors = (
    missing.sum() +
    sum(duplicate_checks.values()) +
    len(invalid) +
    len(rating) +
    len(lead) +
    len(preferred) +
    len(status) +
    len(contract)
)

print("=" * 65)

if total_errors == 0:
    print("VALIDATION STATUS : PASSED")
    print("Dataset is ready for MySQL import and analytics.")
else:
    print("VALIDATION STATUS : FAILED")
    print(f"Total Validation Errors : {total_errors}")

print("=" * 65)