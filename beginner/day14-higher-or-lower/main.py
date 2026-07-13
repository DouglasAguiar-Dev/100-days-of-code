import random
import os
from art import logo, vs
from game_data import data

def format_data(account_data):
    return f"{account_data['name']}, a {account_data['description']}, from {account_data['country']}"

print(logo)
print("Welcome to the Higher or Lower Game")

score = 0
game_should_continue = True

# Start with a random choice for B
b_data = random.choice(data)

while game_should_continue:
    # Get a random choice for B every round
    a_data = b_data
    b_data = random.choice(data)

    while a_data == b_data:
        b_data = random.choice(data)

    b_follower_count = b_data["follower_count"]
    a_follower_count = a_data["follower_count"]

    print(f"Compare A: {format_data(a_data)}")
    print(vs)
    print(f"Against B: {format_data(b_data)}")

    choice = input("Who has more followers? Type 'A' or 'B':  ").strip().upper()
    os.system("cls")
    print(logo)
    if choice == "A":
        if a_follower_count >= b_follower_count:
            score += 1
            print(f"Your are right! current score: {score}")
        else:
            print(f"Sorry that's wrong. Final score: {score}")
            game_should_continue = False
    if choice == "B":
        if b_follower_count >= a_follower_count:
            score += 1
            print(f"Your are right! current score: {score}")
        else:
            print(f"Sorry that's wrong. Final score: {score}")
            game_should_continue = False