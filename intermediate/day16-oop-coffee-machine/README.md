# ☕ OOP Coffee Machine

A command-line **Coffee Machine** built with **Object-Oriented Programming (OOP)** in Python as part of **Day 16** of the **100 Days of Code - Python Bootcamp**.

This project is a refactored version of the previous Coffee Machine application, replacing procedural code with classes and objects to create a cleaner, more maintainable, and scalable application.

---

## 🚀 Features

- ☕ Order three different drinks:
  - Espresso
  - Latte
  - Cappuccino
- 💰 Coin payment system
- 💵 Automatic change calculation
- 📊 Machine resource and profit reports
- ✅ Checks ingredient availability before preparing a drink
- 🔄 Updates resources after each successful purchase
- 🧱 Built using Object-Oriented Programming principles
- 🔒 Secret command to turn the machine off

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Classes and Objects
- Methods
- Modules
- Loops
- Conditional Statements

---

## 📂 Project Structure

```text
.
├── main.py
├── menu.py
├── coffee_maker.py
└── money_machine.py
```

Each class has a single responsibility:

- **Menu** → Stores the available drinks and retrieves menu items.
- **CoffeeMaker** → Manages ingredients and prepares drinks.
- **MoneyMachine** → Handles payments, change, and profit.
- **main.py** → Controls the application flow.

---

## 📚 Concepts Practiced

This project helped me practice:

- Object-Oriented Programming
- Creating and using classes
- Instantiating objects
- Calling methods
- Importing modules
- Separation of responsibilities
- Encapsulation
- Writing cleaner and reusable code
- Building scalable applications

---

## ▶️ How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/100-days-of-code.git
```

2. Navigate to the project folder.

3. Run:

```bash
python main.py
```

---

## ☕

Available drinks:

| Drink | Price |
|--------|------:|
| Espresso | $1.50 |
| Latte | $2.50 |
| Cappuccino | $3.00 |

---

## 🎮 Example

```text
What would you like? (espresso/latte/cappuccino): cappuccino

Please insert coins.

Here is $0.50 in change.
Here is your cappuccino ☕️ Enjoy!
```

---

## 📊 Secret Commands

| Command | Description |
|----------|-------------|
| `report` | Displays current resources and total profit |
| `off` | Turns the coffee machine off |

---

## 🎯 What I Learned

This project introduced me to Object-Oriented Programming and demonstrated how it can improve software design.

Some of the key concepts I learned include:

- Creating and using classes
- Instantiating objects
- Calling methods on objects
- Separating code into multiple modules
- Designing software with single responsibilities
- Improving code readability and maintainability

This refactor made the project significantly cleaner than the procedural version from Day 15.

---

## 🚀 Future Improvements

- Add new drink recipes without modifying existing classes
- Save machine resources to a JSON file
- Create a graphical interface using Tkinter or Pygame
- Add inventory refill functionality
- Implement unit tests
- Persist sales history

---

## 👨‍💻 Author

**Douglas Aguiar**

Python Student | Future Software Engineer

Currently following the **100 Days of Code - Python Bootcamp**, building projects daily while improving my Python and software engineering skills.

⭐ If you enjoyed this project, feel free to give it a star!