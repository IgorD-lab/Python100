import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.color("black")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
directions = [0, 90, 180, 270]
turtle.colormode(255)
tim.pensize(2)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# Square
def draw_square():
    for _ in range(4):
        tim.forward(100)


# Dotted line
def dotted_line():
    for steps in range(100):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


# Shapes
def shapes():
    for side in range(3, 11):
        tim.color(random.choice(colours))
        for _ in range(side):
            degree = 360 / side
            tim.right(degree)
            tim.forward(100)


# Random Walk
def random_walk():
    tim.pensize(15)
    tim.speed("fastest")

    for _ in range(2000):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))


# Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


screen = Screen()
screen.exitonclick()
