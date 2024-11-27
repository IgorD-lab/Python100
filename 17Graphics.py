from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

tim = Turtle()
tim.color("black")

# # Square
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# # Dotted line
# for steps in range(100):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# # Shapes
# for side in range(3, 11):
#     tim.color(random.choice(colours))
#     for _ in range(side):
#         degree = 360 / side
#         tim.right(degree)
#         tim.forward(100)

# Random Walk
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()