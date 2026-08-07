from turtle import Turtle

# Text rendering style constants
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle): 
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("intermediate/day21-snake-game/data.txt", mode="r") as data:
           self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260) # Position text near the top of the screen
        self.hideturtle() # Hide the turtle cursor graphic
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # Render the current score text on the screen
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("intermediate/day21-snake-game/data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    