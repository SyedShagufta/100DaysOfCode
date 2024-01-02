import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create a player
player = Player()

# Listen to keys
screen.listen()
screen.onkeypress(player.move, "Up")

# create cars
car_manager = CarManager()

# create a scoreboard object
score_board = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # create and move cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect when the turtle crosses the finish line
    if player.is_at_finishline():
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()

screen.exitonclick()
