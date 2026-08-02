from turtle import Turtle, position
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # Scale food down to half size
        self.color("orange")
        self.speed("fastest")
        self.refresh() # Place food at a random position upon creation

    # Generate random coordinates within safe window boundaries
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)