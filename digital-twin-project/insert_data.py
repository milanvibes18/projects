import sqlite3
import time
import random

# Connect (creates file if not exists)
conn = sqlite3.connect("health_data.db")
c = conn.cursor()

# Create table if not exists
c.execute("""
CREATE TABLE IF NOT EXISTS health(
    timestamp TEXT,
    heart_rate INTEGER
)
""")

# Insert data continuously
print("🚀 Starting fake heart rate generator... (Press CTRL+C to stop)")

while True:
    fake_bpm = random.randint(40, 130)  # simulate wide HR range
    c.execute("INSERT INTO health VALUES (?, ?)", (time.strftime("%Y-%m-%d %H:%M:%S"), fake_bpm))
    conn.commit()
    print("Inserted:", fake_bpm)
    time.sleep(3)  # new reading every 3 seconds
