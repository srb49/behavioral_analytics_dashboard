import pandas as pd

# Load a sample to save memory
df = pd.read_csv('data/data1.csv', nrows=1000)

print("--- Dataset Info ---")
print(df.info())
print("\n--- Event Types Found ---")
print(df['event_type'].value_counts())