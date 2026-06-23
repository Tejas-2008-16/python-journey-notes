# ================================================
#   Day 03 — Integers & Floats Practice Code
#   Python Journey by Tejas
# ================================================
 
# --- Two Types of Numbers ---
age   = 20       # int
price = 9.99     # float
 
print(type(age))    # <class 'int'>
print(type(price))  # <class 'float'>
 
# --- Arithmetic Operators ---
print(3 + 2)    # 5   Addition
print(3 - 2)    # 1   Subtraction
print(3 * 2)    # 6   Multiplication
print(3 / 2)    # 1.5 Division
print(3 // 2)   # 1   Floor Division
print(3 % 2)    # 1   Modulus / Remainder
print(3 ** 2)   # 9   Exponent
 
# --- Storing Math in Variables ---
num1 = 10
num2 = 3
 
print(num1 + num2)   # 13
print(num1 - num2)   # 7
print(num1 * num2)   # 30
print(num1 / num2)   # 3.333...
print(num1 // num2)  # 3
print(num1 % num2)   # 1
print(num1 ** num2)  # 1000
 
# --- Shorthand Operators ---
num = 10
num += 5
print(num)    # 15
num -= 3
print(num)    # 12
num *= 2
print(num)    # 24
num /= 4
print(num)    # 6.0
 
# --- Useful Functions ---
print(abs(-10))          # 10
print(round(3.75))       # 4
print(round(3.14159, 2)) # 3.14
 
# --- Type Conversion ---
print(int(3.9))     # 3   (cuts decimal, does NOT round)
print(float(5))     # 5.0
print(int("42"))    # 42
 
# --- Order of Operations ---
print(2 + 3 * 4)    # 14  (multiply first)
print((2 + 3) * 4)  # 20  (parentheses first)