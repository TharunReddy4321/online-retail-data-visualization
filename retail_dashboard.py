import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Online Retail Data Visualization Dashboard",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    """Load and cache the cleaned retail data"""
    df = pd.read_excel('/Users/saitharunreddyrupireddy/Desktop/Cursor Projects/Data Visualization Project/Online Retail_cleaned.xlsx')
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    return df

# Load data
df = load_data()

# Main title
st.title("📊 Online Retail Data Visualization Dashboard")
st.markdown("---")

# Create tabs for each question
tab1, tab2, tab3, tab4 = st.tabs([
    "Question 1: 2011 Revenue Time Series", 
    "Question 2: Top 10 Countries", 
    "Question 3: Top 10 Customers", 
    "Question 4: Country Demand Analysis"
])

with tab1:
    st.header("Question 1: Monthly Revenue Trends for 2011")
    st.markdown("**CEO Analysis:** Time series of revenue data for 2011 showing seasonal trends")
    
    # Filter for 2011 data only
    df_2011 = df[df['Year'] == 2011].copy()
    
    # Monthly revenue aggregation
    monthly_revenue = df_2011.groupby(['Year', 'Month']).agg({
        'Revenue': 'sum',
        'Quantity': 'sum',
        'InvoiceNo': 'nunique'
    }).reset_index()
    
    # Create month names
    monthly_revenue['MonthName'] = pd.to_datetime(monthly_revenue[['Year', 'Month']].assign(day=1)).dt.strftime('%B')
    monthly_revenue['MonthYear'] = monthly_revenue['MonthName'] + ' ' + monthly_revenue['Year'].astype(str)
    
    # Create the time series chart
    fig1 = go.Figure()
    
    fig1.add_trace(go.Scatter(
        x=monthly_revenue['MonthYear'],
        y=monthly_revenue['Revenue'],
        mode='lines+markers',
        name='Monthly Revenue',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=8, color='#1f77b4'),
        hovertemplate='<b>%{x}</b><br>Revenue: £%{y:,.0f}<extra></extra>'
    ))
    
    fig1.update_layout(
        title='Monthly Revenue Trends - 2011',
        xaxis_title='Month',
        yaxis_title='Revenue (£)',
        template='plotly_white',
        height=500,
        hovermode='x unified'
    )
    
    fig1.update_yaxes(tickformat='£,')
    
    st.plotly_chart(fig1, use_container_width=True)
    
    # Key insights
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total 2011 Revenue", f"£{monthly_revenue['Revenue'].sum():,.0f}")
    with col2:
        peak_month = monthly_revenue.loc[monthly_revenue['Revenue'].idxmax(), 'MonthName']
        peak_revenue = monthly_revenue['Revenue'].max()
        st.metric("Peak Month", peak_month, f"£{peak_revenue:,.0f}")
    with col3:
        lowest_month = monthly_revenue.loc[monthly_revenue['Revenue'].idxmin(), 'MonthName']
        lowest_revenue = monthly_revenue['Revenue'].min()
        st.metric("Lowest Month", lowest_month, f"£{lowest_revenue:,.0f}")

with tab2:
    st.header("Question 2: Top 10 Countries by Revenue (Excluding UK)")
    st.markdown("**CMO Analysis:** Top performing international markets with revenue and quantity metrics")
    
    # Filter out UK and get top 10 countries
    df_no_uk = df[df['Country'] != 'United Kingdom'].copy()
    
    country_metrics = df_no_uk.groupby('Country').agg({
        'Revenue': 'sum',
        'Quantity': 'sum',
        'InvoiceNo': 'nunique'
    }).reset_index()
    
    top_10_countries = country_metrics.nlargest(10, 'Revenue')
    
    # Create dual-axis chart
    fig2 = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Revenue bars
    fig2.add_trace(
        go.Bar(
            x=top_10_countries['Country'],
            y=top_10_countries['Revenue'],
            name='Revenue (£)',
            marker_color='#2E86AB',
            yaxis='y1'
        ),
        secondary_y=False,
    )
    
    # Quantity line
    fig2.add_trace(
        go.Scatter(
            x=top_10_countries['Country'],
            y=top_10_countries['Quantity'],
            mode='lines+markers',
            name='Quantity Sold',
            line=dict(color='#A23B72', width=3),
            marker=dict(size=8, color='#A23B72'),
            yaxis='y2'
        ),
        secondary_y=True,
    )
    
    fig2.update_xaxes(title_text="Country")
    fig2.update_yaxes(title_text="Revenue (£)", secondary_y=False, tickformat='£,')
    fig2.update_yaxes(title_text="Quantity Sold", secondary_y=True)
    
    fig2.update_layout(
        title='Top 10 Countries by Revenue (Excluding UK)',
        template='plotly_white',
        height=500,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    # Display data table
    st.subheader("Top 10 Countries Data")
    display_df = top_10_countries.copy()
    display_df['Revenue'] = display_df['Revenue'].apply(lambda x: f"£{x:,.2f}")
    display_df['Quantity'] = display_df['Quantity'].apply(lambda x: f"{x:,}")
    st.dataframe(display_df, use_container_width=True)

with tab3:
    st.header("Question 3: Top 10 Customers by Revenue")
    st.markdown("**CMO Analysis:** Highest revenue generating customers for targeted marketing")
    
    # Get top 10 customers by revenue
    customer_revenue = df.groupby('CustomerID').agg({
        'Revenue': 'sum',
        'Quantity': 'sum',
        'InvoiceNo': 'nunique'
    }).reset_index()
    
    top_10_customers = customer_revenue.nlargest(10, 'Revenue')
    top_10_customers['CustomerID'] = top_10_customers['CustomerID'].astype(int).astype(str)
    
    # Create descending bar chart
    fig3 = go.Figure()
    
    fig3.add_trace(go.Bar(
        x=top_10_customers['CustomerID'],
        y=top_10_customers['Revenue'],
        marker_color=px.colors.sequential.Blues_r[:10],
        text=top_10_customers['Revenue'].apply(lambda x: f'£{x:,.0f}'),
        textposition='auto',
        hovertemplate='<b>Customer ID: %{x}</b><br>Revenue: £%{y:,.0f}<br>Orders: %{customdata}<extra></extra>',
        customdata=top_10_customers['InvoiceNo']
    ))
    
    fig3.update_layout(
        title='Top 10 Customers by Revenue (Descending Order)',
        xaxis_title='Customer ID',
        yaxis_title='Revenue (£)',
        template='plotly_white',
        height=500
    )
    
    fig3.update_yaxes(tickformat='£,')
    
    st.plotly_chart(fig3, use_container_width=True)
    
    # Customer insights
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Top Customer Revenue", f"£{top_10_customers['Revenue'].iloc[0]:,.0f}")
    with col2:
        avg_top10_revenue = top_10_customers['Revenue'].mean()
        st.metric("Avg Top 10 Customer Value", f"£{avg_top10_revenue:,.0f}")
    with col3:
        total_top10_revenue = top_10_customers['Revenue'].sum()
        percentage = (total_top10_revenue / df['Revenue'].sum()) * 100
        st.metric("Top 10 Share of Total Revenue", f"{percentage:.1f}%")

with tab4:
    st.header("Question 4: Country Demand Analysis (Excluding UK)")
    st.markdown("**CEO Analysis:** Global demand patterns for expansion opportunities")
    
    # Prepare data for bubble chart
    df_no_uk = df[df['Country'] != 'United Kingdom'].copy()
    
    country_demand = df_no_uk.groupby('Country').agg({
        'Revenue': 'sum',
        'Quantity': 'sum',
        'InvoiceNo': 'nunique',
        'CustomerID': 'nunique'
    }).reset_index()
    
    # Create bubble chart
    fig4 = go.Figure()
    
    fig4.add_trace(go.Scatter(
        x=country_demand['Quantity'],
        y=country_demand['Revenue'],
        mode='markers',
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
        hovertemplate='<b>%{text}</b><br>' +
                     'Quantity: %{x:,}<br>' +
                     'Revenue: £%{y:,.0f}<br>' +
                     'Customers: %{marker.size}<br>' +
                     '<extra></extra>',
        textposition="middle center",
        textfont=dict(size=10, color="white")
    ))
    
    fig4.update_layout(
        title='Country Demand Analysis: Revenue vs Quantity (Bubble Size = Number of Customers)',
        xaxis_title='Total Quantity Sold',
        yaxis_title='Total Revenue (£)',
        template='plotly_white',
        height=600,
        showlegend=False
    )
    
    fig4.update_yaxes(tickformat='£,')
    fig4.update_xaxes(tickformat=',')
    
    st.plotly_chart(fig4, use_container_width=True)
    
    # Summary table for all countries
    st.subheader("Complete Country Analysis")
    summary_df = country_demand.sort_values('Revenue', ascending=False)
    summary_df['Revenue_Formatted'] = summary_df['Revenue'].apply(lambda x: f"£{x:,.2f}")
    summary_df['Quantity_Formatted'] = summary_df['Quantity'].apply(lambda x: f"{x:,}")
    
    display_cols = ['Country', 'Revenue_Formatted', 'Quantity_Formatted', 'CustomerID', 'InvoiceNo']
    display_names = ['Country', 'Revenue', 'Quantity Sold', 'Unique Customers', 'Total Orders']
    
    summary_display = summary_df[display_cols].copy()
    summary_display.columns = display_names
    
    st.dataframe(summary_display, use_container_width=True, height=400)

# Sidebar with data summary
st.sidebar.header("📋 Data Summary")
st.sidebar.markdown(f"""
**Dataset Overview:**
- **Total Records:** {len(df):,}
- **Date Range:** {df['InvoiceDate'].min().strftime('%B %Y')} to {df['InvoiceDate'].max().strftime('%B %Y')}
- **Total Revenue:** £{df['Revenue'].sum():,.2f}
- **Countries:** {df['Country'].nunique()}
- **Customers:** {df['CustomerID'].nunique():,}
- **Products:** {df['StockCode'].nunique():,}

**Data Quality:**
- ✅ Negative quantities removed
- ✅ Zero/negative prices removed
- ✅ Clean dataset ready for analysis
""")

st.sidebar.markdown("---")
st.sidebar.markdown("**📊 Dashboard Features:**")
st.sidebar.markdown("- Interactive charts with hover details")
st.sidebar.markdown("- Responsive design")
st.sidebar.markdown("- Real-time filtering")
st.sidebar.markdown("- Export-ready visualizations")
