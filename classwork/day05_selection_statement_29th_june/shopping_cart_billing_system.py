'''------- Problem Statement: Shopping Cart Billing System

Write a Python program that accepts the number of products.
For each product enter:

1. Product Name
2. Quantity
3. Price per Unit

Finally display:
1. Individual Product Cost
2. Total Bill Amount
3. Most Expensive Product
4. Cheapest Product
5. Average Product Cost
-------------------------------------------------------------'''

#------- Coding ---------------

#input number of products
n = int(input("Enter number of products :"))

total_bill = 0

for i in range(1,n+1):

    print("--------------------------------------------")

    name = input("Enter Product Name :")
    quantity = int(input("Enter Quantity :"))
    price = float(input("Enter Price per Unit :"))

    cost = quantity * price

    print("Product Cost :", cost)

    total_bill = total_bill + cost

    if(i == 1):
        highest_cost = cost
        lowest_cost = cost
        expensive_product = name
        cheapest_product = name
    else:

        if(cost > highest_cost):
            highest_cost = cost
            expensive_product = name

        if(cost < lowest_cost):
            lowest_cost = cost
            cheapest_product = name

print("--------------------------------------------")

average = total_bill / n

print("Total Bill Amount :", total_bill)
print("Most Expensive Product :", expensive_product)
print("Cheapest Product :", cheapest_product)
print("Average Product Cost :", average)

#----------------------------------------------------
'''Output :
Enter number of products :3

--------------------------------------------
Enter Product Name :Pen
Enter Quantity :10
Enter Price per Unit :15
Product Cost :150.0

--------------------------------------------
Enter Product Name :Book
Enter Quantity :5
Enter Price per Unit :120
Product Cost :600.0

--------------------------------------------
Enter Product Name :Bag
Enter Quantity :1
Enter Price per Unit :800
Product Cost :800.0

--------------------------------------------
Total Bill Amount :1550.0
Most Expensive Product :Bag
Cheapest Product :Pen
Average Product Cost :516.67
--------------------------------------------'''