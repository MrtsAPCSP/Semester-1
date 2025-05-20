## ✅ MODULE 6: Advanced Functions, File Handling & Final Project Tools

---

### 🔁 REVIEW: Why Use Functions?

Functions help you:

* 🧩 Organize and reuse code
* 📥 Take in inputs (parameters) and give back results (return)
* 🔧 Break big problems into small steps

Now let’s take it to the next level!

---

### 🧠 ADVANCED FUNCTIONS

#### 🔹 Returning Multiple Values

Use commas to return multiple things — it creates a **tuple**.

```python
def stats(a, b):
    return a + b, a * b

total, product = stats(2, 3)
print(total, product)  # 5 6
```

---

#### 🔹 Default Parameters

Set a default value so the function still works if no argument is given.

```python
def greet(name="friend"):
    print("Hello", name)

greet()        # Hello friend
greet("Luna")  # Hello Luna
```

---

#### 🔹 Functions Calling Other Functions

You can use one function *inside* another.

```python
def square(x):
    return x * x

def cube(x):
    return square(x) * x

print(cube(3))  # 27
```

---

### 📄 FILE HANDLING

#### 📖 Reading from a File

Make sure the `.txt` file is in your project folder.

```python
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
```

---

#### 📘 Reading Line by Line

Use `with` so Python handles closing the file for you.

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

#### ✍️ Writing to a File

Write new content (overwrites or appends).

```python
with open("output.txt", "w") as file:
    file.write("Hello file!\n")
    file.write("Another line\n")
```

* `"w"` = write (overwrites the file)
* `"a"` = append (adds to the end)

---

### ✅ Checkpoints

* ✅ Write a function that returns 2 values
* ✅ Call a function inside another
* ✅ Read a file and print each line
* ✅ Write something to a file
* ✅ Use a function with a default parameter

---

### 🎯 Mini Practice Challenge

```python
# Write a function that:
# - Opens "names.txt"
# - Reads each line
# - Writes names starting with "A" to "a_names.txt"
```

---

### 🛠️ TIPS FOR YOUR FINAL PROJECT

#### 🗺️ Plan First!

Use comments or pseudocode:

```python
# Step 1: Ask user for input
# Step 2: Store input in a list
# Step 3: Save data to file
```

---

#### 🧩 Use Functions for Each Step

* One for **input**
* One for **processing**
* One for **saving/printing**

---

#### ⚠️ Error Handling

Use `try`/`except` to avoid crashes:

```python
try:
    num = int(input("Enter a number: "))
except:
    print("That’s not a number!")
```

---

### 🧠 Final Project Must-Know Skills

* ✅ Functions & return values
* ✅ Loops & if statements
* ✅ User input/output
* ✅ Lists & dictionaries
* ✅ File reading & writing

---

### 🚫 Common Mistakes

* ❌ Forgetting to `.close()` a file (unless using `with`)
* ❌ Not using `int()`/`float()` on input
* ❌ Code too long — break it into functions!
* ❌ FileNotFoundError — check your filenames and folders

---

### ⭐ Extra Challenge

Build a simple **To-Do List App**:

* Use a dictionary to store tasks and if they’re done (`True`/`False`)
* Save tasks to a file
* Load the file when the app runs again

---
