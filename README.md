# Ti–Mo Phase Sources Scraper

A Python utility to search Scopus and Google Scholar for publications related to Ti-Mo phase diagrams, limited to 1930–2000, and tally source frequencies.

## 🔍 Search Queries

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

**✅ Successfully completed Scopus search:**
- **144 publications** found across **67 unique sources**
- **Top source:** Metallurgical Transactions A (17 papers)
- **Coverage:** International scope (US, German, Soviet/Russian, Japanese journals)

**❌ Google Scholar:** Rate-limited (common with automated searches)

## 🎯 Key Findings

### Top 5 Most Cited Sources:
1. **Metallurgical Transactions A** (17 papers)
2. **Metallurgical and Materials Transactions A** (9 papers)
3. **Journal of Alloys and Compounds** (7 papers)
4. **Zeitschrift fuer Metallkunde** (5 papers)
5. **Soviet Powder Metallurgy and Metal Ceramics** (5 papers)

### Landmark Papers Detected:
- **1969 papers** (Rudy era): Phase equilibria in Mo-TiC-Ti system
- **1981 paper** (Murray era): Critical evaluation in International Metals Reviews
- **Murray's Bulletin of Alloy Phase Diagrams** appears in reference list

## 📁 Generated Files

- `source_counts.csv` - Frequency count of all 67 sources
- `source_counts_detailed.csv` - Complete publication details (146 entries)
- `timo_phase_analysis_summary.md` - Comprehensive analysis summary
- `timo_phase_analysis.tex` - LaTeX document with results

## 🛠️ Prerequisites

- Python 3.7+  
- Scopus API key (Elsevier)
- WoS API key (Clarivate) - *optional*
- Google Scholar access via `scholarly` library

```bash
pip install requests python-dotenv scholarly
```

## ⚙️ Setup

1. **Clone the repository:**
```bash
git clone <repository-url>
cd timo-phase-sources-scraper
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Create `.env` file:**
```bash
SCOPUS_API_KEY=your_scopus_api_key_here
WOS_API_KEY=your_wos_api_key_here
```

4. **Run the scraper:**
```bash
python timo_phase_sources_scraper.py
```

## 🔬 Research Context

This tool was developed to identify and quantify the most frequently cited publication sources for Ti-Mo phase diagram research, particularly targeting the foundational studies:

- **Hansen, Kamen & Kessler (1951)** - First β-transus determination
- **Rudy (1969)** - AFML technical report on solidus/liquidus
- **Murray (1981)** - Critical review in Bulletin of Alloy Phase Diagrams

## 📖 Documentation

Visit the [project documentation](https://your-username.github.io/timo-phase-sources-scraper/) for detailed analysis and results.

## 📄 License

MIT License - see LICENSE file for details.
