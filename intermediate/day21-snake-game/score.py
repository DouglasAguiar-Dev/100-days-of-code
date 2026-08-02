from turtle import Turtle

# Text rendering style constants
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle): 
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260) # Position text near the top of the screen
        self.hideturtle() # Hide the turtle cursor graphic
        self.update_scoreboard()

    def update_scoreboard(self):
        # Render the current score text on the screen
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear() # Clear previous score text to prevent overlapping text
        self.update_scoreboard()

    def game_over(self):
        # Move turtle to center and display game over message
        self.goto(0, 0)
        self.write("Game Over", align=ALIGMENT, font=FONT)

    