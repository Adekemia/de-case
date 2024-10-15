import duckdb
import pandas as pd

#conn = duckdb.connect('my_database.db')
##conn.execute('SELECT 3').fetchall()


# Load CSV file
data = pd.read_csv('sales_data.csv')
print("Extracted Data:")
print(data.head())

# Connect to DuckDB (creates an in-memory database if no file is provided)
conn = duckdb.connect('sales_warehouse.db')

# Create a table and insert data from Pandas DataFrame
conn.execute("CREATE TABLE sales AS SELECT * FROM sales_data.csv")
print("Data Loaded into DuckDB")


# Verify the data
results = conn.execute("SELECT * FROM sales").fetchdf()
print("Data in DuckDB:")
print(results)

#IDEMPOTENCY
