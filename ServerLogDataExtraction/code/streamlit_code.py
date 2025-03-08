# Import mysql, pandas and streamlit
import mysql.connector
from mysql.connector import Error
import pandas as pd
import streamlit as st

#Establish the connection to mysql
connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='Chellamss@123',  # Replace with your MySQL password
            database='guvi', # Replace with your database name
            auth_plugin='mysql_native_password'
        )

print("Mysql connection established successfully!")

cursor = connection.cursor()
select_options=["1. How many unique email addresses are in the log_history table?",
                "2. Which email address has the most entries in the table?",
                "3. On which date were the most emails received?",
                "4. How many emails were received in the year 2008?",
                "5. Which domain has the most emails?",
                "6. How many emails were received per month in 2008?",
                "7. Which email address has the longest time span between their first and last email?",
                "8. How many emails were received on weekends (Saturday and Sunday)?",
                "9. What is the average number of emails received per day?",
                "10. Which email address has the most recent email?",
                ]
option_selected=st.selectbox("select a query",options=select_options)
if option_selected == "1. How many unique email addresses are in the log_history table?":
    query_selected="SELECT COUNT(DISTINCT email) AS unique_emails FROM log_history;"
    st.title("Distinct Email")

elif option_selected == "2. Which email address has the most entries in the table?":
    query_selected="SELECT email, COUNT(*) AS email_count FROM log_history GROUP BY email ORDER BY email_count DESC LIMIT 1;"
    st.title("Most email entries")

elif option_selected == "3. On which date were the most emails received?":
    query_selected="SELECT DATE(date) AS email_date, COUNT(*) AS email_count FROM log_history GROUP BY DATE(date) ORDER BY email_count DESC LIMIT 1;"
    st.title("Date of most emails received")

elif option_selected == "4. How many emails were received in the year 2008?":
    query_selected="SELECT COUNT(*) AS emails_in_2008 FROM log_history WHERE YEAR(date) = 2008;"
    st.title("Emails received in 2008")

elif option_selected == "5. Which domain has the most emails?":
    query_selected="SELECT SUBSTRING_INDEX(email, '@', -1) AS domain, COUNT(*) AS email_count FROM log_history GROUP BY domain ORDER BY email_count DESC LIMIT 1;"
    st.title("Domain with most emails")

elif option_selected == "6. How many emails were received per month in 2008?":
    query_selected="SELECT YEAR(date) AS year, MONTH(date) AS month, COUNT(*) AS email_count FROM log_history WHERE YEAR(date) = 2008 GROUP BY YEAR(date), MONTH(date) ORDER BY year, month;"
    st.title("Emails received per month in 2008")

elif option_selected == "7. Which email address has the longest time span between their first and last email?":
    query_selected="SELECT email, DATEDIFF(MAX(date), MIN(date)) AS time_span_days FROM log_history GROUP BY email ORDER BY time_span_days DESC LIMIT 1;"
    st.title("Longest time span")

elif option_selected == "8. How many emails were received on weekends (Saturday and Sunday)?":
    query_selected="SELECT COUNT(*) AS weekend_emails FROM log_history WHERE DAYOFWEEK(date) IN (1, 7);"
    st.title("Emails received on weekends")

elif option_selected == "9. What is the average number of emails received per day?":
    query_selected="SELECT AVG(email_count) AS avg_emails_per_day FROM (SELECT DATE(date) AS email_date, COUNT(*) AS email_count FROM log_history GROUP BY DATE(date)) AS daily_emails;"
    st.title("Average number of emails per day")
	
elif option_selected == "10. Which email address has the most recent email?":
    query_selected="SELECT email, MAX(date) AS last_email_date FROM log_history GROUP BY email ORDER BY last_email_date DESC LIMIT 1;"
    st.title("Email addresss with most recetn email")
	

cursor.execute(query_selected)
records = cursor.fetchall()
records_df=pd.DataFrame(records,columns=cursor.column_names)
st.dataframe(records_df)