from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(COLORS[randint(0, 5)])
        random_y = randint(-250, 250)
        self.goto(310, random_y)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.i = 0
        
    def move(self, speed):
        self.forward(speed)


