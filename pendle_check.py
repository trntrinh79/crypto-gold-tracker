import requests
import json

# Pendle API V2 Endpoint for Ethereum (Chain ID 1)
url = "https://api-v2.pendle.finance/core/v1/1/markets"
params = {
    "limit": 100,
    "is_active": "true",
    "select": "simple"  # Use simple view to save bandwidth
}

try:
    print(f"Fetching markets from {url}...")
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    
    markets = data.get("results", [])
    print(f"Found {len(markets)} active markets.")
    
    found_cap = False
    for m in markets:
        # Check name or symbol for "cUSD" or "Cap"
        pt = m.get("pt", {})
        sy = m.get("sy", {})
        name = pt.get("name", "") + " " + sy.get("name", "") + " " + sy.get("symbol", "")
        
        if "cUSD" in name or "Cap" in name:
            print("\n--- FOUND CAP MARKET ---")
            print(f"Name: {pt.get('name')}")
            print(f"Market Address: {m.get('address')}")
            print(f"Expiry: {m.get('expiry')}")
            print(f"Implied APY: {m.get('impliedApy')}")
            print(f"Underlying APY: {m.get('underlyingApy')}")
            print(f"Liquidity: ${m.get('liquidity', {}).get('usd', 0):,.2f}")
            found_cap = True

    if not found_cap:
        print("\nNo direct match for 'cUSD' found in top 100 active markets.")
        
except Exception as e:
    print(f"Error: {e}")
