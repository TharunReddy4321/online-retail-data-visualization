import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

def export_static_charts():
    """Create and export static versions of all charts"""
    
    # Load cleaned data
    df = pd.read_excel('/Users/saitharunreddyrupireddy/Desktop/Cursor Projects/Data Visualization Project/Online Retail_cleaned.xlsx')
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    print("Exporting static charts...")
    
    # Question 1: Monthly Revenue Time Series 2011
    df_2011 = df[df['Year'] == 2011].copy()
    monthly_revenue = df_2011.groupby(['Year', 'Month']).agg({
        'Revenue': 'sum',
        'Quantity': 'sum',
        'InvoiceNo': 'nunique'
    }).reset_index()
    
    monthly_revenue['MonthName'] = pd.to_datetime(monthly_revenue[['Year', 'Month']].assign(day=1)).dt.strftime('%B')
    monthly_revenue['MonthYear'] = monthly_revenue['MonthName'] + ' ' + monthly_revenue['Year'].astype(str)
    
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=monthly_revenue['MonthYear'],
        y=monthly_revenue['Revenue'],
        mode='lines+markers',
        name='Monthly Revenue',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=8, color='#1f77b4')
    ))
    
    fig1.update_layout(
        title='Question 1: Monthly Revenue Trends - 2011',
        xaxis_title='Month',
        yaxis_title='Revenue (£)',
        template='plotly_white',
        height=500,
        width=1000
    )
    fig1.update_yaxes(tickformat='£,')
    fig1.write_image("Question_1_Monthly_Revenue_2011.png", width=1000, height=500)
    print("✅ Question 1 chart exported")
    
    # Question 2: Top 10 Countries (excluding UK)
    df_no_uk = df[df['Country'] != 'United Kingdom'].copy()
    country_metrics = df_no_uk.groupby('Country').agg({
        'Revenue': 'sum',
        'Quantity': 'sum',
        'InvoiceNo': 'nunique'
    }).reset_index()
    
    top_10_countries = country_metrics.nlargest(10, 'Revenue')
    
    fig2 = make_subplots(specs=[[{"secondary_y": True}]])
    fig2.add_trace(
        go.Bar(x=top_10_countries['Country'], y=top_10_countries['Revenue'], 
               name='Revenue (£)', marker_color='#2E86AB'),
        secondary_y=False,
    )
    fig2.add_trace(
        go.Scatter(x=top_10_countries['Country'], y=top_10_countries['Quantity'],
                   mode='lines+markers', name='Quantity Sold',
                   line=dict(color='#A23B72', width=3), marker=dict(size=8, color='#A23B72')),
        secondary_y=True,
    )
    
    fig2.update_xaxes(title_text="Country")
    fig2.update_yaxes(title_text="Revenue (£)", secondary_y=False, tickformat='£,')
    fig2.update_yaxes(title_text="Quantity Sold", secondary_y=True)
    fig2.update_layout(
        title='Question 2: Top 10 Countries by Revenue (Excluding UK)',
        template='plotly_white',
        height=500,
        width=1000
    )
    fig2.write_image("Question_2_Top_10_Countries.png", width=1000, height=500)
    print("✅ Question 2 chart exported")
    
    # Question 3: Top 10 Customers
    customer_revenue = df.groupby('CustomerID').agg({
        'Revenue': 'sum',
        'Quantity': 'sum',
        'InvoiceNo': 'nunique'
    }).reset_index()
    
    top_10_customers = customer_revenue.nlargest(10, 'Revenue')
    top_10_customers['CustomerID'] = top_10_customers['CustomerID'].astype(int).astype(str)
    
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(
        x=top_10_customers['CustomerID'],
        y=top_10_customers['Revenue'],
        marker_color=px.colors.sequential.Blues_r[:10],
        text=top_10_customers['Revenue'].apply(lambda x: f'£{x:,.0f}'),
        textposition='auto'
    ))
    
    fig3.update_layout(
        title='Question 3: Top 10 Customers by Revenue (Descending Order)',
        xaxis_title='Customer ID',
        yaxis_title='Revenue (£)',
        template='plotly_white',
        height=500,
        width=1000
    )
    fig3.update_yaxes(tickformat='£,')
    fig3.write_image("Question_3_Top_10_Customers.png", width=1000, height=500)
    print("✅ Question 3 chart exported")
    
    # Question 4: Country Demand Analysis
    country_demand = df_no_uk.groupby('Country').agg({
        'Revenue': 'sum',
        'Quantity': 'sum',
        'InvoiceNo': 'nunique',
        'CustomerID': 'nunique'
    }).reset_index()
    
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(
        x=country_demand['Quantity'],
        y=country_demand['Revenue'],
        mode='markers+text',
        marker=dict(
            size=country_demand['CustomerID'],
            sizemode='diameter',
            sizeref=2. * max(country_demand['CustomerID']) / (40.**2),
            sizemin=4,
            color=country_demand['Revenue'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Revenue (£)")
        ),
        text=country_demand['Country'],
        textposition="middle center",
        textfont=dict(size=8, color="white")
    ))
    
    fig4.update_layout(
        title='Question 4: Country Demand Analysis (Bubble Size = Customers)',
        xaxis_title='Total Quantity Sold',
        yaxis_title='Total Revenue (£)',
        template='plotly_white',
        height=600,
        width=1000
    )
    fig4.update_yaxes(tickformat='£,')
    fig4.update_xaxes(tickformat=',')
    fig4.write_image("Question_4_Country_Demand_Analysis.png", width=1000, height=600)
    print("✅ Question 4 chart exported")
    
    print("\n🎉 All charts exported successfully!")
    print("Files created:")
    print("- Question_1_Monthly_Revenue_2011.png")
    print("- Question_2_Top_10_Countries.png") 
    print("- Question_3_Top_10_Customers.png")
    print("- Question_4_Country_Demand_Analysis.png")

if __name__ == "__main__":
    export_static_charts()
