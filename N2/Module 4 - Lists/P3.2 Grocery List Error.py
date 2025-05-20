grocery_list = ["eggs", "bread", "apples", "cheese", "bananas"]

print("Current grocery list:", grocery_list)

# Let user add an item
new_item = input("Enter an item to add: ")
grocery_list.append(new_item)
print("List after adding:", grocery_list)

# Let user remove an item, with error handling
remove_item = input("Enter an item to remove: ")

if remove_item in grocery_list:
    grocery_list.remove(remove_item)
    print("List after removing:", grocery_list)
else:
    print(f"Item '{remove_item}' not found in the list.")

# Final state of the list
print("Final grocery list:", grocery_list)
