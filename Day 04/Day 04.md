# 🐍 Day 04 — Lists, Tuples & Sets
 
> **Video:** Python Tutorial for Beginners #4 — Lists, Tuples, and Sets by Corey Schafer
> **Watch it here →** [▶️ YouTube](https://www.youtube.com/watch?v=W8KRzm-HUcc)
> **Date:** June 2026
> **Goal:** Learn how to store multiple values in one variable using Lists, Tuples, and Sets
 
---
 
## 🧠 What I learned today
 
- What a List is and how to create one
- How to access, add, remove, and update items in a List
- Useful List methods
- What a Tuple is and how it's different from a List
- What a Set is and why it's special
- When to use each one
---
 
## 📋 The Problem Lists Solve
 
So far, we've stored one value per variable:
 
```python
name1 = "Tejas"
name2 = "Raj"
name3 = "Aman"
```
 
This gets messy fast. What if you had 100 names?
 
**Lists let you store many values in one variable:**
 
```python
names = ["Tejas", "Raj", "Aman"]
```
 
---
 
## 📝 Lists
 
A **List** is an ordered collection of items. You can store anything in it — strings, numbers, even mixed types.
 
```python
fruits    = ["apple", "banana", "mango"]
numbers   = [1, 2, 3, 4, 5]
mixed     = ["Tejas", 20, 9.5, True]   # mixed types are allowed!
empty     = []                           # empty list
```
 
> 💡 Lists use **square brackets** `[ ]` and items are separated by commas.
 
---
 
### 🔢 Accessing Items — Indexing
 
Just like Strings, Lists use **index numbers** starting from `0`:
 
```python
fruits = ["apple", "banana", "mango"]
 
print(fruits[0])    # apple   → first item
print(fruits[1])    # banana  → second item
print(fruits[2])    # mango   → third item
print(fruits[-1])   # mango   → last item (negative index!)
```
 
---
 
### ✂️ Slicing a List
 
```python
numbers = [10, 20, 30, 40, 50]
 
print(numbers[1:4])   # [20, 30, 40] → index 1 up to (not including) 4
print(numbers[:3])    # [10, 20, 30] → from beginning to index 3
print(numbers[2:])    # [30, 40, 50] → from index 2 to the end
```
 
---
 
### ✏️ Changing Items
 
Lists are **mutable** — you can change them after creating them.
 
```python
fruits = ["apple", "banana", "mango"]
 
fruits[1] = "grape"     # replace "banana" with "grape"
print(fruits)           # ["apple", "grape", "mango"]
```
 
---
 
### ➕ Adding Items
 
```python
fruits = ["apple", "banana"]
 
fruits.append("mango")      # adds to the END of the list
print(fruits)               # ["apple", "banana", "mango"]
 
fruits.insert(1, "grape")   # insert at a specific index
print(fruits)               # ["apple", "grape", "banana", "mango"]
```
 
> 💡 `.append()` → adds to the end (most common)
> 💡 `.insert(index, value)` → adds at a specific position
 
---
 
### ➖ Removing Items
 
```python
fruits = ["apple", "banana", "mango", "banana"]
 
fruits.remove("banana")   # removes the FIRST occurrence of "banana"
print(fruits)             # ["apple", "mango", "banana"]
 
fruits.pop()              # removes and returns the LAST item
print(fruits)             # ["apple", "mango"]
 
fruits.pop(0)             # removes item at index 0
print(fruits)             # ["mango"]
```
 
---
 
### 🔍 Other Useful List Methods
 
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
 
print(len(numbers))          # 8        → total number of items
print(numbers.count(1))      # 2        → how many times 1 appears
print(numbers.index(5))      # 4        → index of first occurrence of 5
print(min(numbers))          # 1        → smallest value
print(max(numbers))          # 9        → largest value
print(sum(numbers))          # 31       → total sum
 
numbers.sort()
print(numbers)               # [1, 1, 2, 3, 4, 5, 6, 9] → sorted low to high
 
numbers.reverse()
print(numbers)               # [9, 6, 5, 4, 3, 2, 1, 1] → reversed
```
 
---
 
### 🔗 Joining Two Lists
 
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
 
combined = list1 + list2
print(combined)    # [1, 2, 3, 4, 5, 6]
```
 
---
 
### 🔎 Checking if an Item Exists
 
```python
fruits = ["apple", "banana", "mango"]
 
print("banana" in fruits)    # True
print("grape" in fruits)     # False
```
 
---
 
## 📦 Tuples
 
A **Tuple** is just like a List BUT it is **immutable** — once you create it, you **cannot change it**.
 
```python
coordinates = (10.5, 20.3)         # uses parentheses ( )
colors      = ("red", "green", "blue")
single      = (42,)                # single item tuple needs a trailing comma!
```
 
> 💡 Tuples use **parentheses** `( )` instead of `[ ]`
 
### Accessing Tuple items (same as Lists):
 
```python
colors = ("red", "green", "blue")
 
print(colors[0])    # red
print(colors[-1])   # blue
print(len(colors))  # 3
```
 
### ❌ You CANNOT change a Tuple:
 
```python
colors = ("red", "green", "blue")
colors[0] = "yellow"    # ❌ ERROR! Tuples cannot be modified
```
 
### When to use a Tuple vs a List?
 
| | List `[ ]` | Tuple `( )` |
|--|-----------|------------|
| **Changeable?** | ✅ Yes | ❌ No |
| **Use when** | Data will change | Data should stay fixed |
| **Example** | Shopping cart items | GPS coordinates, RGB colors |
 
> 💡 Use a **Tuple** when your data should never be changed — like coordinates, days of the week, or fixed settings. It's also slightly faster than a List.
 
---
 
## 🔵 Sets
 
A **Set** is a collection that:
1. Has **no duplicate values** — every item is unique
2. Is **unordered** — items have no fixed position (no indexing!)
```python
my_set = {1, 2, 3, 4, 5}           # uses curly braces { }
names  = {"Tejas", "Raj", "Aman"}
```
 
> 💡 Sets use **curly braces** `{ }` — but so do Dictionaries! The difference is Sets have no key:value pairs.
 
### Duplicates are automatically removed:
 
```python
numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers)    # {1, 2, 3, 4}  → duplicates gone!
```
 
### Adding & Removing from a Set:
 
```python
fruits = {"apple", "banana", "mango"}
 
fruits.add("grape")        # add one item
print(fruits)              # {"apple", "banana", "mango", "grape"}
 
fruits.remove("banana")    # remove an item
print(fruits)              # {"apple", "mango", "grape"}
```
 
### Set Math — Intersections & Unions:
 
```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
 
print(set1 & set2)           # {4, 5}           → items in BOTH sets (intersection)
print(set1 | set2)           # {1,2,3,4,5,6,7,8} → all items combined (union)
print(set1 - set2)           # {1, 2, 3}         → items only in set1 (difference)
```
 
---
 
## 🗂️ Quick Comparison — Which One to Use?
 
| Feature | List `[ ]` | Tuple `( )` | Set `{ }` |
|---------|-----------|------------|----------|
| **Ordered?** | ✅ Yes | ✅ Yes | ❌ No |
| **Changeable?** | ✅ Yes | ❌ No | ✅ Yes |
| **Allows duplicates?** | ✅ Yes | ✅ Yes | ❌ No |
| **Indexed?** | ✅ Yes | ✅ Yes | ❌ No |
| **Best for** | General use | Fixed data | Unique items |
 
---
 
## 🎯 Day 04 Summary
 
- ✅ **List** `[ ]` → ordered, changeable, allows duplicates — most common!
- ✅ Use `.append()` to add, `.remove()` or `.pop()` to delete
- ✅ Use `.sort()`, `.reverse()`, `len()`, `min()`, `max()`, `sum()` on lists
- ✅ **Tuple** `( )` → ordered, NOT changeable — use for fixed data
- ✅ **Set** `{ }` → unordered, NO duplicates — great for unique collections
- ✅ Check if item exists with `"item" in list`
---
 
## 🔜 What's Next — Day 05
 
Next I'll learn about **Dictionaries** — storing data as key-value pairs like a real-world dictionary.
 
---
 
*📺 Source: [Corey Schafer — Python Tutorial for Beginners #4](https://www.youtube.com/watch?v=W8KRzm-HUcc)*