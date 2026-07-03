import sqlite3
import os

DB_PATH = os.path.join("data", "school.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables = cursor.fetchall()

print("Tables in Database:\n")

for table in tables:
    print(table[0])

conn.close()