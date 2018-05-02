#Import Statement
import turtle
my_turtle = turtle.Turtle()

#set speed


#clear screen, move turtle back to initial position
#my_turtle.reset()

#distance = 25
#vertdist = 2
#hordist = 2

def lhex(distance):
    for i in range(0,5):
        my_turtle.fd(distance)
        my_turtle.lt(60)
    my_turtle.fd(distance)
    my_turtle.lt(60)
    return()

def slideup(distance):
    my_turtle.pu()
    my_turtle.lt(120)
    my_turtle.fd(distance)
    my_turtle.rt(60)
    my_turtle.fd(distance)
    my_turtle.rt(60)
    my_turtle.pd()


def rhex(distance):
    for i in range(0,5):
        my_turtle.fd(distance)
        my_turtle.rt(60)
    my_turtle.fd(distance)
    my_turtle.rt(60)
    return()

def slidedown(distance):
    my_turtle.pu()
    for i in range(0,4):
        my_turtle.fd(distance)
        my_turtle.rt(60)
    my_turtle.rt(120)
    my_turtle.pd()

def shiftl2r(distance):
    my_turtle.pu()
    my_turtle.fd(distance)
    my_turtle.lt(60)
    my_turtle.fd(distance)
    my_turtle.rt(60)
    my_turtle.pd()

def hexdown():
    for i in range(0,vertdist):
        rhex()
        slidedown()

def hexup():
    for i in range(0,vertdist+1):
        lhex()
        slideup()

def main(distance, vertdist, hordist):
    speed = 5
    my_turtle.speed(speed)
    hexdown()
    shiftl2r(distance)
    hexup()
    shiftl2r(distance)
    #speed += 5
#need to add main funtion that inputs for either hexup() or hexdown() to go
#one more

#make simple case function saying this is your number, and then another main function calling it.  Need
#to figure out what can get refewrenced where.  Or need to simplfy the above to make sure I get hexdown/hexup
#working how I want it to 


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
