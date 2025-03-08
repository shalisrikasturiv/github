import re # import re module for regular expression
from datetime import datetime # for handling date and time

# Task 1: Extract Email Addresses and Dates
# Match the email id and date with the pattern
email_pattern = re.compile(r'From\s+([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')
date_pattern = re.compile(r'Date:\s+([A-Za-z]{3},\s+\d{1,2}\s+[A-Za-z]{3}\s+\d{4}\s+\d{2}:\d{2}:\d{2}\s+[-+]\d{4})')

# Read the mbox.txt file
with open('C:/Users/shali/Documents/Project/github/ServerLogDataExtraction/sourcefile/mbox.txt','r') as file:
   content=file.read()

emails = email_pattern.findall(content)
dates = date_pattern.findall(content)

# Declare an empty list
structured_data = []

# Task 2: Data Transformation
# Format the date and time
for email, date_str in zip(emails, dates):
    date_obj = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z')
    formatted_date = date_obj.strftime('%Y-%m-%d %H:%M:%S')
    structured_data.append({'email': email,'date': formatted_date})


# Task 3: Save Data to MongoDB
# Import the required library for MongoDB connection
import pymongo
from pymongo import MongoClient

# Establish connection to MongoDB
client = MongoClient("mongodb://localhost:27017/")
print("MongoDB connection established successfully!")

# Check whether the connection is establised by fetching any collection from MongoDB
db = client['guvi']
collection=db['log_history']

if structured_data:
    collection.insert_many(structured_data)
    print(f"Inserted {len(structured_data)} records into the 'log_history' collection.")
else:
    print("No data to insert.")


mongo_data=list(collection.find({}, {'_id': 0}))
print(f"Fetched {len(mongo_data)} records from 'log_history' collection.")


# Task 4: Database Connection and Data Upload
# Import necessary libraries for mysql

import mysql.connector
from mysql.connector import Error

# Establish the connection with mysql

connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Chellamss@123',
            database='guvi',
            auth_plugin='mysql_native_password'
        )
print("Mysql connection established successfully!")

# Create the DDL for the log_history table
CreateDDL = '''CREATE TABLE IF NOT EXISTS log_history (id INT AUTO_INCREMENT PRIMARY KEY,email VARCHAR(255) NOT NULL,date DATETIME NOT NULL)'''
# Create a cursor to execute the commands
# Execute the DDL
cursor = connection.cursor()
cursor.execute(CreateDDL)
print("user_history table created successfully!")

# Create the insert query
insert_query = """INSERT INTO log_history (email, date)VALUES (%s, %s)"""
records_to_insert = [(record['email'], record['date']) for record in mongo_data]

#Execute the insert query and commit it
cursor.executemany(insert_query, records_to_insert)
connection.commit()
print(f"Inserted {cursor.rowcount} records into MySQL.")