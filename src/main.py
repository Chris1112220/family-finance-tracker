import os
from importer.pnc_importer import import_pnc_csv

DATA_DIR = "data"


def get_any_csv():

    for filename in os.listdir(DATA_DIR):
        if filename.lower().endswith(".csv"):
            return os.path.join(DATA_DIR, filename)

    raise FileNotFoundError("No CSV files found in the data/ ")


if __name__ == "__main__":
    csv_path = get_any_csv()
    print(f"Using CSV file: {csv_path}")
    import_pnc_csv(csv_path)
