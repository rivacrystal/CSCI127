#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: October 24, 2021
#This program looks at superbowl data

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(input("Enter name of input file: "))
name = input("Enter name of output file: ")

df["Date"] = pd.to_datetime(df["Date"].apply(str))
df["% Points"] = df["Winner Pts"] / (df["Winner Pts"] + df["Loser Pts"]) * 100

df.plot(x = "Date", y = "% Points")

img = plt.gcf()
img.savefig(name)
