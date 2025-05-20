print("🧠 Welcome to the Mini Quiz!")

score = 0

answer1 = input("What color do you get when you mix red and blue? ")
if answer1.lower() == "purple":
    print("Correct!")
    score += 1
else:
    print("Oops! The correct answer is purple.")

answer2 = input("Is the sun a star? (yes/no) ")
if answer2.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Nope! The sun *is* a star.")

print("\nYou got", score, "out of 2 correct!")
