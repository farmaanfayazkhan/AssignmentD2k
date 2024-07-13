import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('nyc_taxi_data_2019.db')

# Example query: Average trip distance per month
query = '''
    SELECT strftime('%Y-%m', tpep_pickup_datetime) AS month, AVG(trip_distance) AS avg_trip_distance
    FROM trips
    GROUP BY month
    ORDER BY month
'''
df_avg_trip_distance = pd.read_sql(query, conn)
print(df_avg_trip_distance)

# Example query: Total number of trips per month
query = '''
    SELECT strftime('%Y-%m', tpep_pickup_datetime) AS month, COUNT(*) AS total_trips
    FROM trips
    GROUP BY month
    ORDER BY month
'''
df_total_trips = pd.read_sql(query, conn)
print(df_total_trips)

# Example visualization using matplotlib
import matplotlib.pyplot as plt

# Plotting average trip distance per month
plt.figure(figsize=(10, 6))
plt.plot(df_avg_trip_distance['month'], df_avg_trip_distance['avg_trip_distance'], marker='o')
plt.xlabel('Month')
plt.ylabel('Average Trip Distance (miles)')
plt.title('Average Trip Distance per Month in 2019')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()