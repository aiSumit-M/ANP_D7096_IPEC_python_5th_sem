'''------- Problem Statement: Update an Element in a List

Write a Python program to create a list of numbers.
Update the element at a specific index in the list.
Display the updated list.
-------------------------------------------------------------'''

#------- Coding ---------------

#create a list
numbers = [40,70,20,30]

print("Numbers are :")
print(numbers)

print("--------------------------------------------")

#updating element at index 2
numbers[2] = 90

print("After updating element :")
print(numbers)

#----------------------------------------------------
'''Output :
Numbers are :
[40, 70, 20, 30]
--------------------------------------------
After updating element :
[40, 70, 90, 30]
--------------------------------------------'''