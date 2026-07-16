# Tuple_Operations.py

# ------Coding------

students = (
    "Amit", "Rahul", "Riya", "Priya", "Neha",
    "Karan", "Rohit", "Simran", "Ankit", "Sneha",
    "Pooja", "Vikas", "Aman", "Riya", "Deepak"
)

print("Total Students =", len(students))

print("First Five Students =", students[:5])

print("Last Five Students =", students[-5:])

name = input("Enter student name to search: ")

if name in students:
    print(name, "found in tuple.")
else:
    print(name, "not found.")

print("Occurrences of", name, "=", students.count(name))

student_list = list(students)
student_list.sort()

print("Sorted List:")
print(student_list)

# ------Output------

# Sample Output:
# Total Students = 15
# First Five Students = ('Amit', 'Rahul', 'Riya', 'Priya', 'Neha')
# Last Five Students = ('Pooja', 'Vikas', 'Aman', 'Riya', 'Deepak')
# Enter student name to search: Riya
# Riya found in tuple.
# Occurrences of Riya = 2
# Sorted List:
# ['Aman', 'Amit', 'Deepak', 'Karan', 'Neha', 'Pooja', 'Priya', 'Rahul', 'Riya', 'Riya', 'Rohit', 'Simran', 'Sneha', 'Vikas', 'Ankit']