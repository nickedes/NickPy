# create a histogram displaying the frequency of flights by distance.
#
#As per data used from CSV files.
import geo_distance
import csv
import numpy as np
import matplotlib.pyplot as plt

distances = []
latitudes = {}
longitudes = {}
f = open("data/airports.dat")
for row in csv.reader(f):
    airport_id = row[0]
    latitudes[airport_id] = float(row[6])
    longitudes[airport_id] = float(row[7])
f = open("data/routes.dat")    
for row in csv.reader(f):
    source_airport = row[3]
    dest_airport = row[5]
    if source_airport in latitudes and dest_airport in latitudes:
        source_lat = latitudes[source_airport]
        source_long = longitudes[source_airport]
        dest_lat = latitudes[dest_airport]
        dest_long = longitudes[dest_airport]
        distances.append(geo_distance.distance(source_lat,source_long,dest_lat,dest_long))

plt.hist(distances, 100, facecolor='r')
plt.xlabel("Distance (km)")
plt.ylabel("Number of flights")
plt.show()