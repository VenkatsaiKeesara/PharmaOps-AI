# ============================================================
# PharmaOps AI
# Sales Transactions Dataset Validation
# ============================================================

import pandas as pd
from pathlib import Path
from datetime import datetime

# ------------------------------------------------------------
# Project Paths
# ------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = PROJECT_ROOT / "data" / "synthetic"

FILE_PATH = DATA_PATH / "Sales_Transactions.csv"

# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------

print("=" * 70)
print("SALES TRANSACTIONS DATASET VALIDATION")
print("=" * 70)

df = pd.read_csv(FILE_PATH)

print(f"\nDataset Loaded Successfully")
print(f"Rows    : {len(df):,}")
print(f"Columns : {df.shape[1]}")

passed = 0
failed = 0

# ------------------------------------------------------------
# Validation Helper
# ------------------------------------------------------------

def check(condition, message):

    global passed
    global failed

    if condition:

        print(f"PASS : {message}")
        passed += 1

    else:

        print(f"FAIL : {message}")
        failed += 1


# ------------------------------------------------------------
# Required Columns
# ------------------------------------------------------------

required_columns = [

    "Transaction_ID",
    "Invoice_Number",
    "Medicine_ID",
    "Branch_ID",
    "Transaction_Date",
    "Sale_Time",
    "Quantity_Sold",
    "Unit_Selling_Price",
    "Discount_Percentage",
    "Total_Amount",
    "Payment_Method",
    "Customer_Type",
    "Prescription_Required",
    "Pharmacist_ID",
    "Transaction_Status"

]

check(
    list(df.columns) == required_columns,
    "Required Columns"
)

# ------------------------------------------------------------
# Missing Values
# ------------------------------------------------------------

check(
    df.isna().sum().sum() == 0,
    "Missing Values"
)

# ------------------------------------------------------------
# Duplicate Checks
# ------------------------------------------------------------

check(
    df["Transaction_ID"].duplicated().sum() == 0,
    "Duplicate Transaction_ID"
)

check(
    df["Invoice_Number"].duplicated().sum() == 0,
    "Duplicate Invoice_Number"
)

# ------------------------------------------------------------
# ID Formats
# ------------------------------------------------------------

check(
    df["Transaction_ID"].str.match(r"^TXN\d{6}$").all(),
    "Transaction_ID Format"
)

check(
    df["Invoice_Number"].str.match(r"^INV2026\d{6}$").all(),
    "Invoice_Number Format"
)

check(
    df["Medicine_ID"].str.match(r"^MED\d{6}$").all(),
    "Medicine_ID Format"
)

check(
    df["Branch_ID"].isin(
        [
            "BR001",
            "BR002",
            "BR003",
            "BR004",
            "BR005"
        ]
    ).all(),
    "Branch_ID Values"
)

check(
    df["Pharmacist_ID"].str.match(r"^PH\d{3}$").all(),
    "Pharmacist_ID Format"
)

# ------------------------------------------------------------
# Date Validation
# ------------------------------------------------------------

df["Transaction_Date"] = pd.to_datetime(
    df["Transaction_Date"]
)

today = pd.Timestamp.today().normalize()

check(
    (df["Transaction_Date"] <= today).all(),
    "Transaction Date"
)

# ------------------------------------------------------------
# Time Validation
# ------------------------------------------------------------

sale_time = pd.to_datetime(
    df["Sale_Time"],
    format="%H:%M:%S"
).dt.time

check(
    sale_time.apply(
        lambda x:
        datetime.strptime("08:00","%H:%M").time()
        <= x <=
        datetime.strptime("22:00","%H:%M").time()
    ).all(),
    "Sale Time"
)

# ------------------------------------------------------------
# Quantity
# ------------------------------------------------------------

check(
    df["Quantity_Sold"].between(
        1,
        10
    ).all(),
    "Quantity Sold"
)

# ------------------------------------------------------------
# Selling Price
# ------------------------------------------------------------

check(
    df["Unit_Selling_Price"].between(
        10,
        1200
    ).all(),
    "Unit Selling Price"
)

# ------------------------------------------------------------
# Discount
# ------------------------------------------------------------

check(
    df["Discount_Percentage"].isin(
        [0,5,10,15,20]
    ).all(),
    "Discount Percentage"
)

# ------------------------------------------------------------
# Total Amount Validation
# ------------------------------------------------------------

def calculate_total(
    quantity,
    price,
    discount
):

    subtotal = quantity * price

    discount_amount = subtotal * discount / 100

    total = subtotal - discount_amount

    return round(total,2)

expected_total = df.apply(

    lambda row:

    calculate_total(

        row["Quantity_Sold"],

        row["Unit_Selling_Price"],

        row["Discount_Percentage"]

    ),

    axis=1

)

difference = (
    expected_total -
    df["Total_Amount"]
).abs()

check(
    (difference <= 0.01).all(),
    "Total Amount Calculation"
)
# ------------------------------------------------------------
# Payment Method Validation
# ------------------------------------------------------------

payment_methods = [
    "Cash",
    "UPI",
    "Card",
    "Insurance"
]

check(
    df["Payment_Method"].isin(payment_methods).all(),
    "Payment Method"
)

# ------------------------------------------------------------
# Customer Type Validation
# ------------------------------------------------------------

customer_types = [
    "Walk-in",
    "Member",
    "Online"
]

check(
    df["Customer_Type"].isin(customer_types).all(),
    "Customer Type"
)

# ------------------------------------------------------------
# Prescription Validation
# ------------------------------------------------------------

prescription_values = [
    "Yes",
    "No"
]

check(
    df["Prescription_Required"].isin(
        prescription_values
    ).all(),
    "Prescription Required"
)

# ------------------------------------------------------------
# Transaction Status Validation
# ------------------------------------------------------------

transaction_status = [
    "Completed",
    "Returned",
    "Cancelled"
]

check(
    df["Transaction_Status"].isin(
        transaction_status
    ).all(),
    "Transaction Status"
)

# ------------------------------------------------------------
# Additional Business Rule Checks
# ------------------------------------------------------------

check(
    (df["Total_Amount"] >= 0).all(),
    "Total Amount Positive"
)

check(
    (df["Unit_Selling_Price"] > 0).all(),
    "Positive Selling Price"
)

check(
    (df["Quantity_Sold"] > 0).all(),
    "Positive Quantity"
)

# ------------------------------------------------------------
# Dataset Summary
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("DATASET SUMMARY")
print("=" * 70)

print(f"Rows                 : {len(df):,}")
print(f"Columns              : {df.shape[1]}")
print(f"Duplicate IDs        : {df['Transaction_ID'].duplicated().sum()}")
print(f"Duplicate Invoices   : {df['Invoice_Number'].duplicated().sum()}")
print(f"Missing Values       : {df.isna().sum().sum()}")

print("\nTransaction Status Distribution")
print("-" * 70)
print(df["Transaction_Status"].value_counts())

print("\nPayment Method Distribution")
print("-" * 70)
print(df["Payment_Method"].value_counts())

print("\nCustomer Type Distribution")
print("-" * 70)
print(df["Customer_Type"].value_counts())

print("\nPrescription Distribution")
print("-" * 70)
print(df["Prescription_Required"].value_counts())

print("\nBranch Distribution")
print("-" * 70)
print(df["Branch_ID"].value_counts())

print("\nDiscount Distribution")
print("-" * 70)
print(df["Discount_Percentage"].value_counts().sort_index())

# ------------------------------------------------------------
# Validation Score
# ------------------------------------------------------------

total_checks = passed + failed

print("\n" + "=" * 70)
print("VALIDATION RESULT")
print("=" * 70)

print(f"Checks Passed : {passed}")
print(f"Checks Failed : {failed}")
print(f"Validation Score : {(passed/total_checks)*100:.2f}%")

# ------------------------------------------------------------
# Failed Total Amount Diagnostics
# ------------------------------------------------------------

if not (difference <= 0.01).all():

    print("\nRows with incorrect Total Amount:\n")

    failed_rows = df.loc[
        difference > 0.01,
        [
            "Quantity_Sold",
            "Unit_Selling_Price",
            "Discount_Percentage",
            "Total_Amount"
        ]
    ].copy()

    failed_rows["Expected_Total"] = expected_total[
        difference > 0.01
    ].values

    failed_rows["Difference"] = difference[
        difference > 0.01
    ].values

    print(failed_rows.head(20))

# ------------------------------------------------------------
# Final Status
# ------------------------------------------------------------

if failed == 0:

    print("\n" + "=" * 70)
    print("ALL VALIDATION CHECKS PASSED")
    print("Sales_Transactions.csv is READY FOR MYSQL IMPORT")
    print("=" * 70)

else:

    print("\n" + "=" * 70)
    print("VALIDATION FAILED")
    print("Please review the failed validation checks.")
    print("=" * 70)