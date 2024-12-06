from turtle import Turtle

DEFAULT_BALL_SPEED = 0.1
BALL_SPEED_INCREASE = 0.9


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = DEFAULT_BALL_SPEED

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= BALL_SPEED_INCREASE

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = DEFAULT_BALL_SPEED
        self.bounce_x()
