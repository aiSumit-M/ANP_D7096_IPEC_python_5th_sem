'''
Problem Statement:
Write a Python program to create a list of numbers given by the user.
Then ask the user to enter an element. The program should find the
frequency of that element in the list. If the element is not present,
display "not found". If it is present only once, display "no duplicate found".
If it appears more than once, display its frequency and show the list
after reversing it twice (to demonstrate reverse operation).
'''
------------------------------------------------------------

#--------coding---------

# input: creating empty list
numbers = []

# input: taking size of list
n = int(input("Enter number of elements: "))

# input: taking list elements
print("Enter elements:")
for i in range(n):
    num = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(num)

# input: element to find frequency
element = int(input("\nEnter element to find frequency: "))

# logic: finding frequency
freq = numbers.count(element)

# logic: checking conditions
if freq == 0:
    print(element, "not found")

elif freq == 1:
    print("No duplicate found")

else:
    print("Frequency of", element, "is:", freq)

    # logic: reverse list first time
    numbers.reverse()
    print("List after first reverse:", numbers)

    # logic: reverse list second time (back to original)
    numbers.reverse()
    print("List after second reverse:", numbers)