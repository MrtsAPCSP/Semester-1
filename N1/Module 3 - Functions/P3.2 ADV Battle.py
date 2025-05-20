def create_character(name, power, difficulty):
    print("Character:", name, "| Power:", power, "| Difficulty:", difficulty)
    return power  # Returning power level

def battle_result(power1, power2):
    if power1 > power2:
        return "Player 1 wins!"
    elif power2 > power1:
        return "Player 2 wins!"
    else:
        return "It's a tie!"

# Sample Run
p1_power = create_character("Luna", 7, "Easy")
p2_power = create_character("Blaze", 5, "Hard")
result = battle_result(p1_power, p2_power)
print(result)


