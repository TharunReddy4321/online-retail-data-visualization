import pandas as pd
import numpy as np
from datetime import datetime

def generate_business_insights():
    """Generate key business insights for CEO and CMO questions"""
    
    # Load the data
    df = pd.read_excel('/Users/saitharunreddyrupireddy/Desktop/Cursor Projects/Data Visualization Project/Online Retail.xlsx')
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    
    print("=== KEY BUSINESS INSIGHTS FOR EXECUTIVE QUESTIONS ===\n")
    
    # 1. Revenue and Growth Analysis
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly_revenue = df.groupby('Month')['Revenue'].sum()
    print("1. REVENUE TRENDS:")
    print(f"   - Total Revenue: £{df['Revenue'].sum():,.2f}")
    print(f"   - Peak Month: {monthly_revenue.idxmax()} (£{monthly_revenue.max():,.2f})")
    print(f"   - Lowest Month: {monthly_revenue.idxmin()} (£{monthly_revenue.min():,.2f})")
    print(f"   - Month-over-Month Growth: {((monthly_revenue.iloc[-1] / monthly_revenue.iloc[0]) - 1) * 100:.1f}%")
    
    # 2. Customer Analysis
    customer_metrics = df.groupby('CustomerID').agg({
        'Revenue': 'sum',
        'InvoiceNo': 'nunique',
        'InvoiceDate': ['min', 'max']
    }).round(2)
    
    print(f"\n2. CUSTOMER INSIGHTS:")
    print(f"   - Total Customers: {df['CustomerID'].nunique():,}")
    print(f"   - Customer Lifetime Value (avg): £{customer_metrics['Revenue']['sum'].mean():.2f}")
    print(f"   - Top 10% customers contribute: {(customer_metrics['Revenue']['sum'].nlargest(int(len(customer_metrics) * 0.1)).sum() / df['Revenue'].sum() * 100):.1f}% of revenue")
    print(f"   - Average orders per customer: {customer_metrics['InvoiceNo']['nunique'].mean():.1f}")
    
    # 3. Geographic Analysis
    country_revenue = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)
    print(f"\n3. GEOGRAPHIC PERFORMANCE:")
    print(f"   - UK dominates with {(country_revenue['United Kingdom'] / country_revenue.sum() * 100):.1f}% of revenue")
    print(f"   - Top 5 International Markets:")
    for country in country_revenue.drop('United Kingdom').head(5).index:
        print(f"     • {country}: £{country_revenue[country]:,.2f}")
    
    # 4. Product Analysis
    product_performance = df.groupby('StockCode').agg({
        'Revenue': 'sum',
        'Quantity': 'sum',
        'Description': 'first'
    }).sort_values('Revenue', ascending=False)
    
    print(f"\n4. PRODUCT INSIGHTS:")
    print(f"   - Total SKUs: {df['StockCode'].nunique():,}")
    print(f"   - Top product revenue: £{product_performance['Revenue'].iloc[0]:,.2f}")
    print(f"   - Average revenue per SKU: £{product_performance['Revenue'].mean():.2f}")
    
    # 5. Seasonal Patterns
    df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()
    df['Hour'] = df['InvoiceDate'].dt.hour
    daily_revenue = df.groupby('DayOfWeek')['Revenue'].sum()
    hourly_revenue = df.groupby('Hour')['Revenue'].sum()
    
    print(f"\n5. OPERATIONAL PATTERNS:")
    print(f"   - Best day: {daily_revenue.idxmax()} (£{daily_revenue.max():,.2f})")
    print(f"   - Peak hour: {hourly_revenue.idxmax()}:00 (£{hourly_revenue.max():,.2f})")
    
    # 6. Return/Cancellation Analysis
    returns = df[df['Quantity'] < 0]
    print(f"\n6. RETURNS & CANCELLATIONS:")
    print(f"   - Return rate: {len(returns) / len(df) * 100:.2f}% of transactions")
    print(f"   - Revenue impact of returns: £{abs(returns['Revenue'].sum()):,.2f}")
    
    return df

if __name__ == "__main__":
    df = generate_business_insights()


