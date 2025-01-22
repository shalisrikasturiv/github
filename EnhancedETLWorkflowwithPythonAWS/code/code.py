import boto3  # AWS SDK for python
from botocore.exceptions import NoCredentialsError,PartialCredentialsError,ClientError  # for boto3 exceptions
import os  # import os for interacting with operating system
import logging  # to enable logging to log file
from datetime import datetime  # capturing current time
import time  # capturing current time
import pandas as pd  # for handling data using data frame
import xml.etree.ElementTree as ET  # parsing xml
import glob  # for identifying the files with same pattern
from sqlalchemy import create_engine  # establish connection to MySQL DB and to execute queries
import pymysql  # to interact with MySQL DB
from io import StringIO  # in-memory file-like object for reading from S3

#*********************************************************************************************************************************#


#Enable logging to log_file.txt
logging.basicConfig(filename='C:/Users/shali/Documents/Project/github/EnhancedETLWorkflowwithPythonAWS/logfiles/log_file.txt', level=logging.INFO,filemode='w',format='%(asctime)s - %(levelname)s - %(message)s')


logging.info("AWS Session has been setup successfully")

# Declare the region and bucket name
region='ap-south-1'
bucket_name='shalisrikasturiv-etl-project-bucket'
source_folder_name = 'source_files/'
transformed_folder_name = 'transform_files/'
log_folder_name = 'log_files/'
local_download_folder = 'C:/Users/shali/Documents/Project/github/EnhancedETLWorkflowwithPythonAWS/processfiles'
local_source_folder = 'C:/Users/shali/Documents/Project/github/EnhancedETLWorkflowwithPythonAWS/sourcefiles'
local_transform_folder = 'C:/Users/shali/Documents/Project/github/EnhancedETLWorkflowwithPythonAWS/transformfiles'
local_log_folder = 'C:/Users/shali/Documents/Project/github/EnhancedETLWorkflowwithPythonAWS/logfiles'

logging.info(f"Region is : {region}")
logging.info(f"Bucket Name is : {bucket_name}")
logging.info(f"Source Folder Name is : {source_folder_name}")
logging.info(f"Transform Folder Name is : {transformed_folder_name}")
logging.info(f"Local Source Folder Name is : {local_source_folder}")
logging.info(f"Local Download Folder Name is : {local_download_folder}")
logging.info(f"Local Transform Folder Name is : {local_transform_folder}")

# Connect to S3 in the mentioned region
s3=boto3.client('s3',region_name=region)

# Create a function to create mentioned bucket in the given region
def create_bucket(bucket_name, region):
    try:
        s3.create_bucket(Bucket=bucket_name,
                         CreateBucketConfiguration={'LocationConstraint' : region})
        return logging.info(f"Bucket '{bucket_name}' created successfully in region '{region}'")
    except NoCredentialsError:
        return logging.info("AWS Credentials not found")
    except PartialCredentialsError:
        return logging.info("Incomplete AWS Credentials")
    except Exception as e:
        return e

# Create a function to check if the bucket name already exists
def check_bucket_exists(bucket_name):
    try:
        s3.head_bucket(Bucket=bucket_name)
        return True
    except ClientError:
        return False

# If the bucket already exists, then skip the step else create the bucket
if check_bucket_exists(bucket_name):
    logging.info(f"The bucket '{bucket_name}' already exists.")
else:
    bucket_created = create_bucket(bucket_name,region)


# Create a function to create a new S3 folder in the bucket
def create_s3_folder(bucket_name,folder_name):
    try:
        s3.put_object(Bucket = bucket_name, Key = folder_name)
        return logging.info(f"Folder '{folder_name}' created successfully in '{bucket_name}' bucket")
    except ClientError as e:
        return e

# Create a function to check if the s3 folder is already present in the bucket
def check_s3_folder(bucket_name, folder_name):
    try:
        s3.get_object(Bucket = bucket_name, Key = folder_name)
        return True
    except ClientError:
        return False

# If the folder in the s3 bucket is already present, then skip the step else create the folder
if check_s3_folder(bucket_name,source_folder_name):
    logging.info(f"The folder '{source_folder_name}' alredy exists in '{bucket_name}' bucket")
else:
    folder_created = create_s3_folder(bucket_name,source_folder_name)


# Create a function to upload files from a folder to the S3 bucket folder
def upload_files_to_s3 (local_directory, bucket_name, folder_name):
    for root, dirs, files in os.walk(local_directory):
        for file_name in files:
            local_file_path=os.path.join(root,file_name)
            relative_path=os.path.relpath(local_file_path,local_directory)
            s3_file_path=os.path.join(folder_name,relative_path)
            try:
                logging.info(f"Uploading {local_file_path} to s3://{bucket_name}/{s3_file_path}")
                s3.upload_file(local_file_path, bucket_name, s3_file_path)
                logging.info(f"Successfully uploaded {file_name}")
            except Exception as e:
                logging.info(f"Failed to upload file {file_name}. Error : {e}")

# Call the function to upload the files from the local source folder to the source files folder in the S3 bucket
uploaded_files = upload_files_to_s3(local_source_folder,bucket_name,source_folder_name)


# Create a function to download files from S3 bucket folder
def download_files_from_s3 (bucket_name, source_folder_name, local_download_folder):
    os.makedirs(local_download_folder, exist_ok=True)
    response = s3.list_objects_v2 (Bucket = bucket_name, Prefix = source_folder_name)
    if 'Contents' in response:
        for object in response['Contents']:
            file_key = object['Key']
            if file_key.endswith('/'):
                continue
            local_file_path = os.path.join(local_download_folder,file_key[len(source_folder_name):])
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
            s3.download_file(bucket_name,file_key,local_file_path)
            logging.info(f"Downloaded {file_key} to {local_file_path}")
    else:
        logging.info("No files found in the specified S3 folder")

# Call the function to download the files from the source files folder in S3 bucket
downloaded_files = download_files_from_s3 (bucket_name, source_folder_name, local_download_folder)

#*********************************************************************************************************************************#

# Start the ETL Transformation

# Capturing info for the Extraction phase starting
logging.info("Extraction phase started")
# Capturing the start time for the Extraction phase starting
start_time = datetime.now()

# Identify all the csv, json and xml files in the folder
csvfiles=glob.glob(f"{local_download_folder}/*.csv")
jsonfiles=glob.glob(f"{local_download_folder}/*.json")
xmlfiles=glob.glob(f"{local_download_folder}/*.xml")


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

# Check if the local transform folder is present or not, if not present create the folder
os.makedirs(local_transform_folder, exist_ok=True)

# Creating a csv file (transformed_data.csv) of the transformed data
final_df.to_csv(f"{local_transform_folder}/transformed_data.csv",index=False)

# Capturing the end time for the Transformation phase ending
end_time = datetime.now()

# Calculate the elapsed time for the Transformation phase and log it
elapsed_time = end_time - start_time
logging.info(f"Loading Phase completed in {elapsed_time}")

# Create a new transform files folder in the bucket. Check if the folder already exists, else create the folder.
check_s3_folder(bucket_name, transformed_folder_name)

# If the folder in the s3 bucket is already present, then skip the step else create the folder
if check_s3_folder(bucket_name,transformed_folder_name):
    logging.info(f"The folder '{transformed_folder_name}' alredy exists in '{bucket_name}' bucket")
else:
    folder_created = create_s3_folder(bucket_name,transformed_folder_name)

# Upload the transformed file to the transform files folder.
upload_files_to_s3(local_transform_folder,bucket_name,transformed_folder_name)

#*********************************************************************************************************************************#

# Create a new RDS database instance in AWS
# From MySQL Workbench (local machine), give the RDS endpoint, username and password to connect to it
# For this, need to configure the security groups -> create an inbound rules to allow IPV4 all traffic from all IPs

# Establish the rds client connection
rds=boto3.client('rds')
logging.info("Establised RDS connection successfully")

db_instance_identifier='mydbinstance'

# Define a function to check if the rds instance already exists
def check_rds_exists(db_instance_identifier):
    try:
        get_db_instances = rds.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)
        return True
    except:
        return False
    
# If it already exists, skip the step else create the connection
logging.info("Checking if the RDS instance already exists...")
if check_rds_exists(db_instance_identifier):
    logging.info(f"RDS Instance {db_instance_identifier} already exists")
else:
    logging.info("Creating RDS Instance")
    connection = rds.create_db_instance(
        DBName = 'mydatabase',
        DBInstanceIdentifier = 'mydbinstance',
        AllocatedStorage=20,           # Storage size in GB
        DBInstanceClass='db.t4g.micro', # Instance class (e.g., db.t2.micro for small instances)
        Engine='mysql',                # Database engine (e.g., 'mysql', 'postgres', etc.)
        MasterUsername='shalisrikasturiv',        # Master username
        MasterUserPassword='Chellamss123', # Master user password
        VpcSecurityGroupIds=['sg-0a48be2d27820c95d'],  # Security group ID (make sure it's the right one)
        MultiAZ=False,                 # Multi-AZ deployment (set to True for high availability)
        PubliclyAccessible=True,      # Whether the DB instance is publicly accessible
        EngineVersion='8.0')
    logging.info("Waiting for 3 min to create the RDS instance")
    time.sleep(300)

# Get the Endpoint, port from the rds instance
response = rds.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)
db_instance = response['DBInstances'][0]
endpoint = db_instance['Endpoint']['Address']
port = db_instance['Endpoint']['Port']
user = 'shalisrikasturiv'
password = 'Chellamss123'
db = 'mydatabase'

# Get the transformed file name from the transform files folder in S3 bucket
list_transformed_file = s3.list_objects_v2 (Bucket = bucket_name, Prefix = transformed_folder_name)
if 'Contents' in list_transformed_file:
    transformed_file_name = list_transformed_file['Contents'][1]['Key']
    logging.info(f"Transformed file name is {transformed_file_name}")
get_transformed_file = s3.get_object(Bucket=bucket_name, Key=transformed_file_name)

# Read the transformed file
transformed_data = get_transformed_file['Body'].read().decode('utf-8')

# Convert the transformed file to data frame by reading it
df = pd.read_csv(StringIO(transformed_data))
df_row_count = df.shape[0]
logging.info(f"{df_row_count} records are present in {transformed_file_name} file")
engine = pymysql.connect(host=endpoint,
                               user=user,
                               password=password,
                               database=db,
                               port=port)
logging.info("RDS MySQL connection establised successfully")

# Create the DDL for the table to be created, execute and commit it
table_name = "Height_Weight"
CreateDDL = f'''CREATE TABLE IF NOT EXISTS {table_name} (Name varchar(20), Height decimal(10,2), Weight decimal(10,2));'''
cursor=engine.cursor()
cursor.execute(CreateDDL)
engine.commit()
logging.info(f"Table {table_name} created successfully")

# Establish the connection to load the data to the to the table from the data frame and commit the insert
engine_connection = create_engine(f'mysql+pymysql://{user}:{password}@{endpoint}:{port}/{db}')
df.to_sql('Height_Weight', con=engine_connection, index=False, if_exists='replace')
engine.commit()

# Check the count in the table loaded
check_count_in_table = f'''Select count(*) from {db}.{table_name}'''
cursor.execute(check_count_in_table)
table_row_count = cursor.fetchone()[0]
logging.info(f"{table_row_count} records loaded to {table_name} table")

# Check if the df count and the table count is matching or not
if df_row_count==table_row_count:
    logging.info("Record count matched between transformed file and table record count")
else:
    logging.info("Record count is not matched between transformed file and table record count")

# Create a log folder in the S3 bucket
check_s3_folder(bucket_name, log_folder_name)

# If the log folder in the s3 bucket is already present, then skip the step else create the folder
if check_s3_folder(bucket_name,log_folder_name):
    logging.info(f"The folder '{log_folder_name}' alredy exists in '{bucket_name}' bucket")
else:
    folder_created = create_s3_folder(bucket_name,log_folder_name)

# Upload the log file to the transform files folder.
upload_files_to_s3(local_log_folder,bucket_name,log_folder_name)