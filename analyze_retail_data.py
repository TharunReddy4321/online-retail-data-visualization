import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load and analyze the Online Retail dataset
def analyze_retail_data():
    try:
        # Load the Excel file
        df = pd.read_excel('/Users/saitharunreddyrupireddy/Desktop/Cursor Projects/Data Visualization Project/Online Retail.xlsx')
        
        print("=== DATASET OVERVIEW ===")
        print(f"Dataset shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print("\n=== FIRST FEW ROWS ===")
        print(df.head())
        
        print("\n=== DATA TYPES ===")
        print(df.dtypes)
        
        print("\n=== MISSING VALUES ===")
        print(df.isnull().sum())
        
        print("\n=== BASIC STATISTICS ===")
        print(df.describe())
        
        # Check for unique values in key columns
        if 'Country' in df.columns:
            print(f"\n=== UNIQUE COUNTRIES ===")
            print(f"Number of unique countries: {df['Country'].nunique()}")
            print("Top 10 countries by transaction count:")
            print(df['Country'].value_counts().head(10))
        
        # Check date range if InvoiceDate exists
        if 'InvoiceDate' in df.columns:
            print(f"\n=== DATE RANGE ===")
            df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
            print(f"Date range: {df['InvoiceDate'].min()} to {df['InvoiceDate'].max()}")
        
        # Revenue analysis if Quantity and UnitPrice exist
        if 'Quantity' in df.columns and 'UnitPrice' in df.columns:
            df['Revenue'] = df['Quantity'] * df['UnitPrice']
            print(f"\n=== REVENUE ANALYSIS ===")
            print(f"Total Revenue: £{df['Revenue'].sum():,.2f}")
            print(f"Average Order Value: £{df['Revenue'].mean():.2f}")
        
        # Customer analysis if CustomerID exists
        if 'CustomerID' in df.columns:
            print(f"\n=== CUSTOMER ANALYSIS ===")
            print(f"Total unique customers: {df['CustomerID'].nunique()}")
            customer_revenue = df.groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False)
            print(f"Top customer revenue: £{customer_revenue.iloc[0]:,.2f}")
        
        return df
        
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

if __name__ == "__main__":
    df = analyze_retail_data()


