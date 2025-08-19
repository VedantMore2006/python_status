student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grade = {}
for key in student_scores:
    if student_scores[key] > 90:
        student_grade[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grade[key] = "Exceeded Expections"
    elif student_scores[key] > 70:
        student_grade[key] = "Acceptable"
    else:
        student_grade[key] = "Failed"
print(student_grade)
