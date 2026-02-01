import sqlite3

conn = sqlite3.connect('data/analytics.db')
cursor = conn.cursor()

# A simple SQL query to show off those SQL skills
query = """
SELECT segment_label, COUNT(*) as user_count, AVG(monetary) as avg_spend
FROM user_analytics
GROUP BY segment_label
ORDER BY avg_spend DESC;
"""

cursor.execute(query)
for row in cursor.fetchall():
    print(row)

conn.close()