'''------- Problem Statement: Bank Transaction Summary

Write a Python program that accepts transaction amounts from the user.
Positive numbers indicate deposits and negative numbers indicate withdrawals.
The user enters 0 to finish.
Display:
1. Total Deposit
2. Total Withdrawal
3. Final Balance
-------------------------------------------------------------'''

#------- Coding ---------------

total_deposit = 0
total_withdrawal = 0
balance = 0

while(True):

    amount = float(input("Enter Transaction Amount (0 to stop) :"))

    if(amount == 0):
        break

    if(amount > 0):
        total_deposit = total_deposit + amount
    else:
        total_withdrawal = total_withdrawal + abs(amount)

    balance = balance + amount

print("--------------------------------------------")

print("Total Deposit :", total_deposit)
print("Total Withdrawal :", total_withdrawal)
print("Final Balance :", balance)

#----------------------------------------------------
'''Output :
Enter Transaction Amount (0 to stop) :5000
Enter Transaction Amount (0 to stop) :-1000
Enter Transaction Amount (0 to stop) :2500
Enter Transaction Amount (0 to stop) :0
--------------------------------------------
Total Deposit : 7500.0
Total Withdrawal : 1000.0
Final Balance : 6500.0
--------------------------------------------'''