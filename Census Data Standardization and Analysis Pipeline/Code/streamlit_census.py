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
select_options=["1. What is the total population of each district?",
                "2. How many literate males and females are there in each district?",
                "3. What is the percentage of workers (both male and female) in each district?",
                "4. How many households have access to LPG or PNG as a cooking fuel in each district?",
                "5. What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?",
                "6. How many households have internet access in each district?",
                "7. What is the educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district?",
                "8. How many households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district?",
                "9. What is the condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility, with latrine facility, etc.) in each district?",
                "10. How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district?",
                "11. What is the total number of households in each state?",
                "12. How many households have a latrine facility within the premises in each state?",
                "13. What is the average household size in each state?",
                "14. How many households are owned versus rented in each state?",
                "15. What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?",
                "16. How many households have access to drinking water sources near the premises in each state?",
                "17. What is the average household income distribution in each state based on the power parity categories?",
                "18. What is the percentage of married couples with different household sizes in each state?",
                "19. How many households fall below the poverty line in each state based on the power parity categories?",
                "20. What is the overall literacy rate (percentage of literate population) in each state?"
                ]
option_selected=st.selectbox("select a query",options=select_options)
if option_selected == "1. What is the total population of each district?":
    query_selected="select district, sum(population) as sum_population from census group by district"
    st.title("Population")

elif option_selected == "2. How many literate males and females are there in each district?":
    query_selected="select district, sum(Literate_Male) as Literate_Male, sum(Literate_Female) as Literate_Female  from census group by district"
    st.title("Literate")

elif option_selected == "3. What is the percentage of workers (both male and female) in each district?":
    query_selected="select District, (sum(Workers)/sum(Population))*100 as workers_percentage from census group by District"
    st.title("Percentage of workers")

elif option_selected == "4. How many households have access to LPG or PNG as a cooking fuel in each district?":
    query_selected="Select district, sum(LPG_or_PNG_House) as LPG_or_PNG_House from census group by district;"
    st.title("LPG or PNG Households")

elif option_selected == "5. What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?":
    query_selected="Select district, sum(Hindus) as Hindus,	sum(Muslims) as Muslims, sum(Christians) as Christians, sum(Sikhs) as Sikhs, sum(Buddhists) as Buddhists, sum(Jains) as Jains, sum(Others_Religions) as Others_Religions from census group by district;"
    st.title("Religious Composition")

elif option_selected == "6. How many households have internet access in each district?":
    query_selected="Select district, sum(House_with_Internet) as House_with_Internet from census group by district"
    st.title("Households with Internet Access")

elif option_selected == "7. What is the educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district?":
    query_selected="select District,sum(Education_Below_Primary) as Below_Primary,sum(Education_Primary) as Ed_Primary,sum(Education_Middle) as Middle,sum(Education_Secondary_) as Secondary,sum(Education_Higher) as Higher,sum(Education_Graduate) as Graduate,sum(Education_Other) as Other from census group by District"
    st.title("Educational Attainment Distribution")

elif option_selected == "8. How many households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district?":
    query_selected="Select District,sum(House_with_Bicycle) as Bicycle,	sum(House_with_Car_Jeep_Van) as Car_Jeep_Van,sum(House_with_Scooter_Motorcycle_Moped) as Scooter_Motorcycle_Moped from census group by District;"
    st.title("Modes of Transportation")

elif option_selected == "9. What is the condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility, with latrine facility, etc.) in each district?":
    query_selected="select District,sum(Condition_of_occ_census_houses_Dilapidated_House) as Dipilated,sum(House_with_separate_kitchen_Cooking_inside_house) as Separate_kitchen,sum(Having_bathing_fac_Total_House) as bathing_facility,sum(Having_latrine_fac_within_the_premises_Total_House) as latrine_facility from census group by District;"
    st.title("Condition of Occupied census houses")
	
elif option_selected == "10. How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district?":
    query_selected="select District, sum(Household_size_1_person_House) as 1_person,sum(Household_size_2_persons_House) as 2_person,sum(Household_size_3_persons_House) as 3_person,sum(Household_size_4_persons_House) as 4_person,sum(Household_size_5_persons_House) as 5_person,sum(Household_size_6_8_persons_House) as 6_8_person,sum(Household_size_9_persons_and_above_House) as 9_above_person	from census group by District;"
    st.title("Household Size Distribution")
	
elif option_selected == "11. What is the total number of households in each state?":
    query_selected="Select State_UT, sum(House) as Households from census group by State_UT;"
    st.title("Households in each state")
	
elif option_selected == "12. How many households have a latrine facility within the premises in each state?":
    query_selected="Select State_UT, sum(Having_latrine_fac_within_the_premises_Total_House) as Within_premise_latrine from census group by State_UT;"
    st.title("Latrine Facitlity within each state")
    	
elif option_selected == "13. What is the average household size in each state?":
    query_selected="select state_ut, sum(Population)/sum(Household_size_1_to_2_persons+Household_size_3_to_5_persons_House+Household_size_6_8_persons_House+Household_size_9_persons_and_above_House) as Average_household_size from census group by state_ut;"
    st.title("Avg Household size")
	
elif option_selected == "14. How many households are owned versus rented in each state?":
    query_selected="Select State_UT, sum(Ownership_Owned_House) as Owned_House, sum(Ownership_Rented_House) as Rented_House from census group by State_UT;"
    st.title("Owned vs Rented Households")

elif option_selected == "15. What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?":
    query_selected="Select State_UT, sum(Having_latrine_fac_within_the_premises_Total_House) as within_premise, sum(Type_of_latrine_fac_Pit_latrine_House) as pit_latrine, sum(Type_of_latrine_fac_Other_latrine_House) as other_latrine, sum(Type_of_latrine_fac_Night_soil_disposed_into_open_drain_House) as night_soil_disposed, sum(Type_of_latrine_fac_flush_latrine_conect_to_other_system_House) as flush_latrine, sum(Not_having_latrine_fac_within_the_prem_Alter_source_Open_House) as within_premise_alternate from census group by State_UT;"
    st.title("Latrine Facilities")

elif option_selected == "16. How many households have access to drinking water sources near the premises in each state?":
    query_selected="Select State_UT, sum(Location_of_water_source_Near_the_premises_House) as Drinking_water_near_the_premise from census group by State_UT;"
    st.title("Drink water source near the premises")

elif option_selected == "17. What is the average household income distribution in each state based on the power parity categories?":
    query_selected="select state_ut, (sum(Power_Parity_Less_than_Rs_45000)/sum(House))*100 as less_than_45k,(sum(Power_Parity_Rs_45000_150000)/sum(House))*100 as 45k_150k,(sum(Power_Parity_Rs_150000_330000)/sum(House))*100 as 150k_330k,(sum(Power_Parity_Rs_330000_545000)/sum(House))*100 as 330k_545k,(sum(Power_Parity_Above_Rs_545000)/sum(House))*100 as above_545k from census group by state_ut;"
    st.title("Average household income distribution")

elif option_selected == "18. What is the percentage of married couples with different household sizes in each state?":
    query_selected="select state_ut,(sum(Married_couples_1_House)/sum(Married_couples_1_House+Married_couples_2_House+Married_couples_3_House+Married_couples_3_or_more_House))*100 as 1_household,(sum(Married_couples_2_House)/sum(Married_couples_1_House+Married_couples_2_House+Married_couples_3_House+Married_couples_3_or_more_House))*100 as 2_household,(sum(Married_couples_3_House)/sum(Married_couples_1_House+Married_couples_2_House+Married_couples_3_House+Married_couples_3_or_more_House))*100 as 3_household,(sum(Married_couples_4_House)/sum(Married_couples_1_House+Married_couples_2_House+Married_couples_3_House+Married_couples_3_or_more_House))*100 as 4_household,(sum(Married_couples_5__House)/sum(Married_couples_1_House+Married_couples_2_House+Married_couples_3_House+Married_couples_3_or_more_House))*100 as 5_household from census group by state_ut;"
    st.title("Percentage of married couple with different household sizes")

elif option_selected == "19. How many households fall below the poverty line in each state based on the power parity categories?":
    query_selected="select state_ut, (sum(Power_Parity_Less_than_Rs_45000)/sum(house))*100 as households_below_poverty_line from census group by state_ut;"
    st.title("Households below poverty line")

elif option_selected == "20. What is the overall literacy rate (percentage of literate population) in each state?":
    query_selected="select State_UT, (sum(Literate)/sum(Population))*100 as Literacy_rate from census group by State_UT;"
    st.title("Overall Literacy Rate")

cursor.execute(query_selected)
records = cursor.fetchall()
records_df=pd.DataFrame(records,columns=cursor.column_names)
st.dataframe(records_df)