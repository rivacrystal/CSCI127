#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: September 21, 2021
#This makes a colored turtle square

import turtle

color = input("Please enter a 6-digit Hexadeimal number:")
userinput = ("#" + color)

wn = turtle.Screen()

riva = turtle.Turtle()
riva.shape("turtle")
riva.color(userinput)

for x in range(4):
    riva.stamp()
    riva.left(90)
    riva.forward(100)

wn.exitonclick()
