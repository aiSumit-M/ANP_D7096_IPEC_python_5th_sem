'''------- Problem Statement: Count Eligible Voters

Write a Python program to:
Take the ages of 10 people from the user and store
them in a list. Count how many people are eligible for
voting (age 18 or above). Display the total number of
eligible people.
-------------------------------------------------------------'''

#------- Coding ---------------

#create an empty list
ages = []

#to input ages of 10 people
for person in range(1,11):

    age = int(input("Enter age of person "+str(person)+" :"))

    #store age in the list
    ages.append(age)

print("--------------------------------------------")

count = 0

#to count eligible voters
for age in ages:

    if(age >= 18):
        count = count + 1

print("Total Eligible People :", count)

#----------------------------------------------------
'''Output :
Enter age of person 1 :15
Enter age of person 2 :20
Enter age of person 3 :18
Enter age of person 4 :12
Enter age of person 5 :25
Enter age of person 6 :17
Enter age of person 7 :30
Enter age of person 8 :16
Enter age of person 9 :19
Enter age of person 10 :22
--------------------------------------------
Total Eligible People : 6
--------------------------------------------'''