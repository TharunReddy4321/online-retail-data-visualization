import pandas as pd
import numpy as np

def clean_retail_data(file_path):
    """
    Clean the retail data by removing:
    1. Negative quantities (returns)
    2. Zero or negative unit prices (data entry errors)
    """
    
    # Load the data
    print("Loading data...")
    df = pd.read_excel(file_path)
    
    print(f"Original dataset shape: {df.shape}")
    print(f"Original revenue: £{(df['Quantity'] * df['UnitPrice']).sum():,.2f}")
    
    # Check for issues
    negative_qty = df[df['Quantity'] < 1]
    negative_price = df[df['UnitPrice'] <= 0]
    
    print(f"\nData quality issues found:")
    print(f"- Records with quantity < 1: {len(negative_qty):,} ({len(negative_qty)/len(df)*100:.2f}%)")
    print(f"- Records with unit price ≤ £0: {len(negative_price):,} ({len(negative_price)/len(df)*100:.2f}%)")
    
    # Apply cleaning conditions
    print("\nApplying data cleaning rules...")
    print("Rule 1: Quantity must be ≥ 1 unit")
    print("Rule 2: Unit price must be > £0")
    
    # Clean the data
    df_clean = df[(df['Quantity'] >= 1) & (df['UnitPrice'] > 0)].copy()
    
    # Add calculated fields
    df_clean['Revenue'] = df_clean['Quantity'] * df_clean['UnitPrice']
    df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])
    df_clean['Year'] = df_clean['InvoiceDate'].dt.year
    df_clean['Month'] = df_clean['InvoiceDate'].dt.month
    df_clean['MonthName'] = df_clean['InvoiceDate'].dt.strftime('%B')
    df_clean['YearMonth'] = df_clean['InvoiceDate'].dt.to_period('M')
    
    print(f"\nCleaned dataset shape: {df_clean.shape}")
    print(f"Cleaned revenue: £{df_clean['Revenue'].sum():,.2f}")
    print(f"Records removed: {len(df) - len(df_clean):,} ({(len(df) - len(df_clean))/len(df)*100:.2f}%)")
    
    # Save cleaned data
    output_path = file_path.replace('.xlsx', '_cleaned.xlsx')
    df_clean.to_excel(output_path, index=False)
    print(f"\nCleaned data saved to: {output_path}")
    
    return df_clean

if __name__ == "__main__":
    file_path = "/Users/saitharunreddyrupireddy/Desktop/Cursor Projects/Data Visualization Project/Online Retail.xlsx"
    cleaned_data = clean_retail_data(file_path)


