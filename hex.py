#Import Statement
import turtle
my_turtle = turtle.Turtle()

#set speed
my_turtle.speed(2)

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
    my_turtle.lt(120)
    my_turtle.fd(distance)
    my_turtle.rt(60)
    my_turtle.fd(distance)
    my_turtle.rt(60)

def rhex():
    for i in range(0,5):
        my_turtle.fd(distance)
        my_turtle.rt(60)
    my_turtle.fd(distance)
    my_turtle.rt(60)
    return()

def slidedown():
    for i in range(0,4):
        my_turtle.fd(distance)
        my_turtle.rt(60)
    my_turtle.rt(120)

def shiftl2r():
    my_turtle.fd(distance)
    my_turtle.lt(60)
    my_turtle.fd(distance)
    my_turtle.rt(60)

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
