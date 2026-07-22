# Supplier_Master Business Rules

## Dataset Information

- Dataset Name: Suppliers_Master.csv
- Dataset Type: Synthetic Master Dataset
- Number of Records: 75
- Primary Key: Supplier_ID

---

## Business Rule BR-001: Supplier ID

Each supplier must have a unique Supplier_ID.

Format:

SUP0001
SUP0002
...
SUP0075

No duplicate Supplier_ID values are allowed.

---

## Business Rule BR-002: Supplier Name

Supplier names represent real pharmaceutical manufacturers and distributors operating in India.

Each supplier appears only once.

No duplicate supplier names.

---

## Business Rule BR-003: Supplier Type

Allowed values:

- Manufacturer
- Distributor
- Wholesaler

Distribution:

Manufacturer : 40%

Distributor : 35%

Wholesaler : 25%

---

## Business Rule BR-004: State

Allowed states include major pharmaceutical hubs:

- Telangana
- Maharashtra
- Gujarat
- Karnataka
- Tamil Nadu
- Andhra Pradesh
- Delhi
- Uttar Pradesh

No null values.

---

## Business Rule BR-005: City

Each city must belong to its respective state.

Examples:

Hyderabad → Telangana

Ahmedabad → Gujarat

Mumbai → Maharashtra

---

## Business Rule BR-006: Contact Email

Each supplier must have one unique business email.

No duplicate emails.

Email must follow standard email format.

---

## Business Rule BR-007: Contact Number

Each supplier must have one unique 10-digit mobile number.

No duplicate phone numbers.

---

## Business Rule BR-008: Lead Time

Lead_Time_Days must be between

2

and

20

days.

---

## Business Rule BR-009: Supplier Rating

Supplier_Rating must be between

3.5

and

5.0

Most suppliers should have ratings above 4.0.

---

## Business Rule BR-010: Active Status

Allowed values:

- Active
- Inactive

Distribution:

Active : 92%

Inactive : 8%

---

## Business Rule BR-011: Contract Dates

Contract_Start_Date

Between

2022-01-01

and

2025-12-31

Contract_End_Date

Must be later than Contract_Start_Date.

---

## Business Rule BR-012: GST Number

Every supplier must have one unique GST number.

Format:

36ABCDE1234F1Z5

---

## Business Rule BR-013: Data Quality

The dataset must satisfy:

✔ No duplicate Supplier_ID

✔ No duplicate Supplier_Name

✔ No duplicate Contact_Email

✔ No duplicate Contact_Number

✔ No missing values

✔ Valid lead times

✔ Valid ratings

✔ Valid contract dates

✔ Valid GST numbers