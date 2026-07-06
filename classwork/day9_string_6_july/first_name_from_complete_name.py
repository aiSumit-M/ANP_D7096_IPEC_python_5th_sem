'''------- Problem Statement: Display First Name

Write a Python program to accept the complete name
of a person from the user and display only the first
name without using any library method.
-------------------------------------------------------------'''

#------- Coding ---------------

#input complete name from the user
name = input("Enter your complete name :")

firstname = ""

#to extract first name
for ch in name:

    if(ch == ' '):
        break

    firstname = firstname + ch

print("--------------------------------------------")

print("First Name :", firstname)

#----------------------------------------------------
'''Output :
Enter your complete name : Sumit Mandal
--------------------------------------------
First Name : Sumit
--------------------------------------------'''