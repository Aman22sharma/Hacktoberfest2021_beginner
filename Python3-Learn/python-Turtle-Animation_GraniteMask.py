"""
AUTHOR: Ratnadeep Das Choudhury
Python3 Concept: Python Animation of a Star using Turtle Library
GITHUB: https://github.com/GraniteMask

It's a program to draw a star which constitutes of 5 small stars. Python turtle library has been used to achieve this.
"""

import turtle

pegasus=turtle.Turtle()
pegasus.getscreen().bgcolor("Green")

pegasus.penup()
pegasus.goto((-200,100))
pegasus.pendown()

def star(turtle,size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)
        turtle.end_fill()

star(pegasus,360)