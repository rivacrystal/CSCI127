#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: November 4, 2021
#This program makes a map with attraction locations on it

import folium
import pandas as pd

attraction = pd.read_csv(input("Enter CSV file name: "))
save_file = input("Enter output file: ")
mappy = folium.Map(location=[40.785091,-73.968285], tiles="Cartodb Positron")

for index,row in attraction.iterrows():
    lon = row["LONGITUDE"]
    lat = row["LATITUDE"]
    name = row["NAME"]
    label = folium.Marker([lat,lon], popup=name)
    label.add_to(mappy)

mappy.save(outfile=save_file)