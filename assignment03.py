#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: September 9, 2021
#This program makes a house with two turtles

import turtle
wn = turtle.Screen()
wn.bgcolor("khaki")


tess = turtle.Turtle()
tess.color("darkblue")
tess.pensize(5)

alex = turtle.Turtle()
alex.color("violet")
alex.pensize(5)

for i in range(4):
    tess.forward(100)
    tess.left(90)

alex.left(90)
alex.forward(100)
alex.right(30)
alex.forward(100)

for i in range(2):
    alex.right(120)
    alex.forward(100)

wn.exitonclick()
