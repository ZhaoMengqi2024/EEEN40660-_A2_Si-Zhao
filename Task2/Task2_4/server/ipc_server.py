# ipc_server.py - volume-only offloading version (final with detailed steps)
import json
import time
import pandas as pd
import os

input_path = "/data/input.json"
output_path = "/data/result.json"

# Step 1: Wait for client data input
print("[Server]  Waiting for /data/input.json ...")
while not os.path.exists(input_path):
    time.sleep(1)
print("[Server]  input.json found. Processing...")

# Step 2: Load raw data
with open(input_path, "r", encoding="utf-8") as f:
    sales = json.load(f)

df = pd.DataFrame(sales)

# Step 3: Data cleaning
# 3.1 Standardize payment types
df["Payment Type"] = df["Payment Type"].replace({
    "CC": "Credit Card",
    "pay pal": "PayPal",
    "Pay Pal": "PayPal"
})
# 3.2 Standardize date format
df["Date of Sale"] = pd.to_datetime(df["Date of Sale"], format='%d %b %Y', errors='coerce').fillna(
    pd.to_datetime(df["Date of Sale"], errors='coerce')
)
df["Date of Sale"] = df["Date of Sale"].dt.strftime('%Y-%m-%d')
# 3.3 Ensure correct numeric types
df["Total Price(€)"] = df["Total Price(€)"].astype(float)
df["Total Profit(€)"] = df["Total Profit(€)"].astype(float)
df["Quantity"] = df["Quantity"].astype(int)
# 3.4 Replace arrows in product categories
df["Product Category"] = df["Product Category"].str.replace(" → ", "_", regex=False)
# 3.5 Drop unnecessary columns
df = df.drop(columns=["Sale Index"], errors='ignore')
# 3.6 Remove invalid quantity rows
df = df[df["Quantity"] > 0]
# 3.7 Remove duplicate rows
df = df.drop_duplicates()

print("[Server]  Preview of cleaned data (first 3 rows):")
print(df.head(3).to_string(index=False))
print("[Server]  Data cleaning complete.")

# Step 4: Data analysis
result = {
    "Total Sales": len(df),
    "Revenue (€)": round(df["Total Price(€)"].sum(), 2),
    "Top Category": df["Product Category"].mode()[0],
}
top3 = df.groupby("Product Category")["Total Price(€)"].sum().sort_values(ascending=False).head(3)
result["Top 3 by Sales"] = top3.round(2).to_dict()

# Step 5: Display data analysis results
print("[Server]  Final Analysis Results sent to client:")
for key, value in result.items():
    print(f"{key}: {value}")

# Step 6: Send result back to client
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)

# Step 7: Clean up input.json
try:
    os.remove(input_path)
    print("[Server]  input.json deleted.")
except Exception as e:
    print(f"[Server]  Warning: Failed to delete input.json ({e})")

# Step 8: Wait for manual exit
input("[Server] Press Enter to exit...")

