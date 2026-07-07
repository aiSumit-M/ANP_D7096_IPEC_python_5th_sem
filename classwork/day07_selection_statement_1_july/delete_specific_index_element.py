'''------- Problem Statement: Delete an Element from a Specific Index

Write a Python program to create a list of 10 numbers
by taking input from the user.
Accept an index from the user and delete the element
present at that index.
Display the updated list.
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

print("Original List :", numbers)

#index input from the user
index = int(input("Enter index to delete :"))

#validate index
if(index < 0 or index >= len(numbers)):
    print("Invalid Index")
else:
    del numbers[index]
    print("Updated List :", numbers)

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
Original List : [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Enter index to delete :4
Updated List : [10, 20, 30, 40, 60, 70, 80, 90, 100]
--------------------------------------------'''