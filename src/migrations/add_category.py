import sqlite3

conn = sqlite3.connect("database/finance.db")
cur = conn.cursor()

cur.execute("""
ALTER TABLE transactions
ADD COLUMN category TEXT;
""")

cur.execute("""
ALTER TABLE transactions
ADD COLUMN source TEXT;
""")

conn.commit()
conn.close()

print("Migration completed: added category & source columns.")
