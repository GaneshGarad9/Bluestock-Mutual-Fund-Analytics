# Bluestock Mutual Fund Analytics Platform

## Project Overview
This is an end-to-end Mutual Fund Analytics Capstone Project prepared for Bluestock Fintech. The project covers data ingestion, data cleaning, SQLite data warehouse design, SQL analytics, exploratory data analysis, performance analytics, advanced risk analytics, and dashboard reporting.

## Business Objective
The objective is to help analysts compare mutual fund schemes, understand SIP and AUM trends, evaluate risk-adjusted returns, study investor behavior, and generate dashboard-ready insights for decision-making.

## Completed Modules

| Day | Module | Key Deliverables |
|---|---|---|
| Day 1 | Data Ingestion | Raw CSV loading, mfapi NAV fetch scripts, data quality checks |
| Day 2 | Data Cleaning + SQLite | 10 cleaned CSVs, SQLite database, schema.sql, queries.sql, data dictionary |
| Day 3 | EDA | EDA_Analysis notebook, 15+ charts, EDA findings |
| Day 4 | Performance Analytics | CAGR, Sharpe, Sortino, Alpha/Beta, Drawdown, Scorecard |
| Day 5 | Power BI Dashboard | Dashboard guide, DAX measures, screenshots, dashboard PDF |
| Day 6 | Advanced Analytics | VaR/CVaR, rolling Sharpe, cohort analysis, SIP continuity, recommender |
| Day 7 | Final Documentation | Final report, presentation, README, run_pipeline.py |

## Dataset Summary
- Fund master records: 40 schemes
- NAV history records: 46,000
- Investor transactions: 32,778
- AUM fund houses tracked: 10
- Latest SIP inflow tracked: Rs 31,002 Cr
- Latest folio count tracked: 26.12 Cr

## Project Structure
```text
bluestock_day1_to_day7_final_submission/
├── data/raw/                     # Original datasets
├── data/processed/               # Cleaned and analytics-ready outputs
├── database/                     # SQLite database
├── notebooks/                    # Jupyter notebooks
├── sql/                          # schema.sql and analytical queries
├── reports/                      # Final report, data dictionary, outputs
├── charts/                       # Advanced analytics charts
├── powerbi_dashboard/            # Dashboard assets and screenshots
├── scripts/                      # Python scripts
├── Final_Report.pdf
├── Bluestock_MF_Presentation.pptx
├── README.md
└── run_pipeline.py
```

## Setup Instructions
```bash
pip install -r bluestock_day1_to_day5_final_project/requirements.txt
```

## Run the Pipeline
```bash
python run_pipeline.py
```

## Main Outputs
- `Final_Report.pdf`
- `Bluestock_MF_Presentation.pptx`
- `reports/var_cvar_report.csv`
- `outputs/daily_returns_all_funds.csv`
- `outputs/rolling_90d_sharpe.csv`
- `outputs/investor_cohort_analysis.csv`
- `outputs/sip_continuity_analysis.csv`
- `outputs/sector_hhi_concentration.csv`
- `scripts/recommender.py`

## Power BI Dashboard
Open Power BI Desktop and use the cleaned CSV files from:
```text
bluestock_day1_to_day5_final_project/data/processed/
```
Dashboard screenshots and guide are available in:
```text
bluestock_day1_to_day5_final_project/powerbi_dashboard/
```

## Git Final Commands
```bash
git add .
git commit -m "Final: Complete Bluestock MF Capstone"
git tag v1.0
git push origin main
git push origin v1.0
```

## Author
Ganesh Garad  
Bluestock Fintech Mutual Fund Analytics Capstone  
June 2026
