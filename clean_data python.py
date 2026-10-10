import pandas as pd
import numpy as np
from pathlib import Path

INPUT_FILE = Path("messy_sample_dataset.csv")
OUTPUT_FILE = Path("cleaned_customer_dataset.csv")
MISSING_TOKENS = {"", "unknown", "n/a", "na", "not available", "null", "none"}

def standardize_header(name):
    return "_".join(str(name).strip().lower().replace("-", " ").split())

df = pd.read_csv(INPUT_FILE, dtype=str)
rows_before = len(df)
df.columns = [standardize_header(c) for c in df.columns]
df = df.replace(r"^\\s*$", np.nan, regex=True)
for col in df.columns:
    df[col] = df[col].map(lambda x: np.nan if isinstance(x, str) and x.strip().lower() in MISSING_TOKENS else x)

duplicates_removed = int(df.duplicated().sum())
df = df.drop_duplicates().copy()
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)

df["city"] = df["city"].str.title()
df["membership"] = df["membership"].str.title()
df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce", dayfirst=False).dt.strftime("%Y-%m-%d")
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df.loc[(df["age"] < 0) | (df["age"] > 100), "age"] = np.nan
df["age"] = df["age"].round().astype("Int64")
df["purchase_amount"] = pd.to_numeric(df["purchase_amount"], errors="coerce")
median_amount = df["purchase_amount"].median()
df["purchase_amount"] = df["purchase_amount"].fillna(median_amount).round(2)
df["orders"] = pd.to_numeric(df["orders"], errors="coerce").fillna(0).astype("Int64")
df["customer_name"] = df["customer_name"].fillna("Unknown")
df["membership"] = df["membership"].fillna("Unknown")
df = df.dropna(subset=["customer_id"]).copy()
df.to_csv(OUTPUT_FILE, index=False)

print(f"Rows before cleaning: {rows_before}")
print(f"Exact duplicates removed: {duplicates_removed}")
print(f"Rows after cleaning: {len(df)}")
print("Remaining missing values:")
print(df.isna().sum())
print(f"Saved cleaned data to {OUTPUT_FILE.resolve()}")
