# 🎯 Number Guessing Game

A simple command-line **Number Guessing Game** built with Python as part of the **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

The objective is simple: the computer randomly chooses a number between **1 and 100**, and your mission is to guess it before you run out of attempts.

---

## 📖 Features

* 🎲 Randomly generates a number between **1 and 100**
* ⚡ Two difficulty levels:

  * **Easy** – 10 attempts
  * **Hard** – 5 attempts
* 📈 Provides feedback after every guess:

  * Too high
  * Too low
* 🔄 Play again option after each game
* 🧩 Uses functions to keep the code organized and reusable
* 📝 Includes docstrings for better code readability

---

## 🛠️ Technologies Used

* Python 3
* `random` module
* Custom ASCII art (`art.py`)

---

## 📂 Project Structure

```text
number-guessing-game/
│
├── main.py          # Main game logic
├── art.py           # ASCII logo
└── README.md
```

---

## 🚀 How to Run

1. Clone this repository:

```bash
git clone https://github.com/DouglasAguiar-Dev/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp.git
```

2. Navigate to the project folder:

```bash
cd "Day 12"
```

3. Run the game:

```bash
python main.py
```

---

## 🎮 How to Play

1. Launch the game.
2. Choose a difficulty:

   * `easy`
   * `hard`
3. Enter a number between **1** and **100**.
4. Read the feedback:

   * **Too high**
   * **Too low**
5. Keep guessing until:

   * You find the correct number.
   * You run out of attempts.
6. Choose whether to play another round.

---

## 📚 Concepts Practiced

This project helped reinforce several important Python concepts:

* Functions
* Parameters and return values
* Docstrings
* Local variables
* Constants
* Conditional statements (`if`, `elif`, `else`)
* While loops
* User input validation
* Random number generation
* Game loop design
* Code organization and readability

---

## 📸 Example Gameplay

```text
Welcome to the Number Guessing Game!

I'm thinking of a number between 1 and 100.

Choose a difficulty:
Easy or Hard

You have 10 attempts remaining.

Make a guess: 50

Too low.

You have 9 attempts remaining.

Make a guess: 75

Too high.

...

You guessed the number!
Congratulations!
The number was 67.
```

---

## 🎯 Future Improvements

Some features that could be added in future versions:

* Input validation for non-numeric values
* Difficulty selection menu
* Score tracking
* High score system
* Hint system
* Multiple game modes
* Graphical interface using Tkinter or Pygame
* Unit tests

---

## 👨‍💻 Author

**Douglas Aguiar**

GitHub: **DouglasAguiar-Dev**

Part of my **100 Days of Code** journey, documenting my progress while learning Python and software development.
