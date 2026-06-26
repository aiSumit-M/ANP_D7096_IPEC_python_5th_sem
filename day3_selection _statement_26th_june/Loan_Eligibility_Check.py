'''------- Problem Statement: Loan Eligibility Check

Write a Python program that accepts the applicant's monthly salary from the user.
If the salary is ₹30000 or more, the applicant is eligible for the loan.
Otherwise, the applicant is not eligible.
Display an appropriate message.
-------------------------------------------------------------'''

#------- Coding ---------------

#input of monthly salary from the user
salary = float(input("Enter monthly salary :"))

#validate the salary
if(salary <= 0):
    exit("Salary must be positive")

print("--------------------------------------------")

#to check loan eligibility
if(salary >= 30000):
    print("Congratulations! You are eligible to apply for the loan.")
else:
    print("Sorry! You are not eligible to apply for the loan.")

#----------------------------------------------------
'''Output :
Enter monthly salary :45000
--------------------------------------------
Congratulations! You are eligible to apply for the loan.
--------------------------------------------'''