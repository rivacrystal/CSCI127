#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: October 27, 2021
#This program looks at video game sales

import pandas as pd

vg = pd.read_csv(input("Enter file name: "))

print("There are", vg["Name"].count(), "total games.")
print("The number of games in each genre is")
print(vg["Genre"].value_counts())
print("The top 3 game publishers are")
print(vg["Publisher"].value_counts()[:3])
