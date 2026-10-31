header ="""
NAME: Nageeb Yahya Rezq Al-Surmi
SUPERVISOR: Ms Eman Alsamawi
COURSE: Python and Data Analysis
PROJECT TITLE: Superstore Sales & Profit Analysis using Python
SUBMISSION DATE : 26/10/2026

#---------------------------------------------------------------------------
Section 1- Project idea and dataset
#---------------------------------------------------------------------------
1.1 Introduction
--------------------------
A complete data analysis project in Python that studies the sales and profit of a US superstore
to find what drives profit and what causes losses. Retail sales of a US office-supplies
and furniture superstore for the year 2014 to the year 2017.
The dataset downloaded from Kaggle contain 9994 rows and 21 columns. 
The dataset contains products, regions, categories and customer segments and more.

1.2 Problem statement
--------------------------
The main problem there is no picture of which products, which regions,which groups of customers
and which times of year bring the most sales and money to the Superstore.
In addition the analysis must examine how giving discounts affects how money the Superstore keeps
and how well different shipping options work. Many discounts can make sales go up but can cut the profit
margin or even bring losses


1.3 The objective
--------------------------
Understand which products, regions, customer segments and time periods drive
sales and profit in Superstore, and find what causes losses, so the store can make better
pricing and sales decisions.This analysis will provide some business insights to improve the profits
and reduce the losses.

1.4 Questions to answer
--------------------------
    1. Which categories and sub-categories generate the highest sales and profit,
       and which ones lose money?
    2. How do sales and profit change over time (by year and by month)?
    3. Which regions and customer segments are the most profitable?
    4. How does the discount level affect profit?
    5. Which shipping mode is used most, and how long does shipping take on average?


1.5 Methodology
--------------------------
The Analysis will conducts the rules of data analaysis:
1.5.1 Data wrangling
        1. data gathering: Import the data
        Dataset URL: Superstore Dataset from Kaggle
            Dataset containing Sales & Profits of a Superstore
            https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
            (9,994 order lines, 21 columns, orders from 2014 to 2017)

        2. Assesing: understand the dataset, explore the data, check quality, identifing the issues

        3. Cleaning: fix issues by modefying, Replacing, Renaming, Removing problomatic data

1.5.2 Perform EDA (Exploratory Data Analysis)
        1. Explore data using statistics and visual
        2. Discover data pattern
        3. Understand data distribution

1.6   Draw conclusion (RESULTS AND RECOMMENDATIONS)
--------------------------
        Summaries key finding

1.7   Comunicate result
--------------------------
        Share the result

1.8 Acknowledgements
--------------------------
            I do not own this data. I merely found it from the Tableau website: 
            https://trailhead.salesforce.com/trailblazer-community/feed/0D5KX00000kQPXv0AO 
            All credits to the original authors/creators. 
            For educational purposes only
"""
 

import os

import numpy as np                  #for numeric calculations
import pandas as pd                 #for tables
import matplotlib.pyplot as plt     #for charts : pyplot: A sub module inside Matplotlib that provides a stateful, MATLAB-style interface for drawing plots easily.
import seaborn as sns

# Print the project description & objective
print(header)

# ----------------------------------------------------------------------
#Library Setting for: Pandas, seborn and project path
# ----------------------------------------------------------------------
##Prepare setting for seaborn : set white background with gray grid lines for all your data visualizations 
sns.set_theme(style="whitegrid")

##Pandas show every single column in your DataFrame instead of replacing (...)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)  #sets the maximum number of characters per line

## Prepare the absolute path of the current project
os.chdir(os.path.dirname(os.path.abspath(__file__)))

## Title and subtitle output format for each section
def title(text):
    print("\n" + "-" * 80)
    print(text)
    print("-" * 80)

def subtitle(text):
    print("\n" + "-" * 50)
    print(text)
    print("-" * 50)

# ----------------------------------------------------------------------
# Section 2- Data Exploration
# ----------------------------------------------------------------------
title("Section 2- DATA EXPLORATION") #use function to format the title

# Read the data from csv and save it as DataFrame
df = pd.read_csv("data/superstore.csv", encoding="latin1")  # encoding used to prevent errors if the text file contains special accents, symbols, or characters that standard UTF-8 might fail to decode.

# Display the data (Head/Tail)
subtitle("--2.1 First 5 rows:")
print(df.head())

subtitle("--2.2 Last 5 rows:")
print(df.tail())

# Number of rows and columns
subtitle("--2.3 Number of rows and columns")
print("\nRows   :", df.shape[0])
print("Columns:", df.shape[1])

# Column names and data types
subtitle("--2.4 Column names:")
print(list(df.columns))  # print the column name as list not as series

subtitle("--2.5 Data types:") # data type for each column 
df.info()

# Count missing values
subtitle("--2.6 Missing values per column:")
print(df.isnull().sum())

# Count duplicated rows 
subtitle("--2.7 Duplicated rows:")
print(df.duplicated().sum())

# Descriptive statistics ( for numiric col and text col)
subtitle("--2.8 Descriptive statistics (numeric cols):")
print(df.describe()) # summary for numaric col, calculate: count/mean/std/min/max/25%/50%/75%

subtitle("--2.9 Descriptive statistics (text cols):")
print(df.describe(include=["object", "string"]))  #summary of non-numeric col (text and string-based) col, calculate: count/uique/top/freq of top


# ----------------------------------------------------------------------
# Section 3- Data Cleaning
# ----------------------------------------------------------------------
title("Section 3- DATA CLEANING")

# Handle missing values: numeric col by-> median, text col by-> most frequent value
#Loop : to go through col by col and check the null vlaue

for col in df.columns:                  #for each col do check
    if df[col].isnull().sum() > 0:      #if the col has null values only 
        if pd.api.types.is_numeric_dtype(df[col]):      #check the col is numeric or text: true=numeric , False=text. pd.api.types inspect the datatype
            df[col] = df[col].fillna(df[col].median())  #this col is numeric: fill the missed value with median
        else:
            df[col] = df[col].fillna(df[col].mode()[0]) #this col is text: fill every missed value with most frequent text. the mode  returns a Pandas Series containing one or more values , the most freq is on the first index 0

subtitle("--3.1 Missing values after handling:")
print( df.isnull().sum().sum() )

# Remove duplicates
df = df.drop_duplicates()
subtitle("--3.2 Rows after removing duplicates:")
print(df.shape[0])

# Fix data types: Order Date and Ship Date are stored as text(string) -> convert to datetime
# Pandas convert date as US format m/d/y,
# To change US to UK format d/m/y you have to convert datatype to string
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")  # date : US format
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")    #date : US format

subtitle("--3.3 Date column types (changed from string to Date):")
print(df[["Order Date", "Ship Date"]].dtypes)

# Handle invalid values: text (extra space) & numeric (negativ/wrong date/outside of range /depend on col datatype)
#Process: find invalid in text or numeric col then delete the row

#1-Process the the col that their datatype is string: 
# remove leading and trailing whitespace (spaces, tabs, newlines)
text_cols = df.select_dtypes(include=["object", "string"]).columns  #: Extracts the names of cols that their data type is text as a pandas Index list
df[text_cols] = df[text_cols].apply(lambda s: s.str.strip())  #remove extra space from all text in the col that their datatype is string(text) and resaved in th df

#2-Process the the col that their datatype is numeric: 
#filters out corrupted, erroneous, or logically impossible data
#The code creates a boolean mask named invalid. 
# A row is marked as True (invalid) if it meets any of the following conditions (connected by the | OR operator):
#we have to check numeric col by col bcs every col has diffeent datatypes
#then delete the whole row if one value is invalid 
invalid = (                  
    (df["Sales"] <= 0)
    | (df["Quantity"] <= 0)                 #The number of items ordered is zero or negative
    | (~df["Discount"].between(0, 1))       # ~df: check discount is outside of 0% and 100%
    | (df["Ship Date"] < df["Order Date"])  #The shipping date happens before the order date
)

#Summing the boolean mask counts and prints the total number of rows that failed at least one of the rules above.
subtitle("--3.4 Number of Invalid rows found:")
print( invalid.sum())
#The deleted rows
# 1. Print the actual data of the invalid rows
subtitle("--3.5 Invalid Rows Data:")
print(df[invalid])


df = df[~invalid]       #Cleaning the Dataset:  inverts the mask, This overwrites the original DataFrame, keeping only the valid data rows and permanently dropping the bad ones



# Rename columns: lowercase with underscores
df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace("-", "_")
subtitle("--3.6 New column names: (change space with underscore)")
print(list(df.columns))

# Drop unimportant columns: row_id is only an index, country has a single value,
# postal_code is not needed for this analysis
subtitle("--3.7 Unique countries:")
print(list(df["country"].unique()))

if len(list(df["country"].unique())):
    print(f"Recomended to delete this column: {list(df["country"].unique())}")

#delete the unrequired columns
print("Recomended to delete this columns: row_id and postal_code")

df = df.drop(columns=["row_id", "country", "postal_code"])  # delete the columns that not needed in data analysis
subtitle("--3.8 Shape after cleaning:") 
print(df.shape)

print(df.head())


# ----------------------------------------------------------------------
# Section 4- Data Analysis
# ----------------------------------------------------------------------
title("Section 4- DATA ANALYSIS :")

# Working with dates: split the year, month
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month
df["year_month"] = df["order_date"].dt.to_period("M")
df["shipping_days"] = (df["ship_date"] - df["order_date"]).dt.days

subtitle("--4.1 Date features - DATA ANALYSIS:")
print(df[["order_date", "ship_date", "order_year", "order_month", "shipping_days"]].head())

# Calculations with NumPy
df["profit_margin"] = np.round(df["profit"] / df["sales"] * 100, 2)
df["profit_status"] = np.where(df["profit"] >= 0, "Profit", "Loss")

subtitle("--4.2 Calculations with NumPy - DATA ANALYSIS:")
print(f"Total sales      : {np.round(np.sum(df["sales"]), 2)}" )
print(f"Total profit     : {np.round(np.sum(df["profit"]), 2)}" )
print(f"Average sale     : {np.round(np.mean(df["sales"]), 2)}" )
print(f"Median sale      : {np.round(np.median(df["sales"]), 2)}" )
print(f"Std of profit    : {np.round(np.std(df["profit"]), 2)}" )
print(f"90% of sales-mean: {np.round(np.percentile(df["sales"], 90), 2)}" ) #The 90% percentile threshold:represent how much the average of 90% of your sales, example: you sal every day by 500 rinngget for three monthsm at the last week you sale by 70,000 ringget, it does not reflect the actual daily sales .Tells NumPy to sort the values from smallest to largest and find the value sitting at the 90% of your sales, to reflect actual sales
print(f"Overall margin % : {np.round(df["profit"].sum() / df["sales"].sum() * 100, 2)}" )


# Apply: group each discount into a discount band
#DIVIDE THE ORDERS INTO GROUPS BASED ON AMOUNT OF DISCOUNT, THEN DISPLAY THE GROUP NAME AND NUMBER OF PRODUCTS
#NAME OF GROUPING: 0%:No Discount , 1%-20%: lOW, 21%-40% mEDIUM, >40% : HIGH 
def discount_band(d):
    if d == 0:
        return "No Discount"
    elif d <= 0.2:
        return "Low (1-20%)"
    elif d <= 0.4:
        return "Medium (21-40%)"
    else:
        return "High (>40%)"


df["discount_band"] = df["discount"].apply(discount_band) ##passes every individual value from "discount" column into a custom function name "discount_band"
subtitle("--4.3 Group: Order lines per discount band:")
print(df["discount_band"].value_counts())       #display the group name with no of products: low (238) ,medium (649),high.....  

# Filtering
subtitle("--4.5 Filtering: Order lines with a loss (Profit < 0):")
loss_orders = df[df["profit"] < 0]
print("Order lines with a loss:", len(loss_orders), f"({len(loss_orders) / len(df):.1%})")
print("Total money lost  ($)  :", round(loss_orders["profit"].sum(), 2))

#Orders shipped to the West region over $1,000 : for example : don't pay shipping fees
west_big = df[(df["region"] == "West") & (df["sales"] > 1000)]
print("Orders shipped to the West above $1000:", len(west_big))

# Sorting: sort by profit from smallest to largest (ascending):
# returns the top 10 rows with the lowest profit/biggest losses 
subtitle("4.6 Sorting by profit from smallest to largest:")
print("Top 10 biggest losses/lowest profit:\n")
print(df.sort_values("profit").head(10)[["order_id", "product_name", "sub_category", "sales", "discount", "profit"]])  #sort and show only this columns 

title("\nAnswer the questions:")

# ----------------------------------------------------------------------------
# Q1 - Which categories and sub-categories generate the most sales and profit?
# ------------------------------------------------------------------------------
title("Q1- SALES AND PROFIT BY CATEGORY AND SUB-CATEGORY \nWhich categories and sub-categories generate the highest sales and profit,and which ones lose money?")

#Group by, Agg, sort
#1-Category Summary as dataframe: number of rows = number of aggregated categories 
##create a new datafram with new claculated columns 
category_summary = (            
    df.groupby("category")
      .agg(total_sales=("sales", "sum"), total_profit=("profit", "sum"), orders=("order_id", "nunique"))
      .sort_values("total_sales", ascending=False)  #sort the category from largest to smallest
)
category_summary["margin_%"] = (category_summary["total_profit"] / category_summary["total_sales"] * 100).round(2)  #create new col to calculate the margine in %

subtitle("--Q1.1 Category Summary - (Group by, Agg, sort, round)")
print(category_summary.round(2))

#2-Sub Category Summary as dataframe: number of rows = number of aggregated sub categories 
subcat_summary = (
    df.groupby("sub_category")
      .agg(total_sales=("sales", "sum"), total_profit=("profit", "sum"))
      .sort_values("total_profit", ascending=False)
      .round(2)
)

subtitle("--Q1.2 Sub Category Summary (Group by, Agg, sort, round)")
print("\n", subcat_summary)

# 3-Concat: top 3 and bottom 3 sub-categories by profit in one table
top3 = subcat_summary.head(3).assign(group="Top 3")
bottom3 = subcat_summary.tail(3).assign(group="Bottom 3")
top_bottom = pd.concat([top3, bottom3])

subtitle("--Q1.3 Concat Top 3 and bottom 3 sub-categories by total profit:")
print(top_bottom)

# ---------------------------------------------------------------------
# Q2 - How do sales and profit change over time?
# ---------------------------------------------------------------------
title("Q2 - SALES AND PROFIT OVER TIME \nHow do sales and profit change over time (by year and by month)?")

#1-by year: Groupby order_year which calculated in step 4.1 data analysis
# yearly is new dataframe hold the profit for each year
#calculates the year-over-year percentage growth in total sales
#Calculates the percentage change between the current year's sales and the previous year's sales
yearly = df.groupby("order_year").agg(total_sales=("sales", "sum"), total_profit=("profit", "sum")).round(2)    
yearly["sales_growth_%"] = (yearly["total_sales"].pct_change() * 100).round(2)  #sales_growth_% is a new col added: .pct_change(): Calculates the percentage change between the current year's sales and the previous year's sales

subtitle("--Q2.1 Sales and profit over time by year:")
print(yearly)

#2.1-by month: Groupby
#groups data by the time period 
monthly = df.groupby("year_month").agg(total_sales=("sales", "sum"), total_profit=("profit", "sum"))
monthly.index = monthly.index.to_timestamp()    #Prepare for plot: This line converts the index into standard datetime timestamps (example: changing "2026-01" to 2026-01-01).

#2.3-best 10 month for all years
best_month = df.groupby("order_month")["sales"].sum().sort_values(ascending=False)
subtitle("--Q2.2 Best 10 months for sales (all years):")
print(best_month.head(10).round(2))

# ---------------------------------------------------------------------
# Q3 - Which regions and segments are the most profitable?
# ---------------------------------------------------------------------
title("Q3 - REGIONS AND SEGMENTS \nWhich regions and customer segments are the most profitable?")

region_sales = df.groupby("region").agg(total_sales=("sales", "sum"), total_profit=("profit", "sum"))
region_orders = df.groupby("region").agg(orders=("order_id", "nunique"), customers=("customer_id", "nunique"))

# Merge: join the two region tables on region
region_summary = pd.merge(region_sales, region_orders, on="region")
region_summary["margin_%"] = region_summary["total_profit"] / region_summary["total_sales"] * 100

subtitle("--Q3.1 Sales summary by Region: ")
print(region_summary.sort_values("total_profit", ascending=False).round(2))

segment_summary = (
    df.groupby("segment")
      .agg(total_sales=("sales", "sum"), total_profit=("profit", "sum"), customers=("customer_id", "nunique"))
      .sort_values("total_sales", ascending=False)
)
segment_summary["sales_share_%"] = segment_summary["total_sales"] / segment_summary["total_sales"].sum() * 100
subtitle("--Q3.2 Sales summary by Segment ") 
print( segment_summary.round(2))

state_profit = df.groupby("state")["profit"].sum().sort_values()
subtitle("--Q3.3 States with the biggest losses:")
print(state_profit.head(5).round(2))

# ---------------------------------------------------------------------
# Q4 - How does discount affect profit?
# ---------------------------------------------------------------------
title("Q4 - DISCOUNT VS PROFIT \nHow does the discount level affect profit?")

band_order = ["No Discount", "Low (1-20%)", "Medium (21-40%)", "High (>40%)"]
discount_summary = (
    df.groupby("discount_band")
      .agg(order_lines=("order_id", "count"), avg_profit=("profit", "mean"), total_profit=("profit", "sum"))
      .reindex(band_order)
      .round(2)
)
subtitle("--Q4.1 Discount summary:")
print(discount_summary)

corr = np.corrcoef(df["discount"], df["profit"])[0, 1]   #calculate the correlation cooffecient using numpy function
subtitle("--Q4.2 Correlation between discount and profit:") 
print( round(corr, 3))

# ---------------------------------------------------------------------
# Q5 - Which shipping mode is used most and how long does shipping take?
# ---------------------------------------------------------------------
title("Q5 - SHIPPING \nWhich shipping mode is used most, and how long does shipping take on average?")

ship_summary = (
    df.groupby("ship_mode")
      .agg(orders=("order_id", "nunique"), avg_shipping_days=("shipping_days", "mean"))
      .sort_values("orders", ascending=False)
      .round(2)
)
subtitle("--Q5.1 Ship summary")
print(ship_summary)

subtitle("--Q5.2 Average shipping time (all orders):") 
print( round(df["shipping_days"].mean(), 2), "days")


# ----------------------------------------------------------------------
# Section 5- Data Visualization
# ----------------------------------------------------------------------
title("Section 5- DATA VISUALIZATION")

#Q1 - chart
# 1.1 Bar Chart - Profit by sub-category (Q1)
plt.figure(figsize=(11, 6))
colors = np.where(subcat_summary["total_profit"] >= 0, "#2a9d8f", "#e76f51")
plt.barh(subcat_summary.index, subcat_summary["total_profit"], color=colors)
plt.gca().invert_yaxis()
plt.title("Total Profit by Sub-Category - Nageeb Project")
plt.xlabel("Profit ($)")
plt.ylabel("Sub-Category")
plt.tight_layout()
plt.savefig("images/bar_profit_by_subcategory.png", dpi=120)    #save the chart as image

#Q2: sales and profit change over time
# 2.1 Line Chart - Monthly sales and profit (Q2)
plt.figure(figsize=(12, 5))
plt.plot(monthly.index, monthly["total_sales"], marker="o", label="Sales")
plt.plot(monthly.index, monthly["total_profit"], marker="o", label="Profit")
plt.title("Monthly Sales and Profit (2014-2017) - Nageeb Project")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()
plt.savefig("images/line_monthly_sales_profit.png", dpi=120)    #save the chart as image

# 2.2 Line Chart - Yearly sales and profit (Q2)
plt.figure(figsize=(12, 5))
plt.plot(yearly.index , yearly["total_sales"], marker="o", label="Sales")
plt.plot(yearly.index, yearly["total_profit"], marker="o", label="Profit")
plt.title("Yearly Sales and Profit (2014-2017) - Nageeb Project")
plt.xlabel("Year")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()
plt.savefig("images/line_Yearly_sales_profit.png", dpi=120)    #save the chart as image

#Q3:regions and customer segments are the most profitable
# 3.1 Pie Chart - Sales share by customer segment (Q3)
plt.figure(figsize=(6, 6))
plt.pie(segment_summary["total_sales"], labels=segment_summary.index, autopct="%1.1f%%", startangle=90,
        colors=sns.color_palette("Set2"))
plt.title("Sales Share by Customer Segment - Nageeb Project")
plt.tight_layout()
plt.savefig("images/pie_sales_by_segment.png", dpi=120)     #save the chart as image

# 3.2 Bar Chart - Profit by region (Q3)
plt.figure(figsize=(8, 5))
sns.barplot(x=region_summary.index, y=region_summary["total_profit"], hue=region_summary.index,
            palette="viridis", legend=False)
plt.title("Total Profit by Region - Nageeb Project")
plt.xlabel("Region")
plt.ylabel("Profit ($)")
plt.tight_layout()
plt.savefig("images/bar_profit_by_region.png", dpi=120)     #save the chart as image

#Q4: Discount vs profit
# 4.1 Scatter Plot - Discount vs profit (Q4)
plt.figure(figsize=(9, 6))
sns.scatterplot(data=df, x="discount", y="profit", hue="category", alpha=0.6)
plt.axhline(0, color="black", linewidth=1)
plt.title("Discount vs Profit - Nageeb Project")
plt.xlabel("Discount")
plt.ylabel("Profit ($)")
plt.tight_layout()
plt.savefig("images/scatter_discount_vs_profit.png", dpi=120)       #save the chart as image

#Q5:Shipping days vs number of order
# 5.1 Histogram - Distribution of shipping days (Q5)
plt.figure(figsize=(8, 5))
sns.histplot(df["shipping_days"], bins=range(0, 9), discrete=True, color="#457b9d")
plt.title("Distribution of Shipping Days - Nageeb Project")
plt.xlabel("Shipping Days")
plt.ylabel("Number of Order Lines")
plt.tight_layout()
plt.savefig("images/hist_shipping_days.png", dpi=120)       #save the chart as image

print("7 charts saved in the images/ folder.")


# ----------------------------------------------------------------------
# Section 6- Results and Recommendations
# ----------------------------------------------------------------------
title("Section 6- RESULTS AND RECOMMENDATIONS")

print("""
Main observations
- The store sold $2.30M with a profit of $286K, so the overall profit margin is 12.5%.
- 18.7% of order lines lost money, adding up to $156K in losses.
- The average sale ($230) is much higher than the median sale ($54): most orders are small,
  and a few large orders raise the average.
- The data was already clean: no missing values, no duplicates and no invalid rows were found.

Patterns and trends
- Sales go up every year after 2015 (+29.5% in 2016, +20.4% in 2017), and profit goes up every year.
- Sales are seasonal: November, December and September are the strongest months every year.
- Higher discount means lower profit (correlation = -0.22). Every discount above 20% loses money on average.

Key findings
1. Technology is the most profitable category ($145K profit, 17.4% margin).
   Furniture sells almost as much ($742K) but earns only a 2.5% margin.
2. Tables (-$17.7K), Bookcases (-$3.5K) and Supplies (-$1.2K) lose money,
   while Copiers, Phones and Accessories bring the most profit.
3. Discounts above 20% destroy profit: the medium-discount band loses $35.8K
   and the high-discount band (>40%) loses $99.6K.
4. The West is the best region ($108K profit, 14.9% margin). The Central region has the
   lowest margin (7.9%), and Texas, Ohio and Pennsylvania lose the most money.
5. The Consumer segment brings 50.6% of sales. Standard Class is the most used shipping mode
   (2,994 orders, ~5 days); the average shipping time is about 4 days.

Recommendations
- Limit discounts to 20% at most, especially on Machines, Binders and Tables,
  where the biggest single losses happen.
- Review the pricing and costs of Tables and Bookcases, or stop discounting them,
  to turn Furniture into a profitable category.
- Focus marketing on Technology (Copiers, Phones, Accessories) because it has the highest margin.
- Investigate the loss-making states (Texas, Ohio, Pennsylvania, Illinois) and check their discount policy.
- Prepare stock and campaigns before September-December, the peak sales season.
""")

# Show all the charts (close the chart windows to end the program)
plt.show()

#End of data analysis project - Nageeb project made on 26/10/2026