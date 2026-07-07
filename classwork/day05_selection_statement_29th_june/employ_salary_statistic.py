'''------- Problem Statement: Employee Salary Statistics

Write a Python program that accepts the salary of N employees.
Display:
1. Highest Salary
2. Lowest Salary
3. Average Salary
4. Number of employees earning more than ₹50,000
-------------------------------------------------------------'''

#------- Coding ---------------

n = int(input("Enter number of employees :"))

total = 0
count = 0

for i in range(1, n+1):

    salary = float(input("Enter salary of employee "+str(i)+" :"))

    total = total + salary

    if(i == 1):
        highest = salary
        lowest = salary
    else:
        if(salary > highest):
            highest = salary

        if(salary < lowest):
            lowest = salary

    if(salary > 50000):
        count = count + 1

print("--------------------------------------------")

average = total / n

print("Highest Salary :", highest)
print("Lowest Salary :", lowest)
print("Average Salary :", average)
print("Employees earning more than ₹50000 :", count)

#----------------------------------------------------
'''Output :
Enter number of employees :3
Enter salary of employee 1 :45000
Enter salary of employee 2 :60000
Enter salary of employee 3 :80000
--------------------------------------------
Highest Salary : 80000.0
Lowest Salary : 45000.0
Average Salary : 61666.67
Employees earning more than ₹50000 : 2
--------------------------------------------'''