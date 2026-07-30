import pandas as pd
from pathlib import Path

# ----------------------------------------
# Project Paths
# ----------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"
REFERENCE_DATA = PROJECT_ROOT / "data" / "reference"

REFERENCE_DATA.mkdir(parents=True, exist_ok=True)


# ----------------------------------------
# Load Clean Dataset
# ----------------------------------------

def load_dataset():

    file_path = PROCESSED_DATA / "Medicines_Master_Clean.csv"

    df = pd.read_csv(file_path)

    print("=" * 60)
    print("MEDICINES MASTER LOADED")
    print("=" * 60)
    print(f"Records : {len(df):,}")

    return df


# ----------------------------------------
# Generate Pharm Class Reference
# ----------------------------------------

def generate_pharm_class_reference(df):

    pharm = (
        df["Pharm_Class"]
        .dropna()
        .drop_duplicates()
        .sort_values()
        .reset_index(drop=True)
    )

    reference = pd.DataFrame({
        "Pharm_Class": pharm
    })

    reference.to_csv(
        REFERENCE_DATA / "Pharm_Class_Reference.csv",
        index=False
    )

    print("✓ Pharm_Class_Reference.csv Created")
    print(f"Total Pharm Classes : {len(reference):,}")


# ----------------------------------------
# Generate Dosage Form Reference
# ----------------------------------------

def generate_dosage_reference(df):

    dosage = (
        df["Dosage_Form"]
        .drop_duplicates()
        .sort_values()
        .reset_index(drop=True)
    )

    reference = pd.DataFrame({
        "Dosage_Form": dosage
    })

    reference.to_csv(
        REFERENCE_DATA / "Dosage_Form_Reference.csv",
        index=False
    )

    print("✓ Dosage_Form_Reference.csv Created")
    print(f"Total Dosage Forms : {len(reference):,}")


# ----------------------------------------
# Generate Active Ingredient Reference
# ----------------------------------------

def generate_active_reference(df):

    active = (
        df["Active_Ingredient"]
        .drop_duplicates()
        .sort_values()
        .reset_index(drop=True)
    )

    reference = pd.DataFrame({
        "Active_Ingredient": active
    })

    reference.to_csv(
        REFERENCE_DATA / "Active_Ingredient_Reference.csv",
        index=False
    )

    print("✓ Active_Ingredient_Reference.csv Created")
    print(f"Total Active Ingredients : {len(reference):,}")


# ----------------------------------------
# Main
# ----------------------------------------

def main():

    df = load_dataset()

    generate_pharm_class_reference(df)

    generate_dosage_reference(df)

    generate_active_reference(df)

    print("\nReference Tables Generated Successfully!")


if __name__ == "__main__":
    main()