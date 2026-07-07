'''------- Problem Statement: Electricity Bill Discount

Write a Python program that accepts the total electricity bill amount from the user.
If the bill amount is ₹5000 or more, apply a 10% discount.
Otherwise, no discount is applied.
Display the final bill amount.
-------------------------------------------------------------'''

#------- Coding ---------------

#input of electricity bill amount from the user
bill = float(input("Enter electricity bill amount :"))

#validate the bill amount
if(bill <= 0):
    exit("Bill amount must be positive")

print("--------------------------------------------")

#to calculate final bill amount
if(bill >= 5000):
    discount = bill * 0.10
    final_bill = bill - discount
    print("Discount Applied!")
    print("Final Bill Amount : ₹", final_bill)
else:
    print("No Discount Applied!")
    print("Final Bill Amount : ₹", bill)

#----------------------------------------------------
'''Output :
Enter electricity bill amount :6200
--------------------------------------------
Discount Applied!
Final Bill Amount : ₹ 5580.0
--------------------------------------------'''