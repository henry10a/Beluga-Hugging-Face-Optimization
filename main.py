import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("HF_API_KEY")

if not API_KEY:
    print("❌ ERROR: Hugging Face API key not found. Please set HF_API_KEY in your .env file.")
    exit(1)

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

url = "https://webhook.site/45edac62-a567-46f4-835d-c50a89d1c47a"

print("📡 Sending request to", url)
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print("✅ Response received:")
    print(response.json())
except requests.exceptions.RequestException as e:
    print("❌ Request failed:", e)
