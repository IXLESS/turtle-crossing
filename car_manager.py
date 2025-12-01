from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()  # Need parentheses to call method
        self.shape("square")
        self.color(COLORS[randint(0, 5)])  # Random color on each car
        random_y = randint(-250, 250)  # Random vertical position for each car
        self.goto(310, random_y)  # Start near the right edge (600 / 2 = 300, +10 buffer)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)  # Face left
        self.i = 0
        
    def move(self, speed):
        self.forward(speed)


