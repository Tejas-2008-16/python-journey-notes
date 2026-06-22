# 🐍 Day 02 — Strings
 
> **Video:** Python Tutorial for Beginners #2 — Strings by Corey Schafer
> **Watch it here →** [▶️ YouTube](https://www.youtube.com/watch?v=k9TUPpGqYTo)
> **Date:** June 2026
> **Goal:** Understand what Strings are, how to create them, and how to manipulate them
 
---
 
## 🧠 What I learned today
 
- What a String is
- How to create Strings (single, double, triple quotes)
- How to access individual characters inside a String
- How to slice a String
- Useful String methods like `.upper()`, `.lower()`, `.replace()` and more
- How to find the length of a String
---
 
## 📖 What is a String?
 
A **String** is just **text**. Any time you wrap something in quotes, Python treats it as a String.
 
```python
name    = "Tejas"
message = "I am learning Python!"
city    = 'Pune'
```
 
> 💡 You can use `" "` double quotes or `' '` single quotes — both work exactly the same!
 
---
 
## 📝 Multi-line Strings (Triple Quotes)
 
If you want to write a long text that spans **multiple lines**, use **triple quotes** `""" """`:
 
```python
message = """Hello!
My name is Tejas.
I am learning Python."""
 
print(message)
```
 
Output:
```
Hello!
My name is Tejas.
I am learning Python.
```
 
> 💡 Triple quotes are useful for long paragraphs, descriptions, or whenever your text has line breaks.
 
---
 
## 🔢 Accessing Characters — Indexing
 
Every character in a String has a **position number** called an **index**.
Counting starts from **0**, not 1!
 
```
S  t  r  i  n  g
0  1  2  3  4  5
```
 
```python
greeting = "Hello"
 
print(greeting[0])   # H  → first character
print(greeting[1])   # e  → second character
print(greeting[4])   # o  → fifth character
```
 
### Negative Indexing — counting from the end
 
You can also count **backwards** using negative numbers:
 
```python
greeting = "Hello"
 
print(greeting[-1])  # o  → last character
print(greeting[-2])  # l  → second to last
```
 
> 💡 `-1` always gives you the **last character** — super handy!
 
---
 
## ✂️ Slicing — Grabbing a Chunk of a String
 
**Slicing** lets you grab a section of a String using `[start:end]`.
 
> ⚠️ The **start** is included, the **end** is NOT included.
 
```python
greeting = "Hello, World!"
 
print(greeting[0:5])   # Hello   → from index 0 up to (not including) 5
print(greeting[7:12])  # World   → from index 7 up to (not including) 12
print(greeting[:5])    # Hello   → no start = begin from 0
print(greeting[7:])    # World!  → no end = go all the way to the end
```
 
Think of it like cutting a piece from a sentence:
 
```
H  e  l  l  o  ,     W  o  r  l  d  !
0  1  2  3  4  5  6  7  8  9  10 11 12
```
 
---
 
## 📏 String Length — `len()`
 
`len()` gives you the **total number of characters** in a String (including spaces!).
 
```python
name = "Tejas"
print(len(name))   # 5
 
city = "Pune, India"
print(len(city))   # 11
```
 
---
 
## 🔧 String Methods
 
Methods are **built-in tools** that come with every String. You use them with a dot `.` after the variable.
 
### Change Case
 
```python
name = "tejas"
 
print(name.upper())       # TEJAS  → all uppercase
print(name.lower())       # tejas  → all lowercase
print(name.capitalize())  # Tejas  → only first letter capitalized
```
 
---
 
### Count & Find
 
```python
message = "I love Python and Python loves me"
 
print(message.count("Python"))    # 2  → how many times "Python" appears
print(message.find("Python"))     # 7  → index where "Python" first appears
print(message.find("Java"))       # -1 → returns -1 if NOT found
```
 
---
 
### Replace
 
```python
message = "I love Python"
 
new_message = message.replace("Python", "coding")
print(new_message)   # I love coding
```
 
> 💡 `replace()` does NOT change the original — it creates a **new** String!
 
---
 
### Strip — Remove Extra Spaces
 
Very useful when working with user input that might have accidental spaces:
 
```python
username = "   tejas   "
 
print(username.strip())    # "tejas"  → removes spaces from both sides
print(username.lstrip())   # "tejas   "  → removes only left spaces
print(username.rstrip())   # "   tejas"  → removes only right spaces
```
 
---
 
### startswith & endswith
 
```python
email = "tejas@gmail.com"
 
print(email.startswith("tejas"))   # True
print(email.endswith(".com"))      # True
print(email.endswith(".org"))      # False
```
 
---
 
## 🔗 Joining Strings — Concatenation
 
You can **combine** Strings using `+`:
 
```python
first_name = "Tejas"
last_name  = "More"
 
full_name = first_name + " " + last_name
print(full_name)   # Tejas More
```
 
> ⚠️ You can only use `+` to join Strings with other Strings.
> Joining a String and a number will cause an error!
 
```python
name = "Tejas"
age  = 20
 
print(name + age)        # ❌ ERROR!
print(name + str(age))   # ✅ Tejas20 → convert number to String first using str()
```
 
---
 
## ✨ f-Strings — The Clean Way to Mix Variables and Text
 
Instead of `+` to join, Python has a much cleaner way called **f-Strings**:
 
```python
name = "Tejas"
age  = 20
 
message = f"My name is {name} and I am {age} years old."
print(message)
# Output: My name is Tejas and I am 20 years old.
```
 
Just put `f` before the opening quote, and wrap your variables in `{ }` — that's it!
 
> 💡 f-Strings are the **modern and recommended way** to format text in Python. Use them!
 
---
 
## 📌 Quick Reference — All Methods at a Glance
 
| Method | What it does | Example |
|--------|-------------|---------|
| `.upper()` | ALL CAPS | `"hello".upper()` → `"HELLO"` |
| `.lower()` | all lowercase | `"HELLO".lower()` → `"hello"` |
| `.capitalize()` | First letter capital | `"hello".capitalize()` → `"Hello"` |
| `.len()` | Count characters | `len("hello")` → `5` |
| `.count("x")` | Count occurrences | `"hello".count("l")` → `2` |
| `.find("x")` | Find index of x | `"hello".find("e")` → `1` |
| `.replace("a","b")` | Swap text | `"cat".replace("c","b")` → `"bat"` |
| `.strip()` | Remove side spaces | `"  hi  ".strip()` → `"hi"` |
| `.startswith("x")` | Starts with check | `"hello".startswith("he")` → `True` |
| `.endswith("x")` | Ends with check | `"hello".endswith("lo")` → `True` |
 
---
 
## 🎯 Day 02 Summary
 
- ✅ Strings = text wrapped in quotes `" "` or `' '`
- ✅ Triple quotes `""" """` for multi-line text
- ✅ Indexing starts at `0` → `greeting[0]` gives first character
- ✅ Negative index → `greeting[-1]` gives last character
- ✅ Slicing → `text[0:5]` grabs a chunk
- ✅ `len()` counts total characters
- ✅ Methods like `.upper()`, `.lower()`, `.replace()`, `.strip()` are your tools
- ✅ Use **f-Strings** to cleanly mix variables into text
---
 
## 🔜 What's Next — Day 03
 
Next I'll learn about **Integers and Floats** — working with numbers in Python.
 
---
 
*📺 Source: [Corey Schafer — Python Tutorial for Beginners #2](https://www.youtube.com/watch?v=k9TUPpGqYTo)*