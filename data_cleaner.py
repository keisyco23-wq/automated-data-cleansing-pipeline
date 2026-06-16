import pandas as pd
import numpy as np

def clean_operational_data(file_path):
    print("Initializing Automated Cleansing Pipeline...")
    
    # Load raw, corrupted business data
    df = pd.read_csv(file_path)
    
    # 1. Standardize text columns (Remove trailing spaces and fix casing)
    df['Customer_Name'] = df['Customer_Name'].str.strip().str.title()
    df['Country'] = df['Country'].str.strip().str.upper()
    
    # 2. Handle missing structural values safely
    df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')
    df['Revenue'].fillna(df['Revenue'].median(), inplace=True)
    
    # 3. Handle anomalies and negative business values
    df['Quantity'] = df['Quantity'].apply(lambda x: x if x > 0 else 1)
    
    # 4. Standardize corporate date formats
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
    df['Order_Date'].fillna(method='ffill', inplace=True)
    
    print("Data cleansing completed successfully. Exporting normalized dataset...")
    df.to_csv("cleaned_corporate_data.csv", index=False)

# Simulated execution
# clean_operational_data("dirty_raw_data.csv")
