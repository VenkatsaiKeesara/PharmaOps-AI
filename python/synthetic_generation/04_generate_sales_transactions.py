# ============================================================
# PharmaOps AI
# Sales Transactions Dataset Generator
# Dataset: Sales_Transactions.csv
# ============================================================

import pandas as pd
import numpy as np
import random
from pathlib import Path
from datetime import datetime, timedelta, time

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

random.seed(42)
np.random.seed(42)

TOTAL_RECORDS = 10000

# ------------------------------------------------------------
# Project Paths
# ------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

PROCESSED_PATH = PROJECT_ROOT / "data" / "processed"
SYNTHETIC_PATH = PROJECT_ROOT / "data" / "synthetic"

SYNTHETIC_PATH.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------
# Load Reference Dataset
# ------------------------------------------------------------

inventory_df = pd.read_csv(
    PROJECT_ROOT / "data" / "synthetic" / "Medicines_Inventory.csv"
)

medicine_ids = (
    inventory_df["Medicine_ID"]
    .drop_duplicates()
    .tolist()
)
# ------------------------------------------------------------
# Lookup Values
# ------------------------------------------------------------

BRANCH_IDS = [
    "BR001",
    "BR002",
    "BR003",
    "BR004",
    "BR005"
]

PAYMENT_METHODS = [
    "Cash",
    "UPI",
    "Card",
    "Insurance"
]

CUSTOMER_TYPES = [
    "Walk-in",
    "Member",
    "Online"
]

PRESCRIPTION_REQUIRED = [
    "Yes",
    "No"
]

TRANSACTION_STATUS = [
    "Completed",
    "Returned",
    "Cancelled"
]

PHARMACIST_IDS = [
    f"PH{i:03d}"
    for i in range(1, 16)
]

DISCOUNTS = [
    0,
    5,
    10,
    15,
    20
]

# ------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------

def random_transaction_date():
    """
    Generate a transaction date within
    the last two years.
    """

    today = datetime.today()

    start_date = today - timedelta(days=730)

    delta = (today - start_date).days

    return start_date + timedelta(
        days=random.randint(0, delta)
    )


def random_sale_time():
    """
    Generate a random sale time between
    08:00 AM and 10:00 PM.
    """

    start_minutes = 8 * 60
    end_minutes = 22 * 60

    minutes = random.randint(
        start_minutes,
        end_minutes
    )

    hour = minutes // 60
    minute = minutes % 60

    return time(hour, minute)


def calculate_total(
    quantity,
    unit_price,
    discount
):
    """
    Calculate total amount after discount.
    """

    subtotal = quantity * unit_price

    total = subtotal - (
        subtotal * discount / 100
    )

    return round(total, 2)
# ------------------------------------------------------------
# Generate Sales Transactions
# ------------------------------------------------------------

sales_transactions = []

for i in range(1, TOTAL_RECORDS + 1):

    # --------------------------------------------------------
    # IDs
    # --------------------------------------------------------

    transaction_id = f"TXN{i:06d}"

    invoice_number = f"INV2026{i:06d}"

    medicine_id = random.choice(
        medicine_ids
    )

    branch_id = random.choice(
        BRANCH_IDS
    )

    # --------------------------------------------------------
    # Date & Time
    # --------------------------------------------------------

    transaction_date = random_transaction_date()

    sale_time = random_sale_time()

    # --------------------------------------------------------
    # Quantity Sold
    # --------------------------------------------------------

    quantity_sold = random.choices(
        population=[1,2,3,4,5,6,7,8,9,10],
        weights=[40,25,15,6,4,5,2,1,1,1],
        k=1
    )[0]

    # --------------------------------------------------------
    # Unit Selling Price
    # --------------------------------------------------------

    unit_selling_price = round(
        random.uniform(10,1200),
        2
    )

    # --------------------------------------------------------
    # Discount Percentage
    # --------------------------------------------------------

    discount_percentage = random.choices(
        population=DISCOUNTS,
        weights=[45,25,15,10,5],
        k=1
    )[0]

    # --------------------------------------------------------
    # Total Amount
    # --------------------------------------------------------

    total_amount = calculate_total(
        quantity_sold,
        unit_selling_price,
        discount_percentage
    )

    # --------------------------------------------------------
    # Payment Method
    # --------------------------------------------------------

    payment_method = random.choices(
        population=PAYMENT_METHODS,
        weights=[30,45,20,5],
        k=1
    )[0]

    # --------------------------------------------------------
    # Customer Type
    # --------------------------------------------------------

    customer_type = random.choices(
        population=CUSTOMER_TYPES,
        weights=[60,30,10],
        k=1
    )[0]

    # --------------------------------------------------------
    # Prescription Required
    # --------------------------------------------------------

    prescription_required = random.choices(
        population=PRESCRIPTION_REQUIRED,
        weights=[30,70],   # Yes, No
        k=1
    )[0]

    # --------------------------------------------------------
    # Pharmacist
    # --------------------------------------------------------

    pharmacist_id = random.choice(
        PHARMACIST_IDS
    )

    # --------------------------------------------------------
    # Transaction Status
    # --------------------------------------------------------

    transaction_status = random.choices(
        population=TRANSACTION_STATUS,
        weights=[95,3,2],
        k=1
    )[0]

    # --------------------------------------------------------
    # Store Record
    # --------------------------------------------------------

    sales_transactions.append({

        "Transaction_ID": transaction_id,

        "Invoice_Number": invoice_number,

        "Medicine_ID": medicine_id,

        "Branch_ID": branch_id,

        "Transaction_Date": transaction_date.date(),

        "Sale_Time": sale_time.strftime("%H:%M:%S"),

        "Quantity_Sold": quantity_sold,

        "Unit_Selling_Price": unit_selling_price,

        "Discount_Percentage": discount_percentage,

        "Total_Amount": total_amount,

        "Payment_Method": payment_method,

        "Customer_Type": customer_type,

        "Prescription_Required": prescription_required,

        "Pharmacist_ID": pharmacist_id,

        "Transaction_Status": transaction_status

    })
# ------------------------------------------------------------
# Create DataFrame
# ------------------------------------------------------------

sales_transactions_df = pd.DataFrame(sales_transactions)

# Sort by Transaction ID
sales_transactions_df.sort_values(
    by="Transaction_ID",
    inplace=True
)

sales_transactions_df.reset_index(
    drop=True,
    inplace=True
)

# ------------------------------------------------------------
# Export Dataset
# ------------------------------------------------------------

output_file = SYNTHETIC_PATH / "Sales_Transactions.csv"

sales_transactions_df.to_csv(
    output_file,
    index=False
)

# ------------------------------------------------------------
# Dataset Summary
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("SALES TRANSACTIONS DATASET GENERATED SUCCESSFULLY")
print("=" * 70)

print(f"Output File : {output_file}")
print(f"Rows        : {len(sales_transactions_df):,}")
print(f"Columns     : {sales_transactions_df.shape[1]}")

print("\nColumn Names")
print("-" * 70)

for column in sales_transactions_df.columns:
    print(f"- {column}")

print("\nFirst 5 Records")
print("-" * 70)
print(sales_transactions_df.head())

print("\nTransaction Status Distribution")
print("-" * 70)
print(
    sales_transactions_df["Transaction_Status"].value_counts()
)

print("\nPayment Method Distribution")
print("-" * 70)
print(
    sales_transactions_df["Payment_Method"].value_counts()
)

print("\nCustomer Type Distribution")
print("-" * 70)
print(
    sales_transactions_df["Customer_Type"].value_counts()
)

print("\nPrescription Requirement Distribution")
print("-" * 70)
print(
    sales_transactions_df["Prescription_Required"].value_counts()
)

print("\nBranch Distribution")
print("-" * 70)
print(
    sales_transactions_df["Branch_ID"].value_counts()
)

print("\nPharmacist Distribution")
print("-" * 70)
print(
    sales_transactions_df["Pharmacist_ID"].value_counts()
)

print("\nDiscount Distribution")
print("-" * 70)
print(
    sales_transactions_df["Discount_Percentage"].value_counts().sort_index()
)

print("\nQuantity Sold Statistics")
print("-" * 70)
print(
    sales_transactions_df["Quantity_Sold"].describe()
)

print("\nSales Amount Statistics")
print("-" * 70)
print(
    sales_transactions_df[
        [
            "Unit_Selling_Price",
            "Total_Amount"
        ]
    ].describe()
)

print("\nDaily Sales Overview")
print("-" * 70)

daily_sales = (
    sales_transactions_df
    .groupby("Transaction_Date")["Total_Amount"]
    .sum()
)

print(f"Unique Transaction Days : {daily_sales.shape[0]}")
print(f"Average Daily Revenue   : ₹{daily_sales.mean():,.2f}")
print(f"Maximum Daily Revenue   : ₹{daily_sales.max():,.2f}")
print(f"Minimum Daily Revenue   : ₹{daily_sales.min():,.2f}")

print("\n" + "=" * 70)
print("Sales_Transactions.csv Ready for Validation")
print("=" * 70)