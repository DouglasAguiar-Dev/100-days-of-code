# imports
from art import logo
import random
logo = logo
EASY = 10
HARD = 5
turns = 0

def checks_answer(guess, random_number, turns):
    """ This function checks if the guess is correct"""
    if guess > random_number:
        print("Your guess is too high.")
        return turns - 1
    elif guess < random_number:
        print("Your guess is too low.")
        return turns - 1
    else:
        print(f"You guessed the number! Congratulations! \n The number was {random_number}")
        return None

def set_difficulty():
    """ This function sets the difficulty of the game"""
    while True:
        difficulty = (input("choose a difficulty. Type 'easy' or 'hard': ")).strip().lower()
        if difficulty == "easy":
            return EASY
        elif difficulty == "hard":
            return HARD
        else:
            print("Invalid Input, Try Again")

def game():
    """ This function starts the game"""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    random_number = random.randint(1, 100)

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = 0
    while guess != random_number:
        guess = int(input("Make a guess: "))
        turns = checks_answer(guess, random_number, turns)
        if turns == 0:
            print("You runout of guesses, Game Over.")
            return
        elif guess != random_number:
            print(f"You have {turns} attempts remaining to guess the number.")

while True:
    game()
    retry = input("Do you want to try again? Type 'y' for yes or 'n' for no: ").strip().lower()
    if retry == "y":
        continue
    else:
        print("Thank you for playing! goodbye!")
        break

