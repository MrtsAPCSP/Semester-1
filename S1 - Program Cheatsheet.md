
# 🐍 Python Programming Cheat Sheet

A quick reference for the key concepts from **Modules 1–6** of our AP CSP Python course.

---

## 📦 Module 1: Variables & Data Types

```python
# Variables
x        = 10          # int
name     = "Alice"     # str
pi       = 3.14        # float
is_happy = True        # bool

# Type checking
print(type(x))         # <class 'int'>

# Type casting
num     = int("5")
decimal = float("3.14")
text    = str(25)
````

**Best Practices:**

* Use **descriptive names**: `total_score` not `ts`
* Don’t start names with numbers or use Python keywords

---

## 🔍 Module 2: Conditions, Booleans, Input/Output

```python
# Input / Output
name = input("Enter your name: ")
print("Hello,", name)

# Booleans & comparisons
a, b = 5, 3
print(a > b)          # True

# If / Elif / Else
age = int(input("Enter your age: "))
if   age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

**Best Practices:**

* Always **cast** input when expecting numbers: `int(input(...))`
* Use **4-space indentation**

---

## 🧩 Module 3: Functions, Parameters, Arguments

```python
# Define & call
def greet(name):
    print("Hello,", name)

greet("Maya")

# With return
def square(n):
    return n * n

result = square(4)

# Recursion
def countdown(n):
    if n == 0:
        print("Liftoff!")
    else:
        print(n)
        countdown(n - 1)
```

**Best Practices:**

* Use `return` for values you’ll reuse
* Name functions with **verbs**: `get_average()`

---

## 🗂️ Module 4: Lists, Dictionaries & Structures

```python
# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[1])         # banana
fruits.append("mango")   # add
fruits[0] = "grape"      # update

# Dictionaries
student = {"name": "Liam", "age": 17}
print(student["name"])   # Liam
student["grade"] = "A"   # add

# List of dicts
classroom = [
    {"name": "Emma", "id": 1},
    {"name": "Noah", "id": 2}
]
print(classroom[0]["name"])  # Emma
```

**Best Practices:**

* Use `[]` for lists, `{}` for dicts
* Keep list items **homogeneous** unless needed

---

## 🔁 Module 5: Loops & Iteration

```python
# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 3:
    print(count)
    count += 1

# Nested loops
for row in range(3):
    for col in range(2):
        print(f"({row}, {col})")
```

**Best Practices:**

* Use `range(start, stop)` correctly
* Always update loop variables to avoid **infinite loops**

---

## 🛠️ Module 6: Advanced Functions & File Handling

```python
# Default parameters
def greet(name="friend"):
    print("Hi", name)

# File reading
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# File writing
with open("output.txt", "w") as file:
    file.write("Hello file!")
```

**Final Project Tips & Best Practices:**

* **Modularize**: Break your program into small functions
* **Document**: Use comments or pseudocode for each step
* **Error-handle**: Use `try/except` around risky operations
* **Files**: Use `with` to auto-close and verify file paths

---

