---
layout: default
title: Ti–Mo Phase Bibliometric Analysis
---

# Ti–Mo Phase Bibliometric Analysis

Automated bibliometric analysis of Ti–Mo binary phase-diagram literature (1930–2000), retrieving metadata from Scopus & Web of Science and tallying source-title frequencies.

---

## 🔖 Topics

`bibliometrics ti-mo-phase-diagram calphad python scopus web-of-science latex`

---

## 🔍 Search Queries

**Primary**  
- "Ti–Mo phase diagram"  
- "Ti–Mo solidus"  
- "Ti–Mo β-transus"  

**Variants**  
- "titanium molybdenum phase diagram"  
- "titanium molybdenum solidus"  
- "titanium molybdenum beta transus"  

**Years:** 1930–2000

---

## 📊 Latest Results (May 27, 2025)

### Summary Statistics
- **144 publications** found across **67 unique sources**
- **Primary database:** Scopus (Google Scholar rate-limited)
- **International coverage:** US, German, Soviet/Russian, Japanese journals

### Top 10 Most Cited Sources

| Rank | Source | Count |
|------|---------|-------|
| 1 | Metallurgical Transactions A | 17 |
| 2 | Metallurgical and Materials Transactions A | 9 |
| 3 | Journal of Alloys and Compounds | 7 |
| 4 | Zeitschrift fuer Metallkunde | 5 |
| 5 | Soviet Powder Metallurgy and Metal Ceramics | 5 |
| 6 | Intermetallics | 5 |
| 7 | Poroshkovaya Metallurgiya | 4 |
| 8 | Keikinzoku/Journal of Japan Institute of Light Metals | 4 |
| 9 | Materials Transactions, JIM | 3 |
| 10 | Nippon Kinzoku Gakkaishi | 3 |

**Detection Status:**
- ✅ **1969 papers** found: Phase equilibria in Mo-TiC-Ti system
- ✅ **1981 paper** found: Critical evaluation in *International Metals Reviews*
- ✅ **Murray's Bulletin** appears in reference frequency list
- ❌ **Hansen 1951** not detected (may require Web of Science)

---

## 📁 Generated Files

- [`source_counts.csv`](../source_counts.csv) – frequency tally of each journal/report  
- [`source_counts_detailed.csv`](../source_counts_detailed.csv) – full metadata for all records  
- [`timo_phase_analysis_summary.md`](../timo_phase_analysis_summary.md) – Markdown summary of results  
- [`timo_phase_analysis.tex`](../timo_phase_analysis.tex) – LaTeX report with tables & figures  
- [`timo_phase_analysis.pdf`](../timo_phase_analysis.pdf) – Generated PDF report (227 KB, 5 pages)

---

## 🛠️ Prerequisites

- Python 3.7+  
- Scopus API key (Elsevier)  
- WoS API key (Clarivate)  

```bash
pip install pybliometrics requests python-dotenv
```

---

## ⚙️ Setup & Usage

1. **Clone**  
   ```bash
   git clone https://github.com/arcticoder/timo-phase-bibliometric-analysis.git
   cd timo-phase-bibliometric-analysis
   ```
2. **Configure**  
   - Copy `.env.example → .env`  
   - Add your keys:
     ```ini
     SCOPUS_API_KEY=your_scopus_key
     WOS_API_KEY=your_wos_key
     ```
3. **Run**  
   ```bash
   python timo_phase_sources_scraper.py
   ```
4. **View Results**  
   - Inspect `source_counts.csv`  
   - Compile LaTeX document for PDF report

---

## 🔬 Research Context

Targets foundational Ti–Mo studies:

- **Hansen, Kamen & Kessler (1951)** – β-transus in *Trans. AIME*  
- **Rudy (1969)** – AFML-TR-62-2 solidus/liquidus data  
- **Murray (1981)** – Bulletin of Alloy Phase Diagrams review  

---

## 📖 Documentation

Project site:  
https://arcticoder.github.io/timo-phase-bibliometric-analysis/
