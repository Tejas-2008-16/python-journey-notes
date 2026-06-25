# ================================================
#   Day 04 — Lists, Tuples & Sets Practice Code
#   Python Journey by Tejas
# ================================================
 
# ---- LISTS ----
 
fruits  = ["apple", "banana", "mango"]
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
 
# Indexing
print(fruits[0])     # apple
print(fruits[-1])    # mango
 
# Slicing
print(numbers[1:4])  # [1, 4, 1]
print(numbers[:3])   # [3, 1, 4]
 
# Changing items
fruits[1] = "grape"
print(fruits)        # ["apple", "grape", "mango"]
 
# Adding items
fruits.append("kiwi")
print(fruits)        # ["apple", "grape", "mango", "kiwi"]
 
fruits.insert(1, "peach")
print(fruits)        # ["apple", "peach", "grape", "mango", "kiwi"]
 
# Removing items
fruits.remove("grape")
print(fruits)        # ["apple", "peach", "mango", "kiwi"]
 
fruits.pop()
print(fruits)        # ["apple", "peach", "mango"]
 
# Useful methods
print(len(numbers))          # 8
print(numbers.count(1))      # 2
print(numbers.index(5))      # 4
print(min(numbers))          # 1
print(max(numbers))          # 9
print(sum(numbers))          # 31
 
numbers.sort()
print(numbers)               # [1, 1, 2, 3, 4, 5, 6, 9]
 
numbers.reverse()
print(numbers)               # [9, 6, 5, 4, 3, 2, 1, 1]
 
# Check if item exists
print("apple" in fruits)     # True
print("grape" in fruits)     # False
 
# Joining lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)         # [1, 2, 3, 4, 5, 6]
 
 
# ---- TUPLES ----
 
coordinates = (10.5, 20.3)
colors      = ("red", "green", "blue")
 
print(colors[0])     # red
print(colors[-1])    # blue
print(len(colors))   # 3
 
# colors[0] = "yellow"  # ❌ Uncomment to see the error!
 
 
# ---- SETS ----
 
my_set  = {1, 2, 2, 3, 3, 3, 4}
print(my_set)        # {1, 2, 3, 4} — duplicates removed!
 
fruits_set = {"apple", "banana", "mango"}
fruits_set.add("grape")
print(fruits_set)
 
fruits_set.remove("banana")
print(fruits_set)
 
# Set math
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
 
print(set1 & set2)   # {4, 5}              intersection
print(set1 | set2)   # {1,2,3,4,5,6,7,8}  union
print(set1 - set2)   # {1, 2, 3}           difference
 