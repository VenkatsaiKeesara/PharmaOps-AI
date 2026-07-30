import json
import pandas as pd
from pathlib import Path

# -------------------------------
# Project Paths
# -------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA = PROJECT_ROOT / "data" / "raw"
INTERIM_DATA = PROJECT_ROOT / "data" / "interim"

# ----------------------------------------
# Stage 1: Read & Validate FDA JSON Dataset
# ----------------------------------------

json_file = RAW_DATA / "drug_ndc.json"

# Check if file exists
if not json_file.exists():
    raise FileNotFoundError(f"Dataset not found: {json_file}")

# Load JSON file
with open(json_file, "r", encoding="utf-8") as file:
    data = json.load(file)

print("=" * 60)
print("FDA NDC DATASET VALIDATION")
print("=" * 60)

print("\nDataset Loaded Successfully!")

# Display top-level keys
print("\nTop-Level Keys:")
print(list(data.keys()))

# Get medicine records
medicine_records = data.get("results", [])

print(f"\nTotal Medicine Records: {len(medicine_records):,}")

# Display available fields
if medicine_records:
    print("\nAvailable Fields in First Record:\n")
    for field in medicine_records[0].keys():
        print(f"- {field}")
else:
    print("No medicine records found.")


# ----------------------------------------
# Stage 2: Inspect First Medicine Record
# ----------------------------------------

print("\n" + "=" * 60)
print("FIRST MEDICINE RECORD")
print("=" * 60)

from pprint import pprint

pprint(medicine_records[0])


# ----------------------------------------
# Stage 3: Create Medicines Master Dataset
# ----------------------------------------

medicine_master = []

for index, record in enumerate(medicine_records, start=1):

    # Extract active ingredient information
    active_ingredients = record.get("active_ingredients", [])

    active_name = None
    strength = None

    if active_ingredients:
        active_name = active_ingredients[0].get("name")
        strength = active_ingredients[0].get("strength")

    # Extract first route
    routes = record.get("route", [])
    route = routes[0] if routes else None

    # Extract first pharmacological class
    pharm_classes = record.get("pharm_class", [])
    pharm_class = pharm_classes[0] if pharm_classes else None

    medicine_master.append({

        "Medicine_ID": f"MED{index:06d}",

        "Product_NDC": record.get("product_ndc"),

        "Generic_Name": record.get("generic_name"),

        "Brand_Name": record.get("brand_name"),

        "Manufacturer": record.get("labeler_name"),

        "Active_Ingredient": active_name,

        "Strength": strength,

        "Dosage_Form": record.get("dosage_form"),

        "Route": route,

        "Marketing_Category": record.get("marketing_category"),

        "Product_Type": record.get("product_type"),

        "Marketing_Start_Date": record.get("marketing_start_date"),

        "Pharm_Class": pharm_class

    })

# Convert to DataFrame
medicines_df = pd.DataFrame(medicine_master)

print("\n")
print("=" * 60)
print("MEDICINES MASTER CREATED")
print("=" * 60)

print(f"Total Records : {len(medicines_df):,}")
print(f"Total Columns : {len(medicines_df.columns)}")

print("\nColumns:")

for column in medicines_df.columns:
    print(f"- {column}")

# Save CSV
output_file = INTERIM_DATA / "Medicines_Master_Raw.csv"

medicines_df.to_csv(output_file, index=False)

print("\nMedicines_Master.csv saved successfully!")
print(f"Location: {output_file}")