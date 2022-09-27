#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: October 28, 2021
#This program makes a turtle tree

import turtle

def setUp():
    riva = turtle.Turtle() #1. instiantiate turtle
    riva.hideturtle() #2. hide trutle
    riva.setheading(90) #3. set heading
    riva.speed(speed=0) #4. set speed
    return riva #5. return turtle

def fractalLeft(t,distance,i):
    if distance > 10: #if distance is greater than 10
        i = i % 255 #1. set value of i to be i % 255
        t.color(0,i,0) #2. set color to be value of i in the green channel
        t.left(30) #3. turn left 30 degrees
        t.forward(distance) #4. move forward "distance"
        t.stamp() #5. stamp
        newDistance = distance-5 #6. set value of "newDistance" to distance-5
        fractalLeft(t,newDistance,i+25) #7. call fractalLeft (LEFT!!)
        t.backward(distance) #8. move backward "distance"
        t.right(30) #9. turn right 30 degrees
        fractalRight(t,newDistance,i+25) #call fractal right (RIGHT!!)

def fractalRight(t,distance,i):
    if distance > 10: #if distance is greater than 10
        i = i % 255 #1. set value of i to be i % 255
        t.color(0,i,0) #2. set color to be value of i in green channel
        t.right(30) #3. turn right 30 degrees
        t.forward(distance) #4. move forward "distance"
        t.stamp() #5. move forward "distance"
        newDistance = distance-5 #6. set value of "newDistance" to distance-5
        fractalRight(t,newDistance,i+25) #7. call fracticalRight (RIGHT!!)
        t.backward(distance) #8. move backward "distance"
        t.left(30) #9. turn left 90 degrees
        fractalLeft(t,newDistance,i+25) #call fractalLeft (LEFT!!))

    ###################################
    ### FILL IN YOUR CODE HERE      ###
    ### Other than your name above, ###
    ### these are the only sections ###
    ### you change in this program. ###
    ###################################




############################################################################################

    
def main():
    ###################################
    ###    DON'T CHANGE THIS: vvv   ###
    ###################################
    t = setUp()
    turtle.colormode(255)
    turtle.bgcolor("khaki")
    t.forward(50)
    fractalRight(t,50,0)
    fractalLeft(t,50,0)

if __name__ == "__main__":
    main()
