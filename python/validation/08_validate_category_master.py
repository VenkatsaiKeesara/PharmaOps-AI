import pandas as pd
from pathlib import Path
from datetime import datetime

DATASET_PATH = Path("data/reference/Category_Master.csv")
REPORT_PATH = Path("python/validation/Category_Master_Validation_Report.txt")

EXPECTED_COLUMNS = [
    "Category_ID",
    "Category_Name",
    "Description"
]
report=[]

def line(c="=",n=70):
    return c*n

def add(x=""):
    print(x)
    report.append(x)

add(line())
add("CATEGORY MASTER VALIDATION REPORT")
add(str(datetime.now()))
add(line())

if not DATASET_PATH.exists():
    raise FileNotFoundError(DATASET_PATH)

df=pd.read_csv(DATASET_PATH)

add("\n1. DATASET OVERVIEW")
add(line("-"))
add(f"Rows : {len(df)}")
add(f"Columns : {len(df.columns)}")

add("\n2. SCHEMA VALIDATION")
add(line("-"))
for c in EXPECTED_COLUMNS:
    add(f"[PASS] {c}" if c in df.columns else f"[FAIL] {c}")

add("\n3. DATA TYPES")
add(line("-"))
for c in df.columns:
    add(f"{c:20} {df[c].dtype}")

add("\n4. MISSING VALUES")
add(line("-"))
for c,v in df.isnull().sum().items():
    add(f"{c:20} {v}")

add("\n5. DUPLICATE VALIDATION")
add(line("-"))
if "Category_ID" in df.columns:
    add(f"Duplicate Category_ID   : {df['Category_ID'].duplicated().sum()}")
if "Category_Name" in df.columns:
    add(f"Duplicate Category_Name : {df['Category_Name'].duplicated().sum()}")

add("\n6. CATEGORY FORMAT VALIDATION")
add(line("-"))
if "Category_ID" in df.columns:
    invalid=df[~df["Category_ID"].astype(str).str.match(r"^CAT\d{3}$",na=False)]
    add(f"Invalid Category_ID Format : {len(invalid)}")

EXPECTED_COUNT=15
add("\n7. BUSINESS VALIDATION")
add(line("-"))
add(f"Expected Categories : {EXPECTED_COUNT}")
add(f"Actual Categories   : {len(df)}")
if len(df)==EXPECTED_COUNT:
    add("Category Count      : PASS")
else:
    add("Category Count      : CHECK")

if "Category_Name" in df.columns:
    add("\nCategory List")
    add(line("-"))
    for name in sorted(df["Category_Name"].astype(str).tolist()):
        add(f"- {name}")

cells=df.shape[0]*df.shape[1]
missing=df.isnull().sum().sum()
completeness=((cells-missing)/cells)*100
dup=0
if "Category_ID" in df.columns:
    dup+=df["Category_ID"].duplicated().sum()
if "Category_Name" in df.columns:
    dup+=df["Category_Name"].duplicated().sum()
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
