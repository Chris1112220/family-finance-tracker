import sqlite3
from tabulate import tabulate

DB_PATH = "database/finance.db"


def view_transactions(limit=20):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT date, description, amount, balance, category, source
        FROM transactions
        ORDER BY date DESC
        LIMIT ?;
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    print(tabulate(
        rows,
        headers=["Date", "Description", "Amount",
                 "Balance", "Category", "Source"],
        tablefmt="pretty"
    ))


if __name__ == "__main__":
    view_transactions(50)
