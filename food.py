from turtle import Turtle
from random import randint


# Food class: creates the food for the snake
class Food(Turtle):
    # Initialises the food object
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)
        self.speed("fastest")

    # Makes the food  spawn in a new location
    def refresh(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)
