import urllib.request
import json
from datetime import datetime

url = "https://api-v2.pendle.finance/core/v1/1/markets?limit=100&is_active=true"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
    
    print("\n--- CAP MONEY PENDLE MARKETS ---\n")
    
    count = 0
    for m in data.get("results", []):
        name = m.get('pt', {}).get('name', '')
        
        if 'cUSD' in name:
            count += 1
            expiry_str = m.get('expiry', '')
            
            # APY math
            imp_apy = m.get('impliedApy', 0) * 100
            long_yld_apy = m.get('longYieldApy', 0) * 100
            liquidity = m.get('liquidity', {}).get('usd', 0)
            
            print(f"Market: {name}")
            print(f"   Expiry: {expiry_str}")
            print(f"   Liquidity: ${liquidity:,.0f}")
            print(f"   Implied APY: {imp_apy:.2f}% (Lower = Cheaper Points)")
            print(f"   Long Yield APY: {long_yld_apy:.2f}% (The 'Points' APY)")
            print("-" * 40)

    if count == 0:
        print("No cUSD markets found.")
    else:
        print(f"\nFound {count} opportunities.")

except Exception as e:
    print(f"Error: {e}")
