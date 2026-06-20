# 🐍 Day 01 — Setting Up Python
 
> **Video:** Python Tutorial for Beginners #1 by Corey Schafer
> **Date:** June 2026
> **Goal:** Install Python, run our first line of code, and understand variables
 
---
 
## 🧠 What I learned today
 
- How to install Python on my computer
- How to check if Python is working
- How to print something on the screen
- What variables are and how to use them
---
 
## ⚙️ Step 1 — Install Python
 
Go to **[python.org](https://python.org)** and download the latest **Python 3** version.
 
> ⚠️ Always download **Python 3**, not Python 2. Python 2 is old and no longer supported.
 
### On Windows:
1. Run the installer
2. **VERY IMPORTANT** → Check the box ✅ **"Add Python to PATH"**
   - If you miss this, Python won't work in the terminal!
3. Click **Install Now** and you're done
### On Mac:
1. Run the `.pkg` file you downloaded
2. Follow the steps — that's it!
---
 
## 🔍 Step 2 — Check if Python is installed
 
Open your **Terminal** (Mac/Linux) or **Command Prompt** (Windows) and type:
 
```bash
# On Windows
python --version
 
# On Mac / Linux
python3 --version
```
 
If you see something like this — you're good to go! ✅
```
Python 3.12.0
```
 
If you see an error — Python isn't installed properly. Go back and reinstall.
 
---
 
## 👋 Step 3 — Hello World (Your First Python Code!)
 
This is a tradition in programming — the very first program everyone writes is **Hello World**.
 
Create a file called `hello.py` and write this inside:
 
```python
print("Hello, World!")
```
 
Now run it from your terminal:
 
```bash
python hello.py        # Windows
python3 hello.py       # Mac
```
 
**Output:**
```
Hello, World!
```
 
🎉 **Congrats — you just ran your first Python program!**
 
---
 
### 🤔 What is `print()`?
 
`print()` is a **function** — it tells Python to display something on the screen.
 
Whatever you put inside the `( )` gets shown in the terminal.
 
```python
print("I love Python!")
print("My name is Tejas")
print(100)
```
 
Output:
```
I love Python!
My name is Tejas
100
```
 
---
 
## 📦 Step 4 — Variables
 
A **variable** is like a box where you store information so you can use it later.
 
```python
name = "Tejas"
```
 
Here:
- `name` → the name of the box (you choose this)
- `=` → means "store this value"
- `"Tejas"` → the value going inside the box
### The 4 basic types of data in Python:
 
```python
name       = "Tejas"   # String  → text, always inside quotes " "
age        = 20        # Integer → whole numbers, no quotes
gpa        = 9.5       # Float   → numbers with a decimal point
is_student = True      # Boolean → only True or False (capital T/F!)
```
 
### Printing variables:
 
```python
name = "Tejas"
age  = 20
 
print(name)   # Output: Tejas
print(age)    # Output: 20
```
 
> 💡 **Notice:** when printing a variable, don't use quotes around it.
> `print(name)` ✅ → prints the value
> `print("name")` ❌ → literally prints the word *name*
 
---
 
## 📌 Things to Remember
 
| Rule | Example |
|------|---------|
| Python is case-sensitive | `print` ✅ &nbsp;&nbsp; `Print` ❌ |
| Strings go inside quotes | `"Hello"` or `'Hello'` |
| Use `#` to write comments | `# this line is ignored by Python` |
| No need to declare variable type | Python figures it out automatically |
 
---
 
## ✍️ Comments
 
A **comment** is a line Python completely ignores. It's just a note for yourself (or anyone reading your code).
 
```python
# This is a comment — Python skips this line
print("But this runs!")   # You can also put comments at the end of a line
```
 
Comments are super useful to explain what your code does.
 
---
 
## 🎯 Day 01 Summary
 
| What | How |
|------|-----|
| Install Python | Download from python.org |
| Check version | `python --version` in terminal |
| Print to screen | `print("your text")` |
| Store a value | `name = "Tejas"` |
| Text data | Use quotes → `"hello"` |
| Number data | No quotes → `20` or `9.5` |
| Yes/No data | `True` or `False` |
 
---
 
## 🔜 What's Next — Day 02
 
Next I'll learn about **Strings** — how to manipulate, combine, and work with text in Python.
 
---
 
*📺 Source: [Corey Schafer — Python Tutorial for Beginners #1](https://www.youtube.com/watch?v=YYXdXT2l-Gg)*