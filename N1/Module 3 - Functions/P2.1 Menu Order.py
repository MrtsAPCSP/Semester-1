def choose_main(protein, style="burger"):
    return f"{style.title()} with {protein.title()}"

def choose_toppings(*toppings):
    return ", ".join(toppings)

def choose_sauce(sauce="ketchup"):
    if sauce == "hot sauce":
        return "🔥 Hot sauce – Spicy!"
    elif sauce == "ranch":
        return "🥛 Ranch – Cooling touch"
    return f"{sauce.title()} – Signature flavor"

def build_combo(main, toppings, sauce, drink="Water"):
    print("\n🍽️ Your Deluxe Combo:")
    print(f"Main: {main}")
    print(f"Toppings: {toppings}")
    print(f"Sauce: {sauce}")
    print(f"Drink: {drink}")
    print("Enjoy your meal!")

# Function calls
main_item = choose_main("tofu", style="taco")
topping_list = choose_toppings("pineapple", "jalapenos", "onions")
sauce_info = choose_sauce("hot sauce")
build_combo(main_item, topping_list, sauce_info, drink="Soda")
