import sqlite3

conn = sqlite3.connect("database/finance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    description TEXT,
    amount REAL,
    balance REAL,
    category TEXT,
    source TEXT
);
""")

conn.commit()
conn.close()

print("Database initialized with full schema.")
