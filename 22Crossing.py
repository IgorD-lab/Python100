import time
from turtle import Screen
from resources.TurtleGame.player import Player, STARTING_POSITION
from resources.TurtleGame.car_manager import CarManager
from resources.TurtleGame.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.delay(0)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.move, "w")
screen.listen()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Finish detection
    if player.check_finish():
        player.goto(STARTING_POSITION)
        car_manager.level_up()
        scoreboard.increase_level()

    # Car collision detection
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
