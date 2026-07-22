# ============================================================
# PharmaOps AI
# Medicines Inventory Dataset Generator
# Dataset: Medicines_Inventory.csv
# ============================================================

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from pathlib import Path

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

random.seed(42)
np.random.seed(42)

TOTAL_RECORDS = 5000

# ------------------------------------------------------------
# Project Paths
# ------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_PATH = PROJECT_ROOT / "data" / "raw"
PROCESSED_PATH = PROJECT_ROOT / "data" / "processed"
SYNTHETIC_PATH = PROJECT_ROOT / "data" / "synthetic"

SYNTHETIC_PATH.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------
# Lookup Values
# ------------------------------------------------------------

WAREHOUSES = [
    "WH-A",
    "WH-B",
    "WH-C",
    "WH-D",
    "WH-E"
]

STORAGE_TYPES = [
    "Room Temperature",
    "Refrigerated (2–8°C)",
    "Frozen (-20°C)"
]

# ------------------------------------------------------------
# Load Reference Datasets (Optional)
# ------------------------------------------------------------

try:
    medicines_df = pd.read_csv(
        PROCESSED_PATH / "Medicines_Master_Clean.csv"
    )
    medicine_ids = medicines_df["Medicine_ID"].tolist()

except Exception:
    print("Medicines_Master not found. Using temporary IDs.")
    medicine_ids = [
        f"MED{i:06d}"
        for i in range(1, 2001)
    ]

try:
    suppliers_df = pd.read_csv(
        SYNTHETIC_PATH / "Suppliers_Master.csv"
    )
    supplier_ids = suppliers_df["Supplier_ID"].tolist()

except Exception:
    print("Suppliers_Master not found. Using temporary IDs.")
    supplier_ids = [
        f"SUP{i:04d}"
        for i in range(1, 76)
    ]

# ------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------

def random_manufacturing_date():
    """
    Generate manufacturing date within
    last 3 years.
    """
    today = datetime.today()

    start = today - timedelta(days=3 * 365)

    delta = (today - start).days

    return start + timedelta(
        days=random.randint(0, delta)
    )


def random_expiry_date(mfg_date):
    """
    Expiry:
    12–36 months after manufacturing.
    """
    months = random.randint(12, 36)

    return mfg_date + timedelta(days=months * 30)


def calculate_stock_status(quantity, reorder):
    """
    Business Rule
    """
    if quantity == 0:
        return "Out of Stock"

    elif quantity <= reorder:
        return "Low Stock"

    else:
        return "In Stock"
    
# ------------------------------------------------------------
# Generate Inventory Records
# ------------------------------------------------------------

inventory_records = []

used_batches = set()

for i in range(1, TOTAL_RECORDS + 1):

    inventory_id = f"INV{i:06d}"

    medicine_id = random.choice(medicine_ids)

    supplier_id = random.choice(supplier_ids)

    # -----------------------------
    # Unique Batch Number
    # -----------------------------
    while True:
        batch_number = f"BAT{random.randint(100000, 999999)}"
        if batch_number not in used_batches:
            used_batches.add(batch_number)
            break

    # -----------------------------
    # Dates
    # -----------------------------
    manufacturing_date = random_manufacturing_date()

    expiry_date = random_expiry_date(manufacturing_date)

    last_restock_date = manufacturing_date + timedelta(
        days=random.randint(15, 180)
    )

    if last_restock_date > datetime.today():
        last_restock_date = datetime.today()

    # -----------------------------
    # Quantity & Reorder Level
    # -----------------------------
    quantity = random.randint(0, 1000)

    reorder_level = random.randint(25, 200)

    # -----------------------------
    # Pricing
    # -----------------------------
    unit_cost = round(
        random.uniform(5, 600),
        2
    )

    markup = random.uniform(1.20, 1.40)

    selling_price = round(
        unit_cost * markup,
        2
    )

    # -----------------------------
    # Storage & Warehouse
    # -----------------------------
    storage = random.choice(STORAGE_TYPES)

    warehouse = random.choice(WAREHOUSES)

    # -----------------------------
    # Stock Status
    # -----------------------------
    stock_status = calculate_stock_status(
        quantity,
        reorder_level
    )

    # -----------------------------
    # Store Record
    # -----------------------------
    inventory_records.append({

        "Inventory_ID": inventory_id,

        "Medicine_ID": medicine_id,

        "Supplier_ID": supplier_id,

        "Batch_Number": batch_number,

        "Manufacturing_Date": manufacturing_date.date(),

        "Expiry_Date": expiry_date.date(),

        "Quantity_In_Stock": quantity,

        "Unit_Cost": unit_cost,

        "Selling_Price": selling_price,

        "Reorder_Level": reorder_level,

        "Storage_Temperature": storage,

        "Warehouse_Location": warehouse,

        "Stock_Status": stock_status,

        "Last_Restock_Date": last_restock_date.date()

    })
# ------------------------------------------------------------
# Create DataFrame
# ------------------------------------------------------------

inventory_df = pd.DataFrame(inventory_records)

# Optional: Sort for cleaner output
inventory_df.sort_values(
    by=["Medicine_ID", "Inventory_ID"],
    inplace=True
)

inventory_df.reset_index(drop=True, inplace=True)

# ------------------------------------------------------------
# Export Dataset
# ------------------------------------------------------------

output_file = SYNTHETIC_PATH / "Medicines_Inventory.csv"

inventory_df.to_csv(
    output_file,
    index=False
)

# ------------------------------------------------------------
# Dataset Summary
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("MEDICINES INVENTORY DATASET GENERATED SUCCESSFULLY")
print("=" * 65)

print(f"Output File   : {output_file}")
print(f"Rows          : {len(inventory_df):,}")
print(f"Columns       : {inventory_df.shape[1]}")

print("\nColumn Names")
print("-" * 65)
for col in inventory_df.columns:
    print(f"- {col}")

print("\nFirst 5 Records")
print("-" * 65)
print(inventory_df.head())

print("\nStock Status Distribution")
print("-" * 65)
print(inventory_df["Stock_Status"].value_counts())

print("\nStorage Temperature Distribution")
print("-" * 65)
print(inventory_df["Storage_Temperature"].value_counts())

print("\nWarehouse Distribution")
print("-" * 65)
print(inventory_df["Warehouse_Location"].value_counts())

print("\nInventory Statistics")
print("-" * 65)
print(inventory_df[[
    "Quantity_In_Stock",
    "Unit_Cost",
    "Selling_Price",
    "Reorder_Level"
]].describe())

print("\n" + "=" * 65)
print("Dataset Ready for Validation")
print("=" * 65)