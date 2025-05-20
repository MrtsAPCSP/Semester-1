# List of student dictionaries
students = [
    {
        "name": "Alice",
        "id": 101,
        "scores": [88, 92, 85]
    },
    {
        "name": "Bob",
        "id": 102,
        "scores": [75, 78, 82]
    },
    {
        "name": "Charlie",
        "id": 103,
        "scores": [90, 85, 87]
    }
]

# Print each student's name and average score
for student in students:
    avg_score = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']} (ID: {student['id']}) has an average score of {avg_score:.2f}")

# Calculate class average across all tests and students
all_scores = []
for student in students:
    all_scores.extend(student["scores"])

class_avg = sum(all_scores) / len(all_scores)
print(f"\nClass average score is {class_avg:.2f}")
