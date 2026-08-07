from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the game screen window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # Turn off automatic screen updates to eliminate rendering lag

# Instantiate core game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Bind keyboard inputs to snake directional methods
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start the main game loop
game_is_on = True
while game_is_on:
    screen.update() # Manually refresh the screen frame
    time.sleep(0.1) # Pause for 0.1 seconds to control gameplay speed
    snake.move() # Advance the snake forward

    # Detect collision between the snake's head and the food item
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision between the snake's head and the window boundaries
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
       scoreboard.reset()
       snake.reset()

    # Detect collision between the snake's head and its own body segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
        
# Keep the window open until clicked
screen.exitonclick()