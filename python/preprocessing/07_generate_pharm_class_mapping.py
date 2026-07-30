# ==========================================================
# PHARMAOPS AI
# Generate Pharm Class Mapping Table
# ==========================================================

from pathlib import Path
import pandas as pd

# ==========================================================
# PROJECT PATHS
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "final" / "Medicines_Master_Final.csv"
OUTPUT_FOLDER = PROJECT_ROOT / "data" / "reference"
OUTPUT_FILE = OUTPUT_FOLDER / "Pharm_Class_Mapping.csv"

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# ==========================================================
# LOAD DATA
# ==========================================================

print("=" * 70)
print("GENERATING PHARM CLASS MAPPING")
print("=" * 70)

try:
    medicines_df = pd.read_csv(INPUT_FILE)
    print(f"\nMedicines Loaded : {len(medicines_df):,}")

except Exception as e:
    print(f"\nError loading Medicines_Master_Final.csv")
    print(e)
    exit()

# ==========================================================
# EXTRACT UNIQUE PHARM CLASSES
# ==========================================================

pharm_classes = (
    medicines_df["Pharm_Class"]
    .fillna("UNKNOWN")
    .astype(str)
    .str.strip()
    .drop_duplicates()
    .sort_values()
    .reset_index(drop=True)
)

# ==========================================================
# CREATE MAPPING TABLE
# ==========================================================

mapping_df = pd.DataFrame({
    "Pharm_Class": pharm_classes,
    "Category_ID": "",
    "Category_Name": ""
})

# ==========================================================
# SAVE FILE
# ==========================================================

mapping_df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8-sig"
)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("PHARM CLASS MAPPING GENERATED")
print("=" * 70)

print(f"Unique Pharm Classes : {len(mapping_df):,}")
print(f"Output File          : {OUTPUT_FILE}")

print("\nFirst 10 Pharm Classes")
print("-" * 70)
print(mapping_df.head(10))

print("\nLast 10 Pharm Classes")
print("-" * 70)
print(mapping_df.tail(10))

print("\nGeneration Completed Successfully.")
print("Pharm_Class_Mapping.csv is READY FOR CATEGORY MAPPING")

print("=" * 70)