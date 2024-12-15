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
select_options=["1. What is the total population of each district?", "2. How many literate males and females are there in each district?"]
option_selected=st.selectbox("select a query",options=select_options)
if option_selected == "1. What is the total population of each district?":
    query_selected="select district, sum(population) as sum_population from census group by district"
    st.title("Population")
elif option_selected == "2. How many literate males and females are there in each district?":
    query_selected="select district, sum(Literate_Male) as Literate_Male, sum(Literate_Female) as Literate_Female  from census group by district"
    st.title("Literate")
cursor.execute(query_selected)
records = cursor.fetchall()
records_df=pd.DataFrame(records,columns=cursor.column_names)
st.dataframe(records_df)