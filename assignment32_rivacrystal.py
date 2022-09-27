#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: October 21, 2021
#This program examines a UFO dataset

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(input("Enter name of input file: "))
name = input("Enter name of output file: ")

state = df.groupby("state")
seconds = state["duration (seconds)"].mean()
data = seconds.sort_values(ascending=False)[:10]

data.plot.bar()
plt.xlabel("State")
plt.ylabel("Seconds")

img = plt.gcf()
img.savefig(name)
