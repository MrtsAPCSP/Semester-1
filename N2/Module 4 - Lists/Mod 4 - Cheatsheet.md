# 📦 Module 4: Lists, Dictionaries & Nested Structures

In this module, you’ll learn how to store and organize data using **lists**, **dictionaries**, and **nested structures** like lists inside dictionaries.

---

## 🗂️ What Is a List?

A **list** holds a group of items in one variable. Think of it like a row of boxes:

```python
colors = ["red", "green", "blue"]
````

* Items are **ordered**
* You access them by **index** (starting at 0):

```python
print(colors[0])   # red
print(colors[2])   # blue
```

---

## 🛠️ List Operations

```python
colors.append("yellow")      # Add to the end
colors.insert(1, "orange")   # Insert at index 1
colors.remove("green")       # Remove by value
colors.pop()                 # Remove last item
print(len(colors))           # Find number of items
```

---

## 🔁 Loops with Lists

Use a loop to go through every item:

```python
for color in colors:
    print(color)
```

---

## 🔑 What Is a Dictionary?

A **dictionary** stores **key-value pairs**—like a mini-database or contact list.

```python
student = {
    "name": "Luna",
    "age": 17,
    "grade": "A"
}
```

* Keys must be **unique**
* Values are accessed by key:

```python
print(student["name"])  # Luna
```

---

## 🛠️ Dictionary Operations

```python
student["age"] = 18                 # Update a value
student["school"] = "HHS"          # Add a new key/value
del student["grade"]               # Remove a key
```

Loop through all keys and values:

```python
for key in student:
    print(key, "->", student[key])
```

---

## 🔗 Lists in Dictionaries

You can **combine structures**:

```python
classroom = {
    "students": ["Luna", "Kai", "Zoe"],
    "teacher": "Mr. Z"
}

print(classroom["students"][1])  # Kai
```

---

## 🔗 Dictionaries in Lists

Useful for tracking many similar objects:

```python
students = [
    {"name": "Luna", "grade": "A"},
    {"name": "Kai", "grade": "B"}
]

print(students[0]["name"])  # Luna
```

---

## ✅ Checkpoints

Try these tasks:

* Make a list of your **3 favorite foods**
* Use a **loop** to print each food
* Make a **dictionary** with your name, age, and favorite color
* Add a new key for **hometown**
* Create a **list of dictionaries**, one for each friend

---

## 🧩 Mini Practice Challenge

```python
# Create a dictionary called pet with keys:
# - name
# - type
# - age

# Then print a sentence like:
# "My pet's name is Max. He is a 3-year-old dog."
```

---

## 🧰 Other Useful Data Structures

| Structure     | Description                            |
| ------------- | -------------------------------------- |
| `tuple`       | Like a list, but **cannot be changed** |
| `set`         | **Unordered**, no duplicates           |
| `nested list` | A list inside another list             |

Example of a nested list:

```python
grid = [[1, 2], [3, 4]]
print(grid[0][1])  # Output: 2
```

---

## ⚠️ Common Mistakes

### ❌ List index starts at 1

✅ Actually, it starts at **0**

---

### ❌ Forgetting quotes around dictionary keys

```python
student[name]      # ❌ ERROR
student["name"]    # ✅ Correct
```

---

### ❌ Mixing up lists and dictionaries

Watch your **brackets vs. braces!**

* List → `[]`
* Dictionary → `{}`

---

## 🚀 Extra Challenge (Stretch Goal)

Make a list of **3 students**.
Each student should be a **dictionary** with:

* `name`
* `age`
* `grade`

Then **print their names and grades** using a loop.

---

## 📚 Coming Up Next...

In the next module, you'll learn how to **import libraries** and use tools like **random numbers**, **dates**, and more to supercharge your programs!

---

