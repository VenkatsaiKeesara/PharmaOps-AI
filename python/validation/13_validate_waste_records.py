import re
from pathlib import Path

import pandas as pd

# ==========================================================
# PROJECT PATHS
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "synthetic" / "Waste_Records.csv"

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(INPUT_FILE)

print("=" * 70)
print("WASTE RECORDS DATASET VALIDATION")
print("=" * 70)

print("\nDataset Loaded Successfully")
print(f"Rows    : {len(df):,}")
print(f"Columns : {len(df.columns)}")

passed = 0
failed = 0

# ==========================================================
# HELPER FUNCTION
# ==========================================================

def check(condition, message):
    global passed, failed

    if condition:
        print(f"PASS : {message}")
        passed += 1
    else:
        print(f"FAIL : {message}")
        failed += 1

# ==========================================================
# REQUIRED COLUMNS
# ==========================================================

required_columns = [

    "Waste_Record_ID",
    "Inventory_ID",
    "Medicine_ID",
    "Batch_Number",
    "Waste_Date",
    "Expiry_Date",
    "Quantity_Wasted",
    "Unit_Cost",
    "Total_Waste_Value",
    "Waste_Reason",
    "Disposal_Method",
    "Disposal_Status",
    "Reported_By",
    "Warehouse_Location",
    "Remarks"

]

check(
    all(col in df.columns for col in required_columns),
    "Required Columns"
)

# ==========================================================
# MISSING VALUES
# ==========================================================

check(
    df.isnull().sum().sum() == 0,
    "Missing Values"
)

# ==========================================================
# DUPLICATE IDS
# ==========================================================

check(
    df["Waste_Record_ID"].duplicated().sum() == 0,
    "Duplicate Waste_Record_ID"
)

# ==========================================================
# ID FORMATS
# ==========================================================

check(
    df["Waste_Record_ID"].str.match(r"^WR\d{6}$").all(),
    "Waste_Record_ID Format"
)

check(
    df["Inventory_ID"].str.match(r"^INV\d{6}$").all(),
    "Inventory_ID Format"
)

check(
    df["Medicine_ID"].str.match(r"^MED\d{6}$").all(),
    "Medicine_ID Format"
)

# ==========================================================
# BATCH NUMBER
# ==========================================================

check(
    df["Batch_Number"].astype(str).str.strip().ne("").all(),
    "Batch_Number Validation"
)
# ==========================================================
# DATE VALIDATION
# ==========================================================

df["Waste_Date"] = pd.to_datetime(df["Waste_Date"])
df["Expiry_Date"] = pd.to_datetime(df["Expiry_Date"])

today = pd.Timestamp.today().normalize()

check(
    (df["Waste_Date"] <= today).all(),
    "Waste Date"
)

check(
    df["Expiry_Date"].notna().all(),
    "Expiry Date"
)

# ==========================================================
# QUANTITY WASTED
# ==========================================================

check(
    df["Quantity_Wasted"].between(1, 200).all(),
    "Quantity Wasted"
)

# ==========================================================
# UNIT COST
# ==========================================================

check(
    (df["Unit_Cost"] > 0).all(),
    "Unit Cost"
)

# ==========================================================
# TOTAL WASTE VALUE
# ==========================================================

expected_total = (
    df["Quantity_Wasted"] *
    df["Unit_Cost"]
).round(2)

difference = (
    expected_total -
    df["Total_Waste_Value"]
).abs()

check(
    (difference <= 0.01).all(),
    "Total Waste Value Calculation"
)

# ==========================================================
# WASTE REASON
# ==========================================================

valid_reasons = [

    "Expired",
    "Damaged",
    "Overstock",
    "Recalled",
    "Contaminated"

]

check(
    df["Waste_Reason"].isin(valid_reasons).all(),
    "Waste Reason"
)

# ==========================================================
# DISPOSAL METHOD
# ==========================================================

valid_methods = [

    "Incineration",
    "Return to Supplier",
    "Biohazard Disposal",
    "Recycling"

]

check(
    df["Disposal_Method"].isin(valid_methods).all(),
    "Disposal Method"
)

# ==========================================================
# DISPOSAL STATUS
# ==========================================================

check(
    df["Disposal_Status"].isin(
        ["Completed", "Pending"]
    ).all(),
    "Disposal Status"
)

# ==========================================================
# EMPLOYEE FORMAT
# ==========================================================

check(
    df["Reported_By"].str.match(
        r"^EMP\d{3}$"
    ).all(),
    "Reported_By Format"
)

# ==========================================================
# WAREHOUSE LOCATION
# ==========================================================

check(
    df["Warehouse_Location"].isin(

        [
            "WH-A",
            "WH-B",
            "WH-C",
            "WH-D",
            "WH-E"
        ]

    ).all(),
    "Warehouse Location"
)

# ==========================================================
# REMARKS
# ==========================================================

check(
    df["Remarks"].astype(str).str.strip().ne("").all(),
    "Remarks"
)

# ==========================================================
# POSITIVE WASTE VALUE
# ==========================================================

check(
    (df["Total_Waste_Value"] > 0).all(),
    "Positive Waste Value"
)

# ==========================================================
# DATASET SIZE
# ==========================================================

check(
    len(df) == 2500,
    "Dataset Size (2500 Records)"
)
# ==========================================================
# DATASET SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("DATASET SUMMARY")
print("=" * 70)

print(f"Rows                 : {len(df):,}")
print(f"Columns              : {len(df.columns)}")
print(f"Duplicate Waste IDs  : {df['Waste_Record_ID'].duplicated().sum()}")
print(f"Missing Values       : {df.isnull().sum().sum()}")

# ==========================================================
# WASTE REASON DISTRIBUTION
# ==========================================================

print("\nWaste Reason Distribution")
print("-" * 70)
print(df["Waste_Reason"].value_counts())

# ==========================================================
# DISPOSAL METHOD DISTRIBUTION
# ==========================================================

print("\nDisposal Method Distribution")
print("-" * 70)
print(df["Disposal_Method"].value_counts())

# ==========================================================
# DISPOSAL STATUS DISTRIBUTION
# ==========================================================

print("\nDisposal Status Distribution")
print("-" * 70)
print(df["Disposal_Status"].value_counts())

# ==========================================================
# WAREHOUSE DISTRIBUTION
# ==========================================================

print("\nWarehouse Distribution")
print("-" * 70)
print(df["Warehouse_Location"].value_counts())

# ==========================================================
# TOP EMPLOYEES REPORTING WASTE
# ==========================================================

print("\nTop 10 Employees Reporting Waste")
print("-" * 70)
print(df["Reported_By"].value_counts().head(10))

# ==========================================================
# WASTE VALUE STATISTICS
# ==========================================================

print("\nWaste Value Statistics")
print("-" * 70)

print(f"Minimum Waste Value : ₹{df['Total_Waste_Value'].min():,.2f}")
print(f"Maximum Waste Value : ₹{df['Total_Waste_Value'].max():,.2f}")
print(f"Average Waste Value : ₹{df['Total_Waste_Value'].mean():,.2f}")
print(f"Total Waste Value   : ₹{df['Total_Waste_Value'].sum():,.2f}")

# ==========================================================
# QUANTITY STATISTICS
# ==========================================================

print("\nQuantity Wasted Statistics")
print("-" * 70)

print(f"Minimum Quantity : {df['Quantity_Wasted'].min()}")
print(f"Maximum Quantity : {df['Quantity_Wasted'].max()}")
print(f"Average Quantity : {df['Quantity_Wasted'].mean():.2f}")

# ==========================================================
# SAMPLE RECORDS
# ==========================================================

print("\nSample Records")
print("-" * 70)
print(df.head())

# ==========================================================
# VALIDATION RESULT
# ==========================================================

print("\n" + "=" * 70)
print("VALIDATION RESULT")
print("=" * 70)

print(f"Checks Passed : {passed}")
print(f"Checks Failed : {failed}")

validation_score = (passed / (passed + failed)) * 100

print(f"Validation Score : {validation_score:.2f}%")

# ==========================================================
# FINAL STATUS
# ==========================================================

if failed == 0:

    print("\n" + "=" * 70)
    print("ALL VALIDATION CHECKS PASSED")
    print("Waste_Records.csv is READY FOR MYSQL IMPORT")
    print("=" * 70)

else:

    print("\n" + "=" * 70)
    print("VALIDATION FAILED")
    print(f"{failed} validation check(s) failed.")
    print("=" * 70)