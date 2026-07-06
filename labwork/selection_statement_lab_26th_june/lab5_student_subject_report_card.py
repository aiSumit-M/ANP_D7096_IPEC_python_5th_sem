'''------- Problem Statement: Student Subject Report Card

Create a nested dictionary to store marks of 3 students
in three subjects.

Calculate and display:
1. Total marks of each student.
2. Average marks of each student.
3. Topper based on total marks.
4. Subject-wise highest marks along with the student's name.
5. Students whose average is greater than or equal to 85.
-------------------------------------------------------------'''

#------- Coding ---------------

#create an empty dictionary
students = {}

#to input details of 3 students
for i in range(1,4):

    name = input("Enter student name "+str(i)+" :")

    math = float(input("Enter Maths marks :"))
    science = float(input("Enter Science marks :"))
    english = float(input("Enter English marks :"))

    #store details in nested dictionary
    students[name] = {
        "Math":math,
        "Science":science,
        "English":english
    }

print("--------------------------------------------")

#variables for topper
topper = ""
highest_total = 0

print("Student Report Card")

#to calculate total and average
for name in students:

    total = students[name]["Math"] + students[name]["Science"] + students[name]["English"]

    average = total / 3

    print("--------------------------------------------")
    print("Name :",name)
    print("Total Marks :",total)
    print("Average Marks :",average)

    if(total > highest_total):
        highest_total = total
        topper = name

print("--------------------------------------------")

print("Topper :",topper)
print("Total Marks :",highest_total)

print("--------------------------------------------")

#to find highest marks in Maths
math_name = list(students.keys())[0]
math_marks = students[math_name]["Math"]

#to find highest marks in Science
science_name = list(students.keys())[0]
science_marks = students[science_name]["Science"]

#to find highest marks in English
english_name = list(students.keys())[0]
english_marks = students[english_name]["English"]

for name in students:

    if(students[name]["Math"] > math_marks):
        math_marks = students[name]["Math"]
        math_name = name

    if(students[name]["Science"] > science_marks):
        science_marks = students[name]["Science"]
        science_name = name

    if(students[name]["English"] > english_marks):
        english_marks = students[name]["English"]
        english_name = name

print("Highest Marks in Maths :",math_name,"-",math_marks)
print("Highest Marks in Science :",science_name,"-",science_marks)
print("Highest Marks in English :",english_name,"-",english_marks)

print("--------------------------------------------")

print("Students having average greater than or equal to 85 :")

for name in students:

    total = students[name]["Math"] + students[name]["Science"] + students[name]["English"]

    average = total / 3

    if(average >= 85):
        print(name,"-",average)

#----------------------------------------------------
'''Output :
Enter student name 1 :Rahul
Enter Maths marks :85
Enter Science marks :90
Enter English marks :88

Enter student name 2 :Priya
Enter Maths marks :78
Enter Science marks :95
Enter English marks :82

Enter student name 3 :Ankit
Enter Maths marks :91
Enter Science marks :89
Enter English marks :94
--------------------------------------------
Student Report Card
--------------------------------------------
Name : Rahul
Total Marks : 263.0
Average Marks : 87.66666666666667
--------------------------------------------
Name : Priya
Total Marks : 255.0
Average Marks : 85.0
--------------------------------------------
Name : Ankit
Total Marks : 274.0
Average Marks : 91.33333333333333
--------------------------------------------
Topper : Ankit
Total Marks : 274.0
--------------------------------------------
Highest Marks in Maths : Ankit - 91.0
Highest Marks in Science : Priya - 95.0
Highest Marks in English : Ankit - 94.0
--------------------------------------------
Students having average greater than or equal to 85 :
Rahul - 87.66666666666667
Priya - 85.0
Ankit - 91.33333333333333
--------------------------------------------'''