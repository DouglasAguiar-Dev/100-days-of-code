# 🧮 Calculator

A command-line calculator built in Python that performs basic arithmetic operations. Users can continuously calculate using the previous result or start a completely new calculation without restarting the program.

This project was built as part of **Angela Yu's 100 Days of Code Python Bootcamp** and is part of my **100 Days of Code** portfolio repository.

## 📋 How It Works

* The program displays a calculator ASCII logo.
* The user enters the first number.
* The user chooses one of four operations:

  * Addition (`+`)
  * Subtraction (`-`)
  * Multiplication (`*`)
  * Division (`/`)
* The user enters the second number.
* The selected operation is executed using a function stored inside a dictionary.
* The result is displayed.
* The user can:

  * Continue calculating using the current result.
  * Start a brand-new calculation.

### Example

```text
Enter the first number: 10
Enter a function +, -, * or /: *
Enter the second number: 5

10.0 * 5.0 = 50.0

Type 'y' to continue calculating with 50.0, or type 'n' to start a new calculation:
```

## 🛠 Concepts Practiced

* **Functions** — separating each mathematical operation into its own reusable function.
* **Function references** — storing functions inside a dictionary and calling them dynamically.
* **Dictionaries** — mapping operator symbols (`+`, `-`, `*`, `/`) to their corresponding functions.
* **while loops** — allowing the calculator to continue running until the user chooses to stop.
* **Recursion** — restarting the calculator by calling the `calculation()` function again.
* **Variables** — updating the first number with the previous result to allow chained calculations.
* **User input** — collecting numbers and operators using `input()`.
* **Type casting (`float`)** — converting string input into floating-point numbers so both integers and decimals can be calculated.
* **f-strings** — formatting readable mathematical expressions and results.
* **Boolean flags** — controlling program execution with the `keep_calculating` variable.

## 🚀 Running the Project

```bash
python main.py
```

Requires:

* Python 3
* `art.py` (contains the calculator ASCII logo)

## 💡 Possible Improvements

* Validate user input to prevent crashes from invalid numbers or operators.
* Handle division by zero gracefully.
* Replace the recursive restart with an outer loop to avoid unnecessary recursive function calls.
* Add more mathematical operations such as:

  * Exponents (`^`)
  * Square roots
  * Percentages
  * Modulus (`%`)
* Display a history of previous calculations.
* Allow the user to quit the program with a command like `q`.

## 🧑‍💻 Author

**Douglas Aguiar** — GitHub

Self-taught Python developer working toward a Junior Software Engineer role in Dublin, Ireland.
