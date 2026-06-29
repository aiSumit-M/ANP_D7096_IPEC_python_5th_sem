import math

radius = float(input("Enter the radius of the circle: "))

# Validation
if radius <= 0:
    print("Invalid input! Radius must be greater than 0.")
else:
    area = math.pi * radius * radius
    print("Area of the circle =", round(area, 2))



'''
Enter the radius of the circle: 7
Area of the circle = 153.94

=== Code Execution Successful ==='''