# ============================================================
# PharmaOps AI
# Medicines Inventory Validation Script
# ============================================================

import pandas as pd
import re
from pathlib import Path
from datetime import datetime

# ------------------------------------------------------------
# Project Paths
# ------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASET_PATH = PROJECT_ROOT / "data" / "synthetic" / "Medicines_Inventory.csv"

# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------

df = pd.read_csv(DATASET_PATH)

print("=" * 65)
print("MEDICINES INVENTORY DATASET VALIDATION")
print("=" * 65)

print(f"Dataset Loaded : {DATASET_PATH.name}")
print(f"Total Records  : {len(df):,}")
print(f"Total Columns  : {df.shape[1]}")

# ------------------------------------------------------------
# Required Columns
# ------------------------------------------------------------

required_columns = [
    "Inventory_ID",
    "Medicine_ID",
    "Supplier_ID",
    "Batch_Number",
    "Manufacturing_Date",
    "Expiry_Date",
    "Quantity_In_Stock",
    "Unit_Cost",
    "Selling_Price",
    "Reorder_Level",
    "Storage_Temperature",
    "Warehouse_Location",
    "Stock_Status",
    "Last_Restock_Date"
]

print("\n" + "=" * 65)
print("COLUMN VALIDATION")
print("=" * 65)

missing_cols = [c for c in required_columns if c not in df.columns]

errors = 0

if len(missing_cols) == 0:
    print("PASS : All required columns exist.")
else:
    errors += len(missing_cols)
    print("FAIL : Missing Columns")
    print(missing_cols)

# ------------------------------------------------------------
# Missing Values
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("MISSING VALUE VALIDATION")
print("=" * 65)

missing = df.isnull().sum().sum()

if missing == 0:
    print("PASS : No Missing Values")
else:
    errors += missing
    print(f"FAIL : {missing} Missing Values Found")

# ------------------------------------------------------------
# Duplicate Validation
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("DUPLICATE VALIDATION")
print("=" * 65)

dup_inventory = df["Inventory_ID"].duplicated().sum()
dup_batch = df["Batch_Number"].duplicated().sum()

print(f"{'PASS' if dup_inventory==0 else 'FAIL'} : Inventory_ID   -> {dup_inventory}")
print(f"{'PASS' if dup_batch==0 else 'FAIL'} : Batch_Number   -> {dup_batch}")

errors += dup_inventory + dup_batch

# ------------------------------------------------------------
# Format Validation
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("FORMAT VALIDATION")
print("=" * 65)

inventory_invalid = (~df["Inventory_ID"].astype(str).str.match(r"^INV\d{6}$")).sum()
medicine_invalid = (~df["Medicine_ID"].astype(str).str.match(r"^MED\d{6}$")).sum()
supplier_invalid = (~df["Supplier_ID"].astype(str).str.match(r"^SUP\d{4}$")).sum()
batch_invalid = (~df["Batch_Number"].astype(str).str.match(r"^BAT\d{6}$")).sum()

print(f"{'PASS' if inventory_invalid==0 else 'FAIL'} : Inventory_ID -> {inventory_invalid}")
print(f"{'PASS' if medicine_invalid==0 else 'FAIL'} : Medicine_ID  -> {medicine_invalid}")
print(f"{'PASS' if supplier_invalid==0 else 'FAIL'} : Supplier_ID  -> {supplier_invalid}")
print(f"{'PASS' if batch_invalid==0 else 'FAIL'} : Batch_Number -> {batch_invalid}")

errors += inventory_invalid + medicine_invalid + supplier_invalid + batch_invalid

# ------------------------------------------------------------
# Date Validation
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("DATE VALIDATION")
print("=" * 65)

today = pd.Timestamp.today().normalize()

df["Manufacturing_Date"] = pd.to_datetime(df["Manufacturing_Date"])
df["Expiry_Date"] = pd.to_datetime(df["Expiry_Date"])
df["Last_Restock_Date"] = pd.to_datetime(df["Last_Restock_Date"])

future_mfg = (df["Manufacturing_Date"] > today).sum()
expiry_error = (df["Expiry_Date"] <= df["Manufacturing_Date"]).sum()
future_restock = (df["Last_Restock_Date"] > today).sum()
restock_before_mfg = (df["Last_Restock_Date"] < df["Manufacturing_Date"]).sum()

print(f"{'PASS' if future_mfg==0 else 'FAIL'} : Future Manufacturing Dates -> {future_mfg}")
print(f"{'PASS' if expiry_error==0 else 'FAIL'} : Expiry Date Validation -> {expiry_error}")
print(f"{'PASS' if future_restock==0 else 'FAIL'} : Future Restock Dates -> {future_restock}")
print(f"{'PASS' if restock_before_mfg==0 else 'FAIL'} : Restock Before Manufacturing -> {restock_before_mfg}")

errors += future_mfg + expiry_error + future_restock + restock_before_mfg

# ------------------------------------------------------------
# Business Rules
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("BUSINESS RULE VALIDATION")
print("=" * 65)

quantity_error = ((df["Quantity_In_Stock"] < 0) | (df["Quantity_In_Stock"] > 1000)).sum()

cost_error = (df["Unit_Cost"] <= 0).sum()

selling_error = (df["Selling_Price"] <= df["Unit_Cost"]).sum()

reorder_error = ((df["Reorder_Level"] < 25) | (df["Reorder_Level"] > 200)).sum()

storage_error = (~df["Storage_Temperature"].isin([
    "Room Temperature",
    "Refrigerated (2–8°C)",
    "Frozen (-20°C)"
])).sum()

warehouse_error = (~df["Warehouse_Location"].isin([
    "WH-A",
    "WH-B",
    "WH-C",
    "WH-D",
    "WH-E"
])).sum()

# Stock Status Validation
expected_status = []

for q, r in zip(df["Quantity_In_Stock"], df["Reorder_Level"]):

    if q == 0:
        expected_status.append("Out of Stock")

    elif q <= r:
        expected_status.append("Low Stock")

    else:
        expected_status.append("In Stock")

stock_error = (df["Stock_Status"] != expected_status).sum()

print(f"{'PASS' if quantity_error==0 else 'FAIL'} : Quantity Range -> {quantity_error}")
print(f"{'PASS' if cost_error==0 else 'FAIL'} : Unit Cost -> {cost_error}")
print(f"{'PASS' if selling_error==0 else 'FAIL'} : Selling Price -> {selling_error}")
print(f"{'PASS' if reorder_error==0 else 'FAIL'} : Reorder Level -> {reorder_error}")
print(f"{'PASS' if storage_error==0 else 'FAIL'} : Storage Temperature -> {storage_error}")
print(f"{'PASS' if warehouse_error==0 else 'FAIL'} : Warehouse Location -> {warehouse_error}")
print(f"{'PASS' if stock_error==0 else 'FAIL'} : Stock Status Logic -> {stock_error}")

errors += (
    quantity_error +
    cost_error +
    selling_error +
    reorder_error +
    storage_error +
    warehouse_error +
    stock_error
)

# ------------------------------------------------------------
# Dataset Summary
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("DATA SUMMARY")
print("=" * 65)

print("\nStock Status Distribution")
print(df["Stock_Status"].value_counts())

print("\nWarehouse Distribution")
print(df["Warehouse_Location"].value_counts())

print("\nStorage Temperature Distribution")
print(df["Storage_Temperature"].value_counts())

print("\nQuantity Statistics")
print(df["Quantity_In_Stock"].describe())

print("\nPricing Statistics")
print(df[["Unit_Cost", "Selling_Price"]].describe())

# ------------------------------------------------------------
# Final Status
# ------------------------------------------------------------

print("\n" + "=" * 65)

if errors == 0:
    print("VALIDATION STATUS : PASSED")
    print("Dataset is ready for MySQL import and analytics.")
else:
    print("VALIDATION STATUS : FAILED")
    print(f"Total Errors Found : {errors}")

print("=" * 65)