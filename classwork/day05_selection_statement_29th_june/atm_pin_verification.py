'''------- Problem Statement: ATM PIN Verification

Write a Python program that accepts PIN from the user.
The correct PIN is 4589.
Keep asking the user until the correct PIN is entered.
Display "Access Granted" when the correct PIN is entered.
-------------------------------------------------------------'''

#------- Coding ---------------

correct_pin = 4589

while(True):
    pin = int(input("Enter PIN :"))

    if(pin == correct_pin):
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")

#----------------------------------------------------
'''Output :
Enter PIN :1234
Incorrect PIN
Enter PIN :9876
Incorrect PIN
Enter PIN :4589
Access Granted
--------------------------------------------'''