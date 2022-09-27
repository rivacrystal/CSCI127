#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: September 25, 2021
#This program loads an image, displays it, and gives it a yellow tinge

import matplotlib.pyplot as plt
import numpy as np

image = input("Enter name of the input file:")
img = plt.imread(image)

img2 = img.copy()
img2[:,:,2] = 0

image2 = input("Enter name of the output file:")
plt.imsave(image2, img2)  #Save the image we created to the file: reds.png
