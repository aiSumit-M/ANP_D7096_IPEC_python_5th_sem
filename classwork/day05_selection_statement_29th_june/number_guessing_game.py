'''------- Problem Statement: Number Guessing Game

Write a Python program to guess a secret number.
The secret number is 37.
Keep asking the user until the correct number is entered.
Display whether the guess is too high, too low or correct.
-------------------------------------------------------------'''

#------- Coding ---------------

secret = 37

while(True):

    guess = int(input("Enter your guess :"))

    if(guess > secret):
        print("Too High")
    elif(guess < secret):
        print("Too Low")
    else:
        print("Correct Guess")
        break

#----------------------------------------------------
'''Output :
Enter your guess :25
Too Low
Enter your guess :45
Too High
Enter your guess :37
Correct Guess
--------------------------------------------'''