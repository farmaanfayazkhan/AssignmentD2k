# NYC Taxi Trip Analysis

This project aims to analyze the New York City taxi trip data for the year 2019. The analysis includes data download, cleaning, loading into an SQLite database, SQL querying for insights, and visualization of findings.

## Project Structure

- **data_download.py**: Python script to automate the download of the NYC Taxi Trip dataset for 2019.
- **data_cleaning.py**: Script for cleaning and transforming the downloaded dataset using Pandas.
- **data_loading.py**: Script to load the cleaned data into an SQLite database using SQLAlchemy.
- **data_analysis.py**: Python script containing SQL queries and visualizations to derive insights from the data.
- **README.md**: This file, providing an overview of the project, its structure, and instructions.

# Requirements

- Python 3.x
-Pandas

## Steps

1. Data Download:
   - Run `python data_download.py` to fetch the NYC Taxi Trip dataset for 2019.

2. Data Cleaning and Transformation:
   - Execute `python data_cleaning.py` to clean and preprocess the dataset, handling missing values and data anomalies.

3. Data Loading:
   - Run `python data_loading.py` to load the cleaned dataset into an SQLite database named `nyc_taxi.db`.

4. Data Analysis:
   - Execute `python data_analysis.py` to perform SQL queries and visualize insights:
     - Peak Hours for Taxi Usage
     - Passenger Count vs. Trip Fare
     - Trends in Taxi Usage Over the Year

5. Visualizations:
   - Visualizations generated by `data_analysis.py` will be displayed using Matplotlib.

# Please call on 9541385900 for any questions. 
