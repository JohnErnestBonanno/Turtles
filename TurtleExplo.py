#Import Statement
import turtle

my_turtle = turtle.Turtle()


#set speed
my_turtle.speed(2)

"""
distance = 100
#move turtle in a square
#def square(distance):
for x in range(0,4):
    my_turtle.fd(distance)
    my_turtle.rt(90)
my_turtle.circle(100)
my_turtle.stamp()
"""

"""
#increasing spiral
distance = 10
for x in range(0,50):
    my_turtle.fd(distance)
    my_turtle.rt(90)
    distance += 3
"""

#fill in the box
turtle.title("My Turtle")

distance = 50
while distance > 0:
    my_turtle.fd(distance)
    my_turtle.rt(50)
    distance = distance - 1

turtle.exitonclick()
