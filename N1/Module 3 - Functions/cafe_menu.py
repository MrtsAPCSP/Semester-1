

### 🧾 Function Café Code Menu — **Practice Writing Call Statements**


#### 🥤 **Appetizers – Simple Void Functions (Print Only)**

def serveWater():
    print("Here is your refreshing glass of water!")

def greetCustomer(name):
    print(f"Welcome to the Function Café, {name}!")

def placeNapkinOnTable():
    print("A napkin has been neatly placed on your table.")

#### 🍝 **Main Course – Functions with Parameters and Return Values**

def grilledCheesePrice(slices_of_cheese, bread_slices):
    total = (slices_of_cheese * 0.75) + (bread_slices * 0.50)
    return round(total, 2)

def makeOmelette(eggs, fillings):
    return f"An omelette with {eggs} eggs and fillings: {', '.join(fillings)}."

def portionSize(pasta_type, appetite_level):
    if appetite_level == "small":
        return f"A small serving of {pasta_type}."
    elif appetite_level == "medium":
        return f"A medium serving of {pasta_type}."
    else:
        return f"A large, hearty bowl of {pasta_type}!"


#### 🍰 **Desserts – String or Number Return Functions**

def getCakeFlavor(frosting, filling):
    return f"You ordered a cake with {frosting} frosting and {filling} filling."

def scoopCount(cone_type, scoops):
    return f"You ordered {scoops} scoop(s) in a {cone_type} cone."

def sugarContent(item):
    sugar_database = {
        "cake": 45,
        "ice cream": 30,
        "cookie": 25
    }
    return sugar_database.get(item, 0)


#### ☕ **Drinks – Multiple Parameters**

def orderCoffee(coffee_type, milk, sweetener):
    return f"A {coffee_type} coffee with {milk} milk and {sweetener}."

def makeSmoothie(fruit1, fruit2, size):
    return f"A {size} smoothie with {fruit1} and {fruit2}."

def brewTea(tea_type, steep_minutes):
    return f"Brewing {tea_type} tea for {steep_minutes} minutes. Please wait!"


#### 🛠️ **Chef’s Specials – Advanced Logic**

def serveSurprise(appetite, is_vegetarian):
    if is_vegetarian:
        meal = "grilled veggie panini"
    else:
        meal = "spicy chicken wrap"
    
    if appetite == "small":
        return f"Your small surprise is a mini {meal}."
    else:
        return f"Your surprise is a full-size {meal}!"

def checkAllergy(ingredient_list, allergy):
    return allergy.lower() in [item.lower() for item in ingredient_list]

def buildMeal(main, side, dessert, drink):
    return f"Your meal includes: {main}, {side}, {dessert}, and a {drink}."

"""
### ✏️ Student Practice — **Call Statement Examples**

Have students write code that:

* Greets a customer named “Ava”
* Calculates price for 3 slices of cheese and 2 slices of bread
* Requests a medium pasta portion of "fettuccine"
* Checks if a list of ingredients contains "peanuts"
* Builds a meal with values of their choice
* Calls **every** function at least once!

Let me know if you’d like these in worksheet format or with blanks for guided practice.
"""