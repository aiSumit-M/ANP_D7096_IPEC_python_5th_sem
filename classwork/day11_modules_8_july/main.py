#----------- main.py ------------

import twodfigures

while True:

    print("\n===== Geometry Calculator =====")
    print("1. Square")
    print("2. Circle")
    print("3. Rectangle")
    print("4. Triangle")
    print("5. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 5:
        print("Thank You")
        break

    print("\n1. Area")
    print("2. Perimeter")

    operation = int(input("Enter your choice : "))

    # Square
    if choice == 1:

        side = float(input("Enter side : "))

        if operation == 1:
            print("Area =", twodfigures.square_area(side))

        elif operation == 2:
            print("Perimeter =", twodfigures.square_perimeter(side))

        else:
            print("Invalid Operation")

    # Circle
    elif choice == 2:

        radius = float(input("Enter radius : "))

        if operation == 1:
            print("Area =", twodfigures.circle_area(radius))

        elif operation == 2:
            print("Circumference =", twodfigures.circle_perimeter(radius))

        else:
            print("Invalid Operation")

    # Rectangle
    elif choice == 3:

        length = float(input("Enter length : "))
        breadth = float(input("Enter breadth : "))

        if operation == 1:
            print("Area =", twodfigures.rectangle_area(length, breadth))

        elif operation == 2:
            print("Perimeter =", twodfigures.rectangle_perimeter(length, breadth))

        else:
            print("Invalid Operation")

    # Triangle
    elif choice == 4:

        if operation == 1:

            base = float(input("Enter base : "))
            height = float(input("Enter height : "))

            print("Area =", twodfigures.triangle_area(base, height))

        elif operation == 2:

            side1 = float(input("Enter first side : "))
            side2 = float(input("Enter second side : "))
            side3 = float(input("Enter third side : "))

            print("Perimeter =", twodfigures.triangle_perimeter(side1, side2, side3))

        else:
            print("Invalid Operation")

    else:
        print("Invalid Choice")