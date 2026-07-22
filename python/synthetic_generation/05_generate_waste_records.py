from pathlib import Path
from datetime import datetime, timedelta
import random
import pandas as pd

# ==========================================================
# PROJECT PATHS
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "synthetic" / "Medicines_Inventory.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "synthetic" / "Waste_Records.csv"

# ==========================================================
# LOAD INVENTORY DATASET
# ==========================================================

inventory_df = pd.read_csv(INPUT_FILE)

print("=" * 70)
print("MEDICINES INVENTORY LOADED")
print("=" * 70)

print(f"Original Inventory Records : {len(inventory_df):,}")

# Keep only records that have stock available
inventory_df = inventory_df[inventory_df["Quantity_In_Stock"] > 0].copy()

print(f"Positive Stock Records     : {len(inventory_df):,}")

# Randomly select 2500 inventory batches
inventory_df = inventory_df.sample(
    n=2500,
    random_state=42,
    replace=False
).reset_index(drop=True)

print(f"Selected Waste Records     : {len(inventory_df):,}")

# ==========================================================
# LOOKUP VALUES
# ==========================================================

today = datetime.today()

WASTE_REASONS = [
    "Expired",
    "Damaged",
    "Overstock",
    "Recalled",
    "Contaminated"
]

WASTE_WEIGHTS = [
    50,
    20,
    15,
    10,
    5
]

DISPOSAL_METHODS = [
    "Incineration",
    "Return to Supplier",
    "Biohazard Disposal",
    "Recycling"
]

DISPOSAL_STATUS = [
    "Completed",
    "Pending"
]

STATUS_WEIGHTS = [
    90,
    10
]

EMPLOYEES = [
    f"EMP{i:03d}"
    for i in range(1, 21)
]

REMARKS = {
    "Expired": [
        "Medicine expired",
        "Expired stock removed"
    ],
    "Damaged": [
        "Packaging damaged",
        "Broken container"
    ],
    "Overstock": [
        "Excess inventory",
        "Low demand"
    ],
    "Recalled": [
        "Manufacturer recall",
        "Safety recall"
    ],
    "Contaminated": [
        "Quality issue",
        "Contaminated during storage"
    ]
}

print("\nLookup Values Initialized Successfully")

# ==========================================================
# START GENERATION
# ==========================================================

waste_records = []
# ==========================================================
# GENERATE WASTE RECORDS
# ==========================================================

for index, row in inventory_df.iterrows():

    waste_id = f"WR{index + 1:06d}"

    inventory_id = row["Inventory_ID"]
    medicine_id = row["Medicine_ID"]
    batch_number = row["Batch_Number"]

    expiry_date = pd.to_datetime(row["Expiry_Date"])

    unit_cost = round(float(row["Unit_Cost"]), 2)

    quantity_in_stock = int(row["Quantity_In_Stock"])

    warehouse = row["Warehouse_Location"]

    # ------------------------------------------------------
    # Waste Reason
    # ------------------------------------------------------

    waste_reason = random.choices(
        WASTE_REASONS,
        weights=WASTE_WEIGHTS,
        k=1
    )[0]

    # ------------------------------------------------------
    # Quantity Wasted
    # ------------------------------------------------------

    max_quantity = min(quantity_in_stock, 200)

    quantity_wasted = random.randint(
        1,
        max_quantity
    )

    # ------------------------------------------------------
    # Waste Date
    # ------------------------------------------------------

    if waste_reason == "Expired":

        if expiry_date >= today:

            waste_date = today

        else:

            days_after = max((today - expiry_date).days, 1)

            waste_date = expiry_date + timedelta(
                days=random.randint(0, days_after)
            )

    else:

        days_before = random.randint(0, 180)

        waste_date = today - timedelta(days=days_before)

    waste_date = waste_date.strftime("%Y-%m-%d")

    # ------------------------------------------------------
    # Disposal Details
    # ------------------------------------------------------

    disposal_method = random.choice(DISPOSAL_METHODS)

    disposal_status = random.choices(
        DISPOSAL_STATUS,
        weights=STATUS_WEIGHTS,
        k=1
    )[0]

    reported_by = random.choice(EMPLOYEES)

    remarks = random.choice(
        REMARKS[waste_reason]
    )

    # ------------------------------------------------------
    # Total Waste Value
    # ------------------------------------------------------

    total_value = round(
        quantity_wasted * unit_cost,
        2
    )

    # ------------------------------------------------------
    # Append Record
    # ------------------------------------------------------

    waste_records.append({

        "Waste_Record_ID": waste_id,

        "Inventory_ID": inventory_id,

        "Medicine_ID": medicine_id,

        "Batch_Number": batch_number,

        "Waste_Date": waste_date,

        "Expiry_Date": expiry_date.strftime("%Y-%m-%d"),

        "Quantity_Wasted": quantity_wasted,

        "Unit_Cost": unit_cost,

        "Total_Waste_Value": total_value,

        "Waste_Reason": waste_reason,

        "Disposal_Method": disposal_method,

        "Disposal_Status": disposal_status,

        "Reported_By": reported_by,

        "Warehouse_Location": warehouse,

        "Remarks": remarks

    })

print("\nWaste Records Generated Successfully")
print(f"Total Records Generated : {len(waste_records):,}")
# ==========================================================
# CREATE DATAFRAME
# ==========================================================

waste_df = pd.DataFrame(waste_records)

# ==========================================================
# SAVE DATASET
# ==========================================================

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

waste_df.to_csv(
    OUTPUT_FILE,
    index=False
)

# ==========================================================
# DISPLAY SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("WASTE RECORDS DATASET GENERATED SUCCESSFULLY")
print("=" * 70)

print(f"Output File : {OUTPUT_FILE}")
print(f"Rows        : {len(waste_df):,}")
print(f"Columns     : {len(waste_df.columns)}")

print("\nColumns")
print("-" * 70)

for col in waste_df.columns:
    print(col)

print("\nWaste Reason Distribution")
print("-" * 70)
print(waste_df["Waste_Reason"].value_counts())

print("\nDisposal Method Distribution")
print("-" * 70)
print(waste_df["Disposal_Method"].value_counts())

print("\nDisposal Status Distribution")
print("-" * 70)
print(waste_df["Disposal_Status"].value_counts())

print("\nWarehouse Distribution")
print("-" * 70)
print(waste_df["Warehouse_Location"].value_counts())

print("\nTop 10 Employees Reporting Waste")
print("-" * 70)
print(waste_df["Reported_By"].value_counts().head(10))

print("\nWaste Value Statistics")
print("-" * 70)

print(f"Minimum Waste Value : ₹{waste_df['Total_Waste_Value'].min():,.2f}")
print(f"Maximum Waste Value : ₹{waste_df['Total_Waste_Value'].max():,.2f}")
print(f"Average Waste Value : ₹{waste_df['Total_Waste_Value'].mean():,.2f}")
print(f"Total Waste Value   : ₹{waste_df['Total_Waste_Value'].sum():,.2f}")

print("\nQuantity Wasted Statistics")
print("-" * 70)

print(f"Minimum Quantity : {waste_df['Quantity_Wasted'].min()}")
print(f"Maximum Quantity : {waste_df['Quantity_Wasted'].max()}")
print(f"Average Quantity : {waste_df['Quantity_Wasted'].mean():.2f}")

print("\nSample Records")
print("-" * 70)

print(waste_df.head())

print("\n" + "=" * 70)
print("GENERATION COMPLETED SUCCESSFULLY")
print("=" * 70)
print("Waste_Records.csv is READY FOR VALIDATION")
print("=" * 70)