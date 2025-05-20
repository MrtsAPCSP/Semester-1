
def print_menu():
    print("\nGradebook Menu:")
    print("1. View all students")
    print("2. Add a new student")
    print("3. Add scores to a student")
    print("4. Remove a student")
    print("5. Print grade report")
    print("6. Quit")

while True:
    print_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        for s in students:
            print(f"{s['name']} (ID: {s['id']})")
    elif choice == "2":
        name = input("Enter new student's name: ")
        student_id = int(input("Enter new student's ID: "))
        scores_str = input("Enter initial scores separated by commas: ")
        scores = [int(score) for score in scores_str.split(",") if score.strip().isdigit()]
        students.append({"name": name, "id": student_id, "scores": scores})
        print(f"{name} added.")
    elif choice == "3":
        student_id = int(input("Enter student ID to add scores: "))
        found = False
        for s in students:
            if s["id"] == student_id:
                scores_str = input("Enter new scores separated by commas: ")
                new_scores = [int(score) for score in scores_str.split(",") if score.strip().isdigit()]
                s["scores"].extend(new_scores)
                print(f"Scores added for {s['name']}.")
                found = True
                break
        if not found:
            print("Student not found.")
    elif choice == "4":
        student_id = int(input("Enter student ID to remove: "))
        initial_len = len(students)
        students = [s for s in students if s["id"] != student_id]
        if len(students) < initial_len:
            print("Student removed.")
        else:
            print("Student not found.")
    elif choice == "5":
        for s in students:
            avg = sum(s["scores"]) / len(s["scores"]) if s["scores"] else 0
            print(f"{s['name']} (ID: {s['id']}): Scores: {s['scores']}, Average: {avg:.2f}")
        all_scores = [score for s in students for score in s["scores"]]
        class_avg = sum(all_scores) / len(all_scores) if all_scores else 0
        print(f"\nClass average: {class_avg:.2f}")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
