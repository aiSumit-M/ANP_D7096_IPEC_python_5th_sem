'''------- Problem Statement: Count Uppercase and Lowercase Characters

Write a Python program to accept a sentence from the user.
Count the number of uppercase and lowercase characters
present in the sentence without using any library function.
Display the total number of uppercase and lowercase characters.
-------------------------------------------------------------'''

#------- Coding ---------------

#input sentence from the user
sentence = input("Enter a sentence :")

uppercase = 0
lowercase = 0

#to count uppercase and lowercase characters
for ch in sentence:

    if(ch >= 'A' and ch <= 'Z'):
        uppercase = uppercase + 1

    elif(ch >= 'a' and ch <= 'z'):
        lowercase = lowercase + 1

print("--------------------------------------------")

print("Total Uppercase Characters :", uppercase)
print("Total Lowercase Characters :", lowercase)

#----------------------------------------------------
'''Output :
Enter a sentence : Welcome To Python Programming
--------------------------------------------
Total Uppercase Characters : 3
Total Lowercase Characters : 23
--------------------------------------------'''