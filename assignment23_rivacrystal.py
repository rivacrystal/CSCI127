#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: October 11, 2021
#This program counts the number of white pixels in an image.

import matplotlib.pyplot as plt
import numpy as np

name1 = input("Enter first image name file: ")
name2 = input("Enter second name image file: ")
t = float(input("Enter threshold of white pixels: "))

img1 = plt.imread(name1)
img2 = plt.imread(name2)

countSnow1 = 0
countSnow2 = 0

for x in range(img1.shape[0]):
     for y in range(img1.shape[1]):
          if (img1[x,y,0] > t) and (img1[x,y,1] > t) and (img1[x,y,2] > t):
               countSnow1 = countSnow1 + 1

for x in range(img2.shape[0]):
     for y in range(img2.shape[1]):
          if (img2[x,y,0] > t) and (img2[x,y,1] > t) and (img2[x,y,2] > t):
               countSnow2 = countSnow2 + 1

print("Snow count of first image:", countSnow1)
print("Snow count of second image:", countSnow2)

print("Difference between first and second image:", countSnow1 - countSnow2)
