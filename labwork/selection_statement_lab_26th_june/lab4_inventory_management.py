'''------- Problem Statement: Inventory Management

Create a dictionary to maintain the stock of products
in a shop.

Implement the following operations:
1. Add a new product.
2. Update the stock of an existing product.
3. Remove a product from inventory.
4. Display products having stock less than 20.
5. Display the total number of items available in the inventory.
-------------------------------------------------------------'''

#------- Coding ---------------

#create an empty dictionary
inventory = {}

#to input details of 5 products
for i in range(1,6):

    product = input("Enter product name "+str(i)+" :")
    stock = int(input("Enter stock :"))

    #store product and stock in dictionary
    inventory[product] = stock

print("--------------------------------------------")

print("Inventory Records :")

#to display inventory
for product in inventory:
    print(product, ":", inventory[product])

print("--------------------------------------------")

#to add a new product
product = input("Enter new product name :")
stock = int(input("Enter stock :"))

inventory[product] = stock

print("Product Added Successfully")

print("--------------------------------------------")

#to update stock
product = input("Enter product name to update :")

if(product in inventory):

    stock = int(input("Enter new stock :"))
    inventory[product] = stock

    print("Stock Updated Successfully")

else:
    print("Product Not Found")

print("--------------------------------------------")

#to remove product
product = input("Enter product name to remove :")

if(product in inventory):

    del inventory[product]

    print("Product Removed Successfully")

else:
    print("Product Not Found")

print("--------------------------------------------")

print("Products having stock less than 20 :")

#to display products having stock less than 20
for product in inventory:

    if(inventory[product] < 20):
        print(product, ":", inventory[product])

print("--------------------------------------------")

#to calculate total stock
total = 0

for product in inventory:

    total = total + inventory[product]

print("Total Items Available :", total)

#----------------------------------------------------
'''Output :
Enter product name 1 :Laptop
Enter stock :15
Enter product name 2 :Mouse
Enter stock :40
Enter product name 3 :Keyboard
Enter stock :25
Enter product name 4 :Monitor
Enter stock :10
Enter product name 5 :Printer
Enter stock :18
--------------------------------------------
Inventory Records :
Laptop : 15
Mouse : 40
Keyboard : 25
Monitor : 10
Printer : 18
--------------------------------------------
Enter new product name :Scanner
Enter stock :12
Product Added Successfully
--------------------------------------------
Enter product name to update :Mouse
Enter new stock :45
Stock Updated Successfully
--------------------------------------------
Enter product name to remove :Keyboard
Product Removed Successfully
--------------------------------------------
Products having stock less than 20 :
Laptop : 15
Monitor : 10
Printer : 18
Scanner : 12
--------------------------------------------
Total Items Available : 100
--------------------------------------------'''