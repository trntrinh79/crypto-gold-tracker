import requests
import json

# URL đoán dựa trên cấu trúc API Web của Binance (thường dùng bapi cho alpha/new features)
# URL từ doc: https://developers.binance.com/docs/alpha/market-data/rest-api/token-list
# Nhưng doc không ghi rõ Base URL, tôi sẽ thử các base phổ biến.

URLS = [
    "https://www.binance.com/bapi/bigdata/v1/public/bigdata/finance/exchange/alpha/tokenList",
    "https://api.binance.com/api/v3/alpha/tokenList", 
    "https://data-api.binance.vision/api/v3/alpha/tokenList"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

print("Testing Binance Alpha Endpoints...")

for url in URLS:
    try:
        print(f"Trying: {url}")
        r = requests.get(url, headers=headers, timeout=5)
        print(f"Status: {r.status_code}")
        if r.status_code == 200:
            data = r.json()
            print("SUCCESS! Data found.")
            # Print sample of first token to verify structure
            if "data" in data and len(data["data"]) > 0:
                token = data["data"][0]
                print(f"Sample: {token.get('symbol')} | ID: {token.get('alphaId')} | Price: {token.get('price')}")
            break
    except Exception as e:
        print(f"Error: {e}")
