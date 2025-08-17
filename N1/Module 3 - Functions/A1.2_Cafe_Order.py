# practice_cafe_calls.py

import cafe_menu

# 🥤 Appetizer Practice
# 1. Greet the customer named "Ava"
cafe_menu.greetCustomer("Ava")

# 2. Place a napkin on the table
cafe_menu.placeNapkinOnTable()

# 🍝 Main Course Practice
# 3. Calculate the cost of a grilled cheese with 3 slices of cheese and 2 slices of bread
price = cafe_menu.grilledCheesePrice(3, 2)
print("Grilled Cheese Cost: $", price)

# 4. Order an omelette with 2 eggs and ["mushrooms", "spinach"]
omelette = cafe_menu.makeOmelette(2, ["mushrooms", "spinach"])
print(omelette)

# 5. Get a medium portion of fettuccine
portion = cafe_menu.portionSize("fettuccine", "medium")
print(portion)

# 🍰 Dessert Practice
# 6. Order a cake with vanilla frosting and raspberry filling
cake = cafe_menu.getCakeFlavor("vanilla", "raspberry")
print(cake)

# 7. Count scoops in a waffle cone with 3 scoops
scoops = cafe_menu.scoopCount("waffle", 3)
print(scoops)

# 8. Find the sugar content in a cookie
sugar = cafe_menu.sugarContent("cookie")
print("Sugar content:", sugar, "grams")

# ☕ Drink Practice
# 9. Order a latte with oat milk and 2 sugar cubes
coffee = cafe_menu.orderCoffee("latte", "oat", "2 sugar cubes")
print(coffee)

# 10. Make a large smoothie with banana and strawberry
smoothie = cafe_menu.makeSmoothie("banana", "strawberry", "large")
print(smoothie)

# 11. Brew green tea for 5 minutes
tea = cafe_menu.brewTea("green", 5)
print(tea)

# 🛠️ Chef's Specials Practice
# 12. Get a vegetarian surprise meal for a big appetite
surprise = cafe_menu.serveSurprise("large", True)
print(surprise)

# 13. Check if ["milk", "peanuts", "flour"] contains "peanuts"
has_allergy = cafe_menu.checkAllergy(["milk", "peanuts", "flour"], "peanuts")
print("Contains allergy ingredient?", has_allergy)

# 14. Build a meal with: pizza, salad, brownie, lemonade
meal = cafe_menu.buildMeal("pizza", "salad", "brownie", "lemonade")
print(meal)
