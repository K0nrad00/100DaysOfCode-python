from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.car_fleet = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_car_generation_frequency = randint(1,6) # to reduce number of cars generated
        if random_car_generation_frequency == 1:
            new_car = Turtle("square")
            new_car.pu()
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_coor = randint(-250, 250)
            new_car.goto(300, y_coor)
            self.car_fleet.append(new_car)


    def move_cars(self):
        for car in self.car_fleet:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT



