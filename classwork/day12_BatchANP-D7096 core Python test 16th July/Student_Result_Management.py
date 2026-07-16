# Student_Result_Management.py

# ------Coding------

students = {}

print("Enter Marks of 10 Students")

for i in range(10):
    roll = input("Enter Roll No: ")
    marks = int(input("Enter Marks: "))
    students[roll] = marks

topper = max(students, key=students.get)
average = sum(students.values()) / len(students)

print("\nTopper Roll No =", topper)
print("Topper Marks =", students[topper])

print("Average Marks =", average)

print("\nStudents Scoring Above Average:")
for roll, marks in students.items():
    if marks > average:
        print(roll, ":", marks)

failed = 0

print("\nGrades:")

for roll, marks in students.items():

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 35:
        grade = "D"
    else:
        grade = "Fail"
        failed += 1

    print("Roll No:", roll, "Marks:", marks, "Grade:", grade)

print("\nFailed Students =", failed)

# ------Output------

# Sample Output:
# Enter Marks of 10 Students
# Enter Roll No: 101
# Enter Marks: 95
# ...
#
# Topper Roll No = 101
# Topper Marks = 95
# Average Marks = 69.5
#
# Students Scoring Above Average:
# 101 : 95
# 104 : 82
#
# Grades:
# Roll No: 101 Marks: 95 Grade: A
# Roll No: 102 Marks: 72 Grade: C
# ...
#
# Failed Students = 2