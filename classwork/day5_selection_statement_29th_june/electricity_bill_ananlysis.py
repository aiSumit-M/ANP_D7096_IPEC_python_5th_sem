'''------- Problem Statement: Electricity Bill Analysis

Write a Python program that accepts monthly electricity
units consumed by N houses.
Display:
1. Total Units
2. Average Units
3. Highest Consumption
4. Lowest Consumption
-------------------------------------------------------------'''

#------- Coding ---------------

#input number of houses
n = int(input("Enter number of houses :"))

total = 0

for i in range(1,n+1):

    units = float(input("Enter units consumed by house "+str(i)+" :"))

    total = total + units

    if(i == 1):
        highest = units
        lowest = units
    else:

        if(units > highest):
            highest = units

        if(units < lowest):
            lowest = units

print("--------------------------------------------")

average = total / n

print("Total Units Consumed :",total)
print("Average Units Consumed :",average)
print("Highest Consumption :",highest)
print("Lowest Consumption :",lowest)

#----------------------------------------------------
'''Output :
Enter number of houses :3
Enter units consumed by house 1 :250
Enter units consumed by house 2 :300
Enter units consumed by house 3 :200
--------------------------------------------
Total Units Consumed :750.0
Average Units Consumed :250.0
Highest Consumption :300.0
Lowest Consumption :200.0
--------------------------------------------'''