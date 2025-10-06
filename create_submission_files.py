import pandas as pd
import numpy as np

def prepare_data_for_bi_tools():
    """Prepare cleaned data in formats suitable for Tableau and Power BI"""
    
    # Load cleaned data
    df = pd.read_excel('/Users/saitharunreddyrupireddy/Desktop/Cursor Projects/Data Visualization Project/Online Retail_cleaned.xlsx')
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    print("Preparing data for BI tools...")
    
    # Create Question 1: Monthly Revenue 2011
    df_2011 = df[df['Year'] == 2011].copy()
    monthly_revenue = df_2011.groupby(['Year', 'Month']).agg({
        'Revenue': 'sum',
        'Quantity': 'sum',
        'InvoiceNo': 'nunique'
    }).reset_index()
    
    monthly_revenue['MonthName'] = pd.to_datetime(monthly_revenue[['Year', 'Month']].assign(day=1)).dt.strftime('%B')
    monthly_revenue['MonthYear'] = monthly_revenue['MonthName'] + ' ' + monthly_revenue['Year'].astype(str)
    monthly_revenue['Question'] = 'Q1_Monthly_Revenue_2011'
    
    # Create Question 2: Top 10 Countries (excluding UK)
    df_no_uk = df[df['Country'] != 'United Kingdom'].copy()
    country_metrics = df_no_uk.groupby('Country').agg({
        'Revenue': 'sum',
        'Quantity': 'sum',
        'InvoiceNo': 'nunique',
        'CustomerID': 'nunique'
    }).reset_index()
    
    top_10_countries = country_metrics.nlargest(10, 'Revenue')
    top_10_countries['Question'] = 'Q2_Top_10_Countries'
    top_10_countries['Rank'] = range(1, 11)
    
    # Create Question 3: Top 10 Customers
    customer_revenue = df.groupby('CustomerID').agg({
        'Revenue': 'sum',
        'Quantity': 'sum',
        'InvoiceNo': 'nunique'
    }).reset_index()
    
    top_10_customers = customer_revenue.nlargest(10, 'Revenue')
    top_10_customers['Question'] = 'Q3_Top_10_Customers'
    top_10_customers['Rank'] = range(1, 11)
    
    # Create Question 4: Country Demand Analysis (excluding UK)
    country_demand = df_no_uk.groupby('Country').agg({
        'Revenue': 'sum',
        'Quantity': 'sum',
        'InvoiceNo': 'nunique',
        'CustomerID': 'nunique'
    }).reset_index()
    country_demand['Question'] = 'Q4_Country_Demand_Analysis'
    
    # Save individual datasets for each question
    monthly_revenue.to_excel('Q1_Monthly_Revenue_2011.xlsx', index=False)
    top_10_countries.to_excel('Q2_Top_10_Countries.xlsx', index=False)
    top_10_customers.to_excel('Q3_Top_10_Customers.xlsx', index=False)
    country_demand.to_excel('Q4_Country_Demand_Analysis.xlsx', index=False)
    
    # Create a combined dataset for comprehensive analysis
    combined_data = df.copy()
    combined_data['Question'] = 'Combined_Dataset'
    
    # Save combined dataset
    combined_data.to_excel('Online_Retail_Combined_Dataset.xlsx', index=False)
    
    print("✅ Data files created for BI tools:")
    print("- Q1_Monthly_Revenue_2011.xlsx")
    print("- Q2_Top_10_Countries.xlsx") 
    print("- Q3_Top_10_Customers.xlsx")
    print("- Q4_Country_Demand_Analysis.xlsx")
    print("- Online_Retail_Combined_Dataset.xlsx")
    
    return {
        'monthly_revenue': monthly_revenue,
        'top_countries': top_10_countries,
        'top_customers': top_10_customers,
        'country_demand': country_demand,
        'combined_data': combined_data
    }

if __name__ == "__main__":
    data = prepare_data_for_bi_tools()


