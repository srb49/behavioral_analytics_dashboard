# Behavioral Analytics Dashboard (SQL + Python + Streamlit)

A full-stack data engineering project demonstrating how to transform raw business metrics into an interactive decision-making tool.

## Overview
This project processes e-commerce user behavior data to provide actionable insights into customer segmentation. It demonstrates a clean separation of concerns between the data storage layer (SQL), processing logic (Python), and the presentation layer (Streamlit).

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

## Project Structure
```text
behavioral-analytics-dashboard/
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
