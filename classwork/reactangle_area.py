length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Validation
if length <= 0 or width <= 0:
    print("Invalid input! Length and width must be greater than 0.")
else:
    area = length * width
    perimeter = 2 * (length + width)

    print("Area of the rectangle =", area)
    print("Perimeter of the rectangle =", perimeter)


'''
Enter the length of the rectangle: 5
Enter the width of the rectangle: 2
Area of the rectangle = 10.0
Perimeter of the rectangle = 14.0

=== Code Execution Successful ==='''