from db import run_query
from pnc_csv import parse_pnc_csv
from pathlib import Path

csv_path = max(Path("data").glob("*.csv"), key=lambda p: p.stat().st_mtime)
print(f"Loading: {csv_path}")

rows = parse_pnc_csv(csv_path)

for r in rows:
    run_query(
        """
        INSERT INTO transactions (date, description, amount, balance, category, source)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        [r["date"], r["description"], r["amount"], r["balance"], None, r["source"]]
    )

print(f"Imported {len(rows)} transactions.")
