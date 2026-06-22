# ================================================
#   Day 02 — Strings Practice Code
#   Python Journey by Tejas
# ================================================
 
# --- Creating Strings ---
name    = "Tejas"
city    = 'Pune'
message = """Hello!
My name is Tejas.
I am learning Python."""
 
print(message)
 
# --- Indexing ---
greeting = "Hello"
print(greeting[0])    # H
print(greeting[-1])   # o
 
# --- Slicing ---
text = "Hello, World!"
print(text[0:5])      # Hello
print(text[7:])       # World!
 
# --- Length ---
print(len(name))      # 5
 
# --- String Methods ---
print(name.upper())             # TEJAS
print(name.lower())             # tejas
print(name.capitalize())        # Tejas
 
sentence = "I love Python and Python is awesome"
print(sentence.count("Python"))         # 2
print(sentence.find("Python"))          # 7
print(sentence.replace("Python", "coding"))
 
messy = "   tejas   "
print(messy.strip())            # tejas
 
email = "tejas@gmail.com"
print(email.startswith("tejas"))   # True
print(email.endswith(".com"))      # True
 
# --- Concatenation ---
first = "Tejas"
last  = "More"
print(first + " " + last)      # Tejas More
 
# --- f-Strings ---
age = 20
print(f"My name is {name} and I am {age} years old.")
 