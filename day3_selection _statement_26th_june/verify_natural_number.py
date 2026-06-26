'''------- Problem Statement: Check Whether a Number is a Natural Number

Write a Python program that accepts a number from the user
and checks whether it is a natural number or not.
A natural number is a positive integer (1, 2, 3, ...).
Display an appropriate message based on the result.
-------------------------------------------------------------'''

#------- Coding ---------------

#input of number from the user
num = int(input("Enter a number :"))

#--------------------------------------------------------------

print("--------------------------------------------")

#to check whether the number is natural or not
if(num > 0):
    print("The given number is a Natural Number")
else:
    print("The given number is not a Natural Number")

#----------------------------------------------------
'''Output :
Enter a number :25
--------------------------------------------
The given number is a Natural Number
--------------------------------------------'''