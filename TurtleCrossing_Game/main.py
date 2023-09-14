import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("gray")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.go_up, "w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() > 280:
        score.update_score()
        player.reset_position()
        car_manager.speed_fast()

screen.exitonclick()
