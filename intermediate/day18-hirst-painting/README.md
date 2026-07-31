# 🎨 Hirst Painting Project

## 📖 About the Project

This project recreates the famous dot paintings inspired by artist Damien Hirst using Python and the Turtle module.

The program extracts colors from an image (using the `colorgram` library) and generates a colorful 10×10 grid of dots with randomly selected colors.

This project helped me practice loops, nested loops, lists, tuples, modules, and graphical programming with Python.

---

## 🚀 Features

* 🎨 Extract colors from an image using `colorgram`
* 🐢 Draw graphics with the Turtle module
* 🔀 Generate random colors from a predefined palette
* 🔁 Use nested loops to create a grid pattern
* 📍 Control the turtle's position on the screen

---

## 🛠️ Technologies Used

* Python 3
* Turtle
* Random
* Colorgram

---

## 📚 What I Learned

While building this project, I practiced:

* Importing and using external libraries
* Working with RGB color values
* Lists and tuples
* Nested `for` loops
* Turtle graphics
* Screen coordinates (`x` and `y`)
* Code organization and readability

### 🧠 New Python Concepts

**`random.choice()`**

Selects a random element from a list.

```python
color = random.choice(color_list)
```

**`tt.dot(size, color)`**

Draws a colored dot.

```python
tt.dot(20, (255, 0, 0))
```

**`tt.ycor()`**

Returns the turtle's current Y coordinate.

```python
current_y = tt.ycor()
```

**`tt.setposition(x, y)`**

Moves the turtle to a specific position.

```python
tt.setposition(-250, -250)
```

---

## 🎯 How It Works

1. Extract colors from an image using `colorgram`.
2. Store the RGB values in a list.
3. Move the turtle to the starting position.
4. Draw 100 dots in a 10×10 grid.
5. Randomly select a color for each dot.
6. Move to the next row and repeat.

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
```

Go to the project folder:

```bash
cd your-repository
```

Run the program:

```bash
python main.py
```

---

## 📸 Final Result

The program generates a painting similar to this:

```
🔴 🟡 🔵 🟢 🟠 🟣 🔴 🟡 🔵 🟢
🟢 🔵 🟠 🟣 🔴 🟡 🟢 🔵 🟠 🟣
🔵 🟢 🔴 🟡 🟣 🟠 🔵 🟢 🔴 🟡
```

---

## 💭 Final Thoughts

Every small project teaches something new. Today it's a grid of colorful dots; tomorrow it could be a complete application.

Looking at this code in the future, I'll probably laugh at some parts and think about how much I've improved—and that's exactly what makes programming exciting. 🚀

---

## 👨‍💻 Author

**Douglas Aguiar**

* 🇧🇷 Brazilian developer based in Ireland
* 🐍 Python student following the **100 Days of Code** challenge
* 💻 Passionate about software development and always learning new technologies

GitHub: **DouglasAguiar-Dev**

*"Every project is another step toward becoming the developer I want to be."* 🚀
