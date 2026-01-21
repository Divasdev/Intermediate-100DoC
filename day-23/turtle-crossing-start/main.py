import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard






#Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north
screen = Screen()
car=CarManager()
player=Player()

scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move,"Up")
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:


    car.create_car()
    car.move_car()
    for single_car in car.all_cars:
        if single_car.distance(player.turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.at_finish_line():
        player.reset_position()
        car.increase_speed()
        scoreboard.increase_level()
    time.sleep(0.1)
    screen.update()
