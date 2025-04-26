# ipc_client.py - volume-only offloading version (with timing)
import json
import time
import os

# Step 1: Load the original retail dataset from local JSON file
with open('/data/Retail_Sales_in_2024.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

# Step 2: Write the raw data to a shared input file (offloading to server)
with open('/data/input.json', 'w', encoding='utf-8') as f:
    json.dump(raw_data, f, indent=2)

print("[Client]  Data written to /data/input.json")

# Step 3: Start timing before waiting for result
print("[Client]  Waiting for /data/result.json ...")
start_time = time.time()

# Step 4: Poll the shared directory until server returns result
while True:
    try:
        with open('/data/result.json', 'r', encoding='utf-8') as f:
            result = json.load(f)
        break
    except FileNotFoundError:
        time.sleep(1)

end_time = time.time()
offload_time = end_time - start_time

# Step 5: Display the result and timing
print("[Client]  Analysis Results from Server:")
for key, value in result.items():
    print(f"{key}: {value}")

print(f"[Client]  Offloading time: {offload_time:.8f} seconds")


# Step 6: Cleanup result.json after reading
try:
    os.remove('/data/result.json')
    print("[Client]  result.json deleted after reading.")
except Exception as e:
    print(f"[Client]  Warning: Failed to delete result.json - {e}")

# Step 7: Wait for user input to exit
input("[Client] Press Enter to exit...")





