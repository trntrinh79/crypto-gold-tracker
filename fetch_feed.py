import requests
import json
import time
import os

FEED_URL = 'https://alpha123.uk/stability/stability_feed_v3.json'
LOCAL_FILE = 'feed.json'

print("Teddy Fetcher Started (No Emojis Mode)")
print(f"Target: {FEED_URL}")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

while True:
    try:
        response = requests.get(FEED_URL, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            with open(LOCAL_FILE, 'w') as f:
                json.dump(data, f)
            print(f"Updated: {len(data.get('items', []))} items")
        else:
            print(f"Error Status: {response.status_code}")
    except Exception as e:
        print(f"Exception: {e}")
    
    time.sleep(3)
