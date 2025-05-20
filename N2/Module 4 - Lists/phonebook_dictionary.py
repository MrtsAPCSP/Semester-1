# Initial phonebook dictionary
phonebook = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

def print_menu():
    print("\nPhonebook Menu:")
    print("1. Look up a contact")
    print("2. Add a new contact")
    print("3. Update an existing contact")
    print("4. Delete a contact")
    print("5. View all contacts")
    print("6. Quit")

while True:
    print_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        name = input("Enter the name to look up: ")
        if name in phonebook:
            print(f"{name}'s phone number is {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")

    elif choice == "2":
        name = input("Enter the new contact's name: ")
        if name in phonebook:
            print(f"{name} already exists.")
        else:
            number = input("Enter the phone number: ")
            phonebook[name] = number
            print(f"{name} added to phonebook.")

    elif choice == "3":
        name = input("Enter the contact name to update: ")
        if name in phonebook:
            number = input("Enter the new phone number: ")
            phonebook[name] = number
            print(f"{name}'s number updated.")
        else:
            print(f"{name} is not in the phonebook.")

    elif choice == "4":
        name = input("Enter the contact name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print(f"{name} has been deleted.")
        else:
            print(f"{name} is not in the phonebook.")

    elif choice == "5":
        print("\nAll contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number from 1 to 6.")
