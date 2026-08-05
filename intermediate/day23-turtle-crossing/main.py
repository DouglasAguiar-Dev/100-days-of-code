import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup and configuration
screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)  # Turn off auto-animation for manual frame updates

# Game instances initialization
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Keyboard controls
screen.listen()
screen.onkeypress(player.move_up, "w")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()  # Refresh screen frame by frame

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision between player turtle and any traffic car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            break

    # Check level completion only if the player hasn't collided
    if game_is_on:
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()

screen.exitonclick()