"""Using vaex, calculate the mean taxi ride distance in "taxi.csv.xz" per
VendorID.
"""
import vaex

csv_file = 'taxi.csv.xz'
time_cols = ['tpep_pickup_datetime','tpep_dropoff_datetime']
# Load the dataframe
vdf = vaex.read_csv(csv_file,parse_dates=time_cols)

# Display the first 5 rows
#print(vdf.head(5))

# Calculate the mean taxi ride distance per VendorID
mean_distance = vdf.groupby(vdf.VendorID).agg({'trip_distance': 'mean'})
print(mean_distance)

