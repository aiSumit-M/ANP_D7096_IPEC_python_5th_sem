'''------- Problem Statement: Password Strength Checker

Write a Python program that accepts a password from the user.
The password must contain at least 8 characters.
Keep asking until a valid password is entered.
-------------------------------------------------------------'''

#------- Coding ---------------

while(True):

    password = input("Enter Password :")

    if(len(password) >= 8):
        print("Password Accepted.")
        break
    else:
        print("Password too short.")

#----------------------------------------------------
'''Output :
Enter Password :hello
Password too short.
Enter Password :python@123
Password Accepted.
--------------------------------------------'''