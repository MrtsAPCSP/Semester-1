## ✅ MODULE 5: LOOPS, ITERATION & CONTROL FLOW

### 🔁 Why Use Loops?

Loops help repeat actions without writing the same code again. Use them to:

* Go through a list or dictionary
* Count through numbers
* Repeat until something happens

---

### 🔄 FOR LOOPS

Use when you know how many times to loop or want to go through a collection.

**Loop Through a List**

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

**Loop Using Range**

```python
for i in range(5):
    print(i)  # 0 to 4
```

**Start and Stop Range**

```python
for i in range(1, 6):
    print(i)  # 1 to 5
```

---

### 🔂 WHILE LOOPS

Use when you don’t know how many times to loop. Repeats **as long as** the condition is `True`.

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

⚠️ Be careful! If your condition **never becomes False**, it loops forever.

---

### ♾️ INFINITE LOOPS

These loops keep going unless stopped with `break`.

```python
while True:
    answer = input("Type 'exit' to quit: ")
    if answer == "exit":
        break
```

---

### 🧩 NESTED LOOPS

A loop inside another loop. Good for grids or combinations.

```python
for row in range(3):
    for col in range(3):
        print(f"Row {row}, Col {col}")
```

---

### 🚦 BREAK and CONTINUE

**break** = stops the loop early
**continue** = skips current loop and goes to the next

```python
for i in range(5):
    if i == 3:
        break
    print(i)  # Stops at 2

for i in range(5):
    if i == 3:
        continue
    print(i)  # Skips 3
```

---

### 📋 Looping Through Dictionaries

```python
student = {"name": "Luna", "grade": "A", "age": 17}

for key in student:
    print(key, "->", student[key])
```

---

### 📚 Looping Through List of Dictionaries

```python
students = [
    {"name": "Luna", "grade": "A"},
    {"name": "Kai", "grade": "B"}
]

for student in students:
    print(student["name"], "has grade", student["grade"])
```

---

### ✅ Checkpoints

* ✅ Use a `for` loop to print numbers 1–10
* ✅ Use a `while` loop to let the user guess a number until it’s right
* ✅ Loop through a list of foods and print each one
* ✅ Use a nested loop to print a grid
* ✅ Add a `break` to exit early

---

### 🎯 Mini Practice Challenge

```python
# Ask user for a password until it's correct
while True:
    password = input("Enter password: ")
    if password == "OpenSesame":
        print("Access granted")
        break
```

---

### ⚠️ Common Mistakes

🚫 Forgetting to update variables in a `while` loop → infinite loop
🚫 Using `=` instead of `==` in conditions
🚫 Off-by-one errors in `range()`
🚫 Missing indentation (Python needs it for loops)

---

### ⭐ Extra Challenge: Triangle of Stars

```python
for i in range(1, 6):
    print("*" * i)
```

Output:

```
*
**
***
****
*****
```
