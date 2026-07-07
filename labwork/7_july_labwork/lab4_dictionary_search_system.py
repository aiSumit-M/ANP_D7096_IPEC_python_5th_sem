'''------- Problem Statement: Dictionary Search System

Write a Python program that defines a function
search_student(student_dict, roll_no).

The function should:
• Accept a dictionary where:
    Key = Roll Number
    Value = Student Name
• Search for the given roll number.
• Return the student name if found,
  otherwise return "Student Not Found".

The main program should:
• Create a dictionary of at least 5 students.
• Accept a roll number from the user.
• Display the search result.
-------------------------------------------------------------'''

#------- Coding ---------------

#function to search student
def search_student(student_dict, roll_no):

    if(roll_no in student_dict):
        return student_dict[roll_no]

    else:
        return "Student Not Found"


#create an empty dictionary
students = {}

#to input details of 5 students
for i in range(1,6):

    roll_no = int(input("Enter Roll Number :"))
    name = input("Enter Student Name :")

    #store details in dictionary
    students[roll_no] = name

print("--------------------------------------------")

#input roll number to search
roll_no = int(input("Enter Roll Number to Search :"))

#calling function
result = search_student(students, roll_no)

print("--------------------------------------------")

print("Search Result :", result)

#----------------------------------------------------
'''Output :
Enter Roll Number :101
Enter Student Name :Rahul
Enter Roll Number :102
Enter Student Name :Priya
Enter Roll Number :103
Enter Student Name :Amit
Enter Roll Number :104
Enter Student Name :Neha
Enter Roll Number :105
Enter Student Name :Rohan
--------------------------------------------
Enter Roll Number to Search :103
--------------------------------------------
Search Result : Amit
--------------------------------------------

Output :
Enter Roll Number :101
Enter Student Name :Rahul
Enter Roll Number :102
Enter Student Name :Priya
Enter Roll Number :103
Enter Student Name :Amit
Enter Roll Number :104
Enter Student Name :Neha
Enter Roll Number :105
Enter Student Name :Rohan
--------------------------------------------
Enter Roll Number to Search :110
--------------------------------------------
Search Result : Student Not Found
--------------------------------------------'''