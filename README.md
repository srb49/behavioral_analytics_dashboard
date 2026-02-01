# Behavioral Analytics Dashboard (SQL + Python + Streamlit)

A full-stack data engineering and analytics application that transforms e-commerce behavioral data into actionable business intelligence. This project demonstrates the ability to manage the entire data lifecycle: from ingestion and relational storage to advanced SQL querying and interactive visualization.

## 🌟 Key Features
* **Dual-Stream Data Pipeline:** Supports both real-world e-commerce datasets and custom-built synthetic data generators (Faker).
* **Relational Storage Layer:** Data is architected in SQLite, utilizing optimized schemas for analytical performance.
* **Advanced Analytics:** Implements Business Logic through SQL CTEs (Common Table Expressions) and complex joins.
* **Interactive UI:** A multi-page Streamlit dashboard featuring real-time filtering, KPI metrics, and dynamic Plotly visualizations.
* **Professional Engineering:** Separation of concerns between SQL logic, Python ETL scripts, and the frontend application.

## 🛠️ Technical Stack
* **Backend/Storage:** Python, SQL (SQLite)
* **Frontend:** Streamlit
* **Data Science:** Pandas, NumPy, Plotly
* **DevOps/Tooling:** Virtual Environments, Faker (Synthetic Data Generation)

## 📂 Project Structure
```text
behavioral-analytics-dashboard/
├── app/                # Streamlit Dashboard (UI Layer)
├── data/               # SQLite Databases (.db) and Raw CSVs
├── scripts/            # ETL & Data Simulation (Logic Layer)
├── sql/                # DDL Schema and Analytical Queries (Data Layer)
├── requirements.txt    # Dependency Management
└── README.md           # Documentation