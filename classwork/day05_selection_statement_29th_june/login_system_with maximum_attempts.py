'''------- Problem Statement: Login System with Maximum Attempts

Write a Python program that allows only three login attempts.
The correct username is admin and the password is python123.
If the credentials are correct, display "Login Successful".
Otherwise, after three unsuccessful attempts,
display "Account Locked".
-------------------------------------------------------------'''

#------- Coding ---------------

correct_username = "admin"
correct_password = "python123"

for attempt in range(1,4):

    print("Attempt", attempt)

    username = input("Enter Username :")
    password = input("Enter Password :")

    if(username == correct_username and password == correct_password):
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")

else:
    print("Account Locked")

#----------------------------------------------------
'''Output :
Attempt 1
Enter Username :admin
Enter Password :abc
Invalid Credentials

Attempt 2
Enter Username :admin
Enter Password :python123
Login Successful
--------------------------------------------'''