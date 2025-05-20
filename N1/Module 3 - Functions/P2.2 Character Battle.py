def create_character(name, power_type, attack, defense):
    return {
        "name": name,
        "power": power_type,
        "attack": attack,
        "defense": defense
    }

def battle(c1, c2):
    print(f"\n🆚 {c1['name']} vs {c2['name']}!")
    damage1 = c1["attack"] - c2["defense"]
    damage2 = c2["attack"] - c1["defense"]

    print(f"{c1['name']} deals {max(damage1, 0)} damage.")
    print(f"{c2['name']} deals {max(damage2, 0)} damage.")

    if damage1 > damage2:
        print(f"🏆 {c1['name']} wins!")
    elif damage2 > damage1:
        print(f"🏆 {c2['name']} wins!")
    else:
        print("🤝 It’s a draw!")

# Example usage
char1 = create_character("Nova", "tech", 8, 4)
char2 = create_character("Blaze", "fire", 6, 6)
battle(char1, char2)


