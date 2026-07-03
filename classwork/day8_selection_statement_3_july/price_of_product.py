'''------- Problem Statement: Product Price Analysis Using Tuple

Write a Python program to create a tuple containing the
name and price of 10 products by taking input from the user.

Display:
1. Lowest Price Product
2. Highest Price Product
3. Number of products whose price is greater than ₹4000.
-------------------------------------------------------------'''

#------- Coding ---------------

#create an empty list
products = []

#to input details of 10 products
for i in range(1,11):

    name = input("Enter product name "+str(i)+" :")
    price = float(input("Enter product price :"))

    #store product name and price in the list
    products.append((name,price))

#create tuple from the list
products = tuple(products)

print("--------------------------------------------")

#initialize variables
lowest_name = products[0][0]
lowest_price = products[0][1]

highest_name = products[0][0]
highest_price = products[0][1]

count = 0

#to find lowest price, highest price and count
for product in products:

    name = product[0]
    price = product[1]

    if(price < lowest_price):
        lowest_price = price
        lowest_name = name

    if(price > highest_price):
        highest_price = price
        highest_name = name

    if(price > 4000):
        count = count + 1

print("Lowest Price Product :", lowest_name)
print("Price :", lowest_price)

print("--------------------------------------------")

print("Highest Price Product :", highest_name)
print("Price :", highest_price)

print("--------------------------------------------")

print("Number of Products with Price Greater than ₹4000 :", count)

#----------------------------------------------------
'''Output :
Enter product name 1 :Mouse
Enter product price :800

Enter product name 2 :Keyboard
Enter product price :1500

Enter product name 3 :Monitor
Enter product price :12000

Enter product name 4 :Speaker
Enter product price :3500

Enter product name 5 :Printer
Enter product price :9000

Enter product name 6 :Laptop
Enter product price :65000

Enter product name 7 :Pen Drive
Enter product price :700

Enter product name 8 :Scanner
Enter product price :5000

Enter product name 9 :Webcam
Enter product price :2500

Enter product name 10 :UPS
Enter product price :4500
--------------------------------------------
Lowest Price Product : Pen Drive
Price : 700.0
--------------------------------------------
Highest Price Product : Laptop
Price : 65000.0
--------------------------------------------
Number of Products with Price Greater than ₹4000 : 5
--------------------------------------------'''