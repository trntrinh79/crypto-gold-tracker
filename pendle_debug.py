import urllib.request
import json

url = "https://api-v2.pendle.finance/core/v1/1/markets?limit=10&is_active=true"

try:
    print(f"Fetching debug data...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        raw = response.read().decode()
        data = json.loads(raw)
        
    print(f"Total entries: {data.get('total')}")
    if data.get('results'):
        print("Sample Market Name:", data['results'][0].get('pt', {}).get('name'))
    else:
        print("No results array found. Keys:", data.keys())

except Exception as e:
    print(f"Error: {e}")
