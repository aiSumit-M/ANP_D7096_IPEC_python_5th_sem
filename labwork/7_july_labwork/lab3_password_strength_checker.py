'''------- Problem Statement: Password Strength Checker

Write a Python program that defines a function
check_password(password).

A password is considered Strong if:
• It contains at least 8 characters.
• It contains at least one uppercase letter.
• It contains at least one lowercase letter.
• It contains at least one digit.

The function should return:
• "Strong Password"
or
• "Weak Password"

The main program should accept a password from the user
and display the result.
-------------------------------------------------------------'''

#------- Coding ---------------

#function to check password strength
def check_password(password):

    uppercase = 0
    lowercase = 0
    digit = 0

    #to check each character
    for ch in password:

        if(ch >= 'A' and ch <= 'Z'):
            uppercase = uppercase + 1

        elif(ch >= 'a' and ch <= 'z'):
            lowercase = lowercase + 1

        elif(ch >= '0' and ch <= '9'):
            digit = digit + 1

    #to verify password strength
    if(len(password) >= 8 and uppercase >= 1 and lowercase >= 1 and digit >= 1):
        return "Strong Password"

    else:
        return "Weak Password"

#input password from the user
password = input("Enter Password :")

#calling function
result = check_password(password)

print("--------------------------------------------")

print(result)

#----------------------------------------------------
'''Output :
Enter Password : Sumit123
--------------------------------------------
Strong Password
--------------------------------------------

Output :
Enter Password : python
--------------------------------------------
Weak Password
--------------------------------------------'''