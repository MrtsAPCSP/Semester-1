# Character 1
name1 = "Luna"
age1 = 21
power1 = 85.5
is_friendly1 = True
element1 = "Water"

# Character 2
name2 = "Blaze"
age2 = 23
power2 = 92.0
is_friendly2 = False
element2 = "Fire"

# Combined variables
average_power = (power1 + power2) / 2
age_difference = abs(age1 - age2)
same_element = element1 == element2
power_difference = round(abs(power1 - power2), 1)

# Output the results
print("=== Character Battle ===")
print(name1 + " vs " + name2)
print(name1 + " is " + str(age1) + " years old and controls " + element1 + ".")
print(name2 + " is " + str(age2) + " years old and controls " + element2 + ".")
print(name1 + "'s power: " + str(power1))
print(name2 + "'s power: " + str(power2))
print("Are they allies? " + str(is_friendly1 and is_friendly2))
print("Do they share the same element? " + str(same_element))
print("Age difference: " + str(age_difference) + " years")
print("Power difference: " + str(power_difference))
print("Average power level: " + str(average_power))
