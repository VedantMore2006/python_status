student_heights = input("Input a list of student heights : ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)
total_height = 0
no_of_students = 0

for height in student_heights:
    total_height += height
    no_of_students += 1

print("Average height is :: ", round(total_height / no_of_students))
student_heights = input("Input a list of student heights : ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)
total_height = 0
no_of_students = 0

for height in student_heights:
    total_height += height
    no_of_students += 1

print("Average height is :: ", round(total_height / no_of_students))

