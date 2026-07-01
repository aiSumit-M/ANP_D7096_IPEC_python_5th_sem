'''------- Problem Statement: Admission Eligibility

Write a Python program to create the record of 50 students
by accepting their name and marks.
Display the names of the students who are eligible for admission.
A student is eligible if the marks are greater than 75.
-------------------------------------------------------------'''

#------- Coding ---------------

#to input records of 50 students
for student in range(1,51):

    name = input("Enter name of student "+str(student)+" :")
    marks = float(input("Enter marks :"))

    #validate marks
    if(marks < 0 or marks > 100):
        print("Invalid Marks")
    elif(marks > 75):
        print(name, "is eligible for admission")

#----------------------------------------------------
'''Output :
Enter name of student 1 :Rahul
Enter marks :82
Rahul is eligible for admission

Enter name of student 2 :Amit
Enter marks :65

Enter name of student 3 :Priya
Enter marks :91
Priya is eligible for admission
...
--------------------------------------------'''