# ================================================
#   Day 05 — Dictionaries Practice Code
#   Python Journey by Tejas
# ================================================
 
# --- Creating a Dictionary ---
student = {
    "name"  : "Tejas",
    "age"   : 20,
    "city"  : "Pune",
    "grade" : 9.5
}
 
# --- Accessing Values ---
print(student["name"])     # Tejas
print(student["age"])      # 20
 
# Safe access with .get()
print(student.get("city"))              # Pune
print(student.get("phone"))             # None
print(student.get("phone", "N/A"))      # N/A
 
# --- Adding & Updating ---
student["email"] = "tejas@gmail.com"   # add new key
student["age"]   = 21                  # update existing key
print(student)
 
# --- Deleting ---
del student["grade"]
print(student)
 
removed = student.pop("email")
print(removed)    # tejas@gmail.com
print(student)
 
# --- Check if Key Exists ---
print("name" in student)      # True
print("phone" in student)     # False
 
# --- Length ---
print(len(student))           # 3
 
# --- Dictionary Methods ---
print(student.keys())         # dict_keys(['name', 'age', 'city'])
print(student.values())       # dict_values(['Tejas', 21, 'Pune'])
print(student.items())        # dict_items([...])
 
# --- Looping ---
for key in student:
    print(key)
 
for value in student.values():
    print(value)
 
for key, value in student.items():
    print(f"{key} : {value}")
 
# --- Nested Dictionary ---
students = {
    "student1": {"name": "Tejas", "age": 20},
    "student2": {"name": "Raj",   "age": 21}
}
 
print(students["student1"]["name"])    # Tejas
print(students["student2"]["age"])     # 21
 
# --- .update() ---
student = {"name": "Tejas", "age": 20}
new_info = {"city": "Pune", "age": 21}
student.update(new_info)
print(student)    # {'name': 'Tejas', 'age': 21, 'city': 'Pune'}
 