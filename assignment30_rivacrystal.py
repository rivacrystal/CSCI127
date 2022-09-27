#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: October 14, 2021
#This program looks at a ramen dataset

import pandas as pd

ramen = pd.read_csv(input("Enter file name: "))

style = ramen.groupby("Style")

singapore = ramen.groupby("Country").get_group("Singapore")
brand = singapore.groupby("Brand")["Stars"].idxmin()

print("The average stars per serving style:")
print(style["Stars"].mean())
print(brand.idxmin(), "has the lowest rating in Singapore with", singapore["Stars"].min(), "stars")
