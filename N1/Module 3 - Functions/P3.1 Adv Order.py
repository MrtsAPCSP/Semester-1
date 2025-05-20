def make_main(main, top1, top2):
    print("Main Item:", main, "with", top1, "and", top2)
    return 5.0 + 0.5 + 0.5  # base + toppings

def add_side(side):
    print("Side:", side)
    return 2.0

def add_drink(drink):
    print("Drink:", drink)
    return 1.5

def calculate_total(main_price, side_price, drink_price):
    return main_price + side_price + drink_price

def print_receipt(total):
    print("Total Price: $", total)

# Sample Call Chain
m = make_main("Burger", "Lettuce", "Tomato")
s = add_side("Fries")
d = add_drink("Soda")
t = calculate_total(m, s, d)
print_receipt(t)


