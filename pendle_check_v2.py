import urllib.request
import json

# Pendle API V2 Endpoint for Ethereum (Chain ID 1)
url = "https://api-v2.pendle.finance/core/v1/1/markets?limit=100&is_active=true&select=simple"

try:
    print(f"Fetching markets from {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
    
    markets = data.get("results", [])
    print(f"Found {len(markets)} active markets.")
    
    found_cap = False
    for m in markets:
        # Check name or symbol for "cUSD" or "Cap"
        pt = m.get("pt", {})
        sy = m.get("sy", {})
        name = (pt.get("name", "") + " " + sy.get("name", "") + " " + sy.get("symbol", "")).lower()
        
        if "cusd" in name:
            print("\n--- FOUND CAP MARKET ---")
            print(f"Name: {pt.get('name')}")
            print(f"Market Address: {m.get('address')}")
            print(f"Expiry: {m.get('expiry')}")
            
            # APY is often a float like 0.15 for 15%
            imp_apy = m.get('impliedApy', 0) * 100
            print(f"Implied APY: {imp_apy:.2f}%")
            
            liq = m.get('liquidity', {}).get('usd', 0)
            print(f"Liquidity: ${liq:,.2f}")
            found_cap = True

    if not found_cap:
        print("\nNo direct match for 'cUSD' found in top 100 active markets.")
        
except Exception as e:
    print(f"Error: {e}")
