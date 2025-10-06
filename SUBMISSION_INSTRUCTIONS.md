# 📊 Submission Instructions for Tableau (.twbx) and Power BI (.pbix)

## 🎯 What You Need to Submit

You have **two options** for submission:

### Option 1: Tableau (.twbx format)
### Option 2: Power BI (.pbix format)

---

## 📁 Files Ready for Import

I've created individual Excel files for each question:

### Question 1: Monthly Revenue 2011
- **File**: `Q1_Monthly_Revenue_2011.xlsx`
- **Data**: Monthly revenue aggregation for 2011
- **Chart Type**: Line chart showing seasonal trends

### Question 2: Top 10 Countries (Excluding UK)
- **File**: `Q2_Top_10_Countries.xlsx`
- **Data**: Top 10 countries by revenue with quantity metrics
- **Chart Type**: Dual-axis chart (Revenue bars + Quantity line)

### Question 3: Top 10 Customers
- **File**: `Q3_Top_10_Customers.xlsx`
- **Data**: Highest revenue generating customers
- **Chart Type**: Descending bar chart

### Question 4: Country Demand Analysis
- **File**: `Q4_Country_Demand_Analysis.xlsx`
- **Data**: All countries with revenue, quantity, and customer metrics
- **Chart Type**: Bubble chart (Revenue vs Quantity, bubble size = customers)

### Combined Dataset
- **File**: `Online_Retail_Combined_Dataset.xlsx`
- **Data**: Full cleaned dataset for comprehensive analysis

---

## 🔧 Option 1: Tableau Instructions (.twbx)

### Step 1: Open Tableau Desktop
1. Launch Tableau Desktop
2. Connect to Excel files

### Step 2: Create Each Visualization

#### Question 1: Monthly Revenue Time Series
1. **Connect to**: `Q1_Monthly_Revenue_2011.xlsx`
2. **Create Line Chart**:
   - Drag `MonthYear` to Columns
   - Drag `Revenue` to Rows
   - Format: Line chart with markers
   - Title: "Question 1: Monthly Revenue Trends - 2011"

#### Question 2: Top 10 Countries
1. **Connect to**: `Q2_Top_10_Countries.xlsx`
2. **Create Dual-Axis Chart**:
   - Drag `Country` to Columns
   - Drag `Revenue` to Rows (first axis)
   - Drag `Quantity` to Rows (second axis)
   - Format: Bar chart for Revenue, Line chart for Quantity
   - Title: "Question 2: Top 10 Countries by Revenue (Excluding UK)"

#### Question 3: Top 10 Customers
1. **Connect to**: `Q3_Top_10_Customers.xlsx`
2. **Create Bar Chart**:
   - Drag `CustomerID` to Columns
   - Drag `Revenue` to Rows
   - Sort by Revenue descending
   - Title: "Question 3: Top 10 Customers by Revenue"

#### Question 4: Country Demand Analysis
1. **Connect to**: `Q4_Country_Demand_Analysis.xlsx`
2. **Create Bubble Chart**:
   - Drag `Quantity` to Columns
   - Drag `Revenue` to Rows
   - Drag `CustomerID` to Size
   - Drag `Country` to Label
   - Title: "Question 4: Country Demand Analysis"

### Step 3: Create Dashboard
1. Create new Dashboard
2. Add each visualization as separate sheets
3. Name tabs: "Question 1", "Question 2", "Question 3", "Question 4"

### Step 4: Save as .twbx
1. File → Save As
2. Choose "Tableau Packaged Workbook (.twbx)"
3. Name: "Online_Retail_Analysis.twbx"

---

## 🔧 Option 2: Power BI Instructions (.pbix)

### Step 1: Open Power BI Desktop
1. Launch Power BI Desktop
2. Get Data → Excel → Select your files

### Step 2: Create Each Visualization

#### Question 1: Monthly Revenue Time Series
1. **Import**: `Q1_Monthly_Revenue_2011.xlsx`
2. **Create Line Chart**:
   - X-axis: MonthYear
   - Y-axis: Revenue
   - Visual: Line chart
   - Title: "Question 1: Monthly Revenue Trends - 2011"

#### Question 2: Top 10 Countries
1. **Import**: `Q2_Top_10_Countries.xlsx`
2. **Create Combo Chart**:
   - X-axis: Country
   - Y-axis: Revenue (Column)
   - Y-axis: Quantity (Line)
   - Title: "Question 2: Top 10 Countries by Revenue (Excluding UK)"

#### Question 3: Top 10 Customers
1. **Import**: `Q3_Top_10_Customers.xlsx`
2. **Create Bar Chart**:
   - X-axis: CustomerID
   - Y-axis: Revenue
   - Sort by Revenue descending
   - Title: "Question 3: Top 10 Customers by Revenue"

#### Question 4: Country Demand Analysis
1. **Import**: `Q4_Country_Demand_Analysis.xlsx`
2. **Create Scatter Chart**:
   - X-axis: Quantity
   - Y-axis: Revenue
   - Size: CustomerID
   - Legend: Country
   - Title: "Question 4: Country Demand Analysis"

### Step 3: Create Report Pages
1. Create 4 separate pages
2. Name pages: "Question 1", "Question 2", "Question 3", "Question 4"
3. Add appropriate visualizations to each page

### Step 4: Save as .pbix
1. File → Save As
2. Choose "Power BI Desktop files (.pbix)"
3. Name: "Online_Retail_Analysis.pbix"

---

## 📋 Quick Reference for Chart Specifications

### Question 1: Monthly Revenue Time Series
- **Chart Type**: Line chart with markers
- **X-axis**: MonthYear (January 2011, February 2011, etc.)
- **Y-axis**: Revenue (£)
- **Format**: Currency formatting for Y-axis

### Question 2: Top 10 Countries
- **Chart Type**: Combo chart (Dual-axis)
- **X-axis**: Country
- **Y-axis 1**: Revenue (Bar chart)
- **Y-axis 2**: Quantity (Line chart)
- **Sort**: By Revenue descending

### Question 3: Top 10 Customers
- **Chart Type**: Bar chart
- **X-axis**: CustomerID
- **Y-axis**: Revenue
- **Sort**: By Revenue descending
- **Color**: Gradient (blue to light blue)

### Question 4: Country Demand Analysis
- **Chart Type**: Scatter/Bubble chart
- **X-axis**: Quantity
- **Y-axis**: Revenue
- **Size**: Number of customers
- **Color**: Revenue (gradient)
- **Labels**: Country names

---

## 🎯 Recommended Submission

**I recommend using Power BI (.pbix)** because:
1. ✅ Easier to create multiple pages (tabs)
2. ✅ Better dual-axis chart support
3. ✅ More intuitive bubble chart creation
4. ✅ Professional formatting options
5. ✅ Better data modeling capabilities

---

## 📁 Files to Upload

After creating your visualization tool:

### For Tableau Users:
- Upload: `Online_Retail_Analysis.twbx`

### For Power BI Users:
- Upload: `Online_Retail_Analysis.pbix`

---

## 🚀 Alternative: Use Existing Static Images

If you prefer, you can also submit the static PNG files I created:
- `Question_1_Monthly_Revenue_2011.png`
- `Question_2_Top_10_Countries.png`
- `Question_3_Top_10_Customers.png`
- `Question_4_Country_Demand_Analysis.png`

These are already created and ready for submission!


