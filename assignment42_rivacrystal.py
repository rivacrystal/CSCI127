#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: November 4, 2021
#This program makes a map of NYC

import folium

nyc = folium.Map(location=[40.75, -74.125])
marker = folium.Marker([40.7420577, -74.0101494], popup="Little Island")
marker.add_to(nyc)

nyc.save(outfile="nycMap.html")