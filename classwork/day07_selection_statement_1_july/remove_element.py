'''------- Problem Statement: Remove an Element from a List

Write a Python program to create a list of numbers.
Remove the first occurrence of the element 90 from the list
using the remove() method.
Display the updated list.
-------------------------------------------------------------'''

#------- Coding ---------------

#create a list
numbers = [40,90,30,40,70,90]

print("Numbers are :")
print(numbers)

print("--------------------------------------------")

#removing 90 from the list
numbers.remove(90)

print("After removing 90 from first occurrence :")
print(numbers)

#----------------------------------------------------
'''Output :
Numbers are :
[40, 90, 30, 40, 70, 90]
--------------------------------------------
After removing 90 from first occurrence :
[40, 30, 40, 70, 90]
--------------------------------------------'''