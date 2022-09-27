# Name: Riva Crystal
# Email: riva.crystal@gmail.com
# Date: September 21, 2021
# This program allows you to make petals

import turtle

turtle.colormode(255)
riva = turtle.Turtle()
riva.shape("turtle")

for i in range(0,255,10):
     riva.forward(10)
     riva.pensize(i)
     riva.color(255,255-i,0)

riva.penup()
riva.color(0,0,0)
riva.pensize(0)
riva.backward(260)
riva.right(90)
riva.pendown()

for i in range(0,255,10):
     riva.forward(10)
     riva.pensize(i)
     riva.color(255,255-i,0)
