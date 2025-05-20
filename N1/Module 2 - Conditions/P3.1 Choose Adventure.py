print("🌟 Welcome to The Mysterious Forest 🌲")

name = input("What is your name, traveler? ")
print("Welcome, " + name + "! Your journey begins now...")

# First decision
path = input("You see two paths: one dark and twisty, one sunny and clear. Which path do you take? (dark/sunny) ")

if path.lower() == "dark":
    print("You walk into the shadows... and hear a growl.")
    action = input("Do you RUN or HIDE? ").lower()
    
    if action == "run":
        print("You trip over a root and... get eaten by a shadow beast. 🐺")
    elif action == "hide":
        print("You hide behind a tree until the danger passes. You find a glowing stone!")
    else:
        print("You freeze. Something touches your shoulder. You faint. The end.")
        
elif path.lower() == "sunny":
    print("You walk into a peaceful meadow with birds chirping.")
    choice = input("Do you pick flowers or chase a butterfly? (flowers/butterfly) ").lower()
    
    if choice == "flowers":
        print("The flowers turn into gold in your hands! You’re rich!")
    elif choice == "butterfly":
        print("The butterfly leads you to a hidden village that welcomes you.")
    else:
        print("You stand there until night falls... and then it gets spooky.")
        
else:
    print("You wander in circles and never choose a path. The forest keeps you forever.")
