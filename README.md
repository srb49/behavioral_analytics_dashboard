# Behavioral Analytics Dashboard (SQL + Python + Streamlit)

A full-stack data engineering and analytics application that transforms e-commerce behavioral data into actionable business intelligence. This project demonstrates the ability to manage the entire data lifecycle: from ingestion and relational storage to advanced SQL querying and interactive visualization.

## 🌟 Key Features
* **Dual-Stream Data Pipeline:** Supports both real-world e-commerce datasets and custom-built synthetic data generators (Faker).
* **Relational Storage Layer:** Data is architected in SQLite, utilizing optimized schemas for analytical performance.
* **Advanced Analytics:** Implements Business Logic through SQL CTEs (Common Table Expressions) and complex joins.
* **Interactive UI:** A multi-page Streamlit dashboard featuring real-time filtering, KPI metrics, and dynamic Plotly visualizations.
* **Professional Engineering:** Separation of concerns between SQL logic, Python ETL scripts, and the frontend application.

<<<<<<< HEAD
## 🛠️ Technical Stack
* **Backend/Storage:** Python, SQL (SQLite)
* **Frontend:** Streamlit
* **Data Science:** Pandas, NumPy, Plotly
* **DevOps/Tooling:** Virtual Environments, Faker (Synthetic Data Generation)
=======
### Key Features
* **Automated ETL Pipeline:** Python scripts to clean and ingest CSV data into a structured SQLite database.
* **Relational Storage:** Uses SQL for efficient data querying and filtering.
* **Behavioral Segmentation:** Interactive dashboard to analyze RFM (Recency, Frequency, Monetary) metrics across different user groups.
* **Dynamic Visualizations:** Real-time charting using Plotly and Streamlit.

## Tech Stack
* **Language:** Python 3.9
* **Database:** SQLite (SQLAlchemy/sqlite3)
* **Frontend:** Streamlit
* **Data Analysis:** Pandas, Plotly
* **Simulation:** Faker 
>>>>>>> dcc7d8e1eb0821ac06dd9ed043458f1c2ec2805d

## 📂 Project Structure
```text
behavioral-analytics-dashboard/
<<<<<<< HEAD
├── app/                # Streamlit Dashboard (UI Layer)
├── data/               # SQLite Databases (.db) and Raw CSVs
├── scripts/            # ETL & Data Simulation (Logic Layer)
├── sql/                # DDL Schema and Analytical Queries (Data Layer)
├── requirements.txt    # Dependency Management
└── README.md           # Documentation
=======
├── data/               # SQLite database and raw CSVs
├── scripts/            # ETL and data ingestion scripts
├── sql/                # SQL schema definitions
├── app/                # Streamlit dashboard application
└── requirements.txt    # Project dependencies

data/: analytics.db (Real) and simulated_analytics.db (Fake)

sql/: schema.sql and kpi_queries.sql

scripts/: ingest_data.py and simulate_data.py

app/: main.py (The dashboard)

Root: README.md and requirements.txt
>>>>>>> dcc7d8e1eb0821ac06dd9ed043458f1c2ec2805d
