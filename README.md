# 📊 Online Retail Data Visualization Project

A comprehensive data analysis and visualization project for online retail business intelligence, featuring interactive dashboards, executive reporting, and strategic insights for CEO and CMO stakeholders.

## 🎯 **Project Overview**

This project analyzes online retail transaction data (2010-2011) to provide strategic business insights through data visualization and interactive dashboards. The analysis addresses four critical business questions and delivers actionable recommendations for executive decision-making.

### **Key Features**
- ✅ **Data Quality Assurance** - Comprehensive data cleaning and validation
- ✅ **Interactive Dashboard** - Streamlit web application with real-time insights
- ✅ **Executive Reporting** - Professional business intelligence reports
- ✅ **Static Visualizations** - Presentation-ready charts and graphs
- ✅ **Strategic Analysis** - CEO and CMO focused business insights

## 📊 **Business Questions Addressed**

### **Question 1: Revenue Trends Analysis**
- **Target**: CEO strategic planning and forecasting
- **Focus**: Monthly revenue patterns and seasonal trends for 2011
- **Insight**: 42% revenue decline from November to December 2011

### **Question 2: International Market Performance**
- **Target**: CMO market strategy and expansion
- **Focus**: Top 10 countries by revenue (excluding UK)
- **Insight**: £1.7M potential from international markets

### **Question 3: Customer Concentration Analysis**
- **Target**: CMO customer retention and risk mitigation
- **Focus**: Top 10 customers by revenue and concentration risk
- **Insight**: Top 10% customers drive 51% of revenue

### **Question 4: Global Expansion Strategy**
- **Target**: CEO strategic planning and market prioritization
- **Focus**: Country demand analysis for expansion opportunities
- **Insight**: 38 countries with varying demand patterns

## 🛠️ **Tech Stack**

### **Core Technologies**
- **Python 3.13** - Primary programming language
- **Pandas 2.3.2** - Data manipulation and analysis
- **Streamlit 1.50.0** - Interactive web dashboard
- **Plotly 6.3.0** - Interactive visualizations
- **Matplotlib 3.10.6** - Static chart generation

### **Data Processing**
- **NumPy 2.3.3** - Numerical computing
- **OpenPyXL 3.1.5** - Excel file handling
- **Seaborn 0.13.2** - Statistical visualization

### **Export & Deployment**
- **Kaleido 1.1.0** - Static image export
- **Pillow 11.3.0** - Image processing
- **Virtual Environment** - Isolated dependencies

## 🚀 **Quick Start**

### **Prerequisites**
- Python 3.13 or higher
- Git
- Web browser

### **Installation**

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/online-retail-data-visualization.git
cd online-retail-data-visualization
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run data cleanup (if needed)**
```bash
python data_cleanup.py
```

5. **Launch interactive dashboard**
```bash
streamlit run retail_dashboard.py
```

6. **Access dashboard**
- Open browser to: `http://localhost:8501`
- Navigate between tabs for each business question

## 📁 **Project Structure**

```
online-retail-data-visualization/
├── 📊 Data Files
│   ├── Online Retail.xlsx                    # Original dataset
│   ├── Online Retail_cleaned.xlsx           # Cleaned dataset
│   ├── Q1_Monthly_Revenue_2011.xlsx         # Question 1 data
│   ├── Q2_Top_10_Countries.xlsx             # Question 2 data
│   ├── Q3_Top_10_Customers.xlsx              # Question 3 data
│   └── Q4_Country_Demand_Analysis.xlsx       # Question 4 data
│
├── 🐍 Python Scripts
│   ├── data_cleanup.py                       # Data cleaning process
│   ├── analyze_retail_data.py               # Initial data analysis
│   ├── business_insights.py                 # Business insights generation
│   ├── retail_dashboard.py                  # Streamlit dashboard
│   ├── export_charts.py                     # Static chart generation
│   └── create_submission_files.py           # BI tool data preparation
│
├── 📈 Visualizations
│   ├── Question_1_Monthly_Revenue_2011.png  # Revenue trends chart
│   ├── Question_2_Top_10_Countries.png      # International markets
│   ├── Question_3_Top_10_Customers.png       # Customer analysis
│   └── Question_4_Country_Demand_Analysis.png # Global expansion
│
├── 📋 Documentation
│   ├── FINAL_EXECUTIVE_REPORT.md            # Executive business report
│   ├── CEO_CMO_Presentation_Script.md       # 5-minute presentation
│   ├── Video_Recording_Guide.md              # Video recording instructions
│   ├── SUBMISSION_INSTRUCTIONS.md           # BI tool submission guide
│   └── PROJECT_SUMMARY.md                   # Project completion summary
│
├── ⚙️ Configuration
│   ├── requirements.txt                      # Python dependencies
│   ├── .gitignore                           # Git ignore rules
│   └── README.md                            # This file
│
└── 📊 Reports
    ├── executive_questions.md                # Business questions analysis
    └── business_insights.py                  # Key business insights
```

## 📊 **Key Insights**

### **Revenue Performance**
- **Total Revenue**: £10.67M (after data cleaning)
- **Peak Month**: November 2011 (£1.46M)
- **Critical Decline**: 42% drop from November to December 2011
- **International Opportunity**: £1.7M from non-UK markets

### **Customer Analysis**
- **Total Customers**: 4,372
- **Top Customer Value**: £279K
- **Customer Concentration**: Top 10% drive 51% of revenue
- **Average CLV**: £1,898 per customer

### **Geographic Distribution**
- **UK Dominance**: 84% of total revenue
- **Top International Markets**: Netherlands, Ireland, Germany
- **Countries Represented**: 38
- **Expansion Potential**: High

### **Operational Metrics**
- **Return Rate**: 1.96%
- **Return Impact**: £897K annually
- **Data Quality**: 97.8% clean data retention
- **Market Coverage**: 38 countries

## 🎯 **Business Impact**

### **Revenue Growth Potential**
| Initiative | Potential Impact | Timeline | Revenue Impact |
|------------|------------------|----------|----------------|
| Customer Retention | +15% revenue | 3 months | +£1.6M |
| International Expansion | +25% revenue | 6 months | +£2.7M |
| Operational Efficiency | +5% revenue | 2 months | +£533K |
| **Combined Potential** | **+45% revenue** | **12 months** | **+£4.8M** |

### **Risk Mitigation**
- **Customer Concentration**: Reduce from 51% to 35%
- **Geographic Concentration**: Reduce UK from 84% to 60%
- **Return Rate**: Reduce from 1.96% to 1.2%

## 📈 **Usage Examples**

### **Interactive Dashboard**
```python
# Launch the Streamlit dashboard
streamlit run retail_dashboard.py
```

### **Data Analysis**
```python
# Run comprehensive data analysis
python analyze_retail_data.py

# Generate business insights
python business_insights.py
```

### **Chart Export**
```python
# Export static charts
python export_charts.py
```

## 🔧 **Development**

### **Data Cleaning Process**
1. **Load Data**: Read Excel file with 541,909 transactions
2. **Identify Issues**: Find negative quantities and invalid prices
3. **Apply Cleaning**: Remove 11,805 problematic records (2.18%)
4. **Validate Results**: Ensure 97.8% data retention
5. **Export Clean Data**: Save processed dataset

### **Visualization Creation**
1. **Question-Specific Analysis**: Address each business question
2. **Chart Generation**: Create interactive and static visualizations
3. **Business Context**: Add strategic insights and recommendations
4. **Export Options**: Support multiple formats (PNG, Excel, PDF)

## 📋 **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 **Authors**

- **Data Analysis Team** - *Initial work* - [Your GitHub](https://github.com/yourusername)

## 🙏 **Acknowledgments**

- Online Retail Dataset for providing comprehensive transaction data
- Streamlit community for excellent dashboard framework
- Plotly team for powerful visualization capabilities
- Python data science ecosystem for robust analysis tools

## 📞 **Contact**

- **Project Link**: [https://github.com/yourusername/online-retail-data-visualization](https://github.com/yourusername/online-retail-data-visualization)
- **Issues**: [GitHub Issues](https://github.com/yourusername/online-retail-data-visualization/issues)

---

**Status**: ✅ Complete and Ready for Production  
**Version**: 1.0  
**Last Updated**: September 2024