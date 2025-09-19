def choose_class(class_type):
    if class_type == "knight":
        print("Knight: High health, low speed")
    elif class_type == "elf":
        print("Elf: Low health, high speed")
    else:
        print("Peasant: Balanced but weak")

def set_attributes(health, speed):
    if health > 100 or speed > 10:
        print("Error: Attributes too high!")
    else:
        print(f"Health = {health}, Speed = {speed}")

def equip_weapon(weapon, damage):
    print(f"Equipped {weapon} with {damage} attack power")

# Example calls - except you should utilize input to gather user information
choose_class("elf")
set_attributes(80, 9)
equip_weapon("Bow", 15)
