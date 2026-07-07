'''------- Problem Statement: Calculate Simple Interest Using Functions

Write a Python program to calculate the Simple Interest
by using a function.
Accept Principal Amount, Rate of Interest and Time
from the user and display the Simple Interest.
-------------------------------------------------------------'''

#------- Coding ---------------

#function to calculate simple interest
def calculateSI(principal, rate, time):

    si = (principal * rate * time) / 100

    return si

#input from the user
principal = float(input("Enter Principal Amount :"))
rate = float(input("Enter Rate of Interest :"))
time = float(input("Enter Time (in years) :"))

#calling the function
interest = calculateSI(principal, rate, time)

print("--------------------------------------------")

print("Simple Interest :", interest)

#----------------------------------------------------
'''Output :
Enter Principal Amount :50000
Enter Rate of Interest :8
Enter Time (in years) :2
--------------------------------------------
Simple Interest : 8000.0
--------------------------------------------'''