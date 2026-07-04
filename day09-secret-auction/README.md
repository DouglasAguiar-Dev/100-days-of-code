# 🔒 Secret Auction

A command-line auction program built in Python. Multiple bidders can enter their name and bid in secret — the terminal is cleared after every entry so no one can see what others have bid. Once all bids are in, the program reveals the highest bidder and their winning amount.

This project was built as part of [Angela Yu's 100 Days of Code](https://www.udemy.com/course/100-days-of-code/) Python bootcamp, and is part of my [`100-days-of-code`](../) portfolio repository.

---

## 📋 How It Works

1. Each bidder is prompted for their **name** and **bid amount**.
2. Their entry is stored in a dictionary as `{name: bid}`.
3. The screen is cleared immediately after each entry, keeping every bid secret from the next bidder.
4. The user is asked whether there are more bidders (`y`/`n`).
5. Once there are no more bidders, the program loops through every entry, tracks the highest bid seen so far, and announces the winner.

```
Welcome to the Bid Auction!
What's your name?
What's the bid?
Are there other bidders? type 'y' for yes and 'n' for no

The Winner is:
 Hermione with a bid of 70
```

---

## 🛠 Concepts Practiced

- **Dictionaries** — storing and updating key-value pairs (`bid_log[name] = bid`)
- **`while` loops** — collecting an unknown number of bidders until a stop condition is met
- **`for` loops with `.items()`** — unpacking both key and value while iterating over a dictionary
- **The running maximum pattern** — initializing a tracker before a loop, then comparing and updating it on every iteration (a pattern reused constantly in real-world programming: highest score, longest word, lowest price, etc.)
- **Type casting (`int()`)** — converting `input()` strings into real numbers, and understanding why comparing numeric strings directly (e.g. `"9" > "10"`) gives the wrong result
- **Variable scope & naming collisions** — avoiding reused variable names across nested loops to prevent silent bugs
- **f-strings** — formatting the final output message

---

## 🚀 Running the Project

```bash
python main.py
```

Requires Python 3 and the included `art.py` file (for the ASCII logo).

---

## 💡 Possible Improvements

- Validate bid input so the program doesn't crash if a non-numeric value is entered
- Handle the edge case where a bidder enters the same name twice (currently overwrites their previous bid)
- Add support for decimal bids using `float()` instead of `int()`

---

## 🧑‍💻 Author

**Douglas Aguiar** — [GitHub](https://github.com/DouglasAguiar-Dev)
Self-taught Python developer working toward a Junior Software Engineer role in Dublin, Ireland.