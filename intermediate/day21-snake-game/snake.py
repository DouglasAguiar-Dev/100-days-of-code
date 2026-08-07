from turtle import Turtle, position

# Constants defining initial setup configuration and movement metrics
STARTING_POSTIONS = [(0, 0), (-20, 0), (-40, 0)] 
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake: 
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] # Store a direct reference to the snake's head

    def create_snake(self):
        # Loop through starting positions to generate initial body parts
        for position in STARTING_POSTIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Instantiate a single turtle segment, style it, and position it
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # Add a new segment at the position of the current tail segment
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Shift each body segment to the position of the segment ahead of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Directional methods with guard clauses to prevent instant reverse self-collisions
    def up (self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down (self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left (self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right (self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
