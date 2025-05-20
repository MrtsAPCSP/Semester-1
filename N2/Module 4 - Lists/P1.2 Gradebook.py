students = ["Alice", "Bob", "Charlie", "Diana"]
# Each sublist holds test scores for a student
scores = [
    [88, 94, 90],
    [92, 85, 87],
    [79, 80, 75],
    [95, 100, 98]
]

for i in range(len(students)):
    total = 0
    for score in scores[i]:
        total += score
    average = total / len(scores[i])
    print(f"{students[i]}'s average score is {average:.2f}")
