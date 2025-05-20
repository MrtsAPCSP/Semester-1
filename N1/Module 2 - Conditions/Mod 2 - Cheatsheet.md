
# 🔍 Module 2: Conditions, Booleans, Input/Output

Welcome to **Module 2** of AP Computer Science Principles!  
In this module, you’ll learn how programs **make decisions**, use **Boolean logic**, and interact with the user through **input and output**.

---

## ❓ What is a Condition?

A condition is something your program **checks** to decide what to do next.  
Conditions evaluate to **True** or **False** (Boolean values).

---

## 🔢 Boolean Logic & Comparison Operators

You can compare values using these operators:

| Operator | Meaning           | Example (`a = 5`, `b = 3`) | Result |
|----------|-------------------|-----------------------------|--------|
| `==`     | Equals             | `a == 5`                    | True   |
| `!=`     | Not equal          | `a != b`                    | True   |
| `>`      | Greater than       | `a > b`                     | True   |
| `<`      | Less than          | `b < a`                     | True   |
| `>=`     | Greater or equal   | `a >= 5`                    | True   |
| `<=`     | Less or equal      | `b <= 3`                    | True   |

You can combine conditions using:

- `and`: Both must be `True`
- `or`: At least one must be `True`
- `not`: Flips `True` to `False` and vice versa

---

## 🧠 Using `if`, `elif`, and `else`

Example:

```python
age = 16

if age >= 18:
    print("You're an adult.")
elif age >= 13:
    print("You're a teen.")
else:
    print("You're a child.")
````

**Important:**

* Each condition ends with a colon `:`
* Code blocks must be **indented**

---

## 💬 Getting Input From a User

Use the `input()` function to ask a question and store the answer:

```python
name = input("What is your name? ")
print("Hello,", name)
```

> Note: Input is always stored as a **string**, even if it looks like a number.

```python
age = input("How old are you? ")
print(type(age))  # Output: <class 'str'>
```

To work with numbers, **convert** the input:

```python
age = int(input("How old are you? "))
```

---

## ✅ Checkpoints

Try these exercises:

* Ask the user for their **name** and print a greeting
* Ask the user for their **age** and print if they’re a child, teen, or adult
* Use `type()` to confirm that input returns a string
* Add a second condition using `and` or `or`

---

## 🧩 Mini Practice Challenge

```python
# Ask the user for a test score (out of 100)
# If it's 90 or above: print "A"
# If 80–89: print "B"
# If 70–79: print "C"
# If below 70: print "Try again"
```

**Example Output:**

```
Enter your score: 85  
Your grade is: B
```

---

## ⚠️ Common Mistakes to Avoid

### ❌ Forgetting to convert input:

```python
age = input("How old are you? ")
if age > 18:  # ❌ ERROR! comparing str and int
```

✅ Fix it by converting the input:

```python
age = int(input("How old are you? "))
```

---

### ❌ Forgetting colons or indentation:

```python
if age >= 18
print("Adult")  # ❌ ERROR!
```

✅ Correct format:

```python
if age >= 18:
    print("Adult")
```

---

## ⭐ Extra Practice Tip

Try asking the user for their favorite food:

```python
food = input("What's your favorite food? ")

if food == "pizza" or food == "tacos":
    print("Great choice!")
else:
    print("Not my favorite.")
```

---

## 📚 What's Next?

In the next module, you'll learn about **functions**—how to define reusable blocks of code and pass in values using **parameters** and **arguments**.

---


