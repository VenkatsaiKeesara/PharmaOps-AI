import pandas as pd
from pathlib import Path

# ============================================================
# Project Paths
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

REFERENCE_FOLDER = PROJECT_ROOT / "data" / "reference"

# ============================================================
# Load Pharm Class Reference
# ============================================================

df = pd.read_csv(
    REFERENCE_FOLDER / "Pharm_Class_Reference.csv"
)

# ============================================================
# Category Mapping
# ============================================================

CATEGORY_MAPPING = {
    "Allergy": "CAT001",
    "Antibiotics": "CAT002",
    "Cardiovascular": "CAT003",
    "Dermatology": "CAT004",
    "Diabetes": "CAT005",
    "Gastrointestinal": "CAT006",
    "Infectious Diseases": "CAT007",
    "Neurology": "CAT008",
    "Oncology": "CAT009",
    "Pain Management": "CAT010",
    "Psychiatry": "CAT011",
    "Respiratory": "CAT012",
    "Others": "CAT013"
}


# ============================================================
# Assign Business Category
# ============================================================

def assign_category(pharm_class):

    if pd.isna(pharm_class):
        return "Others"

    text = pharm_class.upper()

    # Cardiovascular
    if any(k in text for k in [
        "CARDIO",
        "ANGIOTENSIN",
        "ACE",
        "BETA",
        "CALCIUM CHANNEL",
        "VASODILATOR",
        "STATIN",
        "HMG-COA",
        "CHOLESTEROL"
    ]):
        return "Cardiovascular"

    # Diabetes
    if any(k in text for k in [
        "INSULIN",
        "DIABET",
        "GLP",
        "HYPOGLYCEMIC"
    ]):
        return "Diabetes"

    # Antibiotics
    if any(k in text for k in [
        "ANTIBIOTIC",
        "PENICILLIN",
        "MACROLIDE",
        "CEPH",
        "QUINOLONE",
        "SULFONAMIDE"
    ]):
        return "Antibiotics"

    # Pain Management
    if any(k in text for k in [
        "ANTI-INFLAMMATORY",
        "NSAID",
        "OPIOID",
        "ANALGESIC",
        "CYCLOOXYGENASE"
    ]):
        return "Pain Management"

    # Neurology
    if any(k in text for k in [
        "EPILEP",
        "NEURO",
        "CENTRAL NERVOUS",
        "DOPAMINE",
        "SEROTONIN"
    ]):
        return "Neurology"

    # Psychiatry
    if any(k in text for k in [
        "ANTIPSYCHOTIC",
        "ANTIDEPRESS",
        "ANXIOLYTIC"
    ]):
        return "Psychiatry"

    # Respiratory
    if any(k in text for k in [
        "BRONCHO",
        "RESPIRATORY",
        "ASTHMA",
        "LEUKOTRIENE"
    ]):
        return "Respiratory"

    # Gastrointestinal
    if any(k in text for k in [
        "GASTRIC",
        "PROTON",
        "ANTACID",
        "INTESTINAL",
        "LAXATIVE"
    ]):
        return "Gastrointestinal"

    # Dermatology
    if any(k in text for k in [
        "DERM",
        "SKIN",
        "TOPICAL"
    ]):
        return "Dermatology"

    # Ophthalmology -> Dermatology
    if any(k in text for k in [
        "OPHTHALMIC",
        "EYE"
    ]):
        return "Dermatology"

    # Allergy
    if any(k in text for k in [
        "ALLERGEN",
        "HISTAMINE"
    ]):
        return "Allergy"

    # Oncology
    if any(k in text for k in [
        "ANTINEOPLASTIC",
        "ONCO",
        "CANCER",
        "TUMOR"
    ]):
        return "Oncology"

    # Infectious Diseases
    if any(k in text for k in [
        "ANTIVIRAL",
        "ANTIFUNGAL",
        "ANTIPARASITIC"
    ]):
        return "Infectious Diseases"

    return "Others"


# ============================================================
# Generate Mapping
# ============================================================

df["Category_Name"] = df["Pharm_Class"].apply(assign_category)

df["Category_ID"] = df["Category_Name"].map(CATEGORY_MAPPING)

# ============================================================
# Category Master
# ============================================================

category_master = pd.DataFrame({

    "Category_ID": list(CATEGORY_MAPPING.values()),

    "Category_Name": list(CATEGORY_MAPPING.keys())

})

category_master = category_master.sort_values("Category_ID")

# ============================================================
# Pharm Class Mapping
# ============================================================

mapping = df[

    [

        "Pharm_Class",

        "Category_ID",

        "Category_Name"

    ]

].sort_values("Category_Name")

# ============================================================
# Export
# ============================================================

category_master.to_csv(

    REFERENCE_FOLDER / "Category_Master.csv",

    index=False

)

mapping.to_csv(

    REFERENCE_FOLDER / "PharmClass_Category_Map.csv",

    index=False

)

# ============================================================
# Summary
# ============================================================

print("=" * 60)
print("CATEGORY TABLES GENERATED")
print("=" * 60)

print(f"Business Categories : {len(category_master)}")

print(f"Pharm Classes Mapped : {len(mapping)}")

print("\nCategory Master")

print(category_master)

print("\nTop 20 Pharm Class Mapping")

print(mapping.head(20))