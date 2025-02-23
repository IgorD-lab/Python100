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


def paint():
    import colorgram

    # colors = colorgram.extract("./resources/images/hirst.jpg", 31)
    #
    # list_colors = []
    #
    # for color in colors:
    #     rgb = color.rgb
    #     red = rgb.r
    #     green = rgb.g
    #     blue = rgb.b
    #     values = (red, green, blue)
    #     list_colors.append(values)

    list_colors = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83),
                   (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
                   (9, 67, 47),
                   (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186),
                   (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82),
                   (46, 73, 62), (47, 66, 82), (115, 134, 139)]
    turtle.colormode(255)
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()

    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1):
        tim.dot(20, random.choice(list_colors))
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


screen = Screen()
screen.exitonclick()
