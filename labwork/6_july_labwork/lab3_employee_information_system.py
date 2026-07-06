'''------- Problem Statement: Employee Information System

Create a dictionary where:
1. Employee ID is the key.
2. Value is another dictionary containing:
   - Name
   - Department
   - Salary

Perform the following operations:
1. Display all employee details.
2. Search for an employee using Employee ID.
3. Increase the salary of all employees by 10%.
4. Display employees belonging to a specific department.
-------------------------------------------------------------'''

#------- Coding ---------------

#create an empty dictionary
employees = {}

#to input details of 5 employees
for i in range(1,6):

    empid = input("Enter Employee ID :")
    name = input("Enter Employee Name :")
    department = input("Enter Department :")
    salary = float(input("Enter Salary :"))

    employees[empid] = {
        "Name":name,
        "Department":department,
        "Salary":salary
    }

print("--------------------------------------------")

print("Employee Details :")

#to display employee details
for empid in employees:

    print("Employee ID :",empid)
    print("Name :",employees[empid]["Name"])
    print("Department :",employees[empid]["Department"])
    print("Salary :",employees[empid]["Salary"])
    print("--------------------------------------------")

#search employee
searchid = input("Enter Employee ID to Search :")

if(searchid in employees):

    print("Employee Found")
    print("Name :",employees[searchid]["Name"])
    print("Department :",employees[searchid]["Department"])
    print("Salary :",employees[searchid]["Salary"])

else:
    print("Employee Not Found")

print("--------------------------------------------")

#increase salary by 10%
for empid in employees:

    employees[empid]["Salary"] = employees[empid]["Salary"] + (employees[empid]["Salary"] * 10 / 100)

print("Salary Updated Successfully")

print("--------------------------------------------")

#display employees department wise
dept = input("Enter Department :")

print("Employees in",dept,"Department")

for empid in employees:

    if(employees[empid]["Department"] == dept):

        print(employees[empid]["Name"],":",employees[empid]["Salary"])

#----------------------------------------------------
'''Output :
Enter Employee ID :101
Enter Employee Name :Rahul
Enter Department :IT
Enter Salary :50000

Enter Employee ID :102
Enter Employee Name :Amit
Enter Department :HR
Enter Salary :40000

Enter Employee ID :103
Enter Employee Name :Priya
Enter Department :IT
Enter Salary :60000

Enter Employee ID :104
Enter Employee Name :Neha
Enter Department :Sales
Enter Salary :45000

Enter Employee ID :105
Enter Employee Name :Rohan
Enter Department :HR
Enter Salary :55000
--------------------------------------------
Employee Details :
Employee ID :101
Name :Rahul
Department :IT
Salary :50000.0
--------------------------------------------
Employee ID :102
Name :Amit
Department :HR
Salary :40000.0
--------------------------------------------
Employee ID :103
Name :Priya
Department :IT
Salary :60000.0
--------------------------------------------
Employee ID :104
Name :Neha
Department :Sales
Salary :45000.0
--------------------------------------------
Employee ID :105
Name :Rohan
Department :HR
Salary :55000.0
--------------------------------------------
Enter Employee ID to Search :103
Employee Found
Name :Priya
Department :IT
Salary :60000.0
--------------------------------------------
Salary Updated Successfully
--------------------------------------------
Enter Department :HR
Employees in HR Department
Amit : 44000.0
Rohan : 60500.0
--------------------------------------------'''