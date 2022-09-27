#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: September 29, 2021
#This program draws a python logo

import matplotlib.pyplot as plt
import numpy as np

img = np.zeros((30,30,3))
img[:,:6,0::2] = 1
img[:6,:,0::2] = 1
img[:18,25:,0::2] = 1
img[15:21,:,0::2] = 1

plt.imsave("logo.png", img)
