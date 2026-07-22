# ==========================================================
# PharmaOps AI
# Suppliers Master Dataset Generator
# ==========================================================

import pandas as pd
import random
import string
from datetime import datetime, timedelta
from pathlib import Path

# ----------------------------------------------------------
# Random Seed
# ----------------------------------------------------------

random.seed(42)

# ----------------------------------------------------------
# Project Paths
# ----------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

REFERENCE_FILE = BASE_DIR / "data" / "reference" / "Supplier_Names.csv"

OUTPUT_FILE = BASE_DIR / "data" / "synthetic" / "Suppliers_Master.csv"

# ----------------------------------------------------------
# Load Reference Dataset
# ----------------------------------------------------------

suppliers = pd.read_csv(REFERENCE_FILE)

print("=" * 60)
print("REFERENCE DATASET LOADED")
print("=" * 60)
print(f"Records Loaded : {len(suppliers)}")
print()

# ----------------------------------------------------------
# Generate Supplier IDs
# ----------------------------------------------------------

suppliers.insert(
    0,
    "Supplier_ID",
    [f"SUP{str(i+1).zfill(4)}" for i in range(len(suppliers))]
)

# ==========================================================
# COMPANY DOMAIN MAPPING
# ==========================================================

DOMAIN_MAP = {

    "Sun Pharmaceutical Industries Ltd":"sunpharma.com",
    "Dr. Reddy's Laboratories Ltd":"drreddys.com",
    "Cipla Ltd":"cipla.com",
    "Lupin Ltd":"lupin.com",
    "Aurobindo Pharma Ltd":"aurobindo.com",
    "Torrent Pharmaceuticals Ltd":"torrentpharma.com",
    "Alkem Laboratories Ltd":"alkemlabs.com",
    "Mankind Pharma Ltd":"mankindpharma.com",
    "Zydus Lifesciences Ltd":"zyduslife.com",
    "Glenmark Pharmaceuticals Ltd":"glenmarkpharma.com",
    "Abbott India Ltd":"abbott.com",
    "Pfizer India Ltd":"pfizer.com",
    "Sanofi India Ltd":"sanofi.com",
    "GSK Pharmaceuticals Ltd":"gsk.com",
    "Bayer Pharmaceuticals Pvt Ltd":"bayer.com",
    "Cadila Pharmaceuticals Ltd":"cadilapharma.com",
    "Micro Labs Ltd":"microlabs.in",
    "Intas Pharmaceuticals Ltd":"intaspharma.com",
    "Biocon Ltd":"biocon.com",
    "Alembic Pharmaceuticals Ltd":"alembicpharmaceuticals.com",
    "Hetero Labs Ltd":"hetero.com",
    "Natco Pharma Ltd":"natcopharma.co.in",
    "Divi's Laboratories Ltd":"divislabs.com",
    "Granules India Ltd":"granulesindia.com",
    "Ipca Laboratories Ltd":"ipca.com",
    "Wockhardt Ltd":"wockhardt.com",
    "Strides Pharma Science Ltd":"strides.com",
    "Emcure Pharmaceuticals Ltd":"emcure.com",
    "Ajanta Pharma Ltd":"ajantapharma.com",
    "Eris Lifesciences Ltd":"erislifesciences.com",

    "MedPlus Health Services":"medplusmart.com",
    "Apollo Pharmacy Distribution":"apollopharmacy.in",
    "Reliance Retail Pharma":"relianceretail.com",
    "Tata 1mg Distribution":"1mg.com",
    "Netmeds Distribution":"netmeds.com",
    "Wellness Forever Distribution":"wellnessforever.in",
    "PharmEasy Supply Chain":"pharmeasy.in",

}

# ==========================================================
# UNIQUE VALUE TRACKERS
# ==========================================================

USED_PHONE_NUMBERS = set()

USED_GST_NUMBERS = set()

# ==========================================================
# GST STATE CODES
# ==========================================================

GST_STATE_CODES = {

    "Andhra Pradesh":"37",
    "Telangana":"36",
    "Maharashtra":"27",
    "Gujarat":"24",
    "Karnataka":"29",
    "Tamil Nadu":"33",
    "Delhi":"07",
    "Uttar Pradesh":"09",
    "West Bengal":"19",
    "Rajasthan":"08",
    "Haryana":"06"

}

# ==========================================================
# EMAIL GENERATOR
# ==========================================================

# ==========================================================
# EMAIL GENERATOR
# ==========================================================

def generate_email(company_name):

    # Use official domain if available
    if company_name in DOMAIN_MAP:
        return f"procurement@{DOMAIN_MAP[company_name]}"

    # Otherwise generate a realistic domain
    clean = (
        company_name.lower()
        .replace("limited", "")
        .replace("ltd", "")
        .replace("private", "")
        .replace("pvt", "")
        .replace("industries", "")
        .replace("laboratories", "")
        .replace("laboratory", "")
        .replace("pharmaceuticals", "")
        .replace("pharma", "")
        .replace(".", "")
        .replace(",", "")
        .replace("&", "and")
    )

    clean = "".join(c for c in clean if c.isalnum())

    # Prevent empty domain names
    if clean == "":
        clean = "supplier"

    return f"procurement@{clean}.in"
# ==========================================================
# PHONE NUMBER GENERATOR
# ==========================================================

def generate_phone():

    while True:

        phone = str(random.randint(6000000000,9999999999))

        if phone not in USED_PHONE_NUMBERS:

            USED_PHONE_NUMBERS.add(phone)

            return phone

# ==========================================================
# GST NUMBER GENERATOR
# ==========================================================

def generate_gst(state):

    state_code = GST_STATE_CODES.get(state,"36")

    while True:

        gst = (

            state_code +

            ''.join(random.choices(string.ascii_uppercase,k=5)) +

            ''.join(random.choices(string.digits,k=4)) +

            random.choice(string.ascii_uppercase) +

            "1Z5"

        )

        if gst not in USED_GST_NUMBERS:

            USED_GST_NUMBERS.add(gst)

            return gst
        
# ==========================================================
# LEAD TIME GENERATOR
# ==========================================================

def generate_lead_time(supplier_type):

    if supplier_type == "Manufacturer":
        return random.randint(7, 20)

    elif supplier_type == "Distributor":
        return random.randint(3, 10)

    elif supplier_type == "Wholesaler":
        return random.randint(2, 7)

    return random.randint(5, 15)


# ==========================================================
# SUPPLIER RATING GENERATOR
# ==========================================================

def generate_rating(supplier_type):

    if supplier_type == "Manufacturer":
        return round(random.uniform(4.2, 5.0), 1)

    elif supplier_type == "Distributor":
        return round(random.uniform(3.8, 4.8), 1)

    elif supplier_type == "Wholesaler":
        return round(random.uniform(3.5, 4.6), 1)

    return round(random.uniform(3.5, 5.0), 1)


# ==========================================================
# SUPPLIER CATEGORY
# ==========================================================

def generate_supplier_category():

    return random.choices(
        ["Domestic", "International"],
        weights=[90, 10],
        k=1
    )[0]


# ==========================================================
# PREFERRED SUPPLIER
# ==========================================================

def generate_preferred_supplier():

    return random.choices(
        ["Yes", "No"],
        weights=[25, 75],
        k=1
    )[0]


# ==========================================================
# ACTIVE STATUS
# ==========================================================

def generate_status():

    return random.choices(
        ["Active", "Inactive"],
        weights=[92, 8],
        k=1
    )[0]


# ==========================================================
# CONTRACT DATE GENERATOR
# ==========================================================

def generate_contract_dates():

    start_date = datetime(2022, 1, 1)

    end_date = datetime(2025, 12, 31)

    random_days = random.randint(
        0,
        (end_date - start_date).days
    )

    contract_start = start_date + timedelta(days=random_days)

    contract_end = contract_start + timedelta(
        days=365 * random.randint(3, 5)
    )

    return (
        contract_start.strftime("%Y-%m-%d"),
        contract_end.strftime("%Y-%m-%d")
    )


# ==========================================================
# GENERATE DATASET
# ==========================================================

emails = []
phones = []
lead_times = []
ratings = []
categories = []
preferred = []
status = []
contract_start = []
contract_end = []
gst_numbers = []

print("=" * 60)
print("GENERATING SUPPLIER DATA")
print("=" * 60)

for _, row in suppliers.iterrows():

    emails.append(
        generate_email(row["Supplier_Name"])
    )

    phones.append(
        generate_phone()
    )

    lead_times.append(
        generate_lead_time(row["Supplier_Type"])
    )

    ratings.append(
        generate_rating(row["Supplier_Type"])
    )

    categories.append(
        generate_supplier_category()
    )

    preferred.append(
        generate_preferred_supplier()
    )

    status.append(
        generate_status()
    )

    start, end = generate_contract_dates()

    contract_start.append(start)

    contract_end.append(end)

    gst_numbers.append(
        generate_gst(row["State"])
    )


# ==========================================================
# ADD GENERATED COLUMNS
# ==========================================================

suppliers["Supplier_Category"] = categories

suppliers["Preferred_Supplier"] = preferred

suppliers["Contact_Email"] = emails

suppliers["Contact_Number"] = phones

suppliers["Lead_Time_Days"] = lead_times

suppliers["Supplier_Rating"] = ratings

suppliers["Active_Status"] = status

suppliers["Contract_Start_Date"] = contract_start

suppliers["Contract_End_Date"] = contract_end

suppliers["GST_Number"] = gst_numbers

# ==========================================================
# FINAL COLUMN ORDER
# ==========================================================

FINAL_COLUMNS = [

    "Supplier_ID",
    "Supplier_Name",
    "Supplier_Type",
    "Supplier_Category",
    "Preferred_Supplier",
    "City",
    "State",
    "Contact_Email",
    "Contact_Number",
    "Lead_Time_Days",
    "Supplier_Rating",
    "Active_Status",
    "Contract_Start_Date",
    "Contract_End_Date",
    "GST_Number"

]

suppliers = suppliers[FINAL_COLUMNS]

# ==========================================================
# FINAL DATA CLEANUP
# ==========================================================

# Remove duplicate suppliers if any
suppliers.drop_duplicates(
    subset="Supplier_ID",
    inplace=True
)

# Remove leading/trailing spaces
for column in suppliers.select_dtypes(include="object").columns:
    suppliers[column] = suppliers[column].astype(str).str.strip()

# ==========================================================
# FINAL DATA VALIDATION
# ==========================================================

print()
print("=" * 60)
print("FINAL DATASET VALIDATION")
print("=" * 60)

print(f"Total Records           : {len(suppliers)}")
print(f"Total Columns           : {len(suppliers.columns)}")
print()

print(f"Duplicate Supplier_ID   : {suppliers['Supplier_ID'].duplicated().sum()}")
print(f"Duplicate Supplier Name : {suppliers['Supplier_Name'].duplicated().sum()}")
print(f"Duplicate Emails        : {suppliers['Contact_Email'].duplicated().sum()}")
print(f"Duplicate Phone Numbers : {suppliers['Contact_Number'].duplicated().sum()}")
print(f"Duplicate GST Numbers   : {suppliers['GST_Number'].duplicated().sum()}")

print()

print(f"Missing Values          : {suppliers.isnull().sum().sum()}")

print()

print("Supplier Type Distribution")
print(suppliers["Supplier_Type"].value_counts())

print()

print("Supplier Category Distribution")
print(suppliers["Supplier_Category"].value_counts())

print()

print("Preferred Supplier Distribution")
print(suppliers["Preferred_Supplier"].value_counts())

print()

print("Active Status Distribution")
print(suppliers["Active_Status"].value_counts())

print()

print("Lead Time Statistics")
print(suppliers["Lead_Time_Days"].describe())

print()

print("Supplier Rating Statistics")
print(suppliers["Supplier_Rating"].describe())

# ==========================================================
# EXPORT DATASET
# ==========================================================

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

suppliers.to_csv(
    OUTPUT_FILE,
    index=False
)

# ==========================================================
# SUCCESS MESSAGE
# ==========================================================

print()
print("=" * 60)
print("SUPPLIERS MASTER DATASET GENERATED SUCCESSFULLY")
print("=" * 60)

print(f"Dataset Name  : Suppliers_Master.csv")
print(f"Output Path   : {OUTPUT_FILE}")
print(f"Rows          : {len(suppliers)}")
print(f"Columns       : {len(suppliers.columns)}")

print()

print("Columns")

for col in suppliers.columns:
    print(f"✓ {col}")

print()

print("First Five Records")

print(suppliers.head())

print()

print("=" * 60)
print("DATASET READY FOR VALIDATION & MYSQL IMPORT")
print("=" * 60)