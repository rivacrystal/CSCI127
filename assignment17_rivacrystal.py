#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: September 29, 2021
#This program stamps in a spiral(?)

import turtle

stamps = int(input("Enter number of stamps the turtle will print:"))

riva = turtle.Turtle()
turtle.colormode(255)
riva.shape("circle")
riva.penup()
steps, red, green, blue = 10, 186, 164, 145
riva.color(red, green, blue)

for x in range(stamps):
    riva.stamp()
    steps += 2
    if red + 3 <= 255 and green + 3 <= 255 and blue + 3 <= 255:
        red, green, blue = red + 3, green + 3, blue + 3
    riva.color(red, green, blue)
    riva.forward(steps)
    riva.right(24)
