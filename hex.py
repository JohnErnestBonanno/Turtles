#Import Statement
import turtle
my_turtle = turtle.Turtle()

#set speed


#clear screen, move turtle back to initial position
#my_turtle.reset()

distance = 25

def lhex():
    for i in range(0,5):
        my_turtle.fd(distance)
        my_turtle.lt(60)
    my_turtle.fd(distance)
    my_turtle.lt(60)
    return()

def slideup():
    my_turtle.pu()
    my_turtle.lt(120)
    my_turtle.fd(distance)
    my_turtle.rt(60)
    my_turtle.fd(distance)
    my_turtle.rt(60)
    my_turtle.pd()


def rhex():
    for i in range(0,5):
        my_turtle.fd(distance)
        my_turtle.rt(60)
    my_turtle.fd(distance)
    my_turtle.rt(60)
    return()

def slidedown():
    my_turtle.pu()
    for i in range(0,4):
        my_turtle.fd(distance)
        my_turtle.rt(60)
    my_turtle.rt(120)
    my_turtle.pd()

def shiftl2r():
    my_turtle.pu()
    my_turtle.fd(distance)
    my_turtle.lt(60)
    my_turtle.fd(distance)
    my_turtle.rt(60)
    my_turtle.pd()

def hexdown():
    for i in range(0,5):
        rhex()
        slidedown()

def hexup():
    for i in range(0,5):
        lhex()
        slideup()

def main():
    speed = 5
    my_turtle.speed(speed)
    for i in range(0,5):
        hexdown()
        shiftl2r()
        hexup()
        shiftl2r()
        speed += 5
#need to add main funtion that inputs for either hexup() or hexdown() to go
#one more



 #using slide down, can a line of hexagons going down

"""
if turn 120 degrees same direction every time
turtle follows same path around 3 hexagons

if turn 120 degrees, alternating directions
turtuel follows same path around 2 hexagons

"""
#try alternating left and right turns at end of function

def starhex():
    for i in range(0,5):
        my_turtle.fd(distance)
        my_turtle.lt(60)
    my_turtle.fd(distance)
    #call 6 times for starhex
    return()
