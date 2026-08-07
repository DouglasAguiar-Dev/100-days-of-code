# 📧 Mail Merge Project

A simple **Mail Merge** application built with Python as part of the **100 Days of Code** challenge.

The program automatically generates personalized invitation letters by reading a template file and replacing placeholders with names from a list.

---

## 🚀 Features

- Read a template letter from a text file
- Read multiple names from a separate file
- Replace placeholders automatically
- Generate personalized letters for each recipient
- Save the generated files into an output folder

---

## 📂 Project Structure

```text
day24-mail-merge/

├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt
│   │
│   └── Names/
│       └── invited_names.txt
│
├── Output/
│   └── ReadyToSend/
│       ├── letter_for_Douglas.txt
│       ├── letter_for_Zuko.txt
│       ├── letter_for_Katara.txt
│       └── ...
│
├── main.py
├── README.md
└── .gitignore
```

---

## 🛠️ Technologies Used

- Python 3
- Visual Studio Code
- File handling
- String manipulation

---

## 🧠 Concepts Practiced

This project helped reinforce the following Python concepts:

- Reading files with `open()`
- Writing files
- Using the `with` statement
- Working with lists
- Using `read()` and `readlines()`
- Iterating with `for` loops
- String replacement with `replace()`
- Removing line breaks with `strip()`
- Creating dynamic file names with f-strings

---

## 📖 How It Works

1. The program opens the letter template.
2. It reads all names from `invited_names.txt`.
3. Each name is cleaned using `strip()`.
4. The placeholder `[name]` is replaced with the actual name.
5. A new personalized letter is created.
6. The file is saved in the `Output/ReadyToSend` folder.

---

## 💻 Example

### Template (`starting_letter.txt`)

```text
Dear [name],

You are invited to my birthday party.

Hope to see you there!
```

### Names (`invited_names.txt`)

```text
Douglas
Zuko
Katara
Toph
Sokka
```

### Generated file (`letter_for_Douglas.txt`)

```text
Dear Douglas,

You are invited to my birthday party.

Hope to see you there!
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/DouglasAguiar-Dev/100-days-of-code.git
```

Navigate to the project folder:

```bash
cd intermediate/day24-mail-merge
```

Run the program:

```bash
python main.py
```

---

## 📚 New Python Vocabulary

### `strip()`

Removes spaces and line breaks from the beginning and end of a string.

```python
name = "Douglas\n"

clean_name = name.strip()

print(clean_name)
```

Output:

```text
Douglas
```

### `replace()`

Replaces part of a string with another value.

```python
text = "Hello [name]"

new_text = text.replace("[name]", "Douglas")

print(new_text)
```

Output:

```text
Hello Douglas
```

### `readlines()`

Reads all lines from a file and returns them as a list.

```python
with open("invited_names.txt") as file:
    names = file.readlines()
```

---

## 🎯 Learning Goals

- Understand how file manipulation works in Python
- Learn how to automate repetitive tasks
- Practice string manipulation
- Generate files dynamically
- Build a foundation for more advanced automation projects

---

## 🔮 Future Improvements

- Read data from CSV files
- Export letters as PDF documents
- Create a graphical user interface (GUI)
- Send emails automatically
- Allow users to create custom templates

---

## 👨‍💻 Author

**Douglas Aguiar**

- GitHub: https://github.com/DouglasAguiar-Dev
- Project created as part of the **100 Days of Code Python Bootcamp**.
- Built using **Python** and **Visual Studio Code**.