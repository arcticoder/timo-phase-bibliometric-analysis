# Ti–Mo Phase Bibliometric Analysis

Automated bibliometric analysis of Ti–Mo binary phase-diagram literature (1930–2000), retrieving metadata from Scopus & Web of Science and tallying source-title frequencies.

---

## 🔖 Topics

`bibliometrics ti-mo-phase-diagram calphad python scopus web-of-science latex`

---

## 🔍 Search Queries

**Primary**  
- “Ti–Mo phase diagram”  
- “Ti–Mo solidus”  
- “Ti–Mo β-transus”  

**Variants**  
- “titanium molybdenum phase diagram”  
- “titanium molybdenum solidus”  
- “titanium molybdenum beta transus”  

**Years:** 1930–2000

---

## 📁 Generated Files

- `source_counts.csv`              – frequency tally of each journal/report  
- `source_counts_detailed.csv`     – full metadata for all records  
- `timo_phase_analysis_summary.md` – Markdown summary of results  
- `timo_phase_bibliometric_analysis.tex` – LaTeX report with tables & figures  

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
   - Compile `timo_phase_bibliometric_analysis.tex` for a PDF report.

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