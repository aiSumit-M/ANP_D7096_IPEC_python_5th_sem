'''------- Problem Statement: Smart Income Tax Calculator

Write a Python program that accepts annual income, age and gender
from the user and calculates the final tax payable.

Tax Rules:
Income up to ₹5,00,000        -> No Tax
₹5,00,001 to ₹10,00,000       -> 10%
₹10,00,001 to ₹20,00,000      -> 20%
Above ₹20,00,000              -> 30%

Additional Benefits:
Senior Citizens (Age >= 60) receive a 5% rebate on tax.
Women taxpayers receive an additional 2% rebate on tax.
-------------------------------------------------------------'''

#------- Coding ---------------

#input of annual income from the user
income = float(input("Enter Annual Income :"))

#validate the income
if(income <= 0):
    exit("Income must be positive")

#--------------------------------------------------------------

#input of age from the user
age = int(input("Enter Age :"))

#validate the age
if(age <= 0):
    exit("Age must be positive")

#--------------------------------------------------------------

#input of gender from the user
gender = input("Enter Gender (M/F) :")

print("--------------------------------------------")

#to calculate tax before rebate
if(income <= 500000):
    tax = 0
elif(income <= 1000000):
    tax = income * 0.10
elif(income <= 2000000):
    tax = income * 0.20
else:
    tax = income * 0.30

print("Tax before rebate : ₹", tax)

#--------------------------------------------------------------

#senior citizen rebate
if(age >= 60):
    senior_rebate = tax * 0.05
else:
    senior_rebate = 0

print("Senior Citizen Rebate : ₹", senior_rebate)

#--------------------------------------------------------------

#women rebate
if(gender == 'F' or gender == 'f'):
    women_rebate = tax * 0.02
else:
    women_rebate = 0

print("Women Rebate : ₹", women_rebate)

#--------------------------------------------------------------

#final tax payable
final_tax = tax - senior_rebate - women_rebate

print("Final Tax Payable : ₹", final_tax)

#----------------------------------------------------
'''Output :
Enter Annual Income :1200000
Enter Age :65
Enter Gender (M/F) :F
--------------------------------------------
Tax before rebate : ₹ 240000.0
Senior Citizen Rebate : ₹ 12000.0
Women Rebate : ₹ 4800.0
Final Tax Payable : ₹ 223200.0
--------------------------------------------'''