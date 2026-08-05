from turtle import Turtle

MOVE_DISTANCE = 50  

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")

        # Stretch square (20x20) into a vertical paddle (100x20)
        self.shapesize(stretch_wid= 5, stretch_len=1)  
        self.penup()
        self.goto(position)  

    def move_up(self):
        # Move paddle up by 30 pixels
        new_y = self.ycor() + MOVE_DISTANCE  
        self.goto(self.xcor(), new_y)  

    def move_down(self):
        # Move paddle down by 30 pixels
        new_y = self.ycor() - MOVE_DISTANCE  
        self.goto(self.xcor(), new_y) 
