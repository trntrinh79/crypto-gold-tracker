import requests
import json
import time
import os

API_URL = "https://www.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/cex/alpha/all/token/list"
HTML_FILE = 'dashboard_alpha.html'
TARGETS = ['WARD', 'KOGE', 'OWL', 'ZTC', 'FIGHT', 'WMTX', 'TRIA']

print("Teddy Fetcher v5 (No-Refresh Mode)")

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'application/json'
}

while True:
    try:
        response = requests.get(API_URL, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            output_items = []
            
            if data.get('success') and 'data' in data:
                token_list = data['data']
                for t in token_list:
                    symbol_raw = t.get('symbol', '').upper()
                    if symbol_raw in TARGETS:
                        price = float(t.get('price', 0))
                        change_24h = float(t.get('percentChange24h', 0))
                        status = "green:stable"
                        if abs(change_24h) > 2: status = "yellow:moderate"
                        if abs(change_24h) > 5: status = "red:unstable"
                        md_map = {'WARD': 29, 'WMTX': 20, 'FIGHT': 16, 'OWL': 9, 'TRIA': 28, 'ZTC': 1}
                        
                        output_items.append({
                            "n": f"{symbol_raw}/USDT",
                            "p": price,
                            "st": status,
                            "md": md_map.get(symbol_raw, 0),
                            "spr": 0.0
                        })
            
            # Inject into HTML
            if os.path.exists(HTML_FILE):
                with open(HTML_FILE, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                
                json_data = json.dumps({"lastUpdated": int(time.time()), "items": output_items})
                
                start_marker = 'const INJECTED_DATA = '
                end_marker = ';// END_INJECT'
                
                if start_marker in html_content:
                    start_idx = html_content.find(start_marker) + len(start_marker)
                    end_idx = html_content.find(end_marker)
                    
                    # Only write if content actually changed (to save SSD cycles)
                    current_injection = html_content[start_idx:end_idx]
                    if current_injection != json_data:
                        new_html = html_content[:start_idx] + json_data + html_content[end_idx:]
                        with open(HTML_FILE, 'w', encoding='utf-8') as f:
                            f.write(new_html)
                        print(f"Updated Data: {len(output_items)} items")
                    else:
                        print("No change", end='\r')
            
        else:
            print(f"Error: {response.status_code}")
            
    except Exception as e:
        print(f"Exception: {e}")
    
    time.sleep(3)
