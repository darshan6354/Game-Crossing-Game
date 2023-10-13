from turtle import Turtle
import random

COLOUR = ["red", "yellow", "green", "pink", "brown", "blue", "black", "orange", "purple", "cyan"]


class Cars:
    def __init__(self):
        self.car_list = []
        self.move_increment = 5
        self.chance_end = 6
        

    def create_lane(self):
        lane_list = []
        for num in range(-250, 250):
            if num % 30 == 0:
                lane_list.append(num)
        lane_list.remove(0)
        print(lane_list)
        return lane_list

    def make_cars(self):
        lane_list = self.create_lane()
        self.chance = random.randint(0, self.chance_end)
        if self.chance == 1:
            lane = random.choice(lane_list)
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLOUR))
            new_car.goto(x=300, y=lane)
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(self.move_increment)

    def update_level(self):
        self.move_increment += 3
        while self.chance_end >= 2:
            self.chance_end -= 1
        for car in self.car_list:
            car.forward(self.move_increment)
