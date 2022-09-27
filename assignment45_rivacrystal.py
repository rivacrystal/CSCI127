#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: November 9, 2021
#This program shows hotspots of NYC

import folium
import pandas as pd

hotspot = pd.read_csv(input("Please enter the name of the input file: "))
name = input("Please enter the name of the output file: ")
mappy = folium.Map(location=[40.785091, -73.968285], tiles="Stamen Watercolor")

borough = input("Please enter the name of the borough: ")
boro = hotspot.groupby("City").get_group(borough)

for index,row in boro.iterrows():
	lat = row["Latitude"]
	lon = row["Longitude"]
	location = row["Location"]
	spot = folium.Marker([lat, lon], popup=location)
	spot.add_to(mappy)

mappy.save(outfile=name)