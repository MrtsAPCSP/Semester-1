# Dictionary of students with lists of scores as values
gradebook = {
    "Alice": [88, 94, 90],
    "Bob": [92, 85, 87],
    "Charlie": [79, 80, 75],
    "Diana": [95, 100, 98]
}

for student, scores in gradebook.items():
    average = sum(scores) / len(scores)
    print(f"{student}'s average score is {average:.2f}")
