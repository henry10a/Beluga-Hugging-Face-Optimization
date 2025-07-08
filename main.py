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

# Replace this with your actual analysis endpoint
url = "https://www.mysite.com/api/analyze"

print("📡 Sending request to", url)
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print("✅ Response received:")
    print(response.json())
except requests.exceptions.RequestException as e:
    print("❌ Request failed:", e)
