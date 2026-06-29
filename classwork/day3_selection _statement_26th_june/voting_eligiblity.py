'''------- Problem Statement: Check Whether a Person is Eligible for Voting

Write a Python program that accepts the age of a person from the user
and checks whether the person is eligible for voting.
A person is eligible if the age is 18 years or above.
Display an appropriate message based on the result.
-------------------------------------------------------------'''

#------- Coding ---------------

#input of age from the user
age = int(input("Enter your age :"))

#validate the age
if(age <= 0):
    exit("Age must be positive")

print("--------------------------------------------")

#to check voting eligibility
if(age >= 18):
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

#----------------------------------------------------
'''Output :
Enter your age :20
--------------------------------------------
You are eligible for voting
--------------------------------------------'''