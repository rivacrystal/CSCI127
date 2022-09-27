#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: October 20, 2021
#This program looks at homeless data

import pandas as pd
import matplotlib.pyplot as plt

homeless = pd.read_csv(input("Enter name of input file: "))
img = input("Enter name of output file: ")

homeless["Fraction Single Adults"] = homeless["Total Single Adults in Shelter"] / homeless["Total Individuals in Shelter"]

homeless.plot(x = "Date of Census", y = "Fraction Single Adults")

fig = plt.gcf()
fig.savefig(img)
