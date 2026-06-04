import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices_img = [rock, paper, scissors]

user_name = input("What is your name? ")
player_choice = int(input(f"{user_name} What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: "))
if player_choice >= 0 and player_choice <= 2:
    print("Player chose: ")
    print(choices_img[player_choice])

computer_choice = random.randint(0,2)
print("Computer chose: ")
print(choices_img[computer_choice])

if player_choice >= 3 or player_choice <0:
    print(f"Invalid number! Try again")

elif player_choice == 0 and computer_choice == 2:
    print(f"You win!")

elif player_choice == 2 and computer_choice == 0:
    print(f"You lose!")

elif player_choice < computer_choice :
    print(f"You lose!")

elif player_choice > computer_choice :
    print(f"You win!")

elif player_choice == computer_choice :
    print(f"It's a tie!")

