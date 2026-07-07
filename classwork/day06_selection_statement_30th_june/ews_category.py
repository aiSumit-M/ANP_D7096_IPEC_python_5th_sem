'''------- Problem Statement: EWS Category Eligibility

Write a Python program to create the record of 15 persons
by accepting their name and salary.
Display the names of the persons who are eligible for the
EWS category.
A person is eligible if the salary is less than or equal
to ₹5,00,000.
-------------------------------------------------------------'''

#------- Coding ---------------

#to input records of 15 persons
for person in range(1,16):

    name = input("Enter name of person "+str(person)+" :")
    salary = float(input("Enter salary :"))

    #validate salary
    if(salary <= 0):
        print("Invalid Salary")
    elif(salary <= 500000):
        print(name, "is eligible for EWS category")

#----------------------------------------------------
'''Output :
Enter name of person 1 :Rahul
Enter salary :450000
Rahul is eligible for EWS category

Enter name of person 2 :Amit
Enter salary :650000

Enter name of person 3 :Priya
Enter salary :300000
Priya is eligible for EWS category
...
--------------------------------------------'''