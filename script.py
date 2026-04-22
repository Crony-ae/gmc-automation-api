import os
import json

print("Script is running...")

merchant_id = os.getenv("MERCHANT_ID")

with open("credentials.json") as f:
    creds = json.load(f)

print("Merchant ID:", merchant_id)
print("Project ID:", creds.get("project_id"))
