import pandas as pd
import numpy as np
from faker import Faker
import sqlite3

fake = Faker()

def generate_mock_data(num_users=500):
    data = []
    segments = ['Champions', 'At Risk', 'New Customers', 'Loyalists']
    
    for _ in range(num_users):
        data.append({
            'Customer_ID': fake.uuid4()[:8],
            'Recency': np.random.randint(1, 365),
            'Frequency': np.random.randint(1, 50),
            'Monetary': np.random.randint(10, 2000),
            'Avg_Session_Duration': round(np.random.uniform(1.0, 30.0), 2),
            'Segment_Label': np.random.choice(segments)
        })
    
    df = pd.DataFrame(data)
    
    # Save to a NEW database to avoid messing up your real data
    conn = sqlite3.connect('data/simulated_analytics.db')
    df.to_sql('user_analytics', conn, if_exists='replace', index=False)
    conn.close()
    print(f"Created {num_users} fake users in simulated_analytics.db")

if __name__ == "__main__":
    generate_mock_data()