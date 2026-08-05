from turtle import Turtle

# Constants for player setup and movement rules
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Represents the player-controlled turtle in the crossing game."""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start() # Position turtle at starting coordinates
        self.setheading(90) # Face north/upwards
    
    def move_up(self):
        """Moves the turtle forward by the defined move distance."""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Resets the turtle to its starting position at the bottom of the screen."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """
        Checks if the turtle has reached or crossed the finish line.
        Returns True if crossed, False otherwise.
        """
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False 