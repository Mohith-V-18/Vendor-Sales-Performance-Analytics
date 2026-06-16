# Vendor Sales Performance Analytics

An end-to-end data analytics project on **2.6+ million retail transactions** covering data engineering, SQL modeling, exploratory data analysis, statistical testing, and interactive business intelligence reporting using **Python, PostgreSQL, and Power BI**.

---

## Project Overview

This project analyzes vendor purchases, sales, inventory, and freight data to uncover insights into:

* Vendor performance and procurement concentration
* Product profitability and margin optimization
* Inventory turnover and unsold stock risks
* Bulk purchasing impact on unit costs
* Statistical differences between high- and low-performing vendors
* Promotional opportunities for high-margin products

---

## Dataset

| Attribute       | Details                                                        |
| --------------- | -------------------------------------------------------------- |
| Total Records   | 2.6+ Million                                                   |
| Source Files    | 5 Raw CSV Files                                                |
| Vendors         | 119                                                            |
| Derived Dataset | `vendor_sales_summary`                                         |
| Engineered KPIs | GrossProfit, ProfitMargin, StockTurnOver, SalesToPurchaseRatio |

### Source Tables

| Table                |      Rows |
| -------------------- | --------: |
| purchases.csv        | 2,372,474 |
| purchase_prices.csv  |    12,261 |
| vendor_invoice.csv   |     5,543 |
| end_inventory.csv    |   224,489 |
| begin_inventory.csv  |     224K+ |
| vendor_sales_summary |   Derived |

---

## Tech Stack

| Tool                         | Purpose                             |
| ---------------------------- | ----------------------------------- |
| Python (Pandas, NumPy)       | Data Cleaning & Feature Engineering |
| PostgreSQL                   | Data Storage & SQL Analysis         |
| SQL (CTEs, Window Functions) | Data Modeling                       |
| Matplotlib & Seaborn         | Data Visualization                  |
| SciPy                        | Statistical Analysis                |
| SQLAlchemy / psycopg2        | Python → PostgreSQL Integration     |
| Power BI                     | Interactive Dashboard               |
| Jupyter Notebook             | EDA & Analysis                      |

---

## Repository Structure

```text
vendor-sales-performance-analytics/

├── notebooks/
│   ├── exploratory_data_analysis.ipynb
│   └── vendor_analysis.ipynb

├── scripts/
│   ├── ingestion_db.py
│   └── get_vendor_summary.py

├── sql/
│   └── vendor_summary_queries.sql

├── dashboard/
│   └── vendor_sales_dashboard.pbix

├── reports/
│   └── Vendor_Sales_Analytics_Report.pdf

└── README.md
```

---

## Data Engineering Pipeline

### ETL Workflow

```text
Raw CSV Files
      ↓
PostgreSQL Data Ingestion
      ↓
SQL CTE-Based Vendor Aggregation
      ↓
Feature Engineering
      ↓
Exploratory Data Analysis
      ↓
Statistical Analysis
      ↓
Power BI Dashboard
```

### Engineered KPIs

* Gross Profit
* Profit Margin %
* Stock Turnover
* Sales-to-Purchase Ratio

---

## Exploratory Data Analysis

### Data Quality Checks

* Missing value treatment
* Outlier detection using box plots
* Distribution analysis using histograms & KDE plots
* Correlation analysis using Pearson correlation matrix

### Key Findings

* Purchase and sales quantities show a correlation of **0.999**
* Purchase price has minimal impact on revenue generation
* Faster inventory turnover does not necessarily increase profitability
* Freight costs vary significantly across vendors

---

## Business Analysis

### Vendor Concentration Analysis

| Metric                     | Result |
| -------------------------- | -----: |
| Total Vendors              |    119 |
| Top 10 Vendor Contribution | 65.69% |
| Largest Vendor Share       | 16.30% |

**Insight:** Procurement spending is heavily concentrated among a small group of vendors, creating supply-chain dependency risk.

---

### High-Margin Product Opportunities

**Criteria**

* Bottom 15% in Sales
* Top 15% in Profit Margin

**Results**

* 198 products identified
* Profit margins ranging from 65% to 90%

**Insight:** These products offer significant growth opportunities through targeted promotions and better shelf placement.

---

### Bulk Purchasing Impact

| Order Size | Avg Unit Cost |
| ---------- | ------------: |
| Small      |        $39.07 |
| Medium     |        $15.49 |
| Large      |        $10.78 |

**Finding:** Large-volume purchases reduce unit costs by approximately **72%**.

---

### Unsold Inventory Analysis

| Metric                  |                Value |
| ----------------------- | -------------------: |
| Total Unsold Inventory  |               $2.71M |
| Highest Vendor Exposure | DIAGEO NORTH AMERICA |
| Unsold Inventory Value  |                $722K |

**Insight:** Inventory risk is concentrated among a few major vendors and requires proactive stock management.

---

## Statistical Analysis

### Confidence Intervals

| Segment                | Mean Margin |
| ---------------------- | ----------: |
| Top Performing Vendors |      ~31.2% |
| Low Performing Vendors |      ~41.6% |

### Welch's T-Test

| Metric      |   Value |
| ----------- | ------: |
| T-Statistic |  -17.67 |
| P-Value     | < 0.001 |

**Conclusion:** The difference in profit margins between high- and low-performing vendors is statistically significant.

---

## Power BI Dashboard

### Dashboard Features

* Vendor Performance Overview
* Revenue & Profitability Analysis
* Procurement Concentration Monitoring
* Inventory Risk Tracking
* Product Performance Insights

### KPIs

* Total Purchase Dollars
* Total Sales Dollars
* Gross Profit
* Profit Margin
* Inventory Turnover
* Vendor Contribution %

---

## Key Insights

* Top 10 vendors account for **65.69%** of total procurement spend.
* 198 products generate high margins despite low sales volumes.
* Large purchase orders reduce unit costs by **72%**.
* **$2.71M** worth of inventory remains unsold.
* Low-performing vendors achieve significantly higher profit margins than top-selling vendors.

---

## Business Recommendations

| Priority  | Recommendation                                               |
| --------- | ------------------------------------------------------------ |
| 🔴 High   | Reduce procurement concentration by diversifying vendor base |
| 🔴 High   | Promote high-margin, low-sales products                      |
| 🔴 High   | Address $2.71M unsold inventory through clearance strategies |
| 🟡 Medium | Encourage bulk purchasing to improve cost efficiency         |
| 🟡 Medium | Reassess pricing strategies for top-performing vendors       |
| 🟢 Low    | Implement vendor-specific inventory forecasting              |

---

## How to Run

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/vendor-sales-performance-analytics.git

cd vendor-sales-performance-analytics
```

### 2. Install Dependencies

```bash
pip install pandas numpy sqlalchemy psycopg2-binary matplotlib seaborn scipy
```

### 3. Run ETL Pipeline

```bash
python scripts/get_vendor_summary.py
```

### 4. Run Analysis Notebooks

```bash
jupyter notebook
```

### 5. Open Dashboard

Open:

```text
dashboard/vendor_sales_dashboard.pbix
```

in Power BI Desktop and refresh the data source.

---

## Project Outcomes

This project demonstrates practical skills across:

* Data Engineering
* SQL Data Modeling
* Exploratory Data Analysis
* Statistical Testing
* Business Intelligence
* Data Visualization
* Business Problem Solving
