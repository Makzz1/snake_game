from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.goto(x=randint(-280, 280), y=randint(-280, 250))
    def refresh(self):
        self.goto(x=randint(-280, 280), y=randint(-280, 250))
        self.score += 1
