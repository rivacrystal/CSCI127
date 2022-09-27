#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: November 12, 2021
#This program makes a 10x10 image for a user

import matplotlib.pyplot as plt
import numpy as np

print("""------------------------------------------
Welcome to the Color Maker!
------------------------------------------
Please enter for each rbg color the value in which to increase/decrease them.
If all 3 values given are 0, the program will end and save the resulting image.\n""")

name = input("Enter file name: ")

img = np.zeros((10,10,3))

r = 0
g = 0
b = 0

while True:
    red = float(input("How much do you want to change the red value by? "))
    green = float(input("how much do you want to change the green value by? "))
    blue = float(input("How much do you want to change the blue value by? "))

    if red == 0 and green == 0 and blue == 0:
    	break

    r += red/255
    if r < 0:
        r = 0
    if r > 1:
        r = 1
    g += green/255
    if g < 0:
        g = 0
    if g > 1:
        g = 1
    b += blue/255
    if b < 0:
        b = 0
    if b > 1:
        b = 1
    
    print("The current rgb values are:", r, g, b)

img[:,:,0] = float(r)
img[:,:,1] = float(g)
img[:,:,2] = float(b)

print("You're done! Congrats on the color, it looks beautiful!")

plt.show()
plt.imsave(name, img)
