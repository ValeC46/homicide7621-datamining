import pandas as pd

data = pd.read_csv('csv/rawdata.csv')

#print(data.head())

#Clean City Name
temp = data['CNTYFIPS'].str.split(",", n=1, expand=True)

data.rename(columns={'CNTYFIPS':'City'}, inplace=True)

data['City'] = temp[0]
#print(data.head())

#print(data[["City", "Year", "Month"]].tail())

#Creates a DATE column
data['Date'] = pd.to_datetime(data['Year'].map(str) + "/" + data['Month'].map(str), yearfirst= True)

data.drop(columns=['ID', 'VicEthnic', 'OffEthnic'], inplace=True)
data.rename(columns={'Agentype':'Agency'}, inplace=True)

#print(data[["City", "Year", "Month", "Date"]].tail())

data.to_csv('csv/cleandata.csv', index=False)