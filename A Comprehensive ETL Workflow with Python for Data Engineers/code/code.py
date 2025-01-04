# Import required libraries for
# pandas,
# parsing xml,
# glob for identifying the files with same pattern,
# logging to enable logging to log file,
# datetime and time for capturing current time.

import pandas as pd
import xml.etree.ElementTree as ET
import glob
import logging
from datetime import datetime
import time

# Enable logging to the log_file.txt
logging.basicConfig(filename='c:/Users/shali/Documents/Project/github-1/A Comprehensive ETL Workflow with Python for Data Engineers/code/log_file.txt', level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

# Capturing info for the Extraction phase starting
logging.info("Extraction phase started")
# Capturing the start time for the Extraction phase starting
start_time = datetime.now()

# Identify all the csv, json and xml files in the folder
csvfiles=glob.glob("c:/Users/shali/Documents/Project/github-1/A Comprehensive ETL Workflow with Python for Data Engineers/source/*.csv")
jsonfiles=glob.glob("c:/Users/shali/Documents/Project/github-1/A Comprehensive ETL Workflow with Python for Data Engineers/source/*.json")
xmlfiles=glob.glob("c:/Users/shali/Documents/Project/github-1/A Comprehensive ETL Workflow with Python for Data Engineers/source/*.xml")

# Declare an empty list
df_list=[]

# Read all the csv files using pandas in loop and append it to the declared empty list df_list
for csv in csvfiles:
    df_csv=pd.read_csv(csv,delimiter=',')
    df_list.append(df_csv)

# Read all the json files using pandas in loop and append it to the list df_list
for json in jsonfiles:
    df_json=pd.read_json(json, lines = True)
    df_list.append(df_json)

# Read all the xml files using pandas in loop and append it to the list df_list
# For parsing the xml, get all the values by using a for loop and append it to the empty data string declared
for xml in xmlfiles:
    tree=ET.parse(xml)
    root=tree.getroot()
    xmldata=[]
    for person in root.findall("person"):
        name = person.find("name").text
        height = person.find("height").text
        weight = person.find("weight").text
        xmldata.append({"name" : name, "height" : height, "weight" : weight})
    df_xml=pd.DataFrame(xmldata)
    df_list.append(df_xml)

# Concatenate all the records to data frame
final_df = pd.concat(df_list, ignore_index=True)

# Capturing the end time for the Extraction phase ending
end_time = datetime.now()

#Calculate the elapsed time for the Extraction phase and log it
elapsed_time = end_time - start_time
logging.info(f"Extraction Phase completed in {elapsed_time}")

# Capturing info for the Transformation phase starting
logging.info("Transformation phase started")

# Capturing the start time for the Transformation phase starting
start_time = datetime.now()

# Convert the height and weight to numeric data type
final_df['height'] = pd.to_numeric(final_df['height'],errors='coerce')
final_df['weight'] = pd.to_numeric(final_df['weight'],errors='coerce')

# Convert the height from inches to meters and weight from pounds to kilograms
final_df['height'] = final_df['height'] * .0254
final_df['weight'] = final_df['weight'] * 0.45359237

# Capturing the end time for the Transformation phase ending
end_time = datetime.now()

#Calculate the elapsed time for the Transformation phase and log it
elapsed_time = end_time - start_time
logging.info(f"Transformation Phase completed in {elapsed_time}")


# Capturing info for the Loading phase starting
logging.info("Loading phase started")

# Capturing the start time for the Loading phase starting
start_time = datetime.now()

# Creating a csv file (transformed_data.csv) of the transformed data
final_df.to_csv("c:/Users/shali/Documents/Project/github-1/A Comprehensive ETL Workflow with Python for Data Engineers/code/transformed_data.csv",index=False)

# Capturing the end time for the Transformation phase ending
end_time = datetime.now()

#Calculate the elapsed time for the Transformation phase and log it
elapsed_time = end_time - start_time
logging.info(f"Loading Phase completed in {elapsed_time}")