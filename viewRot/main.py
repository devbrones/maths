import numpy
import turtle
import json
from tkinter import *

# Set up Turtle and window
turtle.setup(750, 750)  # Determine the window size
wn = turtle.Screen()  # Get a reference to the window
wn.title("viewRot")  # Change the window title
wn.bgcolor("black")  # Set the background color
bob = turtle.Turtle()  # Create our favorite turtle
bob.color("green")
bob.speed(10000)
bob.hideturtle()


with open("config.json") as j:
    js = json.load(j)


print(js)
arr = []
for x in range(0, js[0]['NFRM']):
    y = js[0]['FLEN']/((2*numpy.pi)*(js[0]['FRAO'] + (x * js[0]['FTHN'])))
    print(str(str(x) + " :: " + str(y)))
    arr.append(y)

# flags
tot = 0
# radius of circle
radius = 250


def drawline(pangle, rad, t, index):
    global tot
    tot += pangle
    t.setheading(tot)
    t.forward(rad)
    t.penup()
    t.forward(20)
    t.write(str(index))
    t.backward(20)
    t.pendown()
    t.goto(0, 0)


#draw circle
bob.setheading(270)
bob.penup()
bob.forward(radius)
bob.setheading(0)
bob.pendown()
bob.circle(radius)
bob.penup()
bob.goto(0,0)
bob.pendown()

n=0
#number of cogs
d=36

while n <= d:
    bob.setheading(n*(360/d))
    bob.penup()
    bob.forward(radius)
    bob.pendown()
    bob.forward(10)
    bob.penup()
    bob.goto(0,0)
    bob.pendown()
    n += 1


multiplier = wn.textinput("Multipiler", "Enter Multiplier:")


for i in range(0, js[0]['NFRM']):
    drawline(arr[i]*int(multiplier), radius, bob, i)


ts = bob.getscreen()
ts.getcanvas().postscript(file="out.eps")

turtle.done()
