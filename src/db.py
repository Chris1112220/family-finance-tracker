import sqlite3
from pathlib import Path

# data base path
DB_PATH = Path(__file__).resolve().parent.parent / "database" / "finance.db"


def get_db_connection():
    return sqlite3.connect(DB_PATH)


def run_query(query, params=()):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()
