import requests
import json
import os
import pyopdb
from dotenv import load_dotenv
load_dotenv()


# Access the API key from the environment variable
api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable.")

# URL to check

url_to_check = input("Enter the URL to check: ").strip()

# Google Safe Browsing API endpoint
api_endpoint = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"

# Prepare the request payload
payload = {
    "client": {
        "clientId": "yourcompanyname",
        "clientVersion": "1.0"
    },
    "threatInfo": {
        "threatTypes": ["SOCIAL_ENGINEERING", "MALWARE", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
        "platformTypes": ["ANY_PLATFORM"],
        "threatEntryTypes": ["URL"],
        "threatEntries": [
            {"url": url_to_check}
        ]
    }
}

# Send the request
response = requests.post(api_endpoint, data=json.dumps(payload))

# Check the response
if response.status_code == 200:
    threats = response.json().get("matches", [])
    if threats:
        print("The URL is flagged as potentially dangerous by Google Safe Browsing.")
        for threat in threats:
            print(f"- Threat Type: {threat['threatType']}")
            print(f"- Platform: {threat['platformType']}")
    else:
        print("The URL is not flagged by Google Safe Browsing.")
else:
    print(f"Error: Received status code {response.status_code} from Google Safe Browsing API")
    

