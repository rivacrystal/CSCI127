#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: September 12, 2021
#This program makes a pinwheel

import turtle
wn = turtle.Screen()

riva = turtle.Turtle()
riva.color("purple")
riva.shape("arrow")
riva.pensize(3)

riva.forward(30)

for x in range(3):
 riva.forward(50)
 riva.right(120)

riva.backward(30)
riva.right(90)
riva.forward(30)

for x in range(3):
 riva.forward(50)
 riva.right(120)

riva.backward(30)
riva.right(90)
riva.forward(30)

for x in range(3):
 riva.forward(50)
 riva.right(120)

riva.backward(30)
riva.right(90)
riva.forward(30)

for x in range(3):
 riva.forward(50)
 riva.right(120)

riva.backward(30)

wn.exitonclick()
