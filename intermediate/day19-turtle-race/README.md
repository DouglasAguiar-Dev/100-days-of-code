# 🐢 Turtle Race Game

Welcome to the **Turtle Race Game**! This project was built using Python's built-in `turtle` module as part of my **100 Days of Code** journey.

The player chooses a turtle color and places a bet before the race begins. Each turtle moves forward by a random distance, and the first one to cross the finish line wins the race.

---

## 📚 What I learned

Through this project, I practiced and improved my understanding of:

* Creating graphical applications with the `turtle` module
* Working with lists and loops
* Using the `random` module
* Creating and managing multiple objects
* Handling user input with `textinput()`
* Using conditional statements (`if` / `else`)
* Organizing code logic

---

## 🚀 Features

* Six turtles with different colors
* User betting system
* Random movement for each turtle
* Automatic winner detection
* Simple graphical interface

---

## 🛠️ Technologies Used

* Python 3
* Turtle module
* Random module

---

## 📂 Project Structure

```text
turtle-race/
│
├── main.py
└── README.md
```

---

## ▶️ How to run the project

1. Clone this repository:

```bash
git clone https://github.com/your-username/turtle-race.git
```

2. Open the project folder:

```bash
cd turtle-race
```

3. Run the program:

```bash
python main.py
```

---

## 🧠 New Python concepts

### `textinput()`

The `textinput()` function creates a pop-up window that asks the user for input.

```python
user_bet = screen.textinput(
    title="Welcome to the Turtle Race!",
    prompt="Enter your bet color:"
)
```

### `xcor()`

The `xcor()` method returns the turtle's current x-coordinate.

```python
if turtle.xcor() > 230:
```

### `penup()`

`penup()` prevents the turtle from drawing lines while moving.

```python
new_turtle.penup()
```

---

## 🎯 Future improvements

* Add a restart button
* Display the winner on the screen
* Allow players to choose the number of turtles
* Add a scoreboard
* Create different race tracks

---

## 👨‍💻 Author

**Douglas Aguiar**

GitHub: **DouglasAguiar-Dev**

Part of my **100 Days of Code** challenge, where I'm documenting my progress and improving my Python skills one project at a time.
