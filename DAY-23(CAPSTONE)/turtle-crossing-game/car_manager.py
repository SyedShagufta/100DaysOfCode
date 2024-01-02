import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        num = random.randint(1, 6)
        if num == 6:
            new_car = Turtle("square")
            new_car.penup()
            new_car.turtlesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))

            # Check for overlapping with existing cars
            is_overlapping = True
            while is_overlapping:
                random_y = random.randrange(-250, 250, 30)
                new_car.goto(300, random_y)
                is_overlapping = any(new_car.distance(car) < 40 for car in self.all_cars)

            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            # Remove the unwanted cars
            if car.xcor() > 350:
                self.all_cars.remove(car)

    def level_up(self):
        self.car_speed += 5
