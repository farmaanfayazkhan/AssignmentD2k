import pandas as pd

# Read the CSV file into a DataFrame
#the actual files in the website have been changed to parquet format, we can use commands like spark.read.format('parquet').load('fileloc')
#I'm assuming here the files are CSV
df = pd.read_csv('./data/nyc_taxi_data_2019.csv')

# Drop rows with missing values or nulls  (NaNs) inplace
#inplace will make sure that df dataframe itself is changed rather than creating another dataframe where the change would be refelcted
df.dropna(inplace=True)

# Converting  'pickup_datetime' column to datetime format
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])

# Need to add more transformations and add new columns 