import requests
import sys

def check_symbol(symbol):
    url = f"https://api.binance.com/api/v3/ticker/bookTicker?symbol={symbol}"
    try:
        print(f"Checking {symbol} on Official API...")
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            print(f"SUCCESS: Found {symbol}")
            print(f"Bid: {data['bidPrice']}, Ask: {data['askPrice']}")
            return True
        else:
            print(f"FAILED: {symbol} not found (Status {r.status_code})")
            # Try searching in exchangeInfo
            return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

# Test for WARD and KOGE
print("--- BINANCE OFFICIAL API TEST ---")
found_ward = check_symbol("WARDUSDT")
found_koge = check_symbol("KOGEUSDT")

if not found_ward:
    print("\nConclusion: Alpha tokens are NOT on public v3 API.")
else:
    print("\nConclusion: Alpha tokens ARE on public v3 API.")
