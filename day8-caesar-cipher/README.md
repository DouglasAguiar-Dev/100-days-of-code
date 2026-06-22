# Caesar Cipher

A simple Python command-line program that encrypts and decrypts messages using the Caesar Cipher technique.

## About The Project

This project was built as part of my Python learning journey. It demonstrates how to use functions, loops, conditional statements, user input, string manipulation, and basic encryption logic.

The program allows the user to:

- Encode a message by shifting each letter forward in the alphabet
- Decode a message by shifting each letter backward in the alphabet
- Keep numbers, symbols, and spaces unchanged
- Restart the program without running the file again

## How It Works

The Caesar Cipher is a basic encryption method where each letter in a message is shifted by a fixed number of positions in the alphabet.

Example:

```text
Message: hello
Shift: 5
Encoded result: mjqqt
```

If the user chooses to decode, the program reverses the shift.

## Features

- Prints a logo when the program starts
- Supports encoding and decoding
- Handles spaces, numbers, and symbols
- Allows the user to continue or exit the program
- Uses clean function-based structure

## Technologies Used

- Python

## What I Learned

While building this project, I practiced:

- Importing values from another Python file
- Creating and calling functions
- Using `if` and `else` statements
- Using `for` loops to process text character by character
- Using the modulo operator `%` to wrap around the alphabet
- Handling characters that are not letters
- Writing clearer variable names such as `should_continue`

## How To Run The Project

1. Make sure Python is installed on your computer.
2. Clone this repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
```

3. Open the project folder:

```bash
cd your-repository-name
```

4. Run the program:

```bash
python main.py
```

## Example Usage

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world!
Type the shift number:
5
Here is the encoded result: mjqqt btwqi!
```

## Future Improvements

- Add validation for invalid options
- Handle uppercase letters without converting everything to lowercase
- Improve error handling for non-number shift values
- Add automated tests
- Create a simple graphical interface

## Author

Douglas Aguiar

GitHub: [DouglasAguiar-Dev](https://github.com/DouglasAguiar-Dev)