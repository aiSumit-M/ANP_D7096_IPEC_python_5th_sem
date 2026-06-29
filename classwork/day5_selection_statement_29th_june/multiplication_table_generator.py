'''------- Problem Statement: Multiplication Table Generator

Write a Python program that accepts a number from the user
and displays its multiplication table up to 20.
-------------------------------------------------------------'''

#------- Coding ---------------

#input of number from the user
num = int(input("Enter Number :"))

#validate the number
if(num <= 0):
    exit("Number must be positive")

print("--------------------------------------------")

#to display multiplication table
for i in range(1,21):
    print(num, "x", i, "=", num*i)

#----------------------------------------------------
'''Output :
Enter Number :8
--------------------------------------------
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
...
8 x 20 = 160
--------------------------------------------'''