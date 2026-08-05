from turtle import Turtle, Screen # Added Turtle for net drawing
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# 1. Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0) 

# Create a dividing line (the net)
line_drawer = Turtle()
line_drawer.color("white")
line_drawer.pensize(3)
line_drawer.hideturtle()
line_drawer.penup()
line_drawer.goto(0, -300) # Start at the bottom center
line_drawer.setheading(90) # Point upwards

# Draw dashed line
for _ in range(20): # Adjust number based on dash/gap size
    line_drawer.pendown()
    line_drawer.forward(15) # Length of dash
    line_drawer.penup()
    line_drawer.forward(15) # Length of gap

# 3. Game Objects Setup
right_paddle = Paddle((350, 0)) 
left_paddle = Paddle((-350, 0)) 
ball = Ball()
scoreboard = Scoreboard()

# 4. Input Listeners
screen.listen()
screen.onkey(right_paddle.move_up, "Up")  
screen.onkey(right_paddle.move_down, "Down")  
screen.onkey(left_paddle.move_up, "w")  
screen.onkey(left_paddle.move_down, "s")  

# 5. Main Game Loop
game_is_on = True
while game_is_on:
    screen.update() 
    time.sleep(ball.move_speed)  # Uses dynamic ball speed
    ball.move()

    # Detect collision with top/bottom wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50: 
        ball.bounce_x() # Speed increase is handled INSIDE bounce_x

    # Detect R paddle miss (L player scores)
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect L paddle miss (R player scores)
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()