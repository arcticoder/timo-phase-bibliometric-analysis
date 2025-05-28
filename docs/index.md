---
layout: default
title: Ti–Mo Phase Sources Scraper
---

# Ti–Mo Phase Sources Scraper

A Python utility to search Scopus and Google Scholar for publications related to Ti-Mo phase diagrams, limited to 1930–2000, and tally source frequencies.

## 🔍 Search Scope

**Primary targets:**
- "Ti–Mo phase diagram" / "Ti-Mo phase diagram"
- "Ti–Mo solidus" / "Ti-Mo solidus"  
- "Ti–Mo β-transus" / "Ti-Mo beta transus"

**Additional variations:**
- "titanium molybdenum phase diagram"
- "titanium molybdenum solidus"
- "titanium molybdenum beta transus"

**Time period:** 1930–2000 (targeting landmark early studies)

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

### Landmark Papers Context

This research targets the foundational Ti-Mo phase studies:

- **Hansen, Kamen & Kessler (1951)** - First β-transus determination (*Trans. AIME*)
- **Rudy (1969)** - AFML technical report on solidus/liquidus  
- **Murray (1981)** - Critical review (*Bulletin of Alloy Phase Diagrams*)

**Detection Status:**
- ✅ **1969 papers** found: Phase equilibria in Mo-TiC-Ti system
- ✅ **1981 paper** found: Critical evaluation in *International Metals Reviews*
- ✅ **Murray's Bulletin** appears in reference frequency list
- ❌ **Hansen 1951** not detected (may require Web of Science)

## 📁 Generated Files

- [`source_counts.csv`](../source_counts.csv) - Frequency count of all 67 sources
- [`source_counts_detailed.csv`](../source_counts_detailed.csv) - Complete publication details
- [`timo_phase_analysis_summary.md`](../timo_phase_analysis_summary.md) - Comprehensive analysis
- [`timo_phase_analysis.tex`](../timo_phase_analysis.tex) - LaTeX bibliometric report

## 📄 Publications

A formal bibliometric analysis has been prepared in LaTeX format:

**"Bibliometric Analysis of Ti–Mo Phase Diagram Literature (1930–2000)"**  
*Author:* Arcticoder  
*Date:* May 27, 2025

This peer-review ready document provides:
- Comprehensive methodology section
- Statistical analysis of 144 publications across 67 sources
- Discussion of publication patterns and international collaboration
- Identification of landmark papers within the dataset
- Complete bibliography of foundational works

## ⚙️ Setup & Usage

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd timo-phase-sources-scraper
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API keys** (create `.env` file):
   ```bash
   SCOPUS_API_KEY=your_scopus_api_key_here
   WOS_API_KEY=your_wos_api_key_here  # optional
   ```

4. **Run the scraper:**
   ```bash
   python timo_phase_sources_scraper.py
   ```

## 🔬 Research Impact

**Key Finding:** *Metallurgical Transactions A* emerges as the dominant publication venue for Ti-Mo phase research, with 17 papers representing 12% of all publications found.

This quantitative analysis provides the first systematic bibliometric foundation for understanding the historical development of Ti-Mo phase research and identifying the most authoritative publication sources.

## 📖 Full Documentation

Visit the [GitHub repository](https://github.com/username/timo-phase-sources-scraper) for complete source code, detailed methodology, and analysis files.
