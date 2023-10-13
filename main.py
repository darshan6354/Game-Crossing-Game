from turtle import Turtle, Screen
import time
from player import Player
from car import Cars
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

p1 = Player()
cars = Cars()
scorebooard = Scoreboard()
screen.onkeypress(p1.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.make_cars()
    cars.move_cars()
    # Detect collision with car
    for moving_car in cars.car_list:
        if p1.distance(moving_car) < 28:
            game_is_on = False

    # Detect successful crossing of turtle
    if p1.ycor() > 270:
        p1.successful_crossing()
        scorebooard.level += 1
        scorebooard.update_scoreboard()
        cars.update_level()

screen.exitonclick()
