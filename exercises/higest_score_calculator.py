student_score = input("List of student_score : ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

higest_score = 0
for score in student_score:
    if score > higest_score:
        higest_score = score
print(higest_score)
