'''------- Problem Statement: List Analysis using Functions

Write a Python program that defines the following functions:

1. find_max(numbers)
2. find_min(numbers)
3. find_average(numbers)

The program should:
• Accept a list of 10 integers from the user.
• Call all three functions.
• Display the maximum value, minimum value,
  and average of the list.
-------------------------------------------------------------'''

#------- Coding ---------------

#function to find maximum number
def find_max(numbers):

    maximum = numbers[0]

    for num in numbers:

        if(num > maximum):
            maximum = num

    return maximum


#function to find minimum number
def find_min(numbers):

    minimum = numbers[0]

    for num in numbers:

        if(num < minimum):
            minimum = num

    return minimum


#function to find average
def find_average(numbers):

    total = 0

    for num in numbers:
        total = total + num

    average = total / len(numbers)

    return average


#create an empty list
numbers = []

#to input 10 numbers
for i in range(1,11):

    num = int(input("Enter number "+str(i)+" :"))
    numbers.append(num)

#calling functions
maximum = find_max(numbers)
minimum = find_min(numbers)
average = find_average(numbers)

print("--------------------------------------------")

print("List :", numbers)
print("Maximum Value :", maximum)
print("Minimum Value :", minimum)
print("Average :", average)

#----------------------------------------------------
'''Output :
Enter number 1 :45
Enter number 2 :12
Enter number 3 :89
Enter number 4 :67
Enter number 5 :23
Enter number 6 :98
Enter number 7 :54
Enter number 8 :31
Enter number 9 :76
Enter number 10 :40
--------------------------------------------
List : [45, 12, 89, 67, 23, 98, 54, 31, 76, 40]
Maximum Value : 98
Minimum Value : 12
Average : 53.5
--------------------------------------------'''