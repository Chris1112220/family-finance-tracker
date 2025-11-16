from importer.pnc_importer import import_pnc_csv

if __name__ == "__main__":
    csv_path = "data/accountActivityExport.csv"
    import_pnc_csv(csv_path)
