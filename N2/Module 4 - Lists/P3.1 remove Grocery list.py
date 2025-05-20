# Start with an empty grocery list
grocery_list = []

# Add initial items
grocery_list.append("milk")
grocery_list.append("eggs")
grocery_list.append("bread")
grocery_list.append("apples")
grocery_list.append("cheese")

print("Initial grocery list:", grocery_list)

# Add bananas
grocery_list.append("bananas")
print("After adding bananas:", grocery_list)

# Remove milk
grocery_list.remove("milk")
print("After removing milk:", grocery_list)

# Print first and last items
print("First item:", grocery_list[0])
print("Last item:", grocery_list[-1])

# Print the total number of items
print("Total items:", len(grocery_list))
