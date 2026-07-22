"""
======================================================================
PHARMAOPS AI
STEP 10 : VALIDATE FINAL MEDICINES MASTER
======================================================================

Purpose:
    Validate the final Medicines Master dataset before loading
    into MySQL and using it for analytics.

Input:
    data/final/Medicines_Master_Final.csv

Output:
    Console Validation Report

======================================================================
"""

import pandas as pd
from pathlib import Path

# ======================================================================
# PATHS
# ======================================================================

BASE_DIR = Path(__file__).resolve().parents[2]

INPUT_FILE = BASE_DIR / "data" / "final" / "Medicines_Master_Final.csv"

# ======================================================================
# LOAD DATA
# ======================================================================

print("=" * 70)
print("PHARMAOPS AI - FINAL MASTER VALIDATION")
print("=" * 70)

df = pd.read_csv(INPUT_FILE)

print(f"\nDataset Loaded Successfully")

print(f"Dataset Name      : {INPUT_FILE.name}")
print(f"Total Records     : {len(df):,}")
print(f"Total Columns     : {len(df.columns)}")

memory_usage = df.memory_usage(deep=True).sum() / (1024 * 1024)

print(f"Memory Usage      : {memory_usage:.2f} MB")

# ======================================================================
# REQUIRED COLUMN VALIDATION
# ======================================================================

print("\n" + "=" * 70)
print("REQUIRED COLUMN VALIDATION")
print("=" * 70)

required_columns = [
    "Medicine_ID",
    "Product_NDC",
    "Generic_Name",
    "Brand_Name",
    "Manufacturer",
    "Active_Ingredient",
    "Strength",
    "Dosage_Form",
    "Route",
    "Pharm_Class",
    "Category_ID",
    "Category_Name"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if len(missing_columns) == 0:
    print("Required Columns : PASS")
else:
    print("Required Columns : FAIL")
    print("\nMissing Columns")
    for col in missing_columns:
        print(f" - {col}")
# ======================================================================
# MISSING VALUE VALIDATION
# ======================================================================

print("\n" + "=" * 70)
print("MISSING VALUE VALIDATION")
print("=" * 70)

missing_values = df.isnull().sum()

missing_df = pd.DataFrame({
    "Column": missing_values.index,
    "Missing_Values": missing_values.values
})

print(missing_df.to_string(index=False))

total_missing = missing_values.sum()

print("\nTotal Missing Values :", total_missing)

# ======================================================================
# DUPLICATE VALIDATION
# ======================================================================

print("\n" + "=" * 70)
print("DUPLICATE VALIDATION")
print("=" * 70)

duplicate_medicine = df["Medicine_ID"].duplicated().sum()

duplicate_ndc = df["Product_NDC"].duplicated().sum()

print(f"Duplicate Medicine_ID : {duplicate_medicine:,}")
print(f"Duplicate Product_NDC : {duplicate_ndc:,}")

# ======================================================================
# CATEGORY VALIDATION
# ======================================================================

print("\n" + "=" * 70)
print("CATEGORY VALIDATION")
print("=" * 70)

valid_categories = [
    "CAT001",
    "CAT002",
    "CAT003",
    "CAT004",
    "CAT005",
    "CAT006",
    "CAT007",
    "CAT008",
    "CAT009",
    "CAT010",
    "CAT011",
    "CAT012",
    "CAT013",
    "CAT014",
    "CAT015"
]

missing_category = df["Category_ID"].isna().sum()

invalid_category = (
    ~df["Category_ID"].isin(valid_categories)
).sum()

print(f"Missing Category_ID : {missing_category:,}")
print(f"Invalid Category_ID : {invalid_category:,}")

# ======================================================================
# PRIMARY KEY VALIDATION
# ======================================================================

print("\n" + "=" * 70)
print("PRIMARY KEY VALIDATION")
print("=" * 70)

if duplicate_medicine == 0:
    print("Medicine_ID Primary Key : PASS")
else:
    print("Medicine_ID Primary Key : FAIL")

if duplicate_ndc == 0:
    print("Product_NDC Uniqueness  : PASS")
else:
    print("Product_NDC Uniqueness  : FAIL")

# ======================================================================
# BASIC DATA QUALITY STATUS
# ======================================================================

print("\n" + "=" * 70)
print("DATA QUALITY STATUS")
print("=" * 70)

if (
    total_missing == 0
    and duplicate_medicine == 0
    and duplicate_ndc == 0
    and invalid_category == 0
):
    print("Overall Validation : PASS")
else:
    print("Overall Validation : FAIL")
# ======================================================================
# CATEGORY DISTRIBUTION
# ======================================================================

print("\n" + "=" * 70)
print("CATEGORY DISTRIBUTION")
print("=" * 70)

category_distribution = (
    df.groupby(["Category_ID", "Category_Name"])
      .size()
      .reset_index(name="Medicine_Count")
      .sort_values(by="Medicine_Count", ascending=False)
)

print(category_distribution.to_string(index=False))

# ======================================================================
# ROUTE DISTRIBUTION
# ======================================================================

print("\n" + "=" * 70)
print("ROUTE DISTRIBUTION")
print("=" * 70)

route_distribution = (
    df["Route"]
    .value_counts(dropna=False)
    .reset_index()
)

route_distribution.columns = ["Route", "Medicine_Count"]

print(route_distribution.to_string(index=False))

# ======================================================================
# DOSAGE FORM DISTRIBUTION
# ======================================================================

print("\n" + "=" * 70)
print("DOSAGE FORM DISTRIBUTION")
print("=" * 70)

dosage_distribution = (
    df["Dosage_Form"]
    .value_counts(dropna=False)
    .reset_index()
)

dosage_distribution.columns = ["Dosage_Form", "Medicine_Count"]

print(dosage_distribution.to_string(index=False))

# ======================================================================
# TOP 10 MANUFACTURERS
# ======================================================================

print("\n" + "=" * 70)
print("TOP 10 MANUFACTURERS")
print("=" * 70)

top_manufacturers = (
    df["Manufacturer"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_manufacturers.columns = ["Manufacturer", "Medicine_Count"]

print(top_manufacturers.to_string(index=False))

# ======================================================================
# TOP 10 ACTIVE INGREDIENTS
# ======================================================================

print("\n" + "=" * 70)
print("TOP 10 ACTIVE INGREDIENTS")
print("=" * 70)

top_ingredients = (
    df["Active_Ingredient"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_ingredients.columns = ["Active_Ingredient", "Medicine_Count"]

print(top_ingredients.to_string(index=False))

# ======================================================================
# BRAND VS GENERIC MEDICINES
# ======================================================================

print("\n" + "=" * 70)
print("BRAND VS GENERIC SUMMARY")
print("=" * 70)

generic_count = df["Generic_Name"].nunique()
brand_count = df["Brand_Name"].nunique()

print(f"Unique Generic Medicines : {generic_count:,}")
print(f"Unique Brand Medicines   : {brand_count:,}")

# ======================================================================
# DATASET STATISTICS
# ======================================================================

print("\n" + "=" * 70)
print("DATASET STATISTICS")
print("=" * 70)

print(f"Unique Manufacturers     : {df['Manufacturer'].nunique():,}")
print(f"Unique Dosage Forms      : {df['Dosage_Form'].nunique():,}")
print(f"Unique Routes            : {df['Route'].nunique():,}")
print(f"Unique Pharm Classes     : {df['Pharm_Class'].nunique():,}")
print(f"Unique Categories        : {df['Category_ID'].nunique():,}")

# ======================================================================
# DATA QUALITY SCORE
# ======================================================================

print("\n" + "=" * 70)
print("FINAL DATA QUALITY REPORT")
print("=" * 70)

# Total cells in dataset
total_cells = df.shape[0] * df.shape[1]

# Completeness Score
missing_cells = df.isnull().sum().sum()
completeness = ((total_cells - missing_cells) / total_cells) * 100

# Uniqueness Score (Medicine_ID + Product_NDC)
medicine_score = (
    (len(df) - duplicate_medicine) / len(df)
) * 100

ndc_score = (
    (len(df) - duplicate_ndc) / len(df)
) * 100

uniqueness = (medicine_score + ndc_score) / 2

# Category Coverage
category_coverage = (
    df["Category_ID"].isin(valid_categories).mean()
) * 100

# Overall Score
overall_score = (
    completeness +
    uniqueness +
    category_coverage
) / 3

# ======================================================================
# DATA QUALITY GRADE
# ======================================================================

if overall_score >= 98:
    grade = "EXCELLENT"
elif overall_score >= 95:
    grade = "VERY GOOD"
elif overall_score >= 90:
    grade = "GOOD"
elif overall_score >= 80:
    grade = "FAIR"
else:
    grade = "POOR"

# ======================================================================
# FINAL VALIDATION STATUS
# ======================================================================

validation_passed = (
    total_missing == 0 and
    duplicate_medicine == 0 and
    duplicate_ndc == 0 and
    invalid_category == 0
)

status = "PASSED" if validation_passed else "FAILED"

print(f"Completeness Score   : {completeness:.2f}%")
print(f"Uniqueness Score     : {uniqueness:.2f}%")
print(f"Category Coverage    : {category_coverage:.2f}%")
print("-" * 70)
print(f"Overall Score        : {overall_score:.2f}/100")
print(f"Dataset Grade        : {grade}")
print(f"Validation Status    : {status}")

# ======================================================================
# SAVE VALIDATION REPORT
# ======================================================================

report_dir = BASE_DIR / "docs" / "reports"
report_dir.mkdir(parents=True, exist_ok=True)

report_file = report_dir / "Medicines_Master_Validation_Report.txt"

with open(report_file, "w", encoding="utf-8") as report:

    report.write("=" * 70 + "\n")
    report.write("PHARMAOPS AI - FINAL MASTER VALIDATION REPORT\n")
    report.write("=" * 70 + "\n\n")

    report.write(f"Dataset Name      : {INPUT_FILE.name}\n")
    report.write(f"Total Records     : {len(df):,}\n")
    report.write(f"Total Columns     : {len(df.columns)}\n")
    report.write(f"Memory Usage      : {memory_usage:.2f} MB\n\n")

    report.write("DATA QUALITY SUMMARY\n")
    report.write("-" * 70 + "\n")
    report.write(f"Missing Values          : {total_missing}\n")
    report.write(f"Duplicate Medicine_ID   : {duplicate_medicine}\n")
    report.write(f"Duplicate Product_NDC   : {duplicate_ndc}\n")
    report.write(f"Invalid Category_ID     : {invalid_category}\n\n")

    report.write(f"Completeness Score      : {completeness:.2f}%\n")
    report.write(f"Uniqueness Score        : {uniqueness:.2f}%\n")
    report.write(f"Category Coverage       : {category_coverage:.2f}%\n")
    report.write(f"Overall Score           : {overall_score:.2f}/100\n")
    report.write(f"Dataset Grade           : {grade}\n")
    report.write(f"Validation Status       : {status}\n")

print("\n" + "=" * 70)
print("VALIDATION REPORT SAVED SUCCESSFULLY")
print("=" * 70)
print(f"Location : {report_file}")

print("\n" + "=" * 70)
print("=" * 70)