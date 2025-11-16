import csv
import sqlite3
from datetime import datetime

DB_PATH = "database/finance.db"


def normalize_date(date_str):
    date_str = date_str.strip()

    # YYYY-MM-DD (what is actually in your CSV)
    if "-" in date_str and len(date_str.split("-")[0]) == 4:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")

    # MM/DD/YYYY (Excel display)
    if "/" in date_str:
        return datetime.strptime(date_str, "%m/%d/%Y").strftime("%Y-%m-%d")

    raise ValueError(f"Unrecognized date: {date_str}")


def normalize_amount(amount_str):
    s = amount_str.strip()

    # Remove $, commas, parentheses
    s = s.replace("$", "")
    s = s.replace(",", "")
    s = s.replace("(", "-")
    s = s.replace(")", "")

    # Remove spaces (fix for "- 277.52")
    s = s.replace(" ", "")

    return float(s)


def import_pnc_csv(csv_path):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print(f"Importing: {csv_path}")

    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        count = 0

        for row in reader:
            date_raw = row["Transaction Date"]
            desc_raw = row["Transaction Description"]
            amount_raw = row["Amount"]
            balance_raw = row["Balance"]

            date = normalize_date(date_raw)
            description = desc_raw.strip()
            amount = normalize_amount(amount_raw)

            # Balance may be blank for some transactions
            try:
                balance = normalize_amount(balance_raw)
            except:
                balance = None

            cursor.execute("""
                INSERT INTO transactions (date, description, amount, balance, category, source)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (date, description, amount, balance, None, "PNC"))

            count += 1

    conn.commit()
    conn.close()

    print(f"Imported {count} PNC transactions.")
