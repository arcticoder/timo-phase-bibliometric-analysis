---
layout: default
title: Ti–Mo Phase Sources Scraper
---

# Ti–Mo Phase Sources Scraper

A Python utility to query Scopus and Web of Science APIs for the queries:

- "Ti–Mo phase diagram"
- "Ti–Mo solidus"
- "Ti–Mo β-transus"

Restricted to years 1930–2000. Outputs a CSV tally of distinct source titles.

## Setup

1. Clone or download this repo.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your API keys:
   ```
   SCOPUS_API_KEY=your_scopus_key
   WOS_API_KEY=your_wos_key
   ```

## Usage

```
python timo_phase_sources_scraper.py
```

This produces `source_counts.csv` with columns `source_title,count`.

## More Info

See the [README](https://github.com/username/timo-phase-sources-scraper) for full details and customization options.
