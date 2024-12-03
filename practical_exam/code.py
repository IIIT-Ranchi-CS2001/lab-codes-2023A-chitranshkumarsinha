import numpy as np
import pandas as pd
data_sett = pd.read_csv("AQI_Data.csv")
print("First five rows of DATASET are:")
print(data_sett.head(5))

print(" ")
print("Last six rows of DATASET are:")
print(data_sett.tail(6))

data_table = pd.DataFrame(data_sett)
summary_statistics = data_table.describe()

print(" ")

print("Summary statistics is:")
print(summary_statistics)
aqi_mean = np.mean(data_sett['AQI'])
PM2_mean = np.mean(data_sett['PM2.5'])
PM10_mean = np.mean(data_sett['PM10'])

print(" ")

print("mean of AQI : ",aqi_mean)
print("mean of PM2.5 : ",PM2_mean)
print("mean of PM10 : ",PM10_mean)


print(" ")
print(" ")

delhi = data_table[data_table["City"] == 'Delhi']
print("all rows with city delhi: ")
print(delhi)

print(" ")

delhi_10rows_specified = delhi.loc[:,['City','AQI','PM2.5']]
print("Top 10 rows with only city,aqi,pm2.5: ")
print(delhi_10rows_specified.head(10))

ar1 = np.array((data_table['AQI'] > 300))
ar2 = np.array((data_table['PM10'] > 200))
condition = data_table[(data_table['AQI'] > 300) & (data_table['PM10'] > 200)]

print(" ")

print("Dataset with api>300 & pm10>400")
print(condition)