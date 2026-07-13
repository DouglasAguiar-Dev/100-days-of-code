# PyPassword Generator

## About This Project

This is my fifth Python project, created while following the **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

PyPassword Generator is a simple command-line tool that creates secure, randomised passwords. The user specifies how many letters (uppercase and lowercase), symbols, and numbers they want, and the program generates a shuffled password with all character types mixed together — making it secure and unpredictable.

## What I Learned

During this project, I practiced:

* Using the `random` module — specifically `random.choice()` to select random items from a list
* Using `random.shuffle()` to randomise the order of a list **in place**
* Understanding the difference between **easy level** (predictable password: letters, then symbols, then numbers) and **hard level** (secure password: all shuffled together randomly)
* Building a character pool using `for` loops and `list.append()`
* Converting a list into a string
* User input with `input()` and type conversion with `int()`
* Using nested `for` loops to populate lists

## Features

* User customisation — specify exactly how many letters, symbols, and numbers you want
* Randomised character selection from predefined pools
* Shuffled output for maximum security
* Simple, interactive command-line interface
* Support for both uppercase and lowercase letters

## Technologies

* Python 3
* `random` module (built-in)

## How to Run

1. Make sure Python 3 is installed on your computer
2. Save the script as `password_generator.py`
3. Open your terminal and navigate to the folder where the file is saved
4. Run the command: `python password_generator.py`
5. Follow the prompts to generate your password

**Example Output:**
```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
8
How many symbols would you like?
2
How many numbers would you like?
2

m#Q3aB!k2Tz
```

## Learning Process

This project was built while studying Angela Yu's Python bootcamp. I focused on understanding how the `random` module works and how to shuffle data to create a more secure password.

I also used Claude as a programming mentor. Rather than asking for complete solutions, I focused on understanding the concepts through questions and solving challenges myself, step by step.

## Future Improvements

Some improvements I plan to add:

* Refactor the code to use functions (separate the "get user input", "generate password", and "display password" into reusable functions)
* Use the `string` module instead of manually typing out letters, numbers, and symbols
* Add input validation to ensure the user enters positive numbers
* Create a GUI interface instead of just command-line
* Add the ability to exclude certain characters (e.g., "no symbols" or "no lowercase")
* Save generated passwords to a file for reference

## Author

**Douglas Aguiar**

Python student and aspiring software developer in Dublin, Ireland. Currently completing the 100 Days of Code bootcamp and building a portfolio of projects on GitHub to work toward my first junior developer role.

🔗 GitHub: [@DouglasAguiar-Dev](https://github.com/DouglasAguiar-Dev)