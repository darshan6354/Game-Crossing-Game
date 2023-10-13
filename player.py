from turtle import Turtle

MOVE_DISTANCE = 10
STARTING_POSITION = (0, -270)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def successful_crossing(self):
        self.goto(STARTING_POSITION)
