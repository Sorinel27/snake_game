import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.random_location()

    def random_location(self):
        rand_x = random.randint(-200, 200)
        rand_y = random.randint(-200, 200)
        self.goto(rand_x, rand_y)
