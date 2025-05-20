top_student = None
top_average = 0

for student, scores in gradebook.items():
    average = sum(scores) / len(scores)
    if average > top_average:
        top_average = average
        top_student = student

print(f"Top student is {top_student} with an average of {top_average:.2f}")
