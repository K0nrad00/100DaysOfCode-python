import time
from turtle import Screen
from player import Player, STARTING_POSITION, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard
# from random import randint

#OUTLINE OF PROJECT (from https://www.udemy.com/course/100-days-of-code/learn/lecture/20343209#overview
"""
1. A turtle moves forwards when you press the "Up" key. 
It can only move forwards, not back, left or right.

2. Cars are randomly generated along the y-axis and will move from 
the right edge of the screen to the left edge.

3. When the turtle hits the top edge of the screen, 
it moves back to the original position and the player levels up. On the next level, the car speed increases.

4. When the turtle collides with a car, it's game over and everything stops.
"""


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle crossing!")

my_turtle = Player()
screen.listen()
screen.onkey(my_turtle.move, "Up")

car_manager = CarManager()

score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # Detect collision with the car
    for car in car_manager.car_fleet:
        if my_turtle.distance(car) < 20:
            game_is_on = False
            # score.update_scoreboard()
            my_turtle.goto(STARTING_POSITION)
            score.game_over()

    if my_turtle.ycor() > FINISH_LINE_Y:
        my_turtle.goto(STARTING_POSITION)
        car_manager.increase_speed()
        score.level_up()

screen.exitonclick()



