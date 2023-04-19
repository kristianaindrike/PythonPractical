# 10.Write a Python program that reads a CSV file containing student grades and writes a new CSV file with the 
# grades sorted by student name.

with open("Student.csv","r") as f:
    students_grades = f.readlines()

lines = list()
for student in students_grades:
    lines.append(student)

student_grades = lines[1:]
student_grades.sort(key=lambda student:student[0])


csv_output = students_grades[0]
for student in lines:
    csv_output += student

with open("Student_sort.csv","w") as f:
    f.write(csv_output)