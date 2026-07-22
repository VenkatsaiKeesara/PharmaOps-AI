# ============================================================
# PharmaOps AI
# Purchase Orders Dataset Validation
# Dataset: Purchase_Orders.csv
# ============================================================

import pandas as pd
import re
from pathlib import Path

# ------------------------------------------------------------
# Project Paths
# ------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = PROJECT_ROOT / "data" / "synthetic"

FILE_PATH = DATA_PATH / "Purchase_Orders.csv"

# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------

print("=" * 70)
print("PURCHASE ORDERS DATASET VALIDATION")
print("=" * 70)

df = pd.read_csv(FILE_PATH)

print(f"\nDataset Loaded Successfully")
print(f"Rows    : {len(df):,}")
print(f"Columns : {df.shape[1]}")

passed = 0
failed = 0

# ------------------------------------------------------------
# Helper Function
# ------------------------------------------------------------

def check(condition, message):
    global passed, failed

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
    "Purchase_Order_ID",
    "Medicine_ID",
    "Supplier_ID",
    "Order_Date",
    "Expected_Delivery_Date",
    "Actual_Delivery_Date",
    "Quantity_Ordered",
    "Unit_Purchase_Cost",
    "Total_Order_Value",
    "Payment_Method",
    "Payment_Status",
    "Order_Status",
    "Warehouse_Location",
    "Procurement_Manager"
]

check(
    list(df.columns) == required_columns,
    "Required columns are correct"
)

# ------------------------------------------------------------
# Missing Values
# ------------------------------------------------------------

missing = df.drop(columns=["Actual_Delivery_Date"]).isnull().sum().sum()

check(
    missing == 0,
    "No missing values (except Actual_Delivery_Date)"
)

# ------------------------------------------------------------
# Duplicate Purchase Orders
# ------------------------------------------------------------

check(
    df["Purchase_Order_ID"].duplicated().sum() == 0,
    "No duplicate Purchase_Order_ID"
)

# ------------------------------------------------------------
# ID Formats
# ------------------------------------------------------------

po_pattern = r"^PO\d{6}$"
med_pattern = r"^MED\d{6}$"
sup_pattern = r"^SUP\d{4}$"

check(
    df["Purchase_Order_ID"].astype(str).str.match(po_pattern).all(),
    "Purchase_Order_ID format valid"
)

check(
    df["Medicine_ID"].astype(str).str.match(med_pattern).all(),
    "Medicine_ID format valid"
)

check(
    df["Supplier_ID"].astype(str).str.match(sup_pattern).all(),
    "Supplier_ID format valid"
)

# ------------------------------------------------------------
# Convert Dates
# ------------------------------------------------------------

df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Expected_Delivery_Date"] = pd.to_datetime(df["Expected_Delivery_Date"])
df["Actual_Delivery_Date"] = pd.to_datetime(
    df["Actual_Delivery_Date"],
    errors="coerce"
)

today = pd.Timestamp.today().normalize()

# ------------------------------------------------------------
# Date Validation
# ------------------------------------------------------------

check(
    (df["Order_Date"] <= today).all(),
    "Order_Date is not in the future"
)

check(
    (df["Expected_Delivery_Date"] >= df["Order_Date"]).all(),
    "Expected_Delivery_Date >= Order_Date"
)

delivered = df[df["Order_Status"] == "Delivered"]

check(
    (delivered["Actual_Delivery_Date"] >= delivered["Order_Date"]).all(),
    "Delivered orders have valid Actual_Delivery_Date"
)

pending_cancelled = df[df["Order_Status"].isin(["Pending", "Cancelled"])]

check(
    pending_cancelled["Actual_Delivery_Date"].isna().all(),
    "Pending/Cancelled orders have blank Actual_Delivery_Date"
)

# ------------------------------------------------------------
# Quantity Validation
# ------------------------------------------------------------

check(
    df["Quantity_Ordered"].between(50, 2000).all(),
    "Quantity Ordered within range"
)

# ------------------------------------------------------------
# Purchase Cost
# ------------------------------------------------------------

check(
    df["Unit_Purchase_Cost"].between(5, 600).all(),
    "Unit Purchase Cost within range"
)

# ------------------------------------------------------------
# Total Order Value
# ------------------------------------------------------------

calculated_total = (
    df["Quantity_Ordered"] *
    df["Unit_Purchase_Cost"]
).round(2)

check(
    (calculated_total == df["Total_Order_Value"].round(2)).all(),
    "Total Order Value calculated correctly"
)

# ------------------------------------------------------------
# Payment Method
# ------------------------------------------------------------

payment_methods = {
    "Bank Transfer",
    "UPI",
    "Credit"
}

check(
    df["Payment_Method"].isin(payment_methods).all(),
    "Payment Method values valid"
)

# ------------------------------------------------------------
# Payment Status
# ------------------------------------------------------------

payment_status = {
    "Paid",
    "Pending",
    "Partial"
}

check(
    df["Payment_Status"].isin(payment_status).all(),
    "Payment Status values valid"
)

# ------------------------------------------------------------
# Order Status
# ------------------------------------------------------------

order_status = {
    "Delivered",
    "Pending",
    "Cancelled"
}

check(
    df["Order_Status"].isin(order_status).all(),
    "Order Status values valid"
)

# ------------------------------------------------------------
# Warehouse
# ------------------------------------------------------------

warehouses = {
    "WH-A",
    "WH-B",
    "WH-C",
    "WH-D",
    "WH-E"
}

check(
    df["Warehouse_Location"].isin(warehouses).all(),
    "Warehouse values valid"
)

# ------------------------------------------------------------
# Procurement Manager
# ------------------------------------------------------------

managers = {
    "Rahul Sharma",
    "Priya Nair",
    "Amit Verma",
    "Sneha Reddy",
    "Karan Mehta",
    "Neha Gupta",
    "Arjun Patel",
    "Rohit Kumar"
}

check(
    df["Procurement_Manager"].isin(managers).all(),
    "Procurement Manager values valid"
)

# ------------------------------------------------------------
# Dataset Summary
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("DATASET SUMMARY")
print("=" * 70)

print(f"Rows                 : {len(df):,}")
print(f"Columns              : {df.shape[1]}")
print(f"Duplicate IDs        : {df['Purchase_Order_ID'].duplicated().sum()}")
print(f"Missing Values       : {missing}")

print("\nOrder Status")
print(df["Order_Status"].value_counts())

print("\nPayment Status")
print(df["Payment_Status"].value_counts())

print("\nPayment Methods")
print(df["Payment_Method"].value_counts())

print("\nWarehouse Distribution")
print(df["Warehouse_Location"].value_counts())

# ------------------------------------------------------------
# Final Result
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("VALIDATION RESULT")
print("=" * 70)

print(f"Checks Passed : {passed}")
print(f"Checks Failed : {failed}")

if failed == 0:
    print("\nALL VALIDATION CHECKS PASSED")
    print("Purchase_Orders.csv is READY FOR MYSQL IMPORT")
else:
    print("\nVALIDATION FAILED")
    print("Please correct the failed checks before proceeding.")

print("=" * 70)