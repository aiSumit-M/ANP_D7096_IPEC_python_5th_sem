'''------- Problem Statement: Sum of 10 Numbers

Write a Python program to accept 10 numbers from the user
and calculate their sum.
Display the total sum.
-------------------------------------------------------------'''

#------- Coding ---------------

sum = 0

#to input 10 numbers
for number in range(1,11):

    num = float(input("Enter number "+str(number)+" :"))

    sum = sum + num

print("--------------------------------------------")

print("Sum of 10 Numbers :", sum)

#----------------------------------------------------
'''Output :
Enter number 1 :10
Enter number 2 :20
Enter number 3 :30
Enter number 4 :40
Enter number 5 :50
Enter number 6 :60
Enter number 7 :70
Enter number 8 :80
Enter number 9 :90
Enter number 10 :100
--------------------------------------------
Sum of 10 Numbers : 550.0
--------------------------------------------'''