'''------- Problem Statement: Student Result Analyzer

Write a Python program that accepts the marks of N students
(out of 100) and displays:

1. Highest Marks
2. Lowest Marks
3. Average Marks
4. Number of students who passed (Marks >= 40)
5. Number of students who scored distinction (Marks >= 75)
-------------------------------------------------------------'''

#------- Coding ---------------

#input number of students
n = int(input("Enter number of students :"))

total = 0
pass_count = 0
distinction = 0

for i in range(1,n+1):

    marks = float(input("Enter marks of student "+str(i)+" :"))

    total = total + marks

    if(i == 1):
        highest = marks
        lowest = marks
    else:

        if(marks > highest):
            highest = marks

        if(marks < lowest):
            lowest = marks

    if(marks >= 40):
        pass_count = pass_count + 1

    if(marks >= 75):
        distinction = distinction + 1

print("--------------------------------------------")

average = total / n

print("Highest Marks :", highest)
print("Lowest Marks :", lowest)
print("Average Marks :", average)
print("Number of Students Passed :", pass_count)
print("Number of Students with Distinction :", distinction)

#----------------------------------------------------
'''Output :
Enter number of students :5
Enter marks of student 1 :65
Enter marks of student 2 :82
Enter marks of student 3 :35
Enter marks of student 4 :91
Enter marks of student 5 :48
--------------------------------------------
Highest Marks : 91.0
Lowest Marks : 35.0
Average Marks : 64.2
Number of Students Passed : 4
Number of Students with Distinction : 2
--------------------------------------------'''