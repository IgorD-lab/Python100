import time
from turtle import Screen
from resources.PongGame.paddle import Paddle
from resources.PongGame.ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up, "w")
screen.onkey(r_paddle.move_down, "s")
screen.onkey(l_paddle.move_up, "Up")
screen.onkey(l_paddle.move_down, "Down")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

screen.exitonclick()
