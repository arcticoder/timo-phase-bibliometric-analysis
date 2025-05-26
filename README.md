# Ti–Mo Phase Sources Scraper

A Python utility to pull publication metadata from Scopus and Web of Science for the queries:
- “Ti–Mo phase diagram”
- “Ti–Mo solidus”
- “Ti–Mo β-transus”

Restricted to years 1930–2000. Outputs a frequency tally of distinct source titles.

---

## Features

- Authenticates via your Scopus & WoS API keys  
- Runs each query in sequence and aggregates `source_title` counts  
- Outputs a CSV of `source_title, count`

---

## Prerequisites

- Python 3.7+  
- An Elsevier (Scopus) API key  
- A Clarivate (WoS) API key  

```bash
pip install pybliometrics requests python-dotenv
