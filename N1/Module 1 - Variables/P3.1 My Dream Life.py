#My Dream Life Program
# Below is a template


"""

🧠 Student Instructions:
Create a program with at least:
2 str variables for who you are and where you live
2 int or float variables for things like salary, hours of sleep, or age
2 bool variables about your lifestyle
1 calculated variable (e.g., monthly income = yearly / 12)
6+ creative print() statements combining your variables to describe your future life

"""

# Basic personal details
name = "Jordan"
future_age = 25
city = "Tokyo"
job = "Game Developer"

# Financial and lifestyle details
yearly_salary = 95000.0
monthly_salary = yearly_salary / 12
has_pet = True
pet_type = "Shiba Inu"
owns_house = False
sleeps_hours = 7.5

# Fun and hobbies
favorite_hobby = "drawing digital art"
daily_screen_time = 6.5  # in hours

# Print dream life summary
print("🌟 My Dream Life in 10 Years 🌟")
print("My name is " + name + " and I will be " + str(future_age) + " years old.")
print("I live in " + city + " and work as a " + job + ".")
print("I earn $" + str(yearly_salary) + " per year, or about $" + str(round(monthly_salary, 2)) + " per month.")
print("Do I own a house? " + str(owns_house))
print("Do I have a pet? " + str(has_pet))
if has_pet:
    print("My pet is a " + pet_type + "!")
print("I sleep " + str(sleeps_hours) + " hours per night.")
print("In my free time, I love " + favorite_hobby + ".")
print("I spend about " + str(daily_screen_time) + " hours a day on screens.")
