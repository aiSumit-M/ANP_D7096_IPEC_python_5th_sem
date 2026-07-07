'''------- Problem Statement: Calculate Velocity

Write a Python program to calculate the velocity
when the distance and time are given by the user.
Use a function to calculate the velocity.

Formula:
Velocity = Distance / Time
-------------------------------------------------------------'''

#------- Coding ---------------

#function to calculate velocity
def calculate_velocity(distance, time):

    velocity = distance / time

    return velocity

#input distance from the user
distance = float(input("Enter Distance (in meters) :"))

#input time from the user
time = float(input("Enter Time (in seconds) :"))

#validate time
if(time <= 0):
    print("Time must be greater than 0")

else:

    #calling function
    velocity = calculate_velocity(distance, time)

    print("--------------------------------------------")

    print("Velocity :", velocity, "m/s")

#----------------------------------------------------
'''Output :
Enter Distance (in meters) :100
Enter Time (in seconds) :20
--------------------------------------------
Velocity : 5.0 m/s
--------------------------------------------'''