def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b  # warn: may error on 0

def exponent(a, b):
    return a ** b


print("Welcome to the Python Calculator!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation: +, -, *, /, ^")
operation = input("Enter your choice: ")

if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
elif operation == "^":
    result = exponent(num1, num2)
else:
    result = "Invalid operation"

print("Result:", result)
