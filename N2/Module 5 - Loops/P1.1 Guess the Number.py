# Python version
secret = 7
guess = int(input("Guess a number: "))
while guess != secret:
    print("Wrong! Try again.")
    guess = int(input("Guess a number: "))
print("Correct!")
