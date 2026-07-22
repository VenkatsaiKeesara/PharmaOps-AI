# ============================================================
# PharmaOps AI
# Purchase Orders Dataset Generator
# Dataset: Purchase_Orders.csv
# ============================================================

import pandas as pd
import numpy as np
import random
from pathlib import Path
from datetime import datetime, timedelta

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

random.seed(42)
np.random.seed(42)

TOTAL_RECORDS = 3000

# ------------------------------------------------------------
# Project Paths
# ------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

PROCESSED_PATH = PROJECT_ROOT / "data" / "processed"
SYNTHETIC_PATH = PROJECT_ROOT / "data" / "synthetic"

SYNTHETIC_PATH.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------
# Load Reference Datasets
# ------------------------------------------------------------

medicines_df = pd.read_csv(
    PROCESSED_PATH / "Medicines_Master_Clean.csv"
)

suppliers_df = pd.read_csv(
    SYNTHETIC_PATH / "Suppliers_Master.csv"
)

medicine_ids = medicines_df["Medicine_ID"].tolist()
supplier_ids = suppliers_df["Supplier_ID"].tolist()

# ------------------------------------------------------------
# Lookup Values
# ------------------------------------------------------------

PAYMENT_METHODS = [
    "Bank Transfer",
    "UPI",
    "Credit"
]

PAYMENT_STATUS = [
    "Paid",
    "Pending",
    "Partial"
]

ORDER_STATUS = [
    "Delivered",
    "Pending",
    "Cancelled"
]

WAREHOUSES = [
    "WH-A",
    "WH-B",
    "WH-C",
    "WH-D",
    "WH-E"
]

PROCUREMENT_MANAGERS = [
    "Rahul Sharma",
    "Priya Nair",
    "Amit Verma",
    "Sneha Reddy",
    "Karan Mehta",
    "Neha Gupta",
    "Arjun Patel",
    "Rohit Kumar"
]

# ------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------

def random_order_date():
    """
    Generate order dates within the last 2 years.
    """
    today = datetime.today()

    start_date = today - timedelta(days=730)

    delta = (today - start_date).days

    return start_date + timedelta(
        days=random.randint(0, delta)
    )


def generate_delivery_dates(order_date, status):
    """
    Generate expected and actual delivery dates.
    """

    expected = order_date + timedelta(
        days=random.randint(2, 10)
    )

    if status == "Delivered":

        actual = expected + timedelta(
            days=random.randint(-1, 3)
        )

        if actual < order_date:
            actual = order_date

    else:
        actual = pd.NaT

    return expected, actual

# ------------------------------------------------------------
# Generate Purchase Orders
# ------------------------------------------------------------

purchase_orders = []

for i in range(1, TOTAL_RECORDS + 1):

    purchase_order_id = f"PO{i:06d}"

    medicine_id = random.choice(medicine_ids)

    supplier_id = random.choice(supplier_ids)

    # --------------------------------------------------------
    # Order Status
    # --------------------------------------------------------

    order_status = random.choices(
        ORDER_STATUS,
        weights=[75, 20, 5],
        k=1
    )[0]

    # --------------------------------------------------------
    # Dates
    # --------------------------------------------------------

    order_date = random_order_date()

    expected_delivery_date, actual_delivery_date = generate_delivery_dates(
        order_date,
        order_status
    )

    # --------------------------------------------------------
    # Quantity
    # --------------------------------------------------------

    quantity_ordered = random.randint(50, 2000)

    # --------------------------------------------------------
    # Pricing
    # --------------------------------------------------------

    unit_purchase_cost = round(
        random.uniform(5, 600),
        2
    )

    total_order_value = round(
        quantity_ordered * unit_purchase_cost,
        2
    )

    # --------------------------------------------------------
    # Payment Method
    # --------------------------------------------------------

    payment_method = random.choice(
        PAYMENT_METHODS
    )

    # --------------------------------------------------------
    # Payment Status
    # --------------------------------------------------------

    if order_status == "Delivered":

        payment_status = random.choices(
            PAYMENT_STATUS,
            weights=[80, 5, 15],
            k=1
        )[0]

    elif order_status == "Pending":

        payment_status = random.choices(
            ["Pending", "Partial"],
            weights=[80, 20],
            k=1
        )[0]

    else:

        payment_status = "Pending"

    # --------------------------------------------------------
    # Warehouse
    # --------------------------------------------------------

    warehouse = random.choice(
        WAREHOUSES
    )

    # --------------------------------------------------------
    # Procurement Manager
    # --------------------------------------------------------

    procurement_manager = random.choice(
        PROCUREMENT_MANAGERS
    )

    # --------------------------------------------------------
    # Store Record
    # --------------------------------------------------------

    purchase_orders.append({

        "Purchase_Order_ID": purchase_order_id,

        "Medicine_ID": medicine_id,

        "Supplier_ID": supplier_id,

        "Order_Date": order_date.date(),

        "Expected_Delivery_Date": expected_delivery_date.date(),

        "Actual_Delivery_Date":
            actual_delivery_date.date()
            if pd.notna(actual_delivery_date)
            else None,

        "Quantity_Ordered": quantity_ordered,

        "Unit_Purchase_Cost": unit_purchase_cost,

        "Total_Order_Value": total_order_value,

        "Payment_Method": payment_method,

        "Payment_Status": payment_status,

        "Order_Status": order_status,

        "Warehouse_Location": warehouse,

        "Procurement_Manager": procurement_manager

    })
# ------------------------------------------------------------
# Create DataFrame
# ------------------------------------------------------------

purchase_orders_df = pd.DataFrame(purchase_orders)

# Sort by Purchase Order ID
purchase_orders_df.sort_values(
    by="Purchase_Order_ID",
    inplace=True
)

purchase_orders_df.reset_index(
    drop=True,
    inplace=True
)

# ------------------------------------------------------------
# Export Dataset
# ------------------------------------------------------------

output_file = SYNTHETIC_PATH / "Purchase_Orders.csv"

purchase_orders_df.to_csv(
    output_file,
    index=False
)

# ------------------------------------------------------------
# Dataset Summary
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("PURCHASE ORDERS DATASET GENERATED SUCCESSFULLY")
print("=" * 65)

print(f"Output File   : {output_file}")
print(f"Rows          : {len(purchase_orders_df):,}")
print(f"Columns       : {purchase_orders_df.shape[1]}")

print("\nColumn Names")
print("-" * 65)

for column in purchase_orders_df.columns:
    print(f"- {column}")

print("\nFirst 5 Records")
print("-" * 65)
print(purchase_orders_df.head())

print("\nOrder Status Distribution")
print("-" * 65)
print(purchase_orders_df["Order_Status"].value_counts())

print("\nPayment Status Distribution")
print("-" * 65)
print(purchase_orders_df["Payment_Status"].value_counts())

print("\nPayment Method Distribution")
print("-" * 65)
print(purchase_orders_df["Payment_Method"].value_counts())

print("\nWarehouse Distribution")
print("-" * 65)
print(purchase_orders_df["Warehouse_Location"].value_counts())

print("\nProcurement Manager Distribution")
print("-" * 65)
print(purchase_orders_df["Procurement_Manager"].value_counts())

print("\nOrder Quantity Statistics")
print("-" * 65)
print(
    purchase_orders_df["Quantity_Ordered"].describe()
)

print("\nPurchase Cost Statistics")
print("-" * 65)
print(
    purchase_orders_df[
        [
            "Unit_Purchase_Cost",
            "Total_Order_Value"
        ]
    ].describe()
)

print("\n" + "=" * 65)
print("Dataset Ready for Validation")
print("=" * 65)
