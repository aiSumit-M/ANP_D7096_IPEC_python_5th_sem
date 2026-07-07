'''------- Problem Statement: Student Grade Calculator

Write a Python program that defines a function
calculate_grade(marks).

The function should:
• Accept marks (0–100) as a parameter.
• Return the grade according to the following criteria:

90 and above  -> A+
75–89         -> A
60–74         -> B
40–59         -> C
Below 40      -> Fail

The main program should:
• Accept marks of 5 students.
• Call the function for each student.
• Display the marks and corresponding grade.
-------------------------------------------------------------'''

#------- Coding ---------------

#function to calculate grade
def calculate_grade(marks):

    if(marks >= 90):
        return "A+"

    elif(marks >= 75):
        return "A"

    elif(marks >= 60):
        return "B"

    elif(marks >= 40):
        return "C"

    else:
        return "Fail"

#to input marks of 5 students
for student in range(1,6):

    marks = float(input("Enter marks of student "+str(student)+" :"))

    #calling function
    grade = calculate_grade(marks)

    print("Marks :", marks)
    print("Grade :", grade)
    print("--------------------------------------------")

#----------------------------------------------------
'''Output :
Enter marks of student 1 :95
Marks : 95.0
Grade : A+
--------------------------------------------
Enter marks of student 2 :82
Marks : 82.0
Grade : A
--------------------------------------------
Enter marks of student 3 :68
Marks : 68.0
Grade : B
--------------------------------------------
Enter marks of student 4 :50
Marks : 50.0
Grade : C
--------------------------------------------
Enter marks of student 5 :35
Marks : 35.0
Grade : Fail
--------------------------------------------'''