'''------- Problem Statement: Geometry Calculator Module

Create a Python module named twodfigures.py
that contains functions to calculate
Area and Perimeter/Circumference of
different two-dimensional figures.

Figures:
1. Square
2. Circle
3. Rectangle
4. Triangle
-------------------------------------------------------------'''

#------- Coding ---------------

#Area of Square
def square_area(side):

    area = side * side

    return area


#Perimeter of Square
def square_perimeter(side):

    perimeter = 4 * side

    return perimeter


#Area of Circle
def circle_area(radius):

    area = 3.14 * radius * radius

    return area


#Circumference of Circle
def circle_perimeter(radius):

    perimeter = 2 * 3.14 * radius

    return perimeter


#Area of Rectangle
def rectangle_area(length,breadth):

    area = length * breadth

    return area


#Perimeter of Rectangle
def rectangle_perimeter(length,breadth):

    perimeter = 2 * (length + breadth)

    return perimeter


#Area of Triangle
def triangle_area(base,height):

    area = (base * height) / 2

    return area


#Perimeter of Triangle
def triangle_perimeter(side1,side2,side3):

    perimeter = side1 + side2 + side3

    return perimeter



'''------- Problem Statement: Geometry Calculator

Write a Python program to import the
twodfigures module and perform
Area/Perimeter calculations of
different geometrical figures using
a menu-driven program.
-------------------------------------------------------------'''

#------- Coding ---------------

#import user defined module
import twodfigures

while(True):

    print("--------------------------------------------")
    print("GEOMETRY CALCULATOR")
    print("--------------------------------------------")
    print("1. Square")
    print("2. Circle")
    print("3. Triangle")
    print("4. Rectangle")
    print("5. Exit")

    choice = int(input("Enter your choice :"))

    if(choice == 5):

        print("Thank You")
        break

    print("--------------------------------------------")
    print("1. Area")
    print("2. Perimeter")

    operation = int(input("Enter your choice :"))

    print("--------------------------------------------")

    #Square
    if(choice == 1):

        side = float(input("Enter Side :"))

        if(operation == 1):

            area = twodfigures.square_area(side)
            print("Area of Square :", area)

        elif(operation == 2):

            perimeter = twodfigures.square_perimeter(side)
            print("Perimeter of Square :", perimeter)

        else:

            print("Invalid Operation")

    #Circle
    elif(choice == 2):

        radius = float(input("Enter Radius :"))

        if(operation == 1):

            area = twodfigures.circle_area(radius)
            print("Area of Circle :", area)

        elif(operation == 2):

            perimeter = twodfigures.circle_perimeter(radius)
            print("Circumference of Circle :", perimeter)

        else:

            print("Invalid Operation")

    #Triangle
    elif(choice == 3):

        if(operation == 1):

            base = float(input("Enter Base :"))
            height = float(input("Enter Height :"))

            area = twodfigures.triangle_area(base,height)

            print("Area of Triangle :", area)

        elif(operation == 2):

            side1 = float(input("Enter First Side :"))
            side2 = float(input("Enter Second Side :"))
            side3 = float(input("Enter Third Side :"))

            perimeter = twodfigures.triangle_perimeter(side1,side2,side3)

            print("Perimeter of Triangle :", perimeter)

        else:

            print("Invalid Operation")

    #Rectangle
    elif(choice == 4):

        length = float(input("Enter Length :"))
        breadth = float(input("Enter Breadth :"))

        if(operation == 1):

            area = twodfigures.rectangle_area(length,breadth)

            print("Area of Rectangle :", area)

        elif(operation == 2):

            perimeter = twodfigures.rectangle_perimeter(length,breadth)

            print("Perimeter of Rectangle :", perimeter)

        else:

            print("Invalid Operation")

    else:

        print("Invalid Choice")

    print("--------------------------------------------")



    '''Output :

--------------------------------------------
GEOMETRY CALCULATOR
--------------------------------------------
1. Square
2. Circle
3. Triangle
4. Rectangle
5. Exit
Enter your choice :1

--------------------------------------------
1. Area
2. Perimeter
Enter your choice :1

--------------------------------------------
Enter Side :5
Area of Square : 25.0
--------------------------------------------

--------------------------------------------
GEOMETRY CALCULATOR
--------------------------------------------
1. Square
2. Circle
3. Triangle
4. Rectangle
5. Exit
Enter your choice :2

--------------------------------------------
1. Area
2. Perimeter
Enter your choice :2

--------------------------------------------
Enter Radius :7
Circumference of Circle : 43.96
--------------------------------------------

--------------------------------------------
GEOMETRY CALCULATOR
--------------------------------------------
1. Square
2. Circle
3. Triangle
4. Rectangle
5. Exit
Enter your choice :3

--------------------------------------------
1. Area
2. Perimeter
Enter your choice :1

--------------------------------------------
Enter Base :10
Enter Height :8
Area of Triangle : 40.0
--------------------------------------------

--------------------------------------------
GEOMETRY CALCULATOR
--------------------------------------------
1. Square
2. Circle
3. Triangle
4. Rectangle
5. Exit
Enter your choice :4

--------------------------------------------
1. Area
2. Perimeter
Enter your choice :2

--------------------------------------------
Enter Length :12
Enter Breadth :8
Perimeter of Rectangle : 40.0
--------------------------------------------

--------------------------------------------
GEOMETRY CALCULATOR
--------------------------------------------
1. Square
2. Circle
3. Triangle
4. Rectangle
5. Exit
Enter your choice :5

Thank You
'''