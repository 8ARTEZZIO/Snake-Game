from turtle import Turtle
from random import choice

SHAPE = 'circle'
COLOR = 'red'

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.generate_food()

    def generate_food(self):
        rand_x = choice(list(range(-280, 280, 20)))
        rand_y = choice(list(range(-280, 280, 20)))
        self.penup()
        self.goto(float(rand_x), float(rand_y))