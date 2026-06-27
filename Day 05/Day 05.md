# 🐍 Day 05 — Dictionaries
 
> **Video:** Python Tutorial for Beginners #5 — Dictionaries by Corey Schafer
> **Watch it here →** [▶️ YouTube](https://www.youtube.com/watch?v=daefaLgNkw0)
> **Date:** June 2026
> **Goal:** Learn how to store data as key-value pairs using Dictionaries
 
---
 
## 🧠 What I learned today
 
- What a Dictionary is and why it's useful
- How to create a Dictionary
- How to access, add, update, and delete values
- How to loop through a Dictionary
- Useful Dictionary methods
- The difference between a Dictionary and a List
---
 
## 📖 What is a Dictionary?
 
A **Dictionary** stores data as **key : value** pairs — just like a real dictionary where you look up a word (key) to find its meaning (value).
 
Instead of accessing data by index number like a List, you access it by a **key name** — which makes your code much more readable!
 
```python
# List — access by index (hard to remember what index 0 means)
student = ["Tejas", 20, "Pune"]
print(student[0])    # Tejas — but what does index 0 mean?
 
# Dictionary — access by key (crystal clear!)
student = {"name": "Tejas", "age": 20, "city": "Pune"}
print(student["name"])    # Tejas — obvious!
```
 
---
 
## 🛠️ Creating a Dictionary
 
Use **curly braces** `{ }` with `key: value` pairs separated by commas:
 
```python
student = {
    "name"  : "Tejas",
    "age"   : 20,
    "city"  : "Pune",
    "grade" : 9.5
}
```
 
> 💡 Keys are usually **strings** `" "`, but values can be anything — strings, numbers, lists, even another dictionary!
 
---
 
## 🔍 Accessing Values
 
### Method 1 — Square Brackets `[ ]`
 
```python
student = {"name": "Tejas", "age": 20, "city": "Pune"}
 
print(student["name"])    # Tejas
print(student["age"])     # 20
print(student["city"])    # Pune
```
 
> ⚠️ If the key doesn't exist, this will throw a **KeyError**!
> ```python
> print(student["phone"])   # ❌ KeyError: 'phone'
> ```
 
---
 
### Method 2 — `.get()` (Safer!)
 
```python
student = {"name": "Tejas", "age": 20}
 
print(student.get("name"))     # Tejas
print(student.get("phone"))    # None  → no error, just returns None
print(student.get("phone", "Not Found"))   # Not Found → custom default value
```
 
> 💡 `.get()` is the **safer way** to access values — it never crashes your program. Use it when you're not sure if the key exists!
 
---
 
## ✏️ Adding & Updating Values
 
```python
student = {"name": "Tejas", "age": 20}
 
# Adding a new key-value pair
student["city"] = "Pune"
print(student)    # {"name": "Tejas", "age": 20, "city": "Pune"}
 
# Updating an existing value
student["age"] = 21
print(student)    # {"name": "Tejas", "age": 21, "city": "Pune"}
```
 
> 💡 Same syntax for both adding and updating — if the key exists it updates, if it doesn't it adds!
 
---
 
## ❌ Deleting Key-Value Pairs
 
```python
student = {"name": "Tejas", "age": 20, "city": "Pune"}
 
del student["city"]
print(student)    # {"name": "Tejas", "age": 20}
 
# .pop() removes AND returns the value
age = student.pop("age")
print(age)        # 20
print(student)    # {"name": "Tejas"}
```
 
---
 
## 🔎 Checking if a Key Exists
 
```python
student = {"name": "Tejas", "age": 20}
 
print("name" in student)     # True
print("phone" in student)    # False
```
 
> 💡 Always check if a key exists before accessing it with `[ ]` to avoid a KeyError!
 
---
 
## 📏 Dictionary Length
 
```python
student = {"name": "Tejas", "age": 20, "city": "Pune"}
 
print(len(student))    # 3 → number of key-value pairs
```
 
---
 
## 🔧 Useful Dictionary Methods
 
```python
student = {
    "name" : "Tejas",
    "age"  : 20,
    "city" : "Pune"
}
 
# Get all keys
print(student.keys())     # dict_keys(['name', 'age', 'city'])
 
# Get all values
print(student.values())   # dict_values(['Tejas', 20, 'Pune'])
 
# Get all key-value pairs as tuples
print(student.items())    # dict_items([('name','Tejas'), ('age',20), ('city','Pune')])
```
 
---
 
## 🔄 Looping Through a Dictionary
 
### Loop through keys (default):
 
```python
student = {"name": "Tejas", "age": 20, "city": "Pune"}
 
for key in student:
    print(key)
# name
# age
# city
```
 
### Loop through values:
 
```python
for value in student.values():
    print(value)
# Tejas
# 20
# Pune
```
 
### Loop through both keys AND values (most useful!):
 
```python
for key, value in student.items():
    print(f"{key} : {value}")
# name : Tejas
# age  : 20
# city : Pune
```
 
> 💡 `.items()` with `key, value` unpacking is the most common way to loop through a dictionary — remember this one!
 
---
 
## 🧩 Nested Dictionaries
 
You can store a dictionary **inside** a dictionary — useful for complex real-world data:
 
```python
students = {
    "student1": {
        "name": "Tejas",
        "age" : 20
    },
    "student2": {
        "name": "Raj",
        "age" : 21
    }
}
 
# Accessing nested values
print(students["student1"]["name"])    # Tejas
print(students["student2"]["age"])     # 21
```
 
---
 
## 🆕 `.update()` — Merge Another Dictionary In
 
```python
student = {"name": "Tejas", "age": 20}
 
new_info = {"city": "Pune", "age": 21}   # age will be updated, city will be added
 
student.update(new_info)
print(student)
# {"name": "Tejas", "age": 21, "city": "Pune"}
```
 
> 💡 `.update()` is great for merging two dictionaries or bulk-updating values!
 
---
 
## 🗂️ Dictionary vs List — When to Use Which?
 
| | List `[ ]` | Dictionary `{ }` |
|--|-----------|-----------------|
| **Access by** | Index number `[0]` | Key name `["name"]` |
| **Best for** | Ordered sequences of items | Labelled data with named fields |
| **Example** | `["apple", "banana"]` | `{"name": "Tejas", "age": 20}` |
| **Readable?** | Medium | ✅ Very readable |
 
> 💡 Rule of thumb: if your data has **labels/names**, use a Dictionary. If it's just a **collection of items**, use a List.
 
---
 
## 📌 Quick Reference — All Methods
 
| Method | What it does | Example |
|--------|-------------|---------|
| `d["key"]` | Access value (crashes if missing) | `student["name"]` |
| `d.get("key")` | Access value safely | `student.get("phone")` |
| `d["key"] = val` | Add or update | `student["age"] = 21` |
| `del d["key"]` | Delete a pair | `del student["city"]` |
| `d.pop("key")` | Remove and return value | `student.pop("age")` |
| `"key" in d` | Check if key exists | `"name" in student` |
| `len(d)` | Count pairs | `len(student)` |
| `d.keys()` | Get all keys | `student.keys()` |
| `d.values()` | Get all values | `student.values()` |
| `d.items()` | Get all pairs | `student.items()` |
| `d.update(d2)` | Merge dictionary in | `student.update(new_info)` |
 
---
 
## 🎯 Day 05 Summary
 
- ✅ Dictionary `{ }` stores **key : value** pairs
- ✅ Access values with `d["key"]` or safely with `d.get("key")`
- ✅ Add or update with `d["key"] = value`
- ✅ Delete with `del d["key"]` or `d.pop("key")`
- ✅ Check existence with `"key" in d`
- ✅ Loop with `.keys()`, `.values()`, or `.items()`
- ✅ Nested dictionaries = dictionary inside a dictionary
- ✅ Use `.update()` to merge two dictionaries
---
 
## 🔜 What's Next — Day 06
 
Next I'll learn about **Conditionals** — making decisions in Python with `if`, `elif`, and `else`.
 
---
 
*📺 Source: [Corey Schafer — Python Tutorial for Beginners #5](https://www.youtube.com/watch?v=daefaLgNkw0)*
