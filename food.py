from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        randX = random.randint(-240, 240)
        randY = random.randint(-240, 240)
        self.goto(randX, randY)
        self.refreshFood()

    def refreshFood(self):
        randX = random.randint(-240, 240)
        randY = random.randint(-240, 240)
        self.goto(randX, randY)
