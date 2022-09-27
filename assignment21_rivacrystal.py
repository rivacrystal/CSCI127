#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: October 7, 2021
#This program makes an image of khaki and rosy stripes

import matplotlib.pyplot as plt
import numpy as np

num = int(input("Enter a size: "))
name = input("Enter a file: ")

img = np.ones((num,num,3))
img[1::2,:,0] = 0.94
img[1::2,:,1] = 0.90
img[1::2,:,2] = 0.55
img[:,1::2,0] = 0.73
img[:,1::2,1] = 0.56
img[:,1::2,2] = 0.56

plt.imsave(name, img)
