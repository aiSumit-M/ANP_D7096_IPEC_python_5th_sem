'''------- Problem Statement: Remove All Occurrences of a Number

Write a Python program to create a list of 20 numbers
given by the user.

Then ask the user to input any other number.
If the number is present in the list, remove all its
occurrences from the list.
If the number is not present, display a message that
the number is not present in the list.
-------------------------------------------------------------'''

#------- Coding ---------------

#create an empty list
numbers = []

#to input 20 numbers
for i in range(1,21):

    num = int(input("Enter number "+str(i)+" :"))
    numbers.append(num)

print("--------------------------------------------")

print("Original List :", numbers)

#input number to search and remove
target = int(input("Enter number to remove :"))

#check if number exists in list
if target in numbers:

    #remove all occurrences
    while target in numbers:
        numbers.remove(target)

    print("All occurrences removed")
    print("Updated List :", numbers)

else:
    print("Number is not present in the list")

#----------------------------------------------------
'''Output :
Enter number 1 :10
Enter number 2 :20
Enter number 3 :30
...
Enter number 20 :10
--------------------------------------------
Original List : [10, 20, 30, 10, 40, 10]
Enter number to remove :10
All occurrences removed
Updated List : [20, 30, 40]
--------------------------------------------'''