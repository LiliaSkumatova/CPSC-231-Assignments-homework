# This code sets up the turtle for use in 231
# By Richard Zhao
# This file should not be edited in any way
# Your code should be created in a new, separate file, and
# import this file by using: from turtlesetup import *

import turtle
# Setting up the turtle environment
BACKGROUND_COLOR = "silver"
WIDTH = 1024
HEIGHT = 768
turtle.bgcolor(BACKGROUND_COLOR)
turtle.setup(WIDTH, HEIGHT, 0, 0)
screen = turtle.getscreen()
screen.screensize(WIDTH, HEIGHT)
screen.setworldcoordinates(-WIDTH//2, -HEIGHT//2, WIDTH//2, HEIGHT//2)
screen.delay(delay=0)
turtle.shape("turtle")
turtle.title("Shapes")
turtle.up()
turtle.speed(0)
turtle.setposition(0, 0)
