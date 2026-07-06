'''------- Problem Statement: Student Marks Management

Create a dictionary to store the marks of 5 students,
where the key is the student's name and the value is
their marks.

Perform the following operations:
1. Display all student names and marks.
2. Add a new student with marks.
3. Update the marks of an existing student.
4. Delete a student by name.
5. Display the student who scored the highest marks.
-------------------------------------------------------------'''

#------- Coding ---------------

#create an empty dictionary
students = {}

#to input details of 5 students
for i in range(1,6):

    name = input("Enter name of student "+str(i)+" :")
    marks = float(input("Enter marks :"))

    #store record in dictionary
    students[name] = marks

print("--------------------------------------------")

print("Student Records :")

#to display all student records
for name in students:
    print(name, ":", students[name])

print("--------------------------------------------")

#to add a new student
name = input("Enter new student name :")
marks = float(input("Enter marks :"))

students[name] = marks

print("Student Added Successfully")

print("--------------------------------------------")

#to update marks of an existing student
name = input("Enter student name to update :")

if(name in students):

    marks = float(input("Enter new marks :"))
    students[name] = marks
    print("Marks Updated Successfully")

else:
    print("Student Not Found")

print("--------------------------------------------")

#to delete a student
name = input("Enter student name to delete :")

if(name in students):

    del students[name]
    print("Student Deleted Successfully")

else:
    print("Student Not Found")

print("--------------------------------------------")

#to find highest marks
highest_name = list(students.keys())[0]
highest_marks = students[highest_name]

for name in students:

    if(students[name] > highest_marks):

        highest_marks = students[name]
        highest_name = name

print("Highest Scorer :", highest_name)
print("Marks :", highest_marks)

#----------------------------------------------------
'''Output :
Enter name of student 1 :Rahul
Enter marks :85
Enter name of student 2 :Amit
Enter marks :76
Enter name of student 3 :Priya
Enter marks :92
Enter name of student 4 :Neha
Enter marks :88
Enter name of student 5 :Rohan
Enter marks :81
--------------------------------------------
Student Records :
Rahul : 85.0
Amit : 76.0
Priya : 92.0
Neha : 88.0
Rohan : 81.0
--------------------------------------------
Enter new student name :Ankit
Enter marks :95
Student Added Successfully
--------------------------------------------
Enter student name to update :Amit
Enter new marks :82
Marks Updated Successfully
--------------------------------------------
Enter student name to delete :Rahul
Student Deleted Successfully
--------------------------------------------
Highest Scorer : Ankit
Marks : 95.0
--------------------------------------------'''