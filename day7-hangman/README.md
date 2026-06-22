# Hangman Game

## About This Project

This is my Python Hangman project, created while following the **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

Hangman is a simple command-line word guessing game. The program chooses a random word, and the player has to guess it one letter at a time. The player starts with 6 lives and loses one life for each wrong guess. The game also shows Hangman art stages as the player loses lives.

This project helped me practice writing cleaner game logic, using external Python files, tracking user guesses, and managing win/loss conditions.

## What I Learned

During this project, I practiced:

- Importing variables from other Python files
- Using `random.choice()` to select a random word from a list
- Creating a hidden word display using underscores
- Using `while` loops to keep the game running
- Using `for` loops to check each letter in the chosen word
- Using lists to store correct letters and guessed letters
- Checking if a user has already guessed a letter
- Preventing repeated guesses from removing lives
- Updating the display after each guess
- Using conditionals to manage wrong guesses, wins, and losses
- Keeping game logic more organized and readable

## Features

- Random word selection from an external word list
- Hangman logo imported from a separate art file
- Hangman stages displayed as lives decrease
- Player starts with 6 lives
- Correct guesses reveal letters in the word
- Wrong guesses remove one life
- Repeated guesses are detected
- Repeated guesses do not remove lives
- Win message when the full word is guessed
- Lose message showing the correct word
- Simple interactive command-line interface

## Technologies

- Python 3
- `random` module
- External Python files for words and art

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Save the project files in the same folder:
   - `main.py`
   - `hangman_words.py`
   - `hangman_art.py`
3. Open your terminal and navigate to the project folder.
4. Run the command:

```bash
python main.py
```

If you are using PyCharm, open the project folder and run `main.py`.

## Example Output

```text
Word to guess: _____
Guess a letter: a
You guessed a, that's not in the word. You lose a life.
****************************5/6 LIVES LEFT****************************
Word to guess: _____
```

## Learning Process

This project was built while studying Angela Yu's Python bootcamp. I focused on understanding how to structure a small game, how to track the player's guesses, and how to avoid common beginner mistakes with indentation and variable names.

I also used AI as a programming mentor. Instead of only asking for complete solutions, I worked through the problem step by step, using hints, debugging questions, and code review feedback to understand the logic properly.

## Future Improvements

Some improvements I plan to add:

- Refactor the code to use functions such as `choose_word()`, `get_guess()`, `update_display()`, and `check_game_over()`
- Add input validation to prevent numbers, symbols, or empty guesses
- Make the game ignore guesses with more than one letter
- Add difficulty levels with different word lists
- Add a score system
- Add a replay option after winning or losing
- Improve the user interface with clearer spacing and messages
- Create a graphical version of the game in the future

## Author

Douglas Aguiar

Python student and aspiring software developer in Dublin, Ireland. Currently completing the 100 Days of Code bootcamp and building a portfolio of projects on GitHub to work toward my first junior developer role.

GitHub: [@DouglasAguiar-Dev](https://github.com/DouglasAguiar-Dev)