import requests

URLS = [
    "https://www.binance.com/bapi/growth/v1/friendly/growth-alpha/token/list",
    "https://www.binance.com/bapi/growth/v1/public/growth-alpha/token/list",
    "https://www.binance.com/bapi/bigdata/v1/friendly/bigdata/finance/exchange/alpha/tokenList"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}

print("Testing Internal BAPI Endpoints...")

for url in URLS:
    try:
        print(f"Trying: {url}")
        r = requests.get(url, headers=headers, timeout=5)
        print(f"Status: {r.status_code}")
        if r.status_code == 200:
            print(f"Response: {r.text[:200]}...")
    except Exception as e:
        print(f"Error: {e}")
