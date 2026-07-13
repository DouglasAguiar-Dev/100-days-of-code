# 🎮 Higher or Lower Game

A simple command-line Python game where you compare two public figures, brands, or organizations and guess which one has more social media followers.

This project was built as part of **Day 14** of the **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

---

## ✨ Features

* 🎲 Randomly selects two accounts from a dataset.
* 👤 Displays each account's name, description, and country.
* 🤔 Lets the player guess which account has more followers.
* 📈 Keeps track of the player's score.
* 🔁 Continues until the player makes an incorrect guess.
* 🖥️ Clears the terminal between rounds for a cleaner game experience.

---

## 🛠️ Technologies Used

* 🐍 Python 3
* 🎲 `random`
* 💻 `os`

---

## 📂 Project Structure

```text
higher-lower-game/
│
├── main.py          # Main game logic
├── art.py           # ASCII art (logo and VS graphic)
├── game_data.py     # Dataset containing account information
└── README.md
```

---

## 🚀 How to Run

1. Clone this repository.

```bash
git clone https://github.com/your-username/your-repository.git
```

2. Navigate to the project folder.

```bash
cd your-repository
```

3. Run the game.

```bash
python main.py
```

---

## 🎯 Gameplay

The game displays two accounts:

```text
Compare A: Person A
VS
Against B: Person B
```

Type:

* 🅰️ `A` if you think Account **A** has more followers.
* 🅱️ `B` if you think Account **B** has more followers.

Each correct answer increases your score by **1 point**. The game ends when you make an incorrect guess.

---

## 📚 What I Practiced

* 🧩 Functions
* 📖 Dictionaries
* 📋 Lists
* 🔄 `while` loops
* ✅ Conditional statements (`if`)
* 🎲 Random selection
* 📦 Variable scope
* 🧠 Basic game logic
* 📁 Working with external Python modules

---

## 🙏 Acknowledgements

This project is based on the **Higher or Lower** challenge from **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.
