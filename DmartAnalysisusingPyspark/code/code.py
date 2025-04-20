from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum
import streamlit as st
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 1: Establish PySpark Connection
# Set up a PySpark environment
# Create a connection to read CSV files into PySpark DataFrames
spark = SparkSession.builder \
    .appName("CSV Reader") \
    .master("local[*]") \
    .config("spark.hadoop.security.authentication", "simple") \
    .getOrCreate()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 2: Load Data into PySpark DataFrames
# Load the products.csv, sales.csv, and customer.csv files into separate PySpark DataFrames
customer_df = spark.read.csv('C:/Users/shali/Documents/Project/github/DmartAnalysisUsingPyspark/input_files/Customer.csv', header=True, inferSchema=True)
product_df = spark.read.csv('C:/Users/shali/Documents/Project/github/DmartAnalysisUsingPyspark/input_files/Product.csv', header=True, inferSchema=True)
sales_df = spark.read.csv('C:/Users/shali/Documents/Project/github/DmartAnalysisUsingPyspark/input_files/Sales.csv', header=True, inferSchema=True)

# Show the first 5 rows of the Customer, Product and Sales DataFrame
print("Customer DataFrame:")
customer_df.show(5)
print("Product DataFrame:")
product_df.show(5)
print("Sales DataFrame:")
sales_df.show(5)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Task 3: Data Transformation and Cleaning
# Perform necessary data cleaning and transformations on the DataFrames:

# 1. Rename columns for consistency if needed
# Rename all the columns with spaces to include _ instead of space
customer_df = customer_df.withColumnRenamed("Customer ID", "Customer_ID") \
                         .withColumnRenamed("Customer Name", "Customer_Name")\
                         .withColumnRenamed("Postal Code", "Postal_Code")

product_df = product_df.withColumnRenamed("Product ID", "Product_ID") \
                         .withColumnRenamed("Product Name", "Product_Name")\
                         .withColumnRenamed("Sub-Category", "Sub_Category")

sales_df = sales_df.withColumnRenamed("Order Line", "Order_Line") \
                   .withColumnRenamed("Order ID", "Order_ID")\
                   .withColumnRenamed("Order Date", "Order_Date")\
                   .withColumnRenamed("Ship Mode", "Ship_Mode")\
                   .withColumnRenamed("Customer ID", "Customer_ID")\
                   .withColumnRenamed("Product ID", "Product_ID")

customer_df.show(5)
product_df.show(5)
sales_df.show(5)


# 2. Handle missing values appropriately

# Check whether there are any missing values in any of the columns
# Function to check missing values for a DataFrame
def check_missing_values(df, df_name):
    missing_count = df.select(
        [sum(col(c).isNull().cast("int")).alias(c) for c in df.columns]
    )
    print(f"Count of missing values in each column for {df_name}:")
    missing_count.show()

    # Check if all missing value counts are 0
    all_zero = missing_count.collect()[0]
    if all(value == 0 for value in all_zero):
        print(f"All columns in {df_name} have 0 missing values.")
    else:
        print(f"Some columns in {df_name} have missing values.")

# Check missing values for all three DataFrames
check_missing_values(customer_df, "Customer DataFrame")
check_missing_values(product_df, "Product DataFrame")
check_missing_values(sales_df, "Sales DataFrame")

# 3. Ensure data types are correctly set for each column.
print("Schema of Customer DataFrame:")
customer_df.printSchema()

print("Schema of Product DataFrame:")
product_df.printSchema()

print("Schema of Sales DataFrame:")
sales_df.printSchema()


# 4. Join the DataFrames on relevant keys (Product ID and Customer ID).
# Join Sales df with Customer df on Customer_ID
sales_customer_df = sales_df.join(customer_df, on = "Customer_ID", how = "inner")

# Join the result with product_df on Product_ID
customer_product_sales_df = sales_customer_df.join(product_df, on="Product_ID", how="inner")

# Show the final DataFrame
print("Final DataFrame after joining:")
customer_product_sales_df.show(10)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 4: Data Analysis and Querying
# Formulate 10 analytical questions based on the integrated dataset

# Register the final DataFrame as a temporary SQL table (customer_product_sales)
customer_product_sales_df.createOrReplaceTempView("customer_product_sales")

# pip install setuptools

# Streamlit App
# Create a Streamlit app to run SQL queries on the DataFrame
st.title("PySpark SQL Query App")
query_option = st.selectbox(
    "Select a query to run:",
    [
        "1. What is the total sales for each product category?",
        "2. Which customer has made the highest number of purchases?",
        "3. What is the average discount given on sales across all products?",
        "4. How many unique products were sold in each region?",
        "5. What is the total profit generated in each state?",
        "6. Which product sub-category has the highest sales?",
        "7. What is the average age of customers in each segment?",
        "8. How many orders were shipped in each shipping mode?",
        "9. What is the total quantity of products sold in each city?",
        "10. Which customer segment has the highest profit margin?"

    ]
)


if query_option == "1. What is the total sales for each product category?":
    query = """
        SELECT Category, SUM(Sales) AS Total_Sales
        FROM customer_product_sales
        GROUP BY Category
    """
elif query_option == "2. Which customer has made the highest number of purchases?":
    query = """
        SELECT Customer_Name, COUNT(Order_ID) AS Purchase_Count
        FROM customer_product_sales
        GROUP BY Customer_Name
        ORDER BY Purchase_Count DESC
        LIMIT 1
    """
elif query_option == "3. What is the average discount given on sales across all products?":
    query = """
        SELECT AVG(Discount) AS Average_Discount
        FROM customer_product_sales
    """
elif query_option == "4. How many unique products were sold in each region?":
    query = """
        SELECT Region, COUNT(DISTINCT Product_ID) AS Unique_Products_Sold
        FROM customer_product_sales
        GROUP BY Region
    """
elif query_option == "5. What is the total profit generated in each state?":
    query = """
        SELECT State, SUM(Profit) AS Total_Profit
        FROM customer_product_sales
        GROUP BY State
    """
elif query_option == "6. Which product sub-category has the highest sales?":
    query = """
        SELECT Sub_Category, SUM(Sales) AS Total_Sales
        FROM customer_product_sales
        GROUP BY Sub_Category
        ORDER BY Total_Sales DESC
        LIMIT 1
    """
elif query_option == "7. What is the average age of customers in each segment?":
    query = """
        SELECT Segment, AVG(Age) AS Average_Age
        FROM customer_product_sales
        GROUP BY Segment
    """
elif query_option == "8. How many orders were shipped in each shipping mode?":  
    query = """
        SELECT Ship_Mode, COUNT(Order_ID) AS Total_Orders_Shipped
        FROM customer_product_sales
        GROUP BY Ship_Mode
    """
elif query_option == "9. What is the total quantity of products sold in each city?":
    query = """
        SELECT City, SUM(Quantity) AS Total_Quantity_Sold
        FROM customer_product_sales
        GROUP BY City
    """
elif query_option == "10. Which customer segment has the highest profit margin?":
    query = """
        SELECT Segment, SUM(Profit) AS Total_Profit
        FROM customer_product_sales
        GROUP BY Segment
        ORDER BY Total_Profit DESC
        LIMIT 1
    """

# Execute the SQL query
if st.button("Run Query"):
    try:
        result = spark.sql(query)
        st.write(result.toPandas()) 
    except Exception as e:
        st.error(f"Error: {e}")