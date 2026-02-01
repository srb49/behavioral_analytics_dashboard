import pandas as pd
import sqlite3
import os

def load_data():
    # 1. Read the CSV
    csv_path = 'data/data1.csv'
    df = pd.read_csv(csv_path)

    # 2. Connect to (or create) SQLite database
    conn = sqlite3.connect('data/analytics.db')
    
    # 3. Load data into SQL table
    # We use 'replace' so you can run this script multiple times without errors
    df.to_sql('user_analytics', conn, if_exists='replace', index=False)
    
    print(f"Success! Loaded {len(df)} rows into analytics.db")
    conn.close()

if __name__ == "__main__":
    load_data()