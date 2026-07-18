import mysql.connector

# Establish connection
data_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="std_management"
)

# Create cursor object
cursor_obj = data_connection.cursor()

# Take input from user
std_id = input("Enter Student ID: ")
std_name = input("Enter Student Name: ")
standard = input("Enter Standard: ")
age = int(input("Enter Age: "))

# Insert query
sql_query = """
INSERT INTO student (std_id, std_name, standard, age)
VALUES (%s, %s, %s, %s)
"""

# Values
value = (std_id, std_name, standard, age)

# Execute query
cursor_obj.execute(sql_query, value)

# Save changes
data_connection.commit()

print("Student record inserted successfully.")

# Close connection
cursor_obj.close()
data_connection.close()