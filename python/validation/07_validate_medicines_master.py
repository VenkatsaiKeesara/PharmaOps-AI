import pandas as pd
from pathlib import Path
from datetime import datetime

DATASET_PATH = Path("data/processed/Medicines_Master_Clean.csv")
REPORT_PATH = Path("python/validation/Medicines_Master_Validation_Report.txt")

EXPECTED_COLUMNS = [
    "Medicine_ID","Product_NDC","Generic_Name","Brand_Name","Manufacturer",
    "Active_Ingredient","Strength","Dosage_Form","Route",
    "Marketing_Category","Product_Type","Marketing_Start_Date","Pharm_Class"
]

ALLOWED_PRODUCT_TYPES = {"HUMAN PRESCRIPTION DRUG","HUMAN OTC DRUG"}

ALLOWED_MARKETING = {"ANDA","NDA","BLA","OTC MONOGRAPH","UNAPPROVED DRUG OTHER"}

def line(c="=",n=70):
    return c*n

report=[]

def add(x=""):
    print(x)
    report.append(x)

add(line())
add("MEDICINES MASTER DATA VALIDATION REPORT")
add(str(datetime.now()))
add(line())

if not DATASET_PATH.exists():
    raise FileNotFoundError(DATASET_PATH)

df=pd.read_csv(DATASET_PATH)

add("\n1. DATASET OVERVIEW")
add(line("-"))
add(f"Rows : {len(df):,}")
add(f"Columns : {len(df.columns)}")

add("\n2. SCHEMA VALIDATION")
add(line("-"))
for c in EXPECTED_COLUMNS:
    add(f"[PASS] {c}" if c in df.columns else f"[FAIL] {c}")

add("\n3. DATA TYPES")
add(line("-"))
for c in df.columns:
    add(f"{c:25} {df[c].dtype}")

add("\n4. MISSING VALUES")
add(line("-"))
for c,v in df.isnull().sum().items():
    add(f"{c:25} {v}")

add("\n5. DUPLICATE VALIDATION")
add(line("-"))
if "Medicine_ID" in df.columns:
    add(f"Duplicate Medicine_ID : {df['Medicine_ID'].duplicated().sum()}")
if "Product_NDC" in df.columns:
    add(f"Duplicate Product_NDC : {df['Product_NDC'].duplicated().sum()}")

add("\n6. BUSINESS RULE VALIDATION")
add(line("-"))
if "Product_Type" in df.columns:
    add(f"Invalid Product Types : {(~df['Product_Type'].isin(ALLOWED_PRODUCT_TYPES)).sum()}")
if "Marketing_Category" in df.columns:
    add(f"Unexpected Marketing Categories : {(~df['Marketing_Category'].isin(ALLOWED_MARKETING)).sum()}")

add("\n7. DOMAIN SUMMARY")
add(line("-"))
for c in ["Product_Type","Marketing_Category","Route","Dosage_Form"]:
    if c in df.columns:
        add(f"\n{c}")
        add(str(df[c].value_counts().head(10)))

cells=df.shape[0]*df.shape[1]
missing=df.isnull().sum().sum()
completeness=((cells-missing)/cells)*100
dup=0
if "Medicine_ID" in df.columns:
    dup+=df["Medicine_ID"].duplicated().sum()
if "Product_NDC" in df.columns:
    dup+=df["Product_NDC"].duplicated().sum()
uniqueness=((len(df)-dup)/len(df))*100
overall=round((completeness+uniqueness)/2,2)

add("\n8. DATA QUALITY SCORE")
add(line("-"))
add(f"Completeness : {completeness:.2f}%")
add(f"Uniqueness   : {uniqueness:.2f}%")
add(f"Overall      : {overall:.2f}%")
add("Status       : APPROVED FOR ANALYTICS" if overall>=95 else "Status : REVIEW REQUIRED")

REPORT_PATH.parent.mkdir(parents=True,exist_ok=True)
REPORT_PATH.write_text("\n".join(report),encoding="utf-8")
print("\nSaved report to:",REPORT_PATH)
