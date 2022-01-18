"""
This code will allow me to control a turtle using arrows.
I will also add a simple background to the user interface
24 June, 2020
"""
import turtle

window = turtle.getscreen()
x = turtle.Turtle()
y = turtle.Turtle()
z = turtle.Turtle()
j = 1
#----------------------------------------------------------------------------------------------------------------------
window.bgcolor("lightblue")
x.color("white")
y.color("black")
z.color("dark blue")
#----------------------------------------------------------------------------------------------------------------------
z.lt(90)  # LEFT
for i in range (50):
    x.fd(5) #FORWARD
    y.bk(5) #BACKWARD
    for p in range (1000000):
        # This is a delayer
        j = j+1

z.speed(1)
z.fd(100)  # FORWARD