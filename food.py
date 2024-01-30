from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("#006600")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_xcor = random.randint(-260, 260)
        random_ycor = random.randint(-260, 260)
        self.goto(random_xcor, random_ycor)
