# Import pandas and numpy
import pandas as pd
import numpy as np

# Read the csv file
df=pd.read_csv('C:/Users/shali/Documents/Project/github/Code/census_2011.csv',delimiter=',',header=None,skiprows=1)

# Task 1: Rename the Column names
# For uniformity in the datasets and taking into consideration the census year, we need to rename some columns

# Read the columns renamed
df.columns=['District_code','State_UT','District','Population','Male','Female','Literate','Literate_Male','Literate_Female','SC','SC_Male','SC_Female','ST','ST_Male','ST_Female','Workers','Workers_Male','Workers_Female','Workers_Main','Workers_Marginal','Workers_Non','Workers_Cultivator','Workers_Agricultural','Workers_Household','Workers_Other','Hindus','Muslims','Christians','Sikhs','Buddhists','Jains','Others_Religions','Religion_Not_Stated','LPG_or_PNG_Households','Housholds_with_Electric_Lighting','Households_with_Internet','Households_with_Computer','Households_Rural','Households_Urban','Households','Education_Below_Primary','Education_Primary','Education_Middle','Education_Secondary_','Education_Higher','Education_Graduate','Education_Other','Education_Literate','Education_Illiterate','Education_Total','Young_and_Adult','Middle_Aged','Senior_Citizen','Age_Not_Stated','Households_with_Bicycle','Households_with_Car_Jeep_Van','Households_with_Radio_Transistor','Households_with_Scooter_Motorcycle_Moped','Households_with_Telephone_Mobile_Phone_Landline_only','Households_with_Telephone_Mobile_Phone_Mobile_only','Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car','Households_with_Television','Households_with_Telephone_Mobile_Phone','Households_with_Telephone_Mobile_Phone_Both','Condition_of_occupied_census_houses_Dilapidated_Households','Households_with_separate_kitchen_Cooking_inside_house','Having_bathing_facility_Total_Households','Having_latrine_facility_within_the_premises_Total_Households','Ownership_Owned_Households','Ownership_Rented_Households','Type_of_bathing_facility_Enclosure_without_roof_Households','Type_of_fuel_used_for_cooking_Any_other_Households','Type_of_latrine_facility_Pit_latrine_Households','Type_of_latrine_facility_Other_latrine_Households','Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households','Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households','Not_having_bathing_facility_within_the_premises_Total_Households','Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households','Main_source_of_drinking_water_Un_covered_well_Households','Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households','Main_source_of_drinking_water_Spring_Households','Main_source_of_drinking_water_River_Canal_Households','Main_source_of_drinking_water_Other_sources_Households','Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households','Location_of_drinking_water_source_Near_the_premises_Households','Location_of_drinking_water_source_Within_the_premises_Households','Main_source_of_drinking_water_Tank_Pond_Lake_Households','Main_source_of_drinking_water_Tapwater_Households','Main_source_of_drinking_water_Tubewell_Borehole_Households','Household_size_1_person_Households','Household_size_2_persons_Households','Household_size_1_to_2_persons','Household_size_3_persons_Households','Household_size_3_to_5_persons_Households','Household_size_4_persons_Households','Household_size_5_persons_Households','Household_size_6_8_persons_Households','Household_size_9_persons_and_above_Households','Location_of_drinking_water_source_Away_Households','Married_couples_1_Households','Married_couples_2_Households','Married_couples_3_Households','Married_couples_3_or_more_Households','Married_couples_4_Households','Married_couples_5__Households','Married_couples_None_Households','Power_Parity_Less_than_Rs_45000','Power_Parity_Rs_45000_90000','Power_Parity_Rs_90000_150000','Power_Parity_Rs_45000_150000','Power_Parity_Rs_150000_240000','Power_Parity_Rs_240000_330000','Power_Parity_Rs_150000_330000','Power_Parity_Rs_330000_425000','Power_Parity_Rs_425000_545000','Power_Parity_Rs_330000_545000','Power_Parity_Above_Rs_545000','Total_Power_Parity']
print("Task 1 (Rename the column names) completed successfully!")


# Task 2: Rename State/UT Names
# The State/UT names are in all caps in the census data, For uniformity across datasets we use the names so that only the first character of each word in the name is in upper case and the rest are in lower case. However, if the word is “and” then it should be all lowercase.if you found & symbol replace it with ‘and

# Convert the Rename State/UT Names
df['State_UT'] =df['State_UT'].apply(lambda x : ' '.join([i.capitalize() if i.lower()!='and' else i.lower() for i in x.split(' ')]))
print("Task 2 (Rename the State/UT names) completed successfully!")

# Task 3: New State/UT formation In 2014 Telangana was formed after it split from Andhra Pradesh, The districts that were included in Telangana are stored in Data/Telangana.txt . Read the text file and Rename the State/UT From “Andhra Pradesh” to “Telangana” for the given districts.
# In 2019 Ladakh was formed after it split from Jammu and Kashmir, which included the districts Leh and Kargil. Rename the State/UT From “Jammu and Kashmir” to “Ladakh” for the given district

# Copy the given Telangana disctricts to a txt file and read it
df_telangana=pd.read_csv('C:/Users/shali/Documents/Project/github/Code/Telangana.txt',header=None)

# Assign the column name
df_telangana.columns=['District']

# Convert the State_UT for the districts in the Telangana txt file
df.loc[df['District'].isin(df_telangana['District']),'State_UT']='Telangana'
print("Rename State/UT the From “Andhra Pradesh” to “Telangana” completed successfully!")


# Copy the given Ladakh disctricts to a txt file and read it
df_Ladakh=pd.read_csv('C:/Users/shali/Documents/Project/github/Code/Leh(Ladakh).txt',header=None)

# Assign the column name
df_Ladakh.columns=['District']

# Convert the State_UT for the districts in the Ladakh txt file
df.loc[df['District'].isin (df_Ladakh['District']),'State_UT']='Ladakh'
print("Rename State/UT the From “Jammu and Kashmir” to “Ladakh” completed successfully!")

print("Task 3 (Rename the State/UT From “Jammu and Kashmir” to “Ladakh”, From “Andhra Pradesh” to “Telangana”) completed successfully!")


# Task 4: Find and store the percentage of data missing for the columns.
# Some data can be found and filled in by using information from other cells. Try to find the correct data by using information from other cells and fillinggit in. Find and store the percentage of data missing for each column.
# Hint:
# Population = Male + Female
# Literate = Literate_Male + Literate_Female
# Population  = Young_and_Adult+  Middle_Aged + Senior_Citizen + Age_Not_Stated
# Households = Households_Rural + Households_Urban _
# compares the amount of missing data before and after the data-filling process was done

# Convert the calculated percentage of null values before cleaning to a data frame
before_cleaning=pd.DataFrame(df.isnull().mean()*100)

# Reset the index of the before cleaning df
before_cleaning.reset_index(inplace=True)

# Assign the column names to the df of getting the mean before cleaning
before_cleaning.columns=['column_name','before_cleaning']

# Create a csv file of the before cleaning values
before_cleaning.to_csv('Before Cleaning Percentage.csv',index='False')

print("Percentage of na values before cleaning was saved to Before Cleaning Percentage.csv")

# Create a plot of the the calculated percentage of na values before cleaning
import matplotlib.pyplot as plt
import numpy as np

y = before_cleaning
mylabels = ["before_cleaning"]
plt.pie(y["before_cleaning"]) 
plt.show() 

print("Plot for the percentage of na values before cleaning has been created!")

# Find the percentage of na values before handling them
df_district_code=df['District_code'].isnull().mean()*100
df_State_UT=df['State_UT'].isnull().mean()*100
df_District=df['District'].isnull().mean()*100

# Find the percentage of na values before handling them in Population
df_Population_before=df['Population'].isnull().mean()*100
df_male_before=df['Male'].isna().mean()*100
df_female_before=df['Female'].isna().mean()*100

# Update the na values in Population
df['Population']=df['Population'].fillna(df['Male']+df['Female'])
df['Male']=df['Male'].fillna(df['Population']-df['Female'])
df['Female']=df['Female'].fillna(df['Population']-df['Male'])

# Find the percentage of na values before handling them in Literate
df_literate_before=df['Literate'].isna().mean()*100
df_literate_male_before=df['Literate_Male'].isna().mean()*100
df_literate_female_before=df['Literate_Female'].isna().mean()*100

# Update the na values in Literate
df['Literate']=df['Literate'].fillna(df['Literate_Male']+df['Literate_Female'])
df['Literate_Male']=df['Literate_Male'].fillna(df['Literate']-df['Literate_Female'])
df['Literate_Female']=df['Literate_Female'].fillna(df['Literate']-df['Literate_Male'])

# Fill na values of Literate_Female, Literate_Male with 0 and update them respectively
df['Literate_Female']=df['Literate_Female'].fillna(0)
df['Literate_Male']=df['Literate_Male'].fillna(df['Literate']-df['Literate_Female'])
df['Literate']=df['Literate'].fillna(df['Literate_Male']+df['Literate_Female'])
df['Literate_Male']=df['Literate_Male'].fillna(0)
df['Literate_Female']=df['Literate_Female'].fillna(df['Literate']-df['Literate_Male'])
df['Literate']=df['Literate'].fillna(df['Literate_Male']+df['Literate_Female'])

# Find the percentage of na values after handling them in Literate
df_literate_after=df['Literate'].isna().mean()*100
df_literate_male_after=df['Literate_Male'].isna().mean()*100
df_literate_female_after=df['Literate_Female'].isna().mean()*100

# Find the percentage of na values before handling them in SC
df_SC_before=df['SC'].isna().mean()*100
df_SC_male_before=df['SC_Male'].isna().mean()*100
df_SC_female_before=df['SC_Female'].isna().mean()*100

# Update the na values in SC
df['SC']=df['SC'].fillna(df['SC_Male']+df['SC_Female'])
df['SC_Male']=df['SC_Male'].fillna(df['SC']-df['SC_Female'])
df['SC_Female']=df['SC_Female'].fillna(df['SC']-df['SC_Male'])

df['SC_Male']=df['SC_Male'].fillna(0)
df['SC_Female']=df['SC_Female'].fillna(df['SC']-df['SC_Male'])
df['SC_Female']=df['SC_Female'].fillna(0)
df['SC']=df['SC'].fillna(df['SC_Male']+df['SC_Female'])

# Find the percentage of na values after handling them in SC
df_SC_after=df['SC'].isna().mean()*100
df_SC_male_after=df['SC_Male'].isna().mean()*100
df_SC_female_after=df['SC_Female'].isna().mean()*100

# Find the percentage of na values before handling them in ST
df_ST_before=df['ST'].isna().mean()*100
df_ST_male_before=df['ST_Male'].isna().mean()*100
df_ST_female_before=df['ST_Female'].isna().mean()*100

# Update the na values in ST
df['ST']=df['ST'].fillna(df['ST_Male']+df['ST_Female'])
df['ST_Male']=df['ST_Male'].fillna(df['ST']-df['ST_Female'])
df['ST_Female']=df['ST_Female'].fillna(df['ST']-df['ST_Male'])

df['ST_Male']=df['ST_Male'].fillna(0)
df['ST_Female']=df['ST_Female'].fillna(0)
df['ST']=df['ST'].fillna(df['ST_Male']+df['ST_Female'])

# Find the percentage of na values after handling them in ST
df_ST_after=df['ST'].isna().mean()*100
df_ST_male_after=df['ST_Male'].isna().mean()*100
df_ST_female_after=df['ST_Female'].isna().mean()*100

# Find the percentage of na values before handling them in Workers
df_Workers_before=df['Workers'].isna().mean()*100
df_Workers_Male_before=df['Workers_Male'].isna().mean()*100
df_Workers_Female_before=df['Workers_Female'].isna().mean()*100
df_Workers_Main_before=df['Workers_Main'].isna().mean()*100
df_Workers_Marginal_before=df['Workers_Marginal'].isna().mean()*100
df_Workers_Non_before=df['Workers_Non'].isna().mean()*100
df_Workers_Cultivator_before=df['Workers_Cultivator'].isna().mean()*100
df_Workers_Agricultural_before=df['Workers_Agricultural'].isna().mean()*100
df_Workers_Household_before=df['Workers_Household'].isna().mean()*100
df_Workers_Other_before=df['Workers_Other'].isna().mean()*100

# Update the na values with the logic of workers is the sum of male and female, and sum of workers and non workers add up to the population
df['Workers']=df['Workers'].fillna(df['Workers_Male']+df['Workers_Female'])
df['Workers_Male']=df['Workers_Male'].fillna(df['Workers']-df['Workers_Female'])
df['Workers_Female']=df['Workers_Female'].fillna(df['Workers']-df['Workers_Male'])
df['Workers_Non']=df['Workers_Non'].fillna(df['Population']-df['Workers'])

# Update the na values with the logic of sum of the other workers columns matches 2 times the count of workers
df['Workers_Main']=df['Workers_Main'].fillna((2*df['Workers'])-(df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Agricultural']+df['Workers_Household']+df['Workers_Other']))
df['Workers_Marginal']=df['Workers_Marginal'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Cultivator']+df['Workers_Agricultural']+df['Workers_Household']+df['Workers_Other']))
df['Workers_Cultivator']=df['Workers_Cultivator'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Agricultural']+df['Workers_Household']+df['Workers_Other']))
df['Workers_Agricultural']=df['Workers_Agricultural'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Household']+df['Workers_Other']))
df['Workers_Household']=df['Workers_Household'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Agricultural']+df['Workers_Other']))
df['Workers_Other']=df['Workers_Other'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Agricultural']+df['Workers_Household']))

# Fill the Workers_Main with 0 and update the remaining field na values with the same logic above
df['Workers_Main']=df['Workers_Main'].fillna(0)
df['Workers_Marginal']=df['Workers_Marginal'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Cultivator']+df['Workers_Agricultural']+df['Workers_Household']+df['Workers_Other']))
df['Workers_Cultivator']=df['Workers_Cultivator'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Agricultural']+df['Workers_Household']+df['Workers_Other']))
df['Workers_Agricultural']=df['Workers_Agricultural'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Household']+df['Workers_Other']))
df['Workers_Household']=df['Workers_Household'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Agricultural']+df['Workers_Other']))
df['Workers_Other']=df['Workers_Other'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Agricultural']+df['Workers_Household']))

# Fill the Workers_Marginal with 0 and update the remaining field na values with the same logic above
df['Workers_Marginal']=df['Workers_Marginal'].fillna(0)
df['Workers_Cultivator']=df['Workers_Cultivator'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Agricultural']+df['Workers_Household']+df['Workers_Other']))
df['Workers_Agricultural']=df['Workers_Agricultural'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Household']+df['Workers_Other']))
df['Workers_Household']=df['Workers_Household'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Agricultural']+df['Workers_Other']))
df['Workers_Other']=df['Workers_Other'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Agricultural']+df['Workers_Household']))

# Fill the Workers_Cultivator with 0 and update the remaining field na values with the same logic above
df['Workers_Cultivator']=df['Workers_Cultivator'].fillna(0)
df['Workers_Agricultural']=df['Workers_Agricultural'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Household']+df['Workers_Other']))
df['Workers_Household']=df['Workers_Household'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Agricultural']+df['Workers_Other']))
df['Workers_Other']=df['Workers_Other'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Agricultural']+df['Workers_Household']))

# Fill the Workers_Marginal with 0 and update the remaining field na values with the same logic above
df['Workers_Agricultural']=df['Workers_Agricultural'].fillna(0)
df['Workers_Household']=df['Workers_Household'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Agricultural']+df['Workers_Other']))
df['Workers_Other']=df['Workers_Other'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Agricultural']+df['Workers_Household']))

# Fill the Workers_Marginal with 0 and update the remaining field na values with the same logic above
df['Workers_Household']=df['Workers_Household'].fillna(0)
df['Workers_Other']=df['Workers_Other'].fillna((2*df['Workers'])-(df['Workers_Main']+df['Workers_Marginal']+df['Workers_Cultivator']+df['Workers_Agricultural']+df['Workers_Household']))


df_Workers_after=df['Workers'].isna().mean()*100
df_Workers_Male_after=df['Workers_Male'].isna().mean()*100
df_Workers_Female_after=df['Workers_Female'].isna().mean()*100
df_Workers_Main_after=df['Workers_Main'].isna().mean()*100
df_Workers_Marginal_after=df['Workers_Marginal'].isna().mean()*100
df_Workers_Non_after=df['Workers_Non'].isna().mean()*100
df_Workers_Cultivator_after=df['Workers_Cultivator'].isna().mean()*100
df_Workers_Agricultural_after=df['Workers_Agricultural'].isna().mean()*100
df_Workers_Household_after=df['Workers_Household'].isna().mean()*100
df_Workers_Other_after=df['Workers_Other'].isna().mean()*100

# Find the percentage of na values before handling them in Religions
df_Hindus_before=df['Hindus'].isna().mean()*100
df_Muslims_before=df['Muslims'].isna().mean()*100
df_Christians_before=df['Christians'].isna().mean()*100
df_Sikhs_before=df['Sikhs'].isna().mean()*100
df_Buddhists_before=df['Buddhists'].isna().mean()*100
df_Jains_before=df['Jains'].isna().mean()*100
df_Others_Religions_before=df['Others_Religions'].isna().mean()*100
df_Religion_Not_Stated_before=df['Religion_Not_Stated'].isna().mean()*100

# Calculate the na values of each religion by subtracting population from the sum other religions
df['Hindus']=df['Hindus'].fillna(df['Population']-(df['Muslims']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Muslims']=df['Muslims'].fillna(df['Population']-(df['Hindus']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Christians']=df['Christians'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Sikhs']=df['Sikhs'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Christians']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Buddhists']=df['Buddhists'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Christians']+df['Sikhs']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Jains']=df['Jains'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Others_Religions']=df['Others_Religions'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Religion_Not_Stated']))
df['Religion_Not_Stated']=df['Religion_Not_Stated'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']))

# Fill the na values of Religion_Not_Stated with 0 and calculate the na values of each religion by subtracting population from the sum other religions
df['Religion_Not_Stated']=df['Religion_Not_Stated'].fillna(0)
df['Hindus']=df['Hindus'].fillna(df['Population']-(df['Muslims']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Muslims']=df['Muslims'].fillna(df['Population']-(df['Hindus']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Christians']=df['Christians'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Sikhs']=df['Sikhs'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Christians']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Buddhists']=df['Buddhists'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Christians']+df['Sikhs']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Jains']=df['Jains'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Others_Religions']=df['Others_Religions'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Religion_Not_Stated']))

# Fill the na values of Others_Religions with 0 and calculate the na values of each religion by subtracting population from the sum other religions
df['Others_Religions']=df['Others_Religions'].fillna(0)
df['Hindus']=df['Hindus'].fillna(df['Population']-(df['Muslims']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Muslims']=df['Muslims'].fillna(df['Population']-(df['Hindus']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Christians']=df['Christians'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Sikhs']=df['Sikhs'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Christians']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Buddhists']=df['Buddhists'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Christians']+df['Sikhs']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Jains']=df['Jains'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Others_Religions']+df['Religion_Not_Stated']))

# Fill the na values of Jains with 0 and calculate the na values of each religion by subtracting population from the sum other religions
df['Jains']=df['Jains'].fillna(0)
df['Hindus']=df['Hindus'].fillna(df['Population']-(df['Muslims']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Muslims']=df['Muslims'].fillna(df['Population']-(df['Hindus']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Christians']=df['Christians'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Sikhs']=df['Sikhs'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Christians']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Buddhists']=df['Buddhists'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Christians']+df['Sikhs']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))

# Fill the na values of Buddhists with 0 and calculate the na values of each religion by subtracting population from the sum other religions
df['Buddhists']=df['Buddhists'].fillna(0)
df['Hindus']=df['Hindus'].fillna(df['Population']-(df['Muslims']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Muslims']=df['Muslims'].fillna(df['Population']-(df['Hindus']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Christians']=df['Christians'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Sikhs']=df['Sikhs'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Christians']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))

# Fill the na values of Sikhs with 0 and calculate the na values of each religion by subtracting population from the sum other religions
df['Sikhs']=df['Sikhs'].fillna(0)
df['Hindus']=df['Hindus'].fillna(df['Population']-(df['Muslims']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Muslims']=df['Muslims'].fillna(df['Population']-(df['Hindus']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Christians']=df['Christians'].fillna(df['Population']-(df['Hindus']+df['Muslims']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))

# Fill the na values of Christians with 0 and calculate the na values of each religion by subtracting population from the sum other religions
df['Christians']=df['Christians'].fillna(0)
df['Hindus']=df['Hindus'].fillna(df['Population']-(df['Muslims']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))
df['Muslims']=df['Muslims'].fillna(df['Population']-(df['Hindus']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))

# Fill the na values of Muslims with 0 and calculate the na values of each religion by subtracting population from the sum other religions
df['Muslims']=df['Muslims'].fillna(0)
df['Hindus']=df['Hindus'].fillna(df['Population']-(df['Muslims']+df['Christians']+df['Sikhs']+df['Buddhists']+df['Jains']+df['Others_Religions']+df['Religion_Not_Stated']))

# Find the percentage of na values after handling them in Religions
df_Hindus_after=df['Hindus'].isna().mean()*100
df_Muslims_after=df['Muslims'].isna().mean()*100
df_Christians_after=df['Christians'].isna().mean()*100
df_Sikhs_after=df['Sikhs'].isna().mean()*100
df_Buddhists_after=df['Buddhists'].isna().mean()*100
df_Jains_after=df['Jains'].isna().mean()*100
df_Others_Religions_after=df['Others_Religions'].isna().mean()*100
df_Religion_Not_Stated_after=df['Religion_Not_Stated'].isna().mean()*100

# Find the percentage of na values before handling them household rural urban
df_Households_Rural_before=df['Households_Rural'].isna().mean()*100
df_Households_Urban_before=df['Households_Urban'].isna().mean()*100
df_Households_before=df['Households'].isna().mean()*100

# Fill na values of Households, Households_Urban and Households_Rural
df['Households']=df['Households'].fillna(df['Households_Rural']+df['Households_Urban'])
df['Households_Rural']=df['Households_Rural'].fillna(df['Households']-df['Households_Urban'])
df['Households_Urban']=df['Households_Urban'].fillna(df['Households']-df['Households_Rural'])

# Fill na values of Households_Urban with 0 and update the Households_Rural and Households_Urban values
df['Households_Urban']=df['Households_Urban'].fillna(0)
df['Households']=df['Households'].fillna(df['Households_Rural']+df['Households_Urban'])
df['Households_Rural']=df['Households_Rural'].fillna(df['Households']-df['Households_Urban'])

# Fill na values of Households_Urban with 0 and update the Households_Rural and Households_Urban values
df['Households_Rural']=df['Households_Rural'].fillna(0)
df['Households']=df['Households'].fillna(df['Households_Rural']+df['Households_Urban'])

# Find the percentage of na values after handling them household rural urban
df_Households_Rural_after=df['Households_Rural'].isna().mean()*100
df_Households_Urban_after=df['Households_Urban'].isna().mean()*100
df_Households_after=df['Households'].isna().mean()*100

# Find the percentage of na values before handling them in household
df_LPG_or_PNG_Households_before=df['LPG_or_PNG_Households'].isna().mean()*100
df_Housholds_with_Electric_Lighting_before=df['Housholds_with_Electric_Lighting'].isna().mean()*100
df_Households_with_Internet_before=df['Households_with_Internet'].isna().mean()*100
df_Households_with_Computer_before=df['Households_with_Computer'].isna().mean()*100

# Fill na values with mean of the columns in household
df['LPG_or_PNG_Households']=df['LPG_or_PNG_Households'].fillna(df['LPG_or_PNG_Households'].mean())
df['Housholds_with_Electric_Lighting']=df['Housholds_with_Electric_Lighting'].fillna(df['Housholds_with_Electric_Lighting'].mean())
df['Households_with_Internet']=df['Households_with_Internet'].fillna(df['Households_with_Internet'].mean())
df['Households_with_Computer']=df['Households_with_Computer'].fillna(df['Households_with_Computer'].mean())

# Find the percentage of na values after handling them in household
df_LPG_or_PNG_Households_after=df['LPG_or_PNG_Households'].isna().mean()*100
df_Housholds_with_Electric_Lighting_after=df['Housholds_with_Electric_Lighting'].isna().mean()*100
df_Households_with_Internet_after=df['Households_with_Internet'].isna().mean()*100
df_Households_with_Computer_after=df['Households_with_Computer'].isna().mean()*100

# Find the percentage of na values before handling them in Education
df_Education_Below_Primary_before=df['Education_Below_Primary'].isna().mean()*100
df_Education_Primary_before=df['Education_Primary'].isna().mean()*100
df_Education_Middle_before=df['Education_Middle'].isna().mean()*100
df_Education_Secondary_before=df['Education_Secondary_'].isna().mean()*100
df_Education_Higher_before=df['Education_Higher'].isna().mean()*100
df_Education_Graduate_before=df['Education_Graduate'].isna().mean()*100
df_Education_Other_before=df['Education_Other'].isna().mean()*100
df_Education_Literate_before=df['Education_Literate'].isna().mean()*100
df_Education_Illiterate_before=df['Education_Illiterate'].isna().mean()*100
df_Education_Total_before=df['Education_Total'].isna().mean()*100

# Calculate the remaining education values

# Fill Education_Illiterate with 0 and update other fields in education
df['Education_Illiterate']=df['Education_Illiterate'].fillna(0)
df['Education_Total']=df['Education_Total'].fillna(df['Education_Literate']+df['Education_Illiterate'])
df['Education_Literate']=df['Education_Literate'].fillna(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other'])
df['Education_Illiterate']=df['Education_Illiterate'].fillna(df['Education_Total']-df['Education_Literate'])
df['Education_Literate']=df['Education_Literate'].fillna(df['Education_Total']-df['Education_Illiterate'])
df['Education_Total']=df['Education_Total'].fillna(df['Education_Literate']+df['Education_Illiterate'])
df['Education_Below_Primary']=df['Education_Below_Primary'].fillna(df['Education_Literate']-(df['Education_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Primary']=df['Education_Primary'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Middle']=df['Education_Middle'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Secondary_']=df['Education_Secondary_'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Middle']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Higher']=df['Education_Higher'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Graduate']+df['Education_Other']))
df['Education_Graduate']=df['Education_Graduate'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Other']))
df['Education_Other']=df['Education_Other'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']))

# Fill Education_Other with 0 and update other fields in education
df['Education_Other']=df['Education_Other'].fillna(0)
df['Education_Below_Primary']=df['Education_Below_Primary'].fillna(df['Education_Literate']-(df['Education_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Primary']=df['Education_Primary'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Middle']=df['Education_Middle'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Secondary_']=df['Education_Secondary_'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Middle']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Higher']=df['Education_Higher'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Graduate']+df['Education_Other']))
df['Education_Graduate']=df['Education_Graduate'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Other']))

# Fill Education_Graduate with 0 and update other fields in education
df['Education_Graduate']=df['Education_Graduate'].fillna(0)
df['Education_Below_Primary']=df['Education_Below_Primary'].fillna(df['Education_Literate']-(df['Education_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Primary']=df['Education_Primary'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Middle']=df['Education_Middle'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Secondary_']=df['Education_Secondary_'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Middle']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Higher']=df['Education_Higher'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Graduate']+df['Education_Other']))

# Fill Education_Higher with 0 and update other fields in education
df['Education_Higher']=df['Education_Higher'].fillna(0)
df['Education_Below_Primary']=df['Education_Below_Primary'].fillna(df['Education_Literate']-(df['Education_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Primary']=df['Education_Primary'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Middle']=df['Education_Middle'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Secondary_']=df['Education_Secondary_'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Middle']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))

# Fill Education_Secondary_ with 0 and update other fields in education
df['Education_Secondary_']=df['Education_Secondary_'].fillna(0)
df['Education_Below_Primary']=df['Education_Below_Primary'].fillna(df['Education_Literate']-(df['Education_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Primary']=df['Education_Primary'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Middle']=df['Education_Middle'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Primary']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))

# Fill Education_Middle with 0 and update other fields in education
df['Education_Middle']=df['Education_Middle'].fillna(0)
df['Education_Below_Primary']=df['Education_Below_Primary'].fillna(df['Education_Literate']-(df['Education_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))
df['Education_Primary']=df['Education_Primary'].fillna(df['Education_Literate']-(df['Education_Below_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))

# Fill Education_Primary with 0 and update other fields in education
df['Education_Primary']=df['Education_Primary'].fillna(0)
df['Education_Below_Primary']=df['Education_Below_Primary'].fillna(df['Education_Literate']-(df['Education_Primary']+df['Education_Middle']+df['Education_Secondary_']+df['Education_Higher']+df['Education_Graduate']+df['Education_Other']))

# Fill Education_Illiterate with 0 and update other fields in education
df['Education_Illiterate']=df['Education_Illiterate'].fillna(0)
df['Education_Total']=df['Education_Total'].fillna(df['Education_Literate']+df['Education_Illiterate'])

# Find the percentage of na values after handling them in Education
df_Education_Below_Primary_after=df['Education_Below_Primary'].isna().mean()*100
df_Education_Primary_after=df['Education_Primary'].isna().mean()*100
df_Education_Middle_after=df['Education_Middle'].isna().mean()*100
df_Education_Secondary_after=df['Education_Secondary_'].isna().mean()*100
df_Education_Higher_after=df['Education_Higher'].isna().mean()*100
df_Education_Graduate_after=df['Education_Graduate'].isna().mean()*100
df_Education_Other_after=df['Education_Other'].isna().mean()*100
df_Education_Literate_after=df['Education_Literate'].isna().mean()*100
df_Education_Illiterate_after=df['Education_Illiterate'].isna().mean()*100
df_Education_Total_after=df['Education_Total'].isna().mean()*100

# Find the percentage of na values before handling them in Age
df_Young_and_Adult_before=df['Young_and_Adult'].isna().mean()*100
df_Middle_Aged_before=df['Middle_Aged'].isna().mean()*100
df_Senior_Citizen_before=df['Senior_Citizen'].isna().mean()*100
df_Age_Not_Stated_before=df['Age_Not_Stated'].isna().mean()*100

# Update the na values in Age by subtracting population from sum of other ages
df['Young_and_Adult']=df['Young_and_Adult'].fillna(df['Population']-(df['Middle_Aged']+df['Senior_Citizen']+df['Age_Not_Stated']))
df['Middle_Aged']=df['Middle_Aged'].fillna(df['Population']-(df['Young_and_Adult']+df['Senior_Citizen']+df['Age_Not_Stated']))
df['Senior_Citizen']=df['Senior_Citizen'].fillna(df['Population']-(df['Young_and_Adult']+df['Middle_Aged']+df['Age_Not_Stated']))
df['Age_Not_Stated']=df['Age_Not_Stated'].fillna(df['Population']-(df['Young_and_Adult']+df['Middle_Aged']+df['Senior_Citizen']))

# Fill na value of Young_and_Adult with 0 and update other field na values by subtracting population from sum of other ages
df['Young_and_Adult']=df['Young_and_Adult'].fillna(0)
df['Middle_Aged']=df['Middle_Aged'].fillna(df['Population']-(df['Young_and_Adult']+df['Senior_Citizen']+df['Age_Not_Stated']))
df['Senior_Citizen']=df['Senior_Citizen'].fillna(df['Population']-(df['Young_and_Adult']+df['Middle_Aged']+df['Age_Not_Stated']))
df['Age_Not_Stated']=df['Age_Not_Stated'].fillna(df['Population']-(df['Young_and_Adult']+df['Middle_Aged']+df['Senior_Citizen']))

# Fill na value of Age_Not_Stated with 0 and update other field na values by subtracting population from sum of other ages
df['Age_Not_Stated']=df['Age_Not_Stated'].fillna(0)
df['Middle_Aged']=df['Middle_Aged'].fillna(df['Population']-(df['Young_and_Adult']+df['Senior_Citizen']+df['Age_Not_Stated']))
df['Senior_Citizen']=df['Senior_Citizen'].fillna(df['Population']-(df['Young_and_Adult']+df['Middle_Aged']+df['Age_Not_Stated']))

# Fill na value of Senior_Citizen with 0 and update other field na values by subtracting population from sum of other ages
df['Senior_Citizen']=df['Senior_Citizen'].fillna(0)
df['Middle_Aged']=df['Middle_Aged'].fillna(df['Population']-(df['Young_and_Adult']+df['Senior_Citizen']+df['Age_Not_Stated']))

# Fill na value of Middle_Aged with 0 and update other field na values by subtracting population from sum of other ages
df['Middle_Aged']=df['Middle_Aged'].fillna(0)
df['Population']=df['Population'].fillna(df['Middle_Aged']+(df['Young_and_Adult']+df['Senior_Citizen']+df['Age_Not_Stated']))
df['Male']=df['Male'].fillna(df['Population']-df['Female'])

# Find the percentage of na values after handling them in Workers
df_Young_and_Adult_after=df['Young_and_Adult'].isna().mean()*100
df_Middle_Aged_after=df['Middle_Aged'].isna().mean()*100
df_Senior_Citizen_after=df['Senior_Citizen'].isna().mean()*100
df_Age_Not_Stated_after=df['Age_Not_Stated'].isna().mean()*100
df_Population_after=df['Population'].isna().mean()*100
df_male_after=df['Male'].isna().mean()*100
df_female_after=df['Female'].isna().mean()*100

# Find the percentage of na values before handling them in households, drinking water and latrine facility
df_Households_with_Bicycle_before=df['Households_with_Bicycle'].isna().mean()*100
df_Households_with_Car_Jeep_Van_before=df['Households_with_Car_Jeep_Van'].isna().mean()*100
df_Households_with_Radio_Transistor_before=df['Households_with_Radio_Transistor'].isna().mean()*100
df_Households_with_Scooter_Motorcycle_Moped_before=df['Households_with_Scooter_Motorcycle_Moped'].isna().mean()*100
df_Households_with_Telephone_Mobile_Phone_Landline_only_before=df['Households_with_Telephone_Mobile_Phone_Landline_only'].isna().mean()*100
df_Households_with_Telephone_Mobile_Phone_Mobile_only_before=df['Households_with_Telephone_Mobile_Phone_Mobile_only'].isna().mean()*100
df_Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car_before=df['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car'].isna().mean()*100
df_Households_with_Television_before=df['Households_with_Television'].isna().mean()*100
df_Households_with_Telephone_Mobile_Phone_before=df['Households_with_Telephone_Mobile_Phone'].isna().mean()*100
df_Households_with_Telephone_Mobile_Phone_Both_before=df['Households_with_Telephone_Mobile_Phone_Both'].isna().mean()*100
df_Condition_of_occupied_census_houses_Dilapidated_Households_before=df['Condition_of_occupied_census_houses_Dilapidated_Households'].isna().mean()*100
df_Households_with_separate_kitchen_Cooking_inside_house_before=df['Households_with_separate_kitchen_Cooking_inside_house'].isna().mean()*100
df_Having_bathing_facility_Total_Households_before=df['Having_bathing_facility_Total_Households'].isna().mean()*100
df_Having_latrine_facility_within_the_premises_Total_Households_before=df['Having_latrine_facility_within_the_premises_Total_Households'].isna().mean()*100
df_Ownership_Owned_Households_before=df['Ownership_Owned_Households'].isna().mean()*100
df_Ownership_Rented_Households_before=df['Ownership_Rented_Households'].isna().mean()*100
df_Type_of_bathing_facility_Enclosure_without_roof_Households_before=df['Type_of_bathing_facility_Enclosure_without_roof_Households'].isna().mean()*100
df_Type_of_fuel_used_for_cooking_Any_other_Households_before=df['Type_of_fuel_used_for_cooking_Any_other_Households'].isna().mean()*100
df_Type_of_latrine_facility_Pit_latrine_Households_before=df['Type_of_latrine_facility_Pit_latrine_Households'].isna().mean()*100
df_Type_of_latrine_facility_Other_latrine_Households_before=df['Type_of_latrine_facility_Other_latrine_Households'].isna().mean()*100
df_Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households_before=df['Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households'].isna().mean()*100
df_Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households_before=df['Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households'].isna().mean()*100
df_Not_having_bathing_facility_within_the_premises_Total_Households_before=df['Not_having_bathing_facility_within_the_premises_Total_Households'].isna().mean()*100
df_Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households_before=df['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Un_covered_well_Households_before=df['Main_source_of_drinking_water_Un_covered_well_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households_before=df['Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Spring_Households_before=df['Main_source_of_drinking_water_Spring_Households'].isna().mean()*100
df_Main_source_of_drinking_water_River_Canal_Households_before=df['Main_source_of_drinking_water_River_Canal_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Other_sources_Households_before=df['Main_source_of_drinking_water_Other_sources_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households_before=df['Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households'].isna().mean()*100
df_Location_of_drinking_water_source_Near_the_premises_Households_before=df['Location_of_drinking_water_source_Near_the_premises_Households'].isna().mean()*100
df_Location_of_drinking_water_source_Within_the_premises_Households_before=df['Location_of_drinking_water_source_Within_the_premises_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Tank_Pond_Lake_Households_before=df['Main_source_of_drinking_water_Tank_Pond_Lake_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Tapwater_Households_before=df['Main_source_of_drinking_water_Tapwater_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Tubewell_Borehole_Households_before=df['Main_source_of_drinking_water_Tubewell_Borehole_Households'].isna().mean()*100
df_Location_of_drinking_water_source_Away_Households_before=df['Location_of_drinking_water_source_Away_Households'].isna().mean()*100

# Update the na values of the fields with the mean of those fields
df['Households_with_Bicycle']=df['Households_with_Bicycle'].fillna(df['Households_with_Bicycle'].mean())
df['Households_with_Car_Jeep_Van']=df['Households_with_Car_Jeep_Van'].fillna(df['Households_with_Car_Jeep_Van'].mean())
df['Households_with_Radio_Transistor']=df['Households_with_Radio_Transistor'].fillna(df['Households_with_Radio_Transistor'].mean())
df['Households_with_Scooter_Motorcycle_Moped']=df['Households_with_Scooter_Motorcycle_Moped'].fillna(df['Households_with_Scooter_Motorcycle_Moped'].mean())
df['Households_with_Telephone_Mobile_Phone_Landline_only']=df['Households_with_Telephone_Mobile_Phone_Landline_only'].fillna(df['Households_with_Telephone_Mobile_Phone_Landline_only'].mean())
df['Households_with_Telephone_Mobile_Phone_Mobile_only']=df['Households_with_Telephone_Mobile_Phone_Mobile_only'].fillna(df['Households_with_Telephone_Mobile_Phone_Mobile_only'].mean())
df['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car']=df['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car'].fillna(df['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car'].mean())
df['Households_with_Television']=df['Households_with_Television'].fillna(df['Households_with_Television'].mean())
df['Households_with_Telephone_Mobile_Phone']=df['Households_with_Telephone_Mobile_Phone'].fillna(df['Households_with_Telephone_Mobile_Phone'].mean())
df['Households_with_Telephone_Mobile_Phone_Both']=df['Households_with_Telephone_Mobile_Phone_Both'].fillna(df['Households_with_Telephone_Mobile_Phone_Both'].mean())
df['Condition_of_occupied_census_houses_Dilapidated_Households']=df['Condition_of_occupied_census_houses_Dilapidated_Households'].fillna(df['Condition_of_occupied_census_houses_Dilapidated_Households'].mean())
df['Households_with_separate_kitchen_Cooking_inside_house']=df['Households_with_separate_kitchen_Cooking_inside_house'].fillna(df['Households_with_separate_kitchen_Cooking_inside_house'].mean())
df['Having_bathing_facility_Total_Households']=df['Having_bathing_facility_Total_Households'].fillna(df['Having_bathing_facility_Total_Households'].mean())
df['Having_latrine_facility_within_the_premises_Total_Households']=df['Having_latrine_facility_within_the_premises_Total_Households'].fillna(df['Having_latrine_facility_within_the_premises_Total_Households'].mean())
df['Ownership_Owned_Households']=df['Ownership_Owned_Households'].fillna(df['Ownership_Owned_Households'].mean())
df['Ownership_Rented_Households']=df['Ownership_Rented_Households'].fillna(df['Ownership_Rented_Households'].mean())
df['Type_of_bathing_facility_Enclosure_without_roof_Households']=df['Type_of_bathing_facility_Enclosure_without_roof_Households'].fillna(df['Type_of_bathing_facility_Enclosure_without_roof_Households'].mean())
df['Type_of_fuel_used_for_cooking_Any_other_Households']=df['Type_of_fuel_used_for_cooking_Any_other_Households'].fillna(df['Type_of_fuel_used_for_cooking_Any_other_Households'].mean())
df['Type_of_latrine_facility_Pit_latrine_Households']=df['Type_of_latrine_facility_Pit_latrine_Households'].fillna(df['Type_of_latrine_facility_Pit_latrine_Households'].mean())
df['Type_of_latrine_facility_Other_latrine_Households']=df['Type_of_latrine_facility_Other_latrine_Households'].fillna(df['Type_of_latrine_facility_Other_latrine_Households'].mean())
df['Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households']=df['Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households'].fillna(df['Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households'].mean())
df['Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households']=df['Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households'].fillna(df['Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households'].mean())
df['Not_having_bathing_facility_within_the_premises_Total_Households']=df['Not_having_bathing_facility_within_the_premises_Total_Households'].fillna(df['Not_having_bathing_facility_within_the_premises_Total_Households'].mean())
df['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households']=df['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households'].fillna(df['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households'].mean())
df['Main_source_of_drinking_water_Un_covered_well_Households']=df['Main_source_of_drinking_water_Un_covered_well_Households'].fillna(df['Main_source_of_drinking_water_Un_covered_well_Households'].mean())
df['Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households']=df['Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households'].fillna(df['Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households'].mean())
df['Main_source_of_drinking_water_Spring_Households']=df['Main_source_of_drinking_water_Spring_Households'].fillna(df['Main_source_of_drinking_water_Spring_Households'].mean())
df['Main_source_of_drinking_water_River_Canal_Households']=df['Main_source_of_drinking_water_River_Canal_Households'].fillna(df['Main_source_of_drinking_water_River_Canal_Households'].mean())
df['Main_source_of_drinking_water_Other_sources_Households']=df['Main_source_of_drinking_water_Other_sources_Households'].fillna(df['Main_source_of_drinking_water_Other_sources_Households'].mean())
df['Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households']=df['Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households'].fillna(df['Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households'].mean())
df['Location_of_drinking_water_source_Near_the_premises_Households']=df['Location_of_drinking_water_source_Near_the_premises_Households'].fillna(df['Location_of_drinking_water_source_Near_the_premises_Households'].mean())
df['Location_of_drinking_water_source_Within_the_premises_Households']=df['Location_of_drinking_water_source_Within_the_premises_Households'].fillna(df['Location_of_drinking_water_source_Within_the_premises_Households'].mean())
df['Main_source_of_drinking_water_Tank_Pond_Lake_Households']=df['Main_source_of_drinking_water_Tank_Pond_Lake_Households'].fillna(df['Main_source_of_drinking_water_Tank_Pond_Lake_Households'].mean())
df['Main_source_of_drinking_water_Tapwater_Households']=df['Main_source_of_drinking_water_Tapwater_Households'].fillna(df['Main_source_of_drinking_water_Tapwater_Households'].mean())
df['Main_source_of_drinking_water_Tubewell_Borehole_Households']=df['Main_source_of_drinking_water_Tubewell_Borehole_Households'].fillna(df['Main_source_of_drinking_water_Tubewell_Borehole_Households'].mean())
df['Location_of_drinking_water_source_Away_Households']=df['Location_of_drinking_water_source_Away_Households'].fillna(df['Location_of_drinking_water_source_Away_Households'].mean())

# Find the percentage of na values after handling them in households, drinking water and latrine facility
df_Households_with_Bicycle_after=df['Households_with_Bicycle'].isna().mean()*100
df_Households_with_Car_Jeep_Van_after=df['Households_with_Car_Jeep_Van'].isna().mean()*100
df_Households_with_Radio_Transistor_after=df['Households_with_Radio_Transistor'].isna().mean()*100
df_Households_with_Scooter_Motorcycle_Moped_after=df['Households_with_Scooter_Motorcycle_Moped'].isna().mean()*100
df_Households_with_Telephone_Mobile_Phone_Landline_only_after=df['Households_with_Telephone_Mobile_Phone_Landline_only'].isna().mean()*100
df_Households_with_Telephone_Mobile_Phone_Mobile_only_after=df['Households_with_Telephone_Mobile_Phone_Mobile_only'].isna().mean()*100
df_Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car_after=df['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car'].isna().mean()*100
df_Households_with_Television_after=df['Households_with_Television'].isna().mean()*100
df_Households_with_Telephone_Mobile_Phone_after=df['Households_with_Telephone_Mobile_Phone'].isna().mean()*100
df_Households_with_Telephone_Mobile_Phone_Both_after=df['Households_with_Telephone_Mobile_Phone_Both'].isna().mean()*100
df_Condition_of_occupied_census_houses_Dilapidated_Households_after=df['Condition_of_occupied_census_houses_Dilapidated_Households'].isna().mean()*100
df_Households_with_separate_kitchen_Cooking_inside_house_after=df['Households_with_separate_kitchen_Cooking_inside_house'].isna().mean()*100
df_Having_bathing_facility_Total_Households_after=df['Having_bathing_facility_Total_Households'].isna().mean()*100
df_Having_latrine_facility_within_the_premises_Total_Households_after=df['Having_latrine_facility_within_the_premises_Total_Households'].isna().mean()*100
df_Ownership_Owned_Households_after=df['Ownership_Owned_Households'].isna().mean()*100
df_Ownership_Rented_Households_after=df['Ownership_Rented_Households'].isna().mean()*100
df_Type_of_bathing_facility_Enclosure_without_roof_Households_after=df['Type_of_bathing_facility_Enclosure_without_roof_Households'].isna().mean()*100
df_Type_of_fuel_used_for_cooking_Any_other_Households_after=df['Type_of_fuel_used_for_cooking_Any_other_Households'].isna().mean()*100
df_Type_of_latrine_facility_Pit_latrine_Households_after=df['Type_of_latrine_facility_Pit_latrine_Households'].isna().mean()*100
df_Type_of_latrine_facility_Other_latrine_Households_after=df['Type_of_latrine_facility_Other_latrine_Households'].isna().mean()*100
df_Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households_after=df['Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households'].isna().mean()*100
df_Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households_after=df['Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households'].isna().mean()*100
df_Not_having_bathing_facility_within_the_premises_Total_Households_after=df['Not_having_bathing_facility_within_the_premises_Total_Households'].isna().mean()*100
df_Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households_after=df['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Un_covered_well_Households_after=df['Main_source_of_drinking_water_Un_covered_well_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households_after=df['Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Spring_Households_after=df['Main_source_of_drinking_water_Spring_Households'].isna().mean()*100
df_Main_source_of_drinking_water_River_Canal_Households_after=df['Main_source_of_drinking_water_River_Canal_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Other_sources_Households_after=df['Main_source_of_drinking_water_Other_sources_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households_after=df['Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households'].isna().mean()*100
df_Location_of_drinking_water_source_Near_the_premises_Households_after=df['Location_of_drinking_water_source_Near_the_premises_Households'].isna().mean()*100
df_Location_of_drinking_water_source_Within_the_premises_Households_after=df['Location_of_drinking_water_source_Within_the_premises_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Tank_Pond_Lake_Households_after=df['Main_source_of_drinking_water_Tank_Pond_Lake_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Tapwater_Households_after=df['Main_source_of_drinking_water_Tapwater_Households'].isna().mean()*100
df_Main_source_of_drinking_water_Tubewell_Borehole_Households_after=df['Main_source_of_drinking_water_Tubewell_Borehole_Households'].isna().mean()*100
df_Location_of_drinking_water_source_Away_Households_after=df['Location_of_drinking_water_source_Away_Households'].isna().mean()*100

# Find the percentage of na values before handling then in Household size
df_Household_size_1_person_Households_before=df['Household_size_1_person_Households'].isna().mean()*100
df_Household_size_2_persons_Households_before=df['Household_size_2_persons_Households'].isna().mean()*100
df_Household_size_1_to_2_persons_before=df['Household_size_1_to_2_persons'].isna().mean()*100
df_Household_size_3_persons_Households_before=df['Household_size_3_persons_Households'].isna().mean()*100
df_Household_size_3_to_5_persons_Households_before=df['Household_size_3_to_5_persons_Households'].isna().mean()*100
df_Household_size_4_persons_Households_before=df['Household_size_4_persons_Households'].isna().mean()*100
df_Household_size_5_persons_Households_before=df['Household_size_5_persons_Households'].isna().mean()*100
df_Household_size_6_8_persons_Households_before=df['Household_size_6_8_persons_Households'].isna().mean()*100
df_Household_size_9_persons_and_above_Households_before=df['Household_size_9_persons_and_above_Households'].isna().mean()*100

# Fill 1 to 2, 2 and 3 persons na values
df['Household_size_1_to_2_persons']=df['Household_size_1_to_2_persons'].fillna(df['Household_size_1_person_Households']+df['Household_size_2_persons_Households'])
df['Household_size_1_person_Households']=df['Household_size_1_person_Households'].fillna(df['Household_size_1_to_2_persons']-df['Household_size_2_persons_Households'])
df['Household_size_2_persons_Households']=df['Household_size_2_persons_Households'].fillna(df['Household_size_1_to_2_persons']-df['Household_size_1_person_Households'])

# Fill 1 person household with 0 and then update the 1 to 2 and 2 persons na values
df['Household_size_1_person_Households']=df['Household_size_1_person_Households'].fillna(0)
df['Household_size_1_to_2_persons']=df['Household_size_1_to_2_persons'].fillna(df['Household_size_1_person_Households']+df['Household_size_2_persons_Households'])
df['Household_size_2_persons_Households']=df['Household_size_2_persons_Households'].fillna(df['Household_size_1_to_2_persons']-df['Household_size_1_person_Households'])

# Fill 2 person household with 0 and then update the 1 to 2
df['Household_size_2_persons_Households']=df['Household_size_2_persons_Households'].fillna(0)
df['Household_size_1_to_2_persons']=df['Household_size_1_to_2_persons'].fillna(df['Household_size_1_person_Households']+df['Household_size_2_persons_Households'])

# Fill 3 to 5, 3, 4 and 5 persons na values
df['Household_size_3_to_5_persons_Households']=df['Household_size_3_to_5_persons_Households'].fillna(df['Household_size_3_persons_Households']+df['Household_size_4_persons_Households']+df['Household_size_5_persons_Households'])
df['Household_size_3_persons_Households']=df['Household_size_3_persons_Households'].fillna(df['Household_size_3_to_5_persons_Households']-(df['Household_size_4_persons_Households']+df['Household_size_5_persons_Households']))
df['Household_size_4_persons_Households']=df['Household_size_4_persons_Households'].fillna(df['Household_size_3_to_5_persons_Households']-(df['Household_size_3_persons_Households']+df['Household_size_5_persons_Households']))
df['Household_size_5_persons_Households']=df['Household_size_5_persons_Households'].fillna(df['Household_size_3_to_5_persons_Households']-(df['Household_size_3_persons_Households']+df['Household_size_4_persons_Households']))

# Fill 5 person household with 0 and then update the 3 to 5, 3 and 4 persons na values
df['Household_size_5_persons_Households']=df['Household_size_5_persons_Households'].fillna(0)
df['Household_size_3_to_5_persons_Households']=df['Household_size_3_to_5_persons_Households'].fillna(df['Household_size_3_persons_Households']+df['Household_size_4_persons_Households']+df['Household_size_5_persons_Households'])
df['Household_size_3_persons_Households']=df['Household_size_3_persons_Households'].fillna(df['Household_size_3_to_5_persons_Households']-(df['Household_size_4_persons_Households']+df['Household_size_5_persons_Households']))
df['Household_size_4_persons_Households']=df['Household_size_4_persons_Households'].fillna(df['Household_size_3_to_5_persons_Households']-(df['Household_size_3_persons_Households']+df['Household_size_5_persons_Households']))

# Fill 3 person household with 0 and then update the 3 to 5 and 4 persons na values
df['Household_size_3_persons_Households']=df['Household_size_3_persons_Households'].fillna(0)
df['Household_size_3_to_5_persons_Households']=df['Household_size_3_to_5_persons_Households'].fillna(df['Household_size_3_persons_Households']+df['Household_size_4_persons_Households']+df['Household_size_5_persons_Households'])
df['Household_size_4_persons_Households']=df['Household_size_4_persons_Households'].fillna(df['Household_size_3_to_5_persons_Households']-(df['Household_size_3_persons_Households']+df['Household_size_5_persons_Households']))

# Fill 4 person household with 0 and then update the 3 to 5 persons na values
df['Household_size_4_persons_Households']=df['Household_size_4_persons_Households'].fillna(0)
df['Household_size_3_to_5_persons_Households']=df['Household_size_3_to_5_persons_Households'].fillna(df['Household_size_3_persons_Households']+df['Household_size_4_persons_Households']+df['Household_size_5_persons_Households'])

# Fill the 6 to 8 persons and 9 persons na values to 0
df['Household_size_6_8_persons_Households']=df['Household_size_6_8_persons_Households'].fillna(0)
df['Household_size_9_persons_and_above_Households']=df['Household_size_9_persons_and_above_Households'].fillna(0)

# Find the percentage of na values after handling then in Household size
df_Household_size_1_person_Households_after=df['Household_size_1_person_Households'].isna().mean()*100
df_Household_size_2_persons_Households_after=df['Household_size_2_persons_Households'].isna().mean()*100
df_Household_size_1_to_2_persons_after=df['Household_size_1_to_2_persons'].isna().mean()*100
df_Household_size_3_persons_Households_after=df['Household_size_3_persons_Households'].isna().mean()*100
df_Household_size_3_to_5_persons_Households_after=df['Household_size_3_to_5_persons_Households'].isna().mean()*100
df_Household_size_4_persons_Households_after=df['Household_size_4_persons_Households'].isna().mean()*100
df_Household_size_5_persons_Households_after=df['Household_size_5_persons_Households'].isna().mean()*100
df_Household_size_6_8_persons_Households_after=df['Household_size_6_8_persons_Households'].isna().mean()*100
df_Household_size_9_persons_and_above_Households_after=df['Household_size_9_persons_and_above_Households'].isna().mean()*100

# Find the percentage of na values before handling them in Married couples household size
df_Married_couples_1_Households_before=df['Married_couples_1_Households'].isna().mean()*100
df_Married_couples_2_Households_before=df['Married_couples_2_Households'].isna().mean()*100
df_Married_couples_3_Households_before=df['Married_couples_3_Households'].isna().mean()*100
df_Married_couples_3_or_more_Households_before=df['Married_couples_3_or_more_Households'].isna().mean()*100
df_Married_couples_4_Households_before=df['Married_couples_4_Households'].isna().mean()*100
df_Married_couples_5__Households_before=df['Married_couples_5__Households'].isna().mean()*100
df_Married_couples_None_Households_before=df['Married_couples_None_Households'].isna().mean()*100

# Fill na values by the logic 3 or more households = 3 + 4 + 5 households
df['Married_couples_3_or_more_Households']=df['Married_couples_3_or_more_Households'].fillna(df['Married_couples_3_Households']+df['Married_couples_4_Households']+df['Married_couples_5__Households'])
df['Married_couples_3_Households']=df['Married_couples_3_Households'].fillna(df['Married_couples_3_or_more_Households']-(df['Married_couples_4_Households']+df['Married_couples_5__Households']))
df['Married_couples_4_Households']=df['Married_couples_4_Households'].fillna(df['Married_couples_3_or_more_Households']-(df['Married_couples_3_Households']+df['Married_couples_5__Households']))
df['Married_couples_5__Households']=df['Married_couples_5__Households'].fillna(df['Married_couples_3_or_more_Households']-(df['Married_couples_3_Households']+df['Married_couples_4_Households']))

# Fill the 3 household value with 0 and calculate the 3 or more, 4 and 5 household size
df['Married_couples_3_Households']=df['Married_couples_3_Households'].fillna(0)
df['Married_couples_3_or_more_Households']=df['Married_couples_3_or_more_Households'].fillna(df['Married_couples_3_Households']+df['Married_couples_4_Households']+df['Married_couples_5__Households'])
df['Married_couples_4_Households']=df['Married_couples_4_Households'].fillna(df['Married_couples_3_or_more_Households']-(df['Married_couples_3_Households']+df['Married_couples_5__Households']))
df['Married_couples_5__Households']=df['Married_couples_5__Households'].fillna(df['Married_couples_3_or_more_Households']-(df['Married_couples_3_Households']+df['Married_couples_4_Households']))

# Fill the 4 household value with 0 and calculate the 3 or more and 5 household size
df['Married_couples_4_Households']=df['Married_couples_4_Households'].fillna(0)
df['Married_couples_3_or_more_Households']=df['Married_couples_3_or_more_Households'].fillna(df['Married_couples_3_Households']+df['Married_couples_4_Households']+df['Married_couples_5__Households'])
df['Married_couples_5__Households']=df['Married_couples_5__Households'].fillna(df['Married_couples_3_or_more_Households']-(df['Married_couples_3_Households']+df['Married_couples_4_Households']))

# Fill the 5 household value with 0 and calculate the 3 or morehousehold size
df['Married_couples_5__Households']=df['Married_couples_5__Households'].fillna(0)
df['Married_couples_3_or_more_Households']=df['Married_couples_3_or_more_Households'].fillna(df['Married_couples_3_Households']+df['Married_couples_4_Households']+df['Married_couples_5__Households'])

# Fill the remaining all household sizes na with 0
df['Married_couples_1_Households']=df['Married_couples_1_Households'].fillna(0)
df['Married_couples_2_Households']=df['Married_couples_2_Households'].fillna(0)
df['Married_couples_None_Households']=df['Married_couples_None_Households'].fillna(0)

# Find the percentage of na values after handling them in Married couples household size
df_Married_couples_1_Households_after=df['Married_couples_1_Households'].isna().mean()*100
df_Married_couples_2_Households_after=df['Married_couples_2_Households'].isna().mean()*100
df_Married_couples_3_Households_after=df['Married_couples_3_Households'].isna().mean()*100
df_Married_couples_3_or_more_Households_after=df['Married_couples_3_or_more_Households'].isna().mean()*100
df_Married_couples_4_Households_after=df['Married_couples_4_Households'].isna().mean()*100
df_Married_couples_5__Households_after=df['Married_couples_5__Households'].isna().mean()*100
df_Married_couples_None_Households_after=df['Married_couples_None_Households'].isna().mean()*100

# Find the percentage of na values before handling them in Partiy
df_Power_Parity_Less_than_Rs_45000_before=df['Power_Parity_Less_than_Rs_45000'].isna().mean()*100
df_Power_Parity_Rs_45000_90000_before=df['Power_Parity_Rs_45000_90000'].isna().mean()*100
df_Power_Parity_Rs_90000_150000_before=df['Power_Parity_Rs_90000_150000'].isna().mean()*100
df_Power_Parity_Rs_45000_150000_before=df['Power_Parity_Rs_45000_150000'].isna().mean()*100
df_Power_Parity_Rs_150000_240000_before=df['Power_Parity_Rs_150000_240000'].isna().mean()*100
df_Power_Parity_Rs_240000_330000_before=df['Power_Parity_Rs_240000_330000'].isna().mean()*100
df_Power_Parity_Rs_150000_330000_before=df['Power_Parity_Rs_150000_330000'].isna().mean()*100
df_Power_Parity_Rs_330000_425000_before=df['Power_Parity_Rs_330000_425000'].isna().mean()*100
df_Power_Parity_Rs_425000_545000_before=df['Power_Parity_Rs_425000_545000'].isna().mean()*100
df_Power_Parity_Rs_330000_545000_before=df['Power_Parity_Rs_330000_545000'].isna().mean()*100
df_Power_Parity_Above_Rs_545000_before=df['Power_Parity_Above_Rs_545000'].isna().mean()*100
df_Total_Power_Parity_before=df['Total_Power_Parity'].isna().mean()*100

# Fill values of na
df['Power_Parity_Rs_45000_150000']=df['Power_Parity_Rs_45000_150000'].fillna(df['Power_Parity_Rs_45000_90000']+df['Power_Parity_Rs_90000_150000'])
df['Power_Parity_Rs_45000_90000']=df['Power_Parity_Rs_45000_90000'].fillna(df['Power_Parity_Rs_45000_150000']-df['Power_Parity_Rs_90000_150000'])
df['Power_Parity_Rs_90000_150000']=df['Power_Parity_Rs_90000_150000'].fillna(df['Power_Parity_Rs_45000_150000']-df['Power_Parity_Rs_45000_90000'])

df['Power_Parity_Rs_150000_330000']=df['Power_Parity_Rs_150000_330000'].fillna(df['Power_Parity_Rs_150000_240000']+df['Power_Parity_Rs_240000_330000'])
df['Power_Parity_Rs_150000_240000']=df['Power_Parity_Rs_150000_240000'].fillna(df['Power_Parity_Rs_150000_330000']-df['Power_Parity_Rs_240000_330000'])
df['Power_Parity_Rs_240000_330000']=df['Power_Parity_Rs_240000_330000'].fillna(df['Power_Parity_Rs_150000_330000']-df['Power_Parity_Rs_150000_240000'])

df['Power_Parity_Rs_330000_545000']=df['Power_Parity_Rs_330000_545000'].fillna(df['Power_Parity_Rs_330000_425000']+df['Power_Parity_Rs_425000_545000'])
df['Power_Parity_Rs_330000_425000']=df['Power_Parity_Rs_330000_425000'].fillna(df['Power_Parity_Rs_330000_545000']-df['Power_Parity_Rs_425000_545000'])
df['Power_Parity_Rs_425000_545000']=df['Power_Parity_Rs_425000_545000'].fillna(df['Power_Parity_Rs_330000_545000']-df['Power_Parity_Rs_330000_425000'])

df['Total_Power_Parity']=df['Total_Power_Parity'].fillna(df['Power_Parity_Less_than_Rs_45000']+df['Power_Parity_Rs_45000_150000']+df['Power_Parity_Rs_150000_330000']+df['Power_Parity_Rs_330000_545000']+df['Power_Parity_Above_Rs_545000'])


df['Power_Parity_Less_than_Rs_45000']=df['Power_Parity_Less_than_Rs_45000'].fillna(df['Total_Power_Parity']-(df['Power_Parity_Rs_45000_150000']+df['Power_Parity_Rs_150000_330000']+df['Power_Parity_Rs_330000_545000']+df['Power_Parity_Above_Rs_545000']))
df['Power_Parity_Rs_45000_150000']=df['Power_Parity_Rs_45000_150000'].fillna(df['Total_Power_Parity']-(df['Power_Parity_Less_than_Rs_45000']+df['Power_Parity_Rs_150000_330000']+df['Power_Parity_Rs_330000_545000']+df['Power_Parity_Above_Rs_545000']))
df['Power_Parity_Rs_150000_330000']=df['Power_Parity_Rs_150000_330000'].fillna(df['Total_Power_Parity']-(df['Power_Parity_Less_than_Rs_45000']+df['Power_Parity_Rs_45000_150000']+df['Power_Parity_Rs_330000_545000']+df['Power_Parity_Above_Rs_545000']))
df['Power_Parity_Rs_330000_545000']=df['Power_Parity_Rs_330000_545000'].fillna(df['Total_Power_Parity']-(df['Power_Parity_Less_than_Rs_45000']+df['Power_Parity_Rs_45000_150000']+df['Power_Parity_Rs_150000_330000']+df['Power_Parity_Above_Rs_545000']))
df['Power_Parity_Above_Rs_545000']=df['Power_Parity_Above_Rs_545000'].fillna(df['Total_Power_Parity']-(df['Power_Parity_Less_than_Rs_45000']+df['Power_Parity_Rs_45000_150000']+df['Power_Parity_Rs_150000_330000']+df['Power_Parity_Rs_330000_545000']))

df['Power_Parity_Rs_45000_90000']=df['Power_Parity_Rs_45000_90000'].fillna(0)
df['Power_Parity_Rs_45000_150000']=df['Power_Parity_Rs_45000_150000'].fillna(df['Power_Parity_Rs_45000_90000']+df['Power_Parity_Rs_90000_150000'])
df['Power_Parity_Rs_90000_150000']=df['Power_Parity_Rs_90000_150000'].fillna(df['Power_Parity_Rs_45000_150000']-df['Power_Parity_Rs_45000_90000'])

df['Power_Parity_Rs_240000_330000']=df['Power_Parity_Rs_240000_330000'].fillna(df['Power_Parity_Rs_150000_330000']-df['Power_Parity_Rs_150000_240000'])
df['Power_Parity_Rs_330000_425000']=df['Power_Parity_Rs_330000_425000'].fillna(df['Power_Parity_Rs_330000_545000']-df['Power_Parity_Rs_425000_545000'])
df['Power_Parity_Rs_425000_545000']=df['Power_Parity_Rs_425000_545000'].fillna(df['Power_Parity_Rs_330000_545000']-df['Power_Parity_Rs_330000_425000'])

df['Power_Parity_Rs_330000_425000']=df['Power_Parity_Rs_330000_425000'].fillna(0)
df['Power_Parity_Rs_425000_545000']=df['Power_Parity_Rs_425000_545000'].fillna(df['Power_Parity_Rs_330000_545000']-df['Power_Parity_Rs_330000_425000'])
df['Power_Parity_Rs_330000_545000']=df['Power_Parity_Rs_330000_545000'].fillna(df['Power_Parity_Rs_330000_425000']+df['Power_Parity_Rs_425000_545000'])

df['Power_Parity_Rs_425000_545000']=df['Power_Parity_Rs_425000_545000'].fillna(0)
df['Power_Parity_Rs_330000_545000']=df['Power_Parity_Rs_330000_545000'].fillna(df['Power_Parity_Rs_330000_425000']+df['Power_Parity_Rs_425000_545000'])

df['Power_Parity_Less_than_Rs_45000']=df['Power_Parity_Less_than_Rs_45000'].fillna(0)
df['Total_Power_Parity']=df['Total_Power_Parity'].fillna(df['Power_Parity_Less_than_Rs_45000']+df['Power_Parity_Rs_45000_150000']+df['Power_Parity_Rs_150000_330000']+df['Power_Parity_Rs_330000_545000']+df['Power_Parity_Above_Rs_545000'])
df['Power_Parity_Above_Rs_545000']=df['Power_Parity_Above_Rs_545000'].fillna(df['Total_Power_Parity']-(df['Power_Parity_Less_than_Rs_45000']+df['Power_Parity_Rs_45000_150000']+df['Power_Parity_Rs_150000_330000']+df['Power_Parity_Rs_330000_545000']))

df['Power_Parity_Above_Rs_545000']=df['Power_Parity_Above_Rs_545000'].fillna(0)
df['Total_Power_Parity']=df['Total_Power_Parity'].fillna(df['Power_Parity_Less_than_Rs_45000']+df['Power_Parity_Rs_45000_150000']+df['Power_Parity_Rs_150000_330000']+df['Power_Parity_Rs_330000_545000']+df['Power_Parity_Above_Rs_545000'])

# Find the percentage of na values after handling them in Partiy

df_Power_Parity_Less_than_Rs_45000_after=df['Power_Parity_Less_than_Rs_45000'].isna().mean()*100
df_Power_Parity_Rs_45000_90000_after=df['Power_Parity_Rs_45000_90000'].isna().mean()*100
df_Power_Parity_Rs_90000_150000_after=df['Power_Parity_Rs_90000_150000'].isna().mean()*100
df_Power_Parity_Rs_45000_150000_after=df['Power_Parity_Rs_45000_150000'].isna().mean()*100
df_Power_Parity_Rs_150000_240000_after=df['Power_Parity_Rs_150000_240000'].isna().mean()*100
df_Power_Parity_Rs_240000_330000_after=df['Power_Parity_Rs_240000_330000'].isna().mean()*100
df_Power_Parity_Rs_150000_330000_after=df['Power_Parity_Rs_150000_330000'].isna().mean()*100
df_Power_Parity_Rs_330000_425000_after=df['Power_Parity_Rs_330000_425000'].isna().mean()*100
df_Power_Parity_Rs_425000_545000_after=df['Power_Parity_Rs_425000_545000'].isna().mean()*100
df_Power_Parity_Rs_330000_545000_after=df['Power_Parity_Rs_330000_545000'].isna().mean()*100
df_Power_Parity_Above_Rs_545000_after=df['Power_Parity_Above_Rs_545000'].isna().mean()*100
df_Total_Power_Parity_after=df['Total_Power_Parity'].isna().mean()*100


# Convert the calculated percentage of null values after cleaning to a data frame
after_cleaning=pd.DataFrame(df.isnull().mean()*100)

# Reset the index of the after cleaning df
after_cleaning.reset_index(inplace=True)

# Assign the column names to the df of getting the mean after cleaning
after_cleaning.columns=['column_name','after_cleaning']

# Create a csv file of the after cleaning values
after_cleaning.to_csv('After Cleaning Percentage.csv')
print("Percentage of na values after cleaning was saved to After Cleaning Percentage.csv")

# Compare the before and after cleaning csv files by merging them
Comparison=before_cleaning.merge(after_cleaning,on='column_name')
Comparison.to_csv('Before & After Comparison.csv')
print("Comparison of before and after cleaning na values was saved to Before & After Comparison.csv")

print("Task 4 (Find and store the percentage of data missing for the columns) completed successfully!")

# Task  5: Save Data to MongoDB
# Save the processed data to mongoDB with a collection named “census”.

# Import the required library for MongoDB connection
# For this, need to install pymongo first
# pip install pymongo in command line
import pymongo
from pymongo import MongoClient

# Establish connection to MongoDB
client = MongoClient("mongodb://localhost:27017/")
print("MongoDB connection established successfully!")

# Check whether the connection is establised by fetching any collection from MongoDB
db = client['guvi']
collection=db['census']
collection

# Convert the data frame to dictionary
data_dict=df.to_dict('records')

# Insert documents to mongodb
collection.insert_many(data_dict)
print("Documents inserted to MongoDB!")
print("Task  5 (Save Data to MongoDB) completed successfully!")

# Task 6: Database connection and data upload
# Data should be fetched from the mongoDB and to be uploaded to a relational database using python code . The table names should be the same as the file names without the extension.
# The primary key and foreign key constraints should be included in the tables wherever require

# Read the collection from MongoDB
mongo_read=list(collection.find())

# Create a Dataframe for the collection read from MongoDB
mongo_df=pd.DataFrame(mongo_read)

# Remove the _id column
mondo_df=mongo_df.drop('_id',axis=1,inplace=True)


# Import necessary libraries for mysql
# For this first need to install the mysql connector plugin
# pip install mysql.connector
# pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error

# Establish the connection with mysql
# for the sha password issue - add auth_plugin='mysql_native_password'

connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='Chellamss@123',  # Replace with your MySQL password
            database='guvi', # Replace with your database name
            auth_plugin='mysql_native_password'
        )
print("Mysql connection established successfully!")

# Create the DDL for the census table
CreateDDL = '''CREATE TABLE census(
District_code INT PRIMARY KEY,State_UT VARCHAR(50),District VARCHAR(50),Population BIGINT,Male BIGINT,Female BIGINT,Literate BIGINT,Literate_Male BIGINT,Literate_Female BIGINT,SC BIGINT,SC_Male BIGINT,SC_Female BIGINT,ST BIGINT,ST_Male BIGINT,ST_Female BIGINT,Workers BIGINT,Workers_Male BIGINT,Workers_Female BIGINT,Workers_Main BIGINT,Workers_Marginal BIGINT,Workers_Non BIGINT,Workers_Cultivator BIGINT,Workers_Agricultural BIGINT,
Workers_Household BIGINT,Workers_Other BIGINT,Hindus BIGINT,Muslims BIGINT,Christians BIGINT,Sikhs BIGINT,Buddhists BIGINT,Jains BIGINT,Others_Religions BIGINT,Religion_Not_Stated BIGINT,LPG_or_PNG_House BIGINT,Housholds_with_Electric_Lighting BIGINT,House_with_Internet BIGINT,House_with_Computer BIGINT,House_Rural BIGINT,House_Urban BIGINT,House BIGINT,Education_Below_Primary BIGINT,Education_Primary BIGINT,Education_Middle BIGINT,Education_Secondary_ BIGINT,Education_Higher BIGINT,Education_Graduate BIGINT,Education_Other BIGINT,Education_Literate BIGINT,Education_Illiterate BIGINT,Education_Total BIGINT,Young_and_Adult BIGINT,Middle_Aged BIGINT,Senior_Citizen BIGINT,Age_Not_Stated BIGINT,House_with_Bicycle BIGINT,House_with_Car_Jeep_Van BIGINT,House_with_Radio_Transistor BIGINT,House_with_Scooter_Motorcycle_Moped BIGINT,House_with_Telephone_Mobile_Phone_Landline_only BIGINT,House_with_Telephone_Mobile_Phone_Mobile_only BIGINT,House_with_TV_Cmp_Lap_Telphn_mob_phn_Scooter_Car BIGINT,House_with_Television BIGINT,House_with_Telephone_Mobile_Phone BIGINT,House_with_Telephone_Mobile_Phone_Both BIGINT,Condition_of_occ_census_houses_Dilapidated_House BIGINT,House_with_separate_kitchen_Cooking_inside_house BIGINT,
Having_bathing_fac_Total_House BIGINT,Having_latrine_fac_within_the_premises_Total_House BIGINT,Ownership_Owned_House BIGINT,Ownership_Rented_House BIGINT,Type_of_bathing_fac_Enclosure_without_roof_House BIGINT,Type_of_fuel_used_for_cooking_Any_other_House BIGINT,Type_of_latrine_fac_Pit_latrine_House BIGINT,Type_of_latrine_fac_Other_latrine_House BIGINT,Type_of_latrine_fac_Night_soil_disposed_into_open_drain_House BIGINT,Type_of_latrine_fac_flush_latrine_conect_to_other_system_House BIGINT,Not_having_bathing_fac_within_the_prem_Total_House BIGINT,Not_having_latrine_fac_within_the_prem_Alter_source_Open_House BIGINT,Main_source_of_water_Un_covered_well_House BIGINT,Main_source_of_water_Handpump_Tubewell_Borewell_House BIGINT,Main_source_of_water_Spring_House BIGINT,Main_source_of_water_River_Canal_House BIGINT,Main_source_of_water_Other_sources_House BIGINT,Main_source_of_Spring_River_Canal_Tank_Pond_Lake_House BIGINT,Location_of_water_source_Near_the_premises_House BIGINT,Location_of_water_source_Within_the_premises_House BIGINT,Main_source_of_water_Tank_Pond_Lake_House BIGINT,Main_source_of_water_Tapwater_House BIGINT,Main_source_of_water_Tubewell_Borehole_House BIGINT,Household_size_1_person_House BIGINT,Household_size_2_persons_House BIGINT,Household_size_1_to_2_persons BIGINT,Household_size_3_persons_House BIGINT,Household_size_3_to_5_persons_House BIGINT,Household_size_4_persons_House BIGINT,Household_size_5_persons_House BIGINT,Household_size_6_8_persons_House BIGINT,Household_size_9_persons_and_above_House BIGINT,Location_of_water_source_Away_House BIGINT,Married_couples_1_House BIGINT,Married_couples_2_House BIGINT,Married_couples_3_House BIGINT,Married_couples_3_or_more_House BIGINT,Married_couples_4_House BIGINT,Married_couples_5__House BIGINT,Married_couples_None_House BIGINT,Power_Parity_Less_than_Rs_45000 BIGINT,Power_Parity_Rs_45000_90000 BIGINT,Power_Parity_Rs_90000_150000 BIGINT,Power_Parity_Rs_45000_150000 BIGINT,Power_Parity_Rs_150000_240000 BIGINT,Power_Parity_Rs_240000_330000 BIGINT,Power_Parity_Rs_150000_330000 BIGINT,Power_Parity_Rs_330000_425000 BIGINT,Power_Parity_Rs_425000_545000 BIGINT,Power_Parity_Rs_330000_545000 BIGINT,Power_Parity_Above_Rs_545000 BIGINT,Total_Power_Parity BIGINT)'''

# Create a cursor to execute the commands
# Execute the DDL
cursor = connection.cursor()
cursor.execute(CreateDDL)
print("Mysql table created successfully!")

# Create the Insert query for the census table
InsertQuery = '''INSERT INTO census(District_code,State_UT,District,Population,Male,Female,Literate,Literate_Male,Literate_Female,SC,SC_Male,SC_Female,ST,ST_Male,ST_Female,Workers,Workers_Male,Workers_Female,Workers_Main,Workers_Marginal,Workers_Non,Workers_Cultivator,Workers_Agricultural,Workers_Household,Workers_Other,Hindus,Muslims,Christians,Sikhs,Buddhists,Jains,Others_Religions,Religion_Not_Stated,LPG_or_PNG_House,Housholds_with_Electric_Lighting,House_with_Internet,House_with_Computer,House_Rural,House_Urban,House,Education_Below_Primary,Education_Primary,Education_Middle,Education_Secondary_,Education_Higher,Education_Graduate,Education_Other,Education_Literate,Education_Illiterate,Education_Total,Young_and_Adult,Middle_Aged,Senior_Citizen,Age_Not_Stated,House_with_Bicycle,House_with_Car_Jeep_Van,House_with_Radio_Transistor,House_with_Scooter_Motorcycle_Moped,House_with_Telephone_Mobile_Phone_Landline_only,House_with_Telephone_Mobile_Phone_Mobile_only,House_with_TV_Cmp_Lap_Telphn_mob_phn_Scooter_Car,House_with_Television,House_with_Telephone_Mobile_Phone,House_with_Telephone_Mobile_Phone_Both,Condition_of_occ_census_houses_Dilapidated_House,House_with_separate_kitchen_Cooking_inside_house,Having_bathing_fac_Total_House,Having_latrine_fac_within_the_premises_Total_House,Ownership_Owned_House,Ownership_Rented_House,Type_of_bathing_fac_Enclosure_without_roof_House,Type_of_fuel_used_for_cooking_Any_other_House,Type_of_latrine_fac_Pit_latrine_House,Type_of_latrine_fac_Other_latrine_House,Type_of_latrine_fac_Night_soil_disposed_into_open_drain_House,Type_of_latrine_fac_flush_latrine_conect_to_other_system_House,Not_having_bathing_fac_within_the_prem_Total_House,Not_having_latrine_fac_within_the_prem_Alter_source_Open_House,Main_source_of_water_Un_covered_well_House,Main_source_of_water_Handpump_Tubewell_Borewell_House,Main_source_of_water_Spring_House,Main_source_of_water_River_Canal_House,Main_source_of_water_Other_sources_House,Main_source_of_Spring_River_Canal_Tank_Pond_Lake_House,Location_of_water_source_Near_the_premises_House,Location_of_water_source_Within_the_premises_House,Main_source_of_water_Tank_Pond_Lake_House,Main_source_of_water_Tapwater_House,Main_source_of_water_Tubewell_Borehole_House,Household_size_1_person_House,Household_size_2_persons_House,Household_size_1_to_2_persons,Household_size_3_persons_House,Household_size_3_to_5_persons_House,Household_size_4_persons_House,Household_size_5_persons_House,Household_size_6_8_persons_House,Household_size_9_persons_and_above_House,Location_of_water_source_Away_House,Married_couples_1_House,Married_couples_2_House,Married_couples_3_House,Married_couples_3_or_more_House,Married_couples_4_House,Married_couples_5__House,Married_couples_None_House,Power_Parity_Less_than_Rs_45000,Power_Parity_Rs_45000_90000,Power_Parity_Rs_90000_150000,Power_Parity_Rs_45000_150000,Power_Parity_Rs_150000_240000,Power_Parity_Rs_240000_330000,Power_Parity_Rs_150000_330000,Power_Parity_Rs_330000_425000,Power_Parity_Rs_425000_545000,Power_Parity_Rs_330000_545000,Power_Parity_Above_Rs_545000,Total_Power_Parity) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}','{21}','{22}','{23}','{24}','{25}','{26}','{27}','{28}','{29}','{30}','{31}','{32}','{33}','{34}','{35}','{36}','{37}','{38}','{39}','{40}','{41}','{42}','{43}','{44}','{45}','{46}','{47}','{48}','{49}','{50}','{51}','{52}','{53}','{54}','{55}','{56}','{57}','{58}','{59}','{60}','{61}','{62}','{63}','{64}','{65}','{66}','{67}','{68}','{69}','{70}','{71}','{72}','{73}','{74}','{75}','{76}','{77}','{78}','{79}','{80}','{81}','{82}','{83}','{84}','{85}','{86}','{87}','{88}','{89}','{90}','{91}','{92}','{93}','{94}','{95}','{96}','{97}','{98}','{99}','{100}','{101}','{102}','{103}','{104}','{105}','{106}','{107}','{108}','{109}','{110}','{111}','{112}','{113}','{114}','{115}','{116}','{117}')'''

# Execute the insert query for all the rows in the DF
for index, row in mongo_df.iterrows():
    #print(InsertQuery.format(row.District_code,row.State_UT,row.District,row.Population,row.Male,row.Female,row.Literate,row.Literate_Male,row.Literate_Female,row.SC,row.SC_Male,row.SC_Female,row.ST,row.ST_Male,row.ST_Female,row.Workers,row.Workers_Male,row.Workers_Female,row.Workers_Main,row.Workers_Marginal,row.Workers_Non,row.Workers_Cultivator,row.Workers_Agricultural,row.Workers_Household,row.Workers_Other,row.Hindus,row.Muslims,row.Christians,row.Sikhs,row.Buddhists,row.Jains,row.Others_Religions,row.Religion_Not_Stated,row.LPG_or_PNG_Households,row.Housholds_with_Electric_Lighting,row.Households_with_Internet,row.Households_with_Computer,row.Households_Rural,row.Households_Urban,row.Households,row.Education_Below_Primary,row.Education_Primary,row.Education_Middle,row.Education_Secondary_,row.Education_Higher,row.Education_Graduate,row.Education_Other,row.Education_Literate,row.Education_Illiterate,row.Education_Total,row.Young_and_Adult,row.Middle_Aged,row.Senior_Citizen,row.Age_Not_Stated,row.Households_with_Bicycle,row.Households_with_Car_Jeep_Van,row.Households_with_Radio_Transistor,row.Households_with_Scooter_Motorcycle_Moped,row.Households_with_Telephone_Mobile_Phone_Landline_only,row.Households_with_Telephone_Mobile_Phone_Mobile_only,row.Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car,row.Households_with_Television,row.Households_with_Telephone_Mobile_Phone,row.Households_with_Telephone_Mobile_Phone_Both,row.Condition_of_occupied_census_houses_Dilapidated_Households,row.Households_with_separate_kitchen_Cooking_inside_house,row.Having_bathing_facility_Total_Households,row.Having_latrine_facility_within_the_premises_Total_Households,row.Ownership_Owned_Households,row.Ownership_Rented_Households,row.Type_of_bathing_facility_Enclosure_without_roof_Households,row.Type_of_fuel_used_for_cooking_Any_other_Households,row.Type_of_latrine_facility_Pit_latrine_Households,row.Type_of_latrine_facility_Other_latrine_Households,row.Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households,row.Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households,row.Not_having_bathing_facility_within_the_premises_Total_Households,row.Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households,row.Main_source_of_drinking_water_Un_covered_well_Households,row.Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households,row.Main_source_of_drinking_water_Spring_Households,row.Main_source_of_drinking_water_River_Canal_Households,row.Main_source_of_drinking_water_Other_sources_Households,row.Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households,row.Location_of_drinking_water_source_Near_the_premises_Households,row.Location_of_drinking_water_source_Within_the_premises_Households,row.Main_source_of_drinking_water_Tank_Pond_Lake_Households,row.Main_source_of_drinking_water_Tapwater_Households,row.Main_source_of_drinking_water_Tubewell_Borehole_Households,row.Household_size_1_person_Households,row.Household_size_2_persons_Households,row.Household_size_1_to_2_persons,row.Household_size_3_persons_Households,row.Household_size_3_to_5_persons_Households,row.Household_size_4_persons_Households,row.Household_size_5_persons_Households,row.Household_size_6_8_persons_Households,row.Household_size_9_persons_and_above_Households,row.Location_of_drinking_water_source_Away_Households,row.Married_couples_1_Households,row.Married_couples_2_Households,row.Married_couples_3_Households,row.Married_couples_3_or_more_Households,row.Married_couples_4_Households,row.Married_couples_5__Households,row.Married_couples_None_Households,row.Power_Parity_Less_than_Rs_45000,row.Power_Parity_Rs_45000_90000,row.Power_Parity_Rs_90000_150000,row.Power_Parity_Rs_45000_150000,row.Power_Parity_Rs_150000_240000,row.Power_Parity_Rs_240000_330000,row.Power_Parity_Rs_150000_330000,row.Power_Parity_Rs_330000_425000,row.Power_Parity_Rs_425000_545000,row.Power_Parity_Rs_330000_545000,row.Power_Parity_Above_Rs_545000,row.Total_Power_Parity))
    cursor.execute(InsertQuery.format(row.District_code,row.State_UT,row.District,row.Population,row.Male,row.Female,row.Literate,row.Literate_Male,row.Literate_Female,row.SC,row.SC_Male,row.SC_Female,row.ST,row.ST_Male,row.ST_Female,row.Workers,row.Workers_Male,row.Workers_Female,row.Workers_Main,row.Workers_Marginal,row.Workers_Non,row.Workers_Cultivator,row.Workers_Agricultural,row.Workers_Household,row.Workers_Other,row.Hindus,row.Muslims,row.Christians,row.Sikhs,row.Buddhists,row.Jains,row.Others_Religions,row.Religion_Not_Stated,row.LPG_or_PNG_Households,row.Housholds_with_Electric_Lighting,row.Households_with_Internet,row.Households_with_Computer,row.Households_Rural,row.Households_Urban,row.Households,row.Education_Below_Primary,row.Education_Primary,row.Education_Middle,row.Education_Secondary_,row.Education_Higher,row.Education_Graduate,row.Education_Other,row.Education_Literate,row.Education_Illiterate,row.Education_Total,row.Young_and_Adult,row.Middle_Aged,row.Senior_Citizen,row.Age_Not_Stated,row.Households_with_Bicycle,row.Households_with_Car_Jeep_Van,row.Households_with_Radio_Transistor,row.Households_with_Scooter_Motorcycle_Moped,row.Households_with_Telephone_Mobile_Phone_Landline_only,row.Households_with_Telephone_Mobile_Phone_Mobile_only,row.Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car,row.Households_with_Television,row.Households_with_Telephone_Mobile_Phone,row.Households_with_Telephone_Mobile_Phone_Both,row.Condition_of_occupied_census_houses_Dilapidated_Households,row.Households_with_separate_kitchen_Cooking_inside_house,row.Having_bathing_facility_Total_Households,row.Having_latrine_facility_within_the_premises_Total_Households,row.Ownership_Owned_Households,row.Ownership_Rented_Households,row.Type_of_bathing_facility_Enclosure_without_roof_Households,row.Type_of_fuel_used_for_cooking_Any_other_Households,row.Type_of_latrine_facility_Pit_latrine_Households,row.Type_of_latrine_facility_Other_latrine_Households,row.Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households,row.Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households,row.Not_having_bathing_facility_within_the_premises_Total_Households,row.Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households,row.Main_source_of_drinking_water_Un_covered_well_Households,row.Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households,row.Main_source_of_drinking_water_Spring_Households,row.Main_source_of_drinking_water_River_Canal_Households,row.Main_source_of_drinking_water_Other_sources_Households,row.Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households,row.Location_of_drinking_water_source_Near_the_premises_Households,row.Location_of_drinking_water_source_Within_the_premises_Households,row.Main_source_of_drinking_water_Tank_Pond_Lake_Households,row.Main_source_of_drinking_water_Tapwater_Households,row.Main_source_of_drinking_water_Tubewell_Borehole_Households,row.Household_size_1_person_Households,row.Household_size_2_persons_Households,row.Household_size_1_to_2_persons,row.Household_size_3_persons_Households,row.Household_size_3_to_5_persons_Households,row.Household_size_4_persons_Households,row.Household_size_5_persons_Households,row.Household_size_6_8_persons_Households,row.Household_size_9_persons_and_above_Households,row.Location_of_drinking_water_source_Away_Households,row.Married_couples_1_Households,row.Married_couples_2_Households,row.Married_couples_3_Households,row.Married_couples_3_or_more_Households,row.Married_couples_4_Households,row.Married_couples_5__Households,row.Married_couples_None_Households,row.Power_Parity_Less_than_Rs_45000,row.Power_Parity_Rs_45000_90000,row.Power_Parity_Rs_90000_150000,row.Power_Parity_Rs_45000_150000,row.Power_Parity_Rs_150000_240000,row.Power_Parity_Rs_240000_330000,row.Power_Parity_Rs_150000_330000,row.Power_Parity_Rs_330000_425000,row.Power_Parity_Rs_425000_545000,row.Power_Parity_Rs_330000_545000,row.Power_Parity_Above_Rs_545000,row.Total_Power_Parity))
print("Data inserted to Mysql table successfully!")	

# Commit the insert
connection.commit()