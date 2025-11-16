# Family Finance Tracker

This project is a simple Python-based tool for importing, cleaning, and storing bank transactions in a SQLite database. It currently supports importing PNC Bank CSV files and normalizes dates, descriptions, and amounts before saving them to the database.

## Features
- Import PNC transaction CSV files
- Clean and normalize transaction fields
- Store transactions in a SQLite database
- Basic script for viewing recent transactions
- Database migrations for schema updates

## Project Structure
- `src/` – importer, setup scripts, and viewer
- `data/` – CSV files to import
- `database/` – local SQLite database (ignored by Git)
- `migrations/` – database schema updates

## Getting Started
Install dependencies:
pip install -r requirements.txt

Create the database:
python src/setup_database.py

Import transactions:
python src/main.py

View transactions:
python src/view_transactions.py


## Notes
The database file is ignored by Git and must be created locally using the setup script.  
Real financial data should not be committed to this repository.
