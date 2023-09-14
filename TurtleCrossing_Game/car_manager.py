from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.create_car()
        self.hideturtle()
        self.car_speed = 5

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(COLORS[random.randint(0, 5)])
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(300, random.randint(-200, 200))
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def speed_fast(self):
        self.car_speed += MOVE_INCREMENT
