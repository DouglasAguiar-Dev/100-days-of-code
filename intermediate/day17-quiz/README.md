# 🧠 Quiz

A simple command-line **True/False Quiz Game** built with **Python** as part of my **100 Days of Code** journey.

The application loads a collection of questions, converts them into `Question` objects, and uses object-oriented programming to manage the quiz flow, validate answers, track the score, and display the final result.

---

## ✨ Features

- 📚 Loads questions from a separate data file
- 🏗️ Object-Oriented Programming (OOP) structure
- ❓ Asks questions one at a time
- ✅ Validates True/False answers
- 📈 Keeps track of the player's score
- 🎯 Displays the final score after all questions are answered

---

## 📂 Project Structure

```
day17-quiz/
│── main.py
│── quiz_brain.py
│── question_model.py
│── data.py
```

### File Overview

- **main.py** → Starts the application and builds the quiz.
- **quiz_brain.py** → Controls the quiz logic, questions, scoring, and user interaction.
- **question_model.py** → Defines the `Question` class.
- **data.py** → Stores the quiz questions and answers.

---

## 🚀 How to Run

1. Clone this repository:

```bash
git clone https://github.com/DouglasAguiar-Dev/100-days-of-code.git
```

2. Navigate to the project folder:

```bash
cd intermediate/day17-quiz
```

3. Run the program:

```bash
python main.py
```

---

## 🖥️ Example

```text
Welcome to General Quiz by Douglas Aguiar

Q.1: A slug's blood is green. (True/False):
> True

You got it right!
The correct answer was: True.
Your current score is: 1/1

...

You've completed the quiz!
Your final score was: 10/12
```

---

## 🧠 Concepts Practiced

- Classes and Objects
- Object-Oriented Programming (OOP)
- Creating Custom Classes
- Importing Modules
- Lists
- Dictionaries
- Loops
- Methods
- Attributes
- User Input
- Program Structure
- Data Separation
- Code Organization

---

## 📚 What I Learned

This project helped me better understand how multiple classes work together in a real application. Instead of writing everything in one file, I separated responsibilities between different modules, making the code cleaner, easier to maintain, and more reusable.

I also gained more experience creating objects from data and using classes to control the flow of an application.

---

## 👨‍💻 Author

**Douglas Aguiar**

GitHub: https://github.com/DouglasAguiar-Dev

---

⭐ Part of my **100 Days of Code** Python learning journey.