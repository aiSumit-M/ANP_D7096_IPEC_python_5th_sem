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

    #store product name and price
    products.append((name,price))

#create tuple from the list
products = tuple(products)

print("--------------------------------------------")

#to find lowest and highest price product
lowest = min(products, key=lambda product: product[1])
highest = max(products, key=lambda product: product[1])

count = 0

#to count products having price greater than 4000
for product in products:

    if(product[1] > 4000):
        count = count + 1

print("Lowest Price Product :", lowest[0])
print("Price :", lowest[1])

print("--------------------------------------------")

print("Highest Price Product :", highest[0])
print("Price :", highest[1])

print("--------------------------------------------")

print("Number of Products with Price Greater than ₹4000 :", count)

#----------------------------------------------------
'''Output :
Enter product name 1 : Mouse
Enter product price : 800
Enter product name 2 : Keyboard
Enter product price : 1500
Enter product name 3 : Monitor
Enter product price : 12000
Enter product name 4 : Speaker
Enter product price : 3500
Enter product name 5 : Printer
Enter product price : 9000
Enter product name 6 : Laptop
Enter product price : 65000
Enter product name 7 : Pen Drive
Enter product price : 700
Enter product name 8 : Scanner
Enter product price : 5000
Enter product name 9 : Webcam
Enter product price : 2500
Enter product name 10 : UPS
Enter product price : 4500
--------------------------------------------
Lowest Price Product : Pen Drive
Price : 700.0
--------------------------------------------
Highest Price Product : Laptop
Price : 65000.0
--------------------------------------------
Number of Products with Price Greater than ₹4000 : 5
--------------------------------------------'''