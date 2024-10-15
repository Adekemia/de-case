import pandas as pd

# Function to load and display CSV data
def load_and_display_csv(file_path):
    try:
        # Load the CSV data into a Pandas DataFrame
        data = pd.read_csv(file_path)
        
        # Display the first few rows of the DataFrame
        print("First 5 rows of the CSV file:")
        print(data.head())
        
        # Display general information about the DataFrame
        print("\nDataFrame Info:")
        print(data.info())
        
        # Display basic statistics of numeric columns
        print("\nSummary Statistics:")
        print(data.describe())
    
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
    except pd.errors.ParserError:
        print("Error: The CSV file is malformed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Path to the CSV file (Update with your CSV file path)
file_path = 'sales_data.csv'

# Load and display the CSV
load_and_display_csv(file_path)
