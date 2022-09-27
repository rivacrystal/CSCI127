#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: September 12, 2021
#This program makes a rhombus flower

import turtle
wn = turtle.Screen()
wn.bgcolor("khaki")

riva = turtle.Turtle()
riva.shape("turtle")
riva.fillcolor("green")
riva.pensize(3)

for x in range(6):
    riva.forward(100)
    riva.left(45)
    riva.forward(100)
    riva.left(135)
    riva.stamp()
    riva.forward(100)
    riva.left(45)
    riva.forward(100)
    riva.left(195)

wn.exitonclick()
    
