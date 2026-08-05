from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle() # Hide turtle icon, keeping only rendered text

        # Player score trackers
        self.left_score = 0
        self.right_score = 0

        # Display initial scores (0 - 0) on screen creation
        self.update_scoreboard()
       
    def update_scoreboard(self):
        # Clear previous text before redrawing updated scores
        self.clear()

        # Display left player score
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Arial", 70, "normal"))

        # Display right player score
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Arial", 70, "normal"))

    def left_point(self):
        # Increment left score and refresh display
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        # Increment right score and refresh display
        self.right_score += 1
        self.update_scoreboard()