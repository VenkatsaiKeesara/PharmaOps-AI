import pandas as pd
from pathlib import Path

# ----------------------------------------
# Project Paths
# ----------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INTERIM_DATA = PROJECT_ROOT / "data" / "interim"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"
REPORTS = PROJECT_ROOT / "docs" / "reports"

# ----------------------------------------
# Load Dataset
# ----------------------------------------

def load_dataset():

    file_path = INTERIM_DATA / "Medicines_Master_Raw.csv"

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    df = pd.read_csv(file_path)

    return df

# ----------------------------------------
# Dataset Summary
# ----------------------------------------

def dataset_summary(df):

    print("\n" + "="*60)
    print("DATASET SUMMARY")
    print("="*60)

    print(f"Rows            : {df.shape[0]:,}")
    print(f"Columns         : {df.shape[1]}")
    print(f"Memory Usage    : {df.memory_usage(deep=True).sum()/1024/1024:.2f} MB")

# ----------------------------------------
# Missing Values
# ----------------------------------------

def missing_values(df):

    print("\n" + "="*60)
    print("MISSING VALUE ANALYSIS")
    print("="*60)

    missing = df.isnull().sum()

    percent = (missing / len(df) * 100).round(2)

    report = pd.DataFrame({

        "Missing Count": missing,

        "Missing %": percent

    })

    report = report.sort_values("Missing Count", ascending=False)

    print(report)

    return report
# ----------------------------------------
# Duplicate Analysis
# ----------------------------------------

def duplicate_analysis(df):

    print("\n" + "=" * 60)
    print("DUPLICATE ANALYSIS")
    print("=" * 60)

    duplicate_ndc = df["Product_NDC"].duplicated().sum()

    duplicate_generic = df["Generic_Name"].duplicated().sum()

    duplicate_brand = df["Brand_Name"].duplicated().sum()

    print(f"Duplicate Product NDC    : {duplicate_ndc:,}")
    print(f"Duplicate Generic Names  : {duplicate_generic:,}")
    print(f"Duplicate Brand Names    : {duplicate_brand:,}")

    return {
        "Duplicate_Product_NDC": duplicate_ndc,
        "Duplicate_Generic_Name": duplicate_generic,
        "Duplicate_Brand_Name": duplicate_brand
    }

# ----------------------------------------
# Product Type Distribution
# ----------------------------------------

def product_type_distribution(df):

    print("\n" + "=" * 60)
    print("PRODUCT TYPE DISTRIBUTION")
    print("=" * 60)

    product_types = (
        df["Product_Type"]
        .value_counts(dropna=False)
        .reset_index()
    )

    product_types.columns = ["Product Type", "Count"]

    print(product_types)

    return product_types

# ----------------------------------------
# Marketing Category Distribution
# ----------------------------------------

def marketing_category_distribution(df):

    print("\n" + "=" * 60)
    print("MARKETING CATEGORY DISTRIBUTION")
    print("=" * 60)

    marketing = (
        df["Marketing_Category"]
        .value_counts(dropna=False)
        .reset_index()
    )

    marketing.columns = ["Marketing Category", "Count"]

    marketing["Percentage"] = (
        marketing["Count"] / len(df) * 100
    ).round(2)

    print(marketing)

    return marketing

# ----------------------------------------
# Dosage Form Distribution
# ----------------------------------------

def dosage_form_distribution(df):

    print("\n" + "=" * 60)
    print("DOSAGE FORM DISTRIBUTION")
    print("=" * 60)

    dosage = (
        df["Dosage_Form"]
        .value_counts(dropna=False)
        .reset_index()
    )

    dosage.columns = ["Dosage Form", "Count"]

    dosage["Percentage"] = (
        dosage["Count"] / len(df) * 100
    ).round(2)

    print(dosage.head(20))

    return dosage

# ----------------------------------------
# Route Distribution
# ----------------------------------------

def route_distribution(df):

    print("\n" + "=" * 60)
    print("ROUTE DISTRIBUTION")
    print("=" * 60)

    route = (
        df["Route"]
        .fillna("UNKNOWN")
        .value_counts(dropna=False)
        .reset_index()
    )

    route.columns = ["Route", "Count"]

    route["Percentage"] = (
        route["Count"] / len(df) * 100
    ).round(2)

    print(route.head(20))

    return route

# ----------------------------------------
# Manufacturer Distribution
# ----------------------------------------

def manufacturer_distribution(df):

    print("\n" + "=" * 60)
    print("TOP 20 MANUFACTURERS")
    print("=" * 60)

    manufacturers = (
        df["Manufacturer"]
        .fillna("UNKNOWN")
        .value_counts()
        .reset_index()
    )

    manufacturers.columns = ["Manufacturer", "Count"]

    manufacturers["Percentage"] = (
        manufacturers["Count"] / len(df) * 100
    ).round(2)

    print(manufacturers.head(20))

    return manufacturers

# ----------------------------------------
# Pharmacological Class Distribution
# ----------------------------------------

def pharm_class_distribution(df):

    print("\n" + "=" * 60)
    print("TOP 20 PHARMACOLOGICAL CLASSES")
    print("=" * 60)

    pharm = (
        df["Pharm_Class"]
        .fillna("UNKNOWN")
        .value_counts()
        .reset_index()
    )

    pharm.columns = ["Pharm Class", "Count"]

    pharm["Percentage"] = (
        pharm["Count"] / len(df) * 100
    ).round(2)

    print(pharm.head(20))

    return pharm

# ----------------------------------------
# Data Quality Score
# ----------------------------------------

def data_quality_score(df):

    print("\n" + "=" * 60)
    print("DATA QUALITY SCORE")
    print("=" * 60)

    total_cells = df.shape[0] * df.shape[1]

    missing_cells = df.isnull().sum().sum()

    completeness = ((total_cells - missing_cells) / total_cells) * 100

    duplicate_ndc = df["Product_NDC"].duplicated().sum()

    uniqueness = (
        (len(df) - duplicate_ndc) / len(df)
    ) * 100

    overall_score = (completeness + uniqueness) / 2

    print(f"Completeness Score : {completeness:.2f}%")
    print(f"Uniqueness Score   : {uniqueness:.2f}%")
    print(f"Overall Score      : {overall_score:.2f}/100")

    if overall_score >= 95:
        grade = "Excellent"
    elif overall_score >= 90:
        grade = "Very Good"
    elif overall_score >= 80:
        grade = "Good"
    else:
        grade = "Needs Improvement"

    print(f"Dataset Grade      : {grade}")

    return {
        "Completeness": round(completeness, 2),
        "Uniqueness": round(uniqueness, 2),
        "Overall Score": round(overall_score, 2),
        "Grade": grade
    }
# ----------------------------------------
# Main
# ----------------------------------------

def main():

    df = load_dataset()

    dataset_summary(df)

    missing_report = missing_values(df)
    duplicate_report = duplicate_analysis(df)
    product_type_report = product_type_distribution(df)
    marketing_report = marketing_category_distribution(df)
    dosage_report = dosage_form_distribution(df)
    route_report = route_distribution(df)
    manufacturer_report = manufacturer_distribution(df)
    pharm_report = pharm_class_distribution(df)
    quality_report = data_quality_score(df)
if __name__ == "__main__":
    main()