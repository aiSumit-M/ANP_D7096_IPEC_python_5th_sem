'''------- Problem Statement: Display Odd Numbers

Write a Python program to accept 10 numbers from the user
and display only the odd numbers among them.
-------------------------------------------------------------'''

#------- Coding ---------------

#create an empty list
numbers = []

#to input 10 numbers
for i in range(1,11):

    num = int(input("Enter number "+str(i)+" :"))

    #store number in the list
    numbers.append(num)

print("--------------------------------------------")

print("Odd Numbers are :")

#to display odd numbers
for num in numbers:

    if(num % 2 != 0):
        print(num)

#----------------------------------------------------
'''Output :
Enter number 1 :10
Enter number 2 :15
Enter number 3 :22
Enter number 4 :37
Enter number 5 :40
Enter number 6 :51
Enter number 7 :68
Enter number 8 :79
Enter number 9 :84
Enter number 10 :95
--------------------------------------------
Odd Numbers are :
15
37
51
79
95
--------------------------------------------'''