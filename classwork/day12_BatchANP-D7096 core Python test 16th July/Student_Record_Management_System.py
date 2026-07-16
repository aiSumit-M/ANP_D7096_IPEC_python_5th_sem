# Student_Record_Management_System.py

# ------Coding------

students = []

def add_student():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["Roll"] == roll:
            print("Roll Number already exists.")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    students.append({
        "Roll": roll,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    })

def display_students():
    if len(students) == 0:
        print("No Records Found")
    else:
        for s in students:
            print(s)

def search_student():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["Roll"] == roll:
            print(s)
            return

    print("Student Not Found")

def update_marks():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["Roll"] == roll:
            s["Marks"] = float(input("Enter New Marks: "))
            print("Marks Updated")
            return

    print("Student Not Found")

def delete_student():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["Roll"] == roll:
            students.remove(s)
            print("Record Deleted")
            return

    print("Student Not Found")

def display_topper():
    if students:
        topper = max(students, key=lambda x: x["Marks"])
        print(topper)

def average_marks():
    if students:
        avg = sum(s["Marks"] for s in students) / len(students)
        print("Average Marks =", avg)

def above_average():
    if students:
        avg = sum(s["Marks"] for s in students) / len(students)

        print("Students Above Average:")

        for s in students:
            if s["Marks"] > avg:
                print(s)

while True:

    print("\n----- MENU -----")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Display Topper")
    print("7. Display Average Marks")
    print("8. Display Students Above Average")
    print("9. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_marks()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        display_topper()
    elif choice == 7:
        average_marks()
    elif choice == 8:
        above_average()
    elif choice == 9:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")

# ------Output------

# Sample Output:
# ----- MENU -----
# 1. Add Student
# 2. Display All Students
# 3. Search Student
# 4. Update Marks
# 5. Delete Student
# 6. Display Topper
# 7. Display Average Marks
# 8. Display Students Above Average
# 9. Exit
#
# Enter Choice: 1
# Enter Roll Number: 101
# Enter Name: Rahul
# Enter Age: 20
# Enter Course: B.Tech
# Enter Marks: 92
#
# Enter Choice: 6
# {'Roll': '101', 'Name': 'Rahul', 'Age': '20', 'Course': 'B.Tech', 'Marks': 92.0}
#
# Enter Choice: 9
# Program Ended