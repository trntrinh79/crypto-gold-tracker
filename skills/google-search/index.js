const fs = require('fs');
const path = require('path');
const https = require('https');

// Load config
const configPath = path.join(__dirname, 'config.json');
let config = {};
try {
    config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
} catch (err) {
    console.error("Error loading config.json:", err.message);
    process.exit(1);
}

const API_KEY = process.env.GOOGLE_SEARCH_API_KEY || config.apiKey;
const CX = process.env.GOOGLE_SEARCH_CX || config.cx;

if (!API_KEY || !CX || CX === 'YOUR_SEARCH_ENGINE_ID_HERE') {
    console.error("Error: Missing API Key or CX (Search Engine ID). Please update skills/google-search/config.json");
    process.exit(1);
}

const query = process.argv[2];
if (!query) {
    console.error("Usage: node search.js <query>");
    process.exit(1);
}

const url = `https://customsearch.googleapis.com/customsearch/v1?key=${API_KEY}&cx=${CX}&q=${encodeURIComponent(query)}`;

https.get(url, (res) => {
    let data = '';
    res.on('data', (chunk) => { data += chunk; });
    res.on('end', () => {
        if (res.statusCode !== 200) {
            console.error(`API Error: ${res.statusCode} ${res.statusMessage}`);
            console.error(data);
            return;
        }
        try {
            const json = JSON.parse(data);
            if (!json.items || json.items.length === 0) {
                console.log("No results found.");
                return;
            }

            // Format for LLM consumption
            const results = json.items.slice(0, 8).map(item => ({
                title: item.title,
                link: item.link,
                snippet: item.snippet
            }));
            
            console.log(JSON.stringify(results, null, 2));
        } catch (e) {
            console.error("Error parsing response:", e.message);
        }
    });
}).on('error', (e) => {
    console.error("Network error:", e.message);
});
