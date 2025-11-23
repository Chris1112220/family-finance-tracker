import csv
from datetime import datetime

# Reading the file and parcing the csv data


def normalize_date(s):
    return datetime.strptime(s.strip(), "%m/%d/%Y").date()


def normalize_amount(s):
    s = s.replace("(", "-").replace(")", "")
    return float(s.replace("$", "").replace(",", "").strip())


def parse_pnc_csv(csv_path):
    rows = []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({
                "date": normalize_date(row["Transaction Date"]),
                "description": row["Transaction Description"].strip(),
                "amount": normalize_amount(row["Amount"]),
                "balance": normalize_amount(row["Balance"]),
                "source": "PNC"
            })
    return rows
