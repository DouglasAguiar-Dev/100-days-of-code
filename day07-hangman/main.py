import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
lives = 6

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
letters_guessed = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in letters_guessed:
        print(f"You've already guessed letter: {guess}!")
    else:
        letters_guessed.append(guess)

        if guess in chosen_word:
            correct_letters.append(guess)

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)
    if lives == 0:
        game_over = True
        print(f"****************************IT WAS {chosen_word}! YOU LOSE****************************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
