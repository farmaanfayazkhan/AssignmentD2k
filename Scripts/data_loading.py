import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('nyc_taxi_data_2019.db')
cur = conn.cursor()

# Create table
cur.execute('''
    CREATE TABLE IF NOT EXISTS trips (
        VendorID INTEGER,
        tpep_pickup_datetime TEXT,
        tpep_dropoff_datetime TEXT,
        passenger_count INTEGER,
        trip_distance REAL,
        RatecodeID INTEGER,
        store_and_fwd_flag TEXT,
        PULocationID INTEGER,
        DOLocationID INTEGER,
        payment_type INTEGER,
        fare_amount REAL,
        extra REAL,
        mta_tax REAL,
        tip_amount REAL,
        tolls_amount REAL,
        improvement_surcharge REAL,
        total_amount REAL,
        congestion_surcharge REAL
    )
''')

# Load cleaned data into the database
df_cleaned = pd.read_csv("cleaned_nyc_taxi_data_2019.csv")
df_cleaned.to_sql('trips', conn, if_exists='replace', index=False)

# Commit and close connection
conn.commit()
conn.close()