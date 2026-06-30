'''------- Problem Statement: Check Adults Among 15 People

Write a Python program to input the age of 15 people.
Display the persons who are adults.
A person is considered an adult if the age is greater than or equal to 18.
-------------------------------------------------------------'''

#------- Coding ---------------

#to input age of 15 people
for person in range(1,16):

    age = int(input("Enter age of person "+str(person)+" :"))

    #validate age
    if(age <= 0):
        print("Invalid Age")
    elif(age >= 18):
        print("Person", person, "is an Adult")

#----------------------------------------------------
'''Output :
Enter age of person 1 :15
Enter age of person 2 :20
Person 2 is an Adult
Enter age of person 3 :18
Person 3 is an Adult
...
Enter age of person 15 :25
Person 15 is an Adult
--------------------------------------------'''