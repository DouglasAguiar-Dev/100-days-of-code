# 🃏 Blackjack Game (Python CLI)

A command-line Blackjack game built in Python where the player competes against a computer dealer using simplified casino rules. The objective is to get as close to 21 as possible without going over.

This project is part of **Angela Yu’s 100 Days of Code – Python Bootcamp** and is included in my personal learning portfolio.

---

## 🎮 How the Game Works

The game follows a simple turn-based flow:

### 🂠 Initial Deal
- Player and dealer each receive 2 cards
- Player sees both of their cards and total score
- Dealer shows only one card

### 👤 Player Turn
The player chooses:
- `y` → draw another card
- `n` → stop drawing

Rules during this phase:
- If score exceeds 21 → player loses immediately (bust)
- A Blackjack (Ace + 10-value card) results in an instant win

### 🤖 Dealer Turn
- Dealer reveals hidden card
- Dealer draws automatically until reaching at least 17

### 🏁 End of Game
- Final hands are revealed
- Scores are compared using Blackjack rules
- Winner is determined

---

## 📜 Game Rules

- Cards 2–10 → face value
- J, Q, K → 10
- Ace → 11 (or 1 if needed to prevent bust)
- Blackjack → 21 with 2 cards (internally represented as score `0`)
- Score > 21 → bust (automatic loss)
- Dealer must draw until reaching 17+

---

## 🧩 Core Functions

### `deal_card()`
Randomly selects and returns a card from the deck using `random.choice()`.

---

### `calculate_score(cards)`
Calculates the total value of a hand.

Key logic:
- Returns `0` if the hand is a Blackjack
- Converts Ace (11 → 1) if total exceeds 21
- Returns final hand score

---

### `compare(user_score, computer_score)`
Determines the outcome of the game:
- Win / Lose / Draw logic
- Handles Blackjack priority
- Handles bust conditions

---

### `play_game()`
Main game controller:
- Initializes hands
- Handles player loop
- Executes dealer logic
- Displays results
- Determines winner

---

## 🧠 Concepts Practiced

### Python Fundamentals
- Functions and modular design
- Lists and list manipulation
- User input handling (`input()`)
- Type handling (integers, booleans)

### Control Flow
- `while` loops for game progression
- `if / elif / else` conditional logic
- Game state management (`is_game_over`)

### Programming Concepts
- Randomization (`random.choice`)
- State management
- Rule-based system design
- Decision-making algorithms

---

## 🚀 How to Run

```bash
python main.py
```

### Requirements
- Python 3.x
- No external dependencies (uses only the built-in `random` module)

---

## 💡 Possible Improvements

- Add betting system (chips / virtual money)
- Implement split and double-down mechanics
- Improve multi-Ace handling logic
- Add multiple decks + shuffle simulation
- Create GUI version (Tkinter or Pygame)
- Track win/loss statistics
- Add difficulty levels for dealer AI

---

## 🧑‍💻 Author

Douglas Aguiar  
GitHub: https://github.com/DouglasAguiar-Dev