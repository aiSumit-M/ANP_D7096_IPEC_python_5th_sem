'''------- Problem Statement: Count Prime Numbers in a Range

Write a Python program that accepts the starting and ending
values of a range and displays all prime numbers.
Finally display the total number of prime numbers found.
-------------------------------------------------------------'''

#------- Coding ---------------

#input of starting value
start = int(input("Enter starting value :"))

#input of ending value
end = int(input("Enter ending value :"))

print("--------------------------------------------")

count = 0

#to display prime numbers
for num in range(start,end+1):

    if(num > 1):

        prime = True

        for i in range(2,num):
            if(num % i == 0):
                prime = False
                break

        if(prime):
            print(num)
            count = count + 1

print("--------------------------------------------")
print("Total Prime Numbers :",count)

#----------------------------------------------------
'''Output :
Enter starting value :10
Enter ending value :25
--------------------------------------------
11
13
17
19
23
--------------------------------------------
Total Prime Numbers : 5
--------------------------------------------'''