# 🐍 Day 03 — Integers & Floats
 
> **Video:** Python Tutorial for Beginners #3 — Integers and Floats by Corey Schafer
> **Watch it here →** [▶️ YouTube](https://www.youtube.com/watch?v=khKv-8q7YmY)
> **Date:** June 2026
> **Goal:** Understand numbers in Python — how to use them, do math with them, and avoid common mistakes
 
---
 
## 🧠 What I learned today
 
- The difference between Integers and Floats
- How to do basic math in Python
- What arithmetic operators are
- How to do math and store the result
- Useful number functions like `abs()`, `round()`
- How to convert between number types
---
 
## 🔢 Two Types of Numbers in Python
 
Python has two main number types:
 
| Type | What it is | Example |
|------|-----------|---------|
| **Integer** (`int`) | Whole numbers, no decimal | `5`, `100`, `-20` |
| **Float** (`float`) | Numbers with a decimal point | `3.14`, `9.5`, `-0.5` |
 
```python
age      = 20       # int   → whole number
price    = 9.99     # float → has a decimal
score    = -5       # int   → negative is fine too
pi       = 3.14159  # float
```
 
> 💡 Python figures out the type automatically — you don't need to tell it!
 
---
 
## ➕ Arithmetic Operators — Doing Math
 
Python can do all basic math operations:
 
```python
print(3 + 2)    # 5   → Addition
print(3 - 2)    # 1   → Subtraction
print(3 * 2)    # 6   → Multiplication
print(3 / 2)    # 1.5 → Division (always gives a float!)
print(3 // 2)   # 1   → Floor Division (removes the decimal, rounds DOWN)
print(3 % 2)    # 1   → Modulus (gives the REMAINDER)
print(3 ** 2)   # 9   → Exponent (3 to the power of 2)
```
 
### What is Floor Division `//`?
 
```python
print(7 / 2)    # 3.5  → normal division
print(7 // 2)   # 3    → floor division, drops the .5
```
 
> 💡 Think of `//` as "how many times does 2 fully fit into 7?" → 3 times.
 
### What is Modulus `%`?
 
```python
print(7 % 2)    # 1  → 7 divided by 2 = 3 remainder 1
print(10 % 3)   # 1  → 10 divided by 3 = 3 remainder 1
print(10 % 2)   # 0  → 10 divided by 2 = 5 remainder 0 (even number!)
```
 
> 💡 Modulus is super useful to check if a number is **even or odd**:
> - If `number % 2 == 0` → even
> - If `number % 2 == 1` → odd
 
---
 
## ⚠️ Watch Out — Division Always Returns a Float!
 
```python
print(4 / 2)    # 2.0  ← notice the .0 — it's a float, not an int!
print(type(4 / 2))    # <class 'float'>
```
 
If you want a whole number result, use `//`:
```python
print(4 // 2)   # 2  ← this is an int
```
 
---
 
## 📦 Storing Math Results in Variables
 
You can do math and save the result into a variable:
 
```python
num1 = 10
num2 = 3
 
addition       = num1 + num2    # 13
subtraction    = num1 - num2    # 7
multiplication = num1 * num2    # 30
division       = num1 / num2    # 3.333...
 
print(addition)
print(subtraction)
print(multiplication)
print(division)
```
 
---
 
## ✏️ Shorthand Operators — Update a Variable Faster
 
Instead of writing `num = num + 1`, Python gives you shortcuts:
 
```python
num = 10
 
num += 5    # same as num = num + 5  → now num is 15
num -= 3    # same as num = num - 3  → now num is 12
num *= 2    # same as num = num * 2  → now num is 24
num /= 4    # same as num = num / 4  → now num is 6.0
 
print(num)  # 6.0
```
 
---
 
## 🛠️ Useful Built-in Number Functions
 
### `abs()` — Absolute Value (removes the negative sign)
 
```python
print(abs(-10))    # 10
print(abs(10))     # 10
print(abs(-3.5))   # 3.5
```
 
> 💡 Useful when you only care about the size of a number, not whether it's positive or negative.
 
---
 
### `round()` — Round a Float
 
```python
print(round(3.75))      # 4    → rounds to nearest whole number
print(round(3.25))      # 3    → rounds down
print(round(3.14159, 2))  # 3.14 → round to 2 decimal places
```
 
---
 
### `type()` — Check What Type a Value Is
 
```python
print(type(5))       # <class 'int'>
print(type(5.0))     # <class 'float'>
print(type("hello")) # <class 'str'>
```
 
> 💡 Very handy when debugging — helps you understand what Python thinks your value is.
 
---
 
## 🔄 Converting Between Types
 
Sometimes you need to switch between `int` and `float`:
 
```python
# Float → Int (cuts off the decimal, does NOT round)
print(int(3.9))     # 3  ← just drops the .9, doesn't round up!
print(int(3.1))     # 3
 
# Int → Float
print(float(5))     # 5.0
 
# String → Int (useful when reading user input)
num = int("42")
print(num + 8)      # 50
```
 
> ⚠️ `int(3.9)` gives `3`, NOT `4` — it doesn't round, it just cuts the decimal off!
> Use `round()` if you want proper rounding.
 
---
 
## 🧮 Order of Operations (PEMDAS / BODMAS)
 
Python follows the same math rules you learned in school:
 
1. **P**arentheses `( )`
2. **E**xponents `**`
3. **M**ultiplication `*` and **D**ivision `/`
4. **A**ddition `+` and **S**ubtraction `-`
```python
print(2 + 3 * 4)      # 14  → multiplication first, then addition
print((2 + 3) * 4)    # 20  → parentheses first!
print(2 ** 3 + 1)     # 9   → exponent first (2³ = 8), then +1
```
 
> 💡 When in doubt — **use parentheses** to make your intention clear!
 
---
 
## 📌 Quick Reference
 
| Operator | What it does | Example | Result |
|----------|-------------|---------|--------|
| `+` | Add | `5 + 3` | `8` |
| `-` | Subtract | `5 - 3` | `2` |
| `*` | Multiply | `5 * 3` | `15` |
| `/` | Divide (float) | `5 / 2` | `2.5` |
| `//` | Floor divide (int) | `5 // 2` | `2` |
| `%` | Remainder | `5 % 2` | `1` |
| `**` | Exponent | `5 ** 2` | `25` |
 
---
 
## 🎯 Day 03 Summary
 
- ✅ `int` = whole numbers, `float` = numbers with decimals
- ✅ Python always returns a **float** from regular division `/`
- ✅ Use `//` for floor division (whole number result)
- ✅ Use `%` to get the remainder
- ✅ Use `**` for powers/exponents
- ✅ Shortcuts: `+=`, `-=`, `*=`, `/=` to update variables fast
- ✅ `abs()` removes negative sign, `round()` rounds decimals
- ✅ `int()` and `float()` convert between types
- ✅ Python follows PEMDAS — use `( )` to control order
---
 
## 🔜 What's Next — Day 04
 
Next I'll learn about **Lists** — storing multiple values in one variable.
 
---
 
*📺 Source: [Corey Schafer — Python Tutorial for Beginners #3](https://www.youtube.com/watch?v=khKv-8q7YmY)*