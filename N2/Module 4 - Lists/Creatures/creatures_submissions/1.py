import random
from creature_data import creatures

used_ids = set()

def get_creatures_by_class(class_period):
    # Filter creatures by class_period, excluding used ones
    return {
        cid: c for cid, c in creatures.items()
        if c.get("class_period") == class_period and cid not in used_ids
    }

def short_id(full_id):
    # Return last 4 characters for simplified ID
    return full_id[-4:]

def display_creatures(creature_dict):
    print(f"\nAvailable creatures in Class Period {next(iter(creature_dict.values()))['class_period']}:\n")
    for cid, c in creature_dict.items():
        wins = c.get("win_count", 0)
        strength = c.get("strength", 100)  # default strength 100 if not set
        print(f" - {c['name']} (ID: {short_id(cid)}, Wins: {wins}, Strength: {strength}, Student: {c['student_name']})")

def select_creature(prompt_text, creatures_dict):
    while True:
        selection = input(prompt_text).strip().lower()
        for cid, c in creatures_dict.items():
            if (
                selection == short_id(cid).lower()
                or selection == c["name"].lower()
                or selection == c["student_name"].lower()
            ):
                used_ids.add(cid)
                return cid, c
        print("❌ Invalid selection. Please choose by name, last 4 of ID, or student name.")

def ask_boost_use(creature):
    if creature.get("terrain_boost_used", False):
        print(f"{creature['name']} has already used their terrain boost.")
        return False
    choice = input(f"Does {creature['name']} want to use their one-time terrain boost? (y/n): ").strip().lower()
    if choice == 'y':
        creature["terrain_boost_used"] = True
        print(f"{creature['name']} used their terrain boost!")
        return True
    else:
        print(f"{creature['name']} did not use their terrain boost.")
        return False

def calculate_effects(creature, terrain, weather, used_boost):
    # For demonstration, assign random effects, you can customize this logic
    base_strength = creature.get("strength", 100)
    terrain_effect = random.randint(-10, 15)  # terrain can give positive or negative boost
    weather_effect = random.randint(-5, 10)   # weather can also help or hurt
    boost_effect = 0
    if used_boost:
        boost_effect = random.randint(5, 20)  # boost always positive

    total_change = terrain_effect + weather_effect + boost_effect
    new_strength = base_strength + total_change
    if new_strength < 0:
        new_strength = 0  # no negative strength

    # Update creature's strength
    creature["strength"] = new_strength

    return terrain_effect, weather_effect, boost_effect, base_strength, new_strength

def main():
    print("🎮 Welcome to the Creature Battle Tournament!\n")
    # Step 1: Select class period
    class_periods = sorted(set(c.get("class_period") for c in creatures.values() if c.get("class_period") is not None))
    print("Available Class Periods:")
    for cp in class_periods:
        print(f" - {cp}")
    class_period = input("Select a class period to battle: ").strip()

    if class_period not in class_periods:
        print("❌ Invalid class period selected.")
        return

    terrains = ["Forest", "Mountain", "Desert", "Swamp", "Plains"]
    weathers = ["Sunny", "Rainy", "Stormy", "Foggy", "Windy"]

    while True:
        available = get_creatures_by_class(class_period)
        if len(available) < 2:
            if len(available) == 1:
                last_cid, last_creature = next(iter(available.items()))
                print(f"\n🎉 Congratulations! The tournament winner is {last_creature['name']} (Student: {last_creature['student_name']}, Wins: {last_creature.get('win_count', 0)}) 🎉")
            else:
                print("\nNo creatures left to battle.")
            break

        display_creatures(available)

        print("\nSelect two creatures to battle:")
        cid1, creature1 = select_creature("Enter the first creature (name, last 4 of ID, or student): ", available)
        available.pop(cid1)
        cid2, creature2 = select_creature("Enter the second creature (name, last 4 of ID, or student): ", available)

        # Randomly select terrain and weather for this battle
        terrain = random.choice(terrains)
        weather = random.choice(weathers)

        print(f"\n🌍 Battle Environment: Terrain - {terrain}, Weather - {weather}\n")

        # Ask each creature if they want to use terrain boost
        boost1 = ask_boost_use(creature1)
        boost2 = ask_boost_use(creature2)

        print(f"\n⚔️ {creature1['name']} (ID: {short_id(cid1)}, Boost Used: {boost1}) vs {creature2['name']} (ID: {short_id(cid2)}, Boost Used: {boost2})\n")

        # Calculate effects and update strength for each creature
        terrain_effect1, weather_effect1, boost_effect1, old_str1, new_str1 = calculate_effects(creature1, terrain, weather, boost1)
        terrain_effect2, weather_effect2, boost_effect2, old_str2, new_str2 = calculate_effects(creature2, terrain, weather, boost2)

        # Show detailed strength info
        print(f"{creature1['name']}:")
        print(f"  Strength before: {old_str1}")
        print(f"  Terrain effect: {terrain_effect1:+}")
        print(f"  Weather effect: {weather_effect1:+}")
        print(f"  Boost effect: {boost_effect1:+}")
        print(f"  Strength after: {new_str1}\n")

        print(f"{creature2['name']}:")
        print(f"  Strength before: {old_str2}")
        print(f"  Terrain effect: {terrain_effect2:+}")
        print(f"  Weather effect: {weather_effect2:+}")
        print(f"  Boost effect: {boost_effect2:+}")
        print(f"  Strength after: {new_str2}\n")

        # Determine winner based on higher new strength (tie breaks randomly)
        if new_str1 > new_str2:
            winner = creature1
            winner_cid = cid1
        elif new_str2 > new_str1:
            winner = creature2
            winner_cid = cid2
        else:
            # Tie: randomly pick winner
            winner = random.choice([creature1, creature2])
            winner_cid = cid1 if winner == creature1 else cid2

        # Increment win count
        winner.setdefault("win_count", 0)
        winner["win_count"] += 1

        print(f"🏆 Winner: {winner['name']} (Student: {winner['student_name']}, Wins: {winner['win_count']})")

        # Ask if winner advances
        keep_winner = input("Should the winner advance to the next round? (y/n): ").strip().lower()
        if keep_winner == 'y':
            used_ids.discard(winner_cid)

    print("\n✅ Tournament complete!")

if __name__ == "__main__":
    main()
