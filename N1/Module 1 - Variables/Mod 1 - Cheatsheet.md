
# 🧠 Module 1: Variables & Data Types

Welcome to **Module 1** of AP Computer Science Principles!  
In this module, you'll learn the **basics of programming**: variables, data types, naming rules, and how to check and convert types in Python.



## 🔹 What is a Variable?

A variable is like a labeled box that holds information so you can use or change it later.

```python
x = 5
````

Here, `x` holds the value `5`.

---

## 🔸 Common Data Types

| Data Type | What It Holds        | Example            |
| --------- | -------------------- | ------------------ |
| `int`     | Whole numbers        | `age = 16`         |
| `float`   | Decimal numbers      | `price = 3.99`     |
| `str`     | Text (in quotes)     | `name = "Luna"`    |
| `bool`    | True or False values | `is_tired = False` |

---

## ✏️ Variable Naming Rules

✅ Must start with a letter or underscore (`_`)
🚫 Cannot start with a number
✅ Use only letters, numbers, and underscores
🔠 Case-sensitive: `Score` ≠ `score`
👍 Be descriptive: use `total_score`, not just `ts`

---

## 🕵️ Checking a Variable’s Type

Use the `type()` function to check what kind of data a variable holds:

```python
x = "hello"
print(type(x))  # Output: <class 'str'>
```

---

## 🔄 Type Conversion (Casting)

You can convert one data type into another using functions like `int()`, `str()`, or `float()`:

```python
str_num = "10"
num = int(str_num)      # Now it's an int

pi = 3.14
text_pi = str(pi)       # Now it's a string
```

---

## ✅ Checkpoints

Try these on your own:

* Create 4 variables: an `int`, `float`, `string`, and `boolean`
* Use `print(type(variable))` for each one
* Try converting `"7"` into an integer using `int("7")`

---

## 🧩 Mini Practice Challenge

```python
# Create and print the following:
# - your name (string)
# - your age (integer)
# - whether you're a student (boolean)

# Example Output:
# Name: Alex
# Age: 16
# Student: True
```

---

## ⚠️ Common Mistakes to Avoid

### ❌ Missing quotes on strings:

```python
name = Luna  # ERROR!
name = "Luna"  # ✅ Correct
```

### ❌ Mixing strings and numbers without conversion:

```python
print("Age: " + 16)  # ERROR!
print("Age: " + str(16))  # ✅ Correct
```

---

## 📚 What's Next?

In the next module, you’ll learn how to make your programs smarter by using **conditions, Booleans, and if/else logic**. Stay curious and keep coding!

---

