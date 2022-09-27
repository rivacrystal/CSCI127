#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: October 9, 2021
#This program makes a spiral of squares

import turtle
wn = turtle.Screen()

riva = turtle.Turtle()
turtle.colormode(255)
riva.speed(0)
riva.pensize(5)
wn.bgcolor("khaki")

for x in range(36):
    riva.pencolor(0,x*7,0)
    riva.forward(10)
    riva.left(10)
    for x in range(4):
        riva.left(90)
        riva.forward(300)
        riva.backward(50)

wn.exitonclick()
