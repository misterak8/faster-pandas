"""Using "bikes.db", find the 5 bikes (using "bike_id") that has the biggest
90% quantile of ride duration in the first quarter of 2017.
"""
#import sqlite3
#import pandas as pd

# Connect to the database
#conn = sqlite3.connect('bikes.db')
# Check table names in db
#query = "SELECT name FROM sqlite_master WHERE type='table'"

# Load the data and filter to first quarter of 2017
#query = "SELECT * FROM bike_rides"

#query = "SELECT * FROM rides WHERE start_time BETWEEN '2017-01-01' AND '2017-03-31'"
#df = pd.read_sql(query, conn)
#print(df.head())

# Calculate 90% quantile of ride duration for each bike
#quantiles = df.groupby('bike_id')['duration'].quantile(0.9)

# Sort bikes by quantile and select top 5
#top_bikes = quantiles.sort_values(ascending=False).head(5)

#print(top_bikes)


import sqlite3
import pandas as pd

# create a connection to the database
conn = sqlite3.connect('bikes.db')

# define the SQL query to filter the first quarter of 2017
query = """
        SELECT * 
        FROM bike_rides
        WHERE year = 2017 AND month IN (1, 2, 3)
        """

# read the data from the database into a DataFrame
df = pd.read_sql(query, conn)

# calculate the 90th percentile of ride duration for each bike_id
quantiles = df.groupby('bike_id')['duration'].quantile(0.9)

# sort the quantiles in descending order and take the top 5 bike_ids
top_bikes = quantiles.sort_values(ascending=False).head(5)

# print the top 5 bike_ids and their corresponding 90th percentile ride durations
print(top_bikes)
