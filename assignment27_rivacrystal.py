#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: October 14, 2021
#This program examines the CSV about NYC COVID cases

import matplotlib.pyplot as plt
import pandas as pd

cases = pd.read_csv("covidCases.csv")
boro = input("Enter borough name: ")
name = input("Enter output name: ")

print("Min:", cases[boro].min())
print("Max:", cases[boro].max())
print("Mean:", cases[boro].mean())
print("Median:", cases[boro].median())
print("Standard deviation:", cases[boro].std())

cases["Fraction"] = cases[boro] / cases["Case Count"]
cases.plot(x = "Date of Interest", y = "Fraction")

img = plt.gcf()
img.savefig(name)
