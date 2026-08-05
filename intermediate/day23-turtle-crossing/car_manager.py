from turtle import Turtle
import random

# Color options for cars and movement speed configurations
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """Manages the generation, movement, and speed progression of traffic cars."""
    def __init__(self):
        self.all_cars = []  
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """
        Generates a new car at a random Y-coordinate on the right edge of the screen.
        Uses a 1-in-6 chance per tick to balance traffic density.
        """
        random_change = random.randint(1, 6)
        if random_change == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2) # Make square rectangular
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y) # Start at right edge
            self.all_cars.append(new_car)
    
    def move_cars(self):
        """
        Moves all active cars backward (from right to left) across the screen.
        Removes cars that have moved off the left edge to free up memory.
        """
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.xcor() < -320:
                self.all_cars.remove(car)

    def level_up(self):
        """Increases car movement speed when the player advances a level."""
        self.car_speed += MOVE_INCREMENT


