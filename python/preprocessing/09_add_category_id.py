"""
===========================================================
PHARMAOPS AI
STEP 09 : ADD CATEGORY ID TO MEDICINES MASTER
===========================================================
Purpose:
    Merge Category_ID and Category_Name into the
    Medicines_Master_Final dataset using Pharm_Class.

Input Files:
    data/final/Medicines_Master_Final.csv
    data/reference/Pharm_Class_Mapping.csv

Output File:
    data/final/Medicines_Master_Final.csv
===========================================================
"""

import pandas as pd
from pathlib import Path

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]

MEDICINES_FILE = BASE_DIR / "data" / "final" / "Medicines_Master_Final.csv"

MAPPING_FILE = BASE_DIR / "data" / "reference" / "Pharm_Class_Mapping.csv"

OUTPUT_FILE = BASE_DIR / "data" / "final" / "Medicines_Master_Final.csv"

# ==========================================================
# LOAD DATA
# ==========================================================

print("=" * 70)
print("PHARMAOPS AI - ADD CATEGORY ID")
print("=" * 70)

medicines_df = pd.read_csv(MEDICINES_FILE)

mapping_df = pd.read_csv(MAPPING_FILE)

print(f"Medicines Loaded : {len(medicines_df):,}")
print(f"Category Mapping Loaded : {len(mapping_df):,}")

# ==========================================================
# KEEP REQUIRED COLUMNS
# ==========================================================

mapping_df = mapping_df[
    [
        "Pharm_Class",
        "Category_ID",
        "Category_Name"
    ]
]

# ==========================================================
# MERGE
# ==========================================================
# Remove duplicate Pharm_Class entries (safety check)
mapping_df = mapping_df.drop_duplicates(subset="Pharm_Class")
merged_df = medicines_df.merge(
    mapping_df,
    on="Pharm_Class",
    how="left"
)

# ==========================================================
# VALIDATION
# ==========================================================

missing_category = merged_df["Category_ID"].isna().sum()

print("\nValidation")
print("-" * 50)
print(f"Total Records        : {len(merged_df):,}")
print(f"Missing Category_ID  : {missing_category:,}")

# ==========================================================
# SAVE
# ==========================================================

merged_df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8-sig"
)

# ==========================================================
# COMPLETED
# ==========================================================

print("\nUpdated Medicines_Master_Final.csv saved successfully.")

print("=" * 70)
print("CATEGORY ID ADDED SUCCESSFULLY")
print("=" * 70)