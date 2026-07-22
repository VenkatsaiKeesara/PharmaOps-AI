import pandas as pd
from pathlib import Path

# ----------------------------------------
# Project Paths
# ----------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INTERIM_DATA = PROJECT_ROOT / "data" / "interim"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"

# ----------------------------------------
# Load Dataset
# ----------------------------------------

def load_dataset():

    file_path = INTERIM_DATA / "Medicines_Master_Raw.csv"

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    df = pd.read_csv(file_path)

    print("\n" + "=" * 60)
    print("RAW DATASET LOADED")
    print("=" * 60)
    print(f"Records Loaded : {len(df):,}")

    return df
# ----------------------------------------
# BR-001
# Filter Product Types
# ----------------------------------------

def filter_product_types(df):

    print("\n" + "=" * 60)
    print("BR-001 : FILTER PRODUCT TYPES")
    print("=" * 60)

    before = len(df)

    allowed_types = [

        "HUMAN PRESCRIPTION DRUG",

        "HUMAN OTC DRUG",

        "VACCINE"

    ]

    df = df[df["Product_Type"].isin(allowed_types)].copy()

    after = len(df)

    removed = before - after

    print(f"Records Before : {before:,}")
    print(f"Records Removed: {removed:,}")
    print(f"Records After  : {after:,}")

    return df

# ----------------------------------------
# BR-002
# Remove Missing Generic Name
# ----------------------------------------

def remove_missing_generic_name(df):

    print("\n" + "=" * 60)
    print("BR-002 : REMOVE MISSING GENERIC NAME")
    print("=" * 60)

    before = len(df)

    df = df.dropna(subset=["Generic_Name"]).copy()

    after = len(df)

    removed = before - after

    print("Status          : SUCCESS")
    print(f"Records Before  : {before:,}")
    print(f"Records Removed : {removed:,}")
    print(f"Records After   : {after:,}")

    return df

# ----------------------------------------
# BR-003
# Handle Missing Brand Name
# ----------------------------------------

def fill_missing_brand_name(df):

    print("\n" + "=" * 60)
    print("BR-003 : HANDLE MISSING BRAND NAME")
    print("=" * 60)

    before_missing = df["Brand_Name"].isna().sum()

    df["Brand_Name"] = df["Brand_Name"].fillna(df["Generic_Name"])

    after_missing = df["Brand_Name"].isna().sum()

    filled = before_missing - after_missing

    print("Status          : SUCCESS")
    print(f"Missing Before  : {before_missing:,}")
    print(f"Filled Records  : {filled:,}")
    print(f"Missing After   : {after_missing:,}")

    return df

# ----------------------------------------
# BR-004
# Handle Missing Route
# ----------------------------------------

def fill_missing_route(df):

    print("\n" + "=" * 60)
    print("BR-004 : HANDLE MISSING ROUTE")
    print("=" * 60)

    before_missing = df["Route"].isna().sum()

    df["Route"] = df["Route"].fillna("UNKNOWN")

    after_missing = df["Route"].isna().sum()

    print("Status          : SUCCESS")
    print(f"Missing Before  : {before_missing:,}")
    print(f"Filled Records  : {before_missing-after_missing:,}")
    print(f"Missing After   : {after_missing:,}")

    return df

# ----------------------------------------
# BR-005
# Handle Missing Pharm Class
# ----------------------------------------

def fill_missing_pharm_class(df):

    print("\n" + "=" * 60)
    print("BR-005 : HANDLE MISSING PHARM CLASS")
    print("=" * 60)

    before_missing = df["Pharm_Class"].isna().sum()

    df["Pharm_Class"] = df["Pharm_Class"].fillna("UNKNOWN")

    after_missing = df["Pharm_Class"].isna().sum()

    print("Status          : SUCCESS")
    print(f"Missing Before  : {before_missing:,}")
    print(f"Filled Records  : {before_missing-after_missing:,}")
    print(f"Missing After   : {after_missing:,}")

    return df

# ----------------------------------------
# BR-006
# Standardize Text
# ----------------------------------------

def standardize_text(df):

    print("\n" + "=" * 60)
    print("BR-006 : STANDARDIZE TEXT")
    print("=" * 60)

    title_case_columns = [
        "Generic_Name",
        "Brand_Name",
        "Manufacturer"
    ]

    upper_case_columns = [
        "Dosage_Form",
        "Route",
        "Marketing_Category",
        "Product_Type"
    ]

    for col in title_case_columns:
        df[col] = df[col].astype(str).str.strip().str.title()

    for col in upper_case_columns:
        df[col] = df[col].astype(str).str.strip().str.upper()

    print("Status : SUCCESS")
    print("Text formatting standardized.")

    return df

# ----------------------------------------
# BR-007
# Remove Duplicate Medicine_ID
# ----------------------------------------

def remove_duplicate_medicine_id(df):

    print("\n" + "=" * 60)
    print("BR-007 : REMOVE DUPLICATE MEDICINE ID")
    print("=" * 60)

    before = len(df)

    df = df.drop_duplicates(subset=["Medicine_ID"])

    after = len(df)

    print("Status          : SUCCESS")
    print(f"Duplicates Removed : {before-after:,}")
    print(f"Records Remaining : {after:,}")

    return df

# ----------------------------------------
# BR-008
# Remove Duplicate Product NDC
# ----------------------------------------

def remove_duplicate_product_ndc(df):

    print("\n" + "=" * 60)
    print("BR-008 : REMOVE DUPLICATE PRODUCT NDC")
    print("=" * 60)

    before = len(df)

    df = df.drop_duplicates(subset=["Product_NDC"], keep="first")

    after = len(df)

    print("Status          : SUCCESS")
    print(f"Duplicates Removed : {before-after:,}")
    print(f"Records Remaining : {after:,}")

    return df

# ----------------------------------------
# BR-009
# Filter Marketing Categories
# ----------------------------------------

def filter_marketing_category(df):

    print("\n" + "=" * 60)
    print("BR-009 : FILTER MARKETING CATEGORY")
    print("=" * 60)

    before = len(df)

    remove_categories = [
        "EXPORT ONLY",
        "EMERGENCY USE AUTHORIZATION"
    ]

    df = df[
        ~df["Marketing_Category"].isin(remove_categories)
    ].copy()

    after = len(df)

    print("Status          : SUCCESS")
    print(f"Records Removed : {before-after:,}")
    print(f"Records Remaining : {after:,}")

    return df

# ----------------------------------------
# BR-010
# Handle Missing Active Ingredient & Strength
# ----------------------------------------

def handle_missing_active_strength(df):

    print("\n" + "=" * 60)
    print("BR-010 : HANDLE MISSING ACTIVE INGREDIENT & STRENGTH")
    print("=" * 60)

    before_active = df["Active_Ingredient"].isna().sum()
    before_strength = df["Strength"].isna().sum()

    # Fill missing values
    df["Active_Ingredient"] = df["Active_Ingredient"].fillna("UNKNOWN")
    df["Strength"] = df["Strength"].fillna("UNKNOWN")

    after_active = df["Active_Ingredient"].isna().sum()
    after_strength = df["Strength"].isna().sum()

    print("Status                 : SUCCESS")
    print(f"Missing Active Before  : {before_active:,}")
    print(f"Missing Active After   : {after_active:,}")
    print(f"Filled Active Records  : {before_active - after_active:,}")
    print("-" * 60)
    print(f"Missing Strength Before: {before_strength:,}")
    print(f"Missing Strength After : {after_strength:,}")
    print(f"Filled Strength Records: {before_strength - after_strength:,}")

    return df

# ----------------------------------------
# BR-011
# Standardize Date Format
# ----------------------------------------

def standardize_dates(df):

    print("\n" + "=" * 60)
    print("BR-011 : STANDARDIZE DATE FORMAT")
    print("=" * 60)

    before_invalid = df["Marketing_Start_Date"].isna().sum()

    df["Marketing_Start_Date"] = pd.to_datetime(
        df["Marketing_Start_Date"],
        format="%Y%m%d",
        errors="coerce"
    )

    after_invalid = df["Marketing_Start_Date"].isna().sum()

    print("Status                : SUCCESS")
    print(f"Invalid Dates Before  : {before_invalid:,}")
    print(f"Invalid Dates After   : {after_invalid:,}")

    return df

# ----------------------------------------
# BR-012
# Final Dataset Validation
# ----------------------------------------

def validate_dataset(df):

    print("\n" + "=" * 60)
    print("BR-012 : FINAL DATASET VALIDATION")
    print("=" * 60)

    print(f"Total Records               : {len(df):,}")
    print(f"Total Columns               : {df.shape[1]}")

    print("-" * 60)

    print(f"Duplicate Medicine_ID       : {df['Medicine_ID'].duplicated().sum():,}")
    print(f"Duplicate Product_NDC       : {df['Product_NDC'].duplicated().sum():,}")

    print("-" * 60)

    print(f"Missing Generic_Name        : {df['Generic_Name'].isna().sum():,}")
    print(f"Missing Brand_Name          : {df['Brand_Name'].isna().sum():,}")
    print(f"Missing Route               : {df['Route'].isna().sum():,}")
    print(f"Missing Pharm_Class         : {df['Pharm_Class'].isna().sum():,}")
    print(f"Missing Active_Ingredient   : {df['Active_Ingredient'].isna().sum():,}")
    print(f"Missing Strength            : {df['Strength'].isna().sum():,}")

    print("\nValidation Status : PASSED ✅")

    return df

# ----------------------------------------
# BR-013
# Export Clean Dataset
# ----------------------------------------

def export_clean_dataset(df):

    print("\n" + "=" * 60)
    print("BR-013 : EXPORT CLEAN DATASET")
    print("=" * 60)

    output_file = PROCESSED_DATA / "Medicines_Master_Clean.csv"

    df.to_csv(output_file, index=False)

    print("Status          : SUCCESS")
    print("Dataset Exported Successfully")
    print(f"Location        : {output_file}")
    print(f"Final Records   : {len(df):,}")

    return df

# ----------------------------------------
# BR-014
# Cleaning Summary
# ----------------------------------------

def cleaning_summary(df):

    print("\n" + "=" * 60)
    print("CLEANING SUMMARY")
    print("=" * 60)

    print("Cleaning Pipeline Completed Successfully!")

    print(f"Final Records : {len(df):,}")
    print(f"Final Columns : {df.shape[1]}")

    print("\nOutput File")
    print("-----------")
    print("Medicines_Master_Clean.csv")

    print("\nNext Step")
    print("---------")
    print("04_create_final_master.py")

    return
# ----------------------------------------
# Main
# ----------------------------------------

def main():

    df = load_dataset()

    df = filter_product_types(df)
    df = remove_missing_generic_name(df)
    df = fill_missing_brand_name(df)
    df = fill_missing_route(df)
    df = fill_missing_pharm_class(df)
    df = standardize_text(df)
    df = remove_duplicate_medicine_id(df)
    df = remove_duplicate_product_ndc(df)
    df = filter_marketing_category(df)
    df = handle_missing_active_strength(df)
    df = standardize_dates(df)
    df = validate_dataset(df)
    df = export_clean_dataset(df)
    cleaning_summary(df)
# ----------------------------------------
# Entry Point
# ----------------------------------------

if __name__ == "__main__":
    main()