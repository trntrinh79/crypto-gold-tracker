---
name: google-search
description: Search the web using Google Custom Search API. Returns titles, links, and snippets. Use for current events, fact-checking, or finding specific pages.
tools:
  - name: google_search
    description: Search Google for a query.
    parameters:
      type: object
      properties:
        query:
          type: string
          description: The search terms.
      required: [query]
    run: |
      node skills/google-search/index.js "{{query}}"
---
# Google Search Skill

This skill allows Clawdbot to search the web using your Google Programmable Search Engine.

## Configuration
Edit `skills/google-search/config.json`:
```json
{
  "apiKey": "YOUR_API_KEY",
  "cx": "YOUR_SEARCH_ENGINE_ID"
}
```

## Setup
1. Get API Key: https://developers.google.com/custom-search/v1/overview
2. Get CX ID: https://programmablesearchengine.google.com/ (Create engine -> "Search the entire web" -> Copy "cx" param)
