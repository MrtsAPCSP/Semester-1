# 🧩 Module 3: Functions, Parameters, Arguments & Recursion

Welcome to **Module 3**!  
In this lesson, you’ll learn how to write **functions**, use **parameters and arguments**, return values, and even explore **recursion**—a powerful concept where a function calls itself!

---

## 🧪 What Is a Function?

A **function** is like a mini-program that does a specific task.  
You give it a name so you can **reuse** it as often as needed.

---

## ✏️ Defining a Function

Use `def` to define a function:

```python
def greet():
    print("Hello!")
````

This won’t do anything until you **call** it:

```python
greet()  # This runs the function
```

---

## 🧍 Parameters and Arguments

* **Parameter** = variable inside the function definition
* **Argument** = actual value passed in when the function is called

```python
def greet(name):      # 'name' is a parameter
    print("Hello", name)

greet("Luna")         # "Luna" is the argument
```

You can have **more than one** parameter:

```python
def add(a, b):
    print(a + b)

add(3, 4)  # Output: 7
```

---

## 🔁 Returning Values

Use `return` to send a value back from a function:

```python
def square(x):
    return x * x

result = square(5)
print(result)  # Output: 25
```

> Without `return`, the function might print something but doesn’t give a value you can store or use later.

---

## 🧠 Why Use Functions?

* Avoid repeating yourself (DRY: Don't Repeat Yourself)
* Organize code into smaller pieces
* Reuse the same logic with different inputs

---

## 🔄 Recursion: A Function That Calls Itself

A **recursive function** solves a problem by calling itself with a smaller version of the problem.

```python
def countdown(n):
    if n == 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
```

⚠️ Every recursive function must have a **base case** to stop it, or it will run forever!

---

## ✅ Checkpoints

Try these exercises:

* Create a function with **no parameters** that prints something
* Create a function that accepts a **name** and says hello
* Create a function that takes **2 numbers** and returns the result of adding them
* Try calling a function with the **wrong number of arguments** — what happens?
* Write a **recursive function** that counts up from 1 to a number

---

## 🧩 Mini Practice Challenge

```python
# Write a function called is_even that:
# - Takes one number
# - Returns True if it's even, False if it's odd

# Then call your function and print the result.
```

**Example Output:**

```
Is 4 even? True
```

---

## ⚠️ Common Mistakes to Avoid

### ❌ Forgetting parentheses when calling a function:

```python
greet    # ❌ Nothing happens
greet()  # ✅ This runs it
```

### ❌ Forgetting to use `return` when returning a value

```python
def add(a, b):
    a + b  # ❌ Doesn't return anything
```

✅ Fix:

```python
def add(a, b):
    return a + b
```

### ❌ Using variables that only exist inside the function

```python
def get_name():
    name = "Luna"

print(name)  # ❌ ERROR! name is undefined outside the function
```

### ❌ Infinite recursion

```python
def loop():
    loop()  # ❌ This never stops!
```

✅ Fix: Add a **base case**!

---

## 🚀 Extra Challenge (Stretch Goal)

Write a recursive function that performs **exponentiation**:
Multiplies a number by itself `n` times.

```python
# Example: power(2, 3) → 2 * 2 * 2 = 8
```

---

## 📚 Coming Up Next...

In the next module, you’ll explore **loops**—for and while loops—and learn how to repeat actions efficiently.

---

