'''------- Problem Statement: Parking Fee Waiver

Write a Python program that accepts the purchase amount from the user.
If the purchase amount is ₹2000 or more, parking fee is waived.
Otherwise, parking fee is ₹100.
Display the parking fee.
-------------------------------------------------------------'''

#------- Coding ---------------

#input of purchase amount from the user
purchase = float(input("Enter purchase amount :"))

#validate the purchase amount
if(purchase <= 0):
    exit("Purchase amount must be positive")

print("--------------------------------------------")

#to check parking fee
if(purchase >= 2000):
    parking_fee = 0
    print("Parking Fee Waived!")
    print("Parking Fee : ₹", parking_fee)
else:
    parking_fee = 100
    print("Parking Fee Applicable!")
    print("Parking Fee : ₹", parking_fee)

#----------------------------------------------------
'''Output :
Enter purchase amount :2500
--------------------------------------------
Parking Fee Waived!
Parking Fee : ₹ 0
--------------------------------------------'''