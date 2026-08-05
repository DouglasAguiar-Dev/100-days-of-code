from turtle import Turtle

# Font style for level display and game over text
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Handles rendering the current game level and game over overlay."""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)  # Top-left corner position
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears previous text and writes the current level on screen."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increments level count and updates the visual scoreboard."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays 'GAME OVER' at the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)