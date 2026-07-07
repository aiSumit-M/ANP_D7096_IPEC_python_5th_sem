'''------- Problem Statement: Count Special Characters in a Sentence

Write a Python program to accept a sentence from the user.
Count the total number of special characters present in it
using a loop and the formula:
Special Characters = Length of Sentence - Number of Alphanumeric Characters
-------------------------------------------------------------'''

#------- Coding ---------------

#input sentence from the user
sentence = input("Enter a sentence :")

alphanumeric = 0

#to count alphanumeric characters
for ch in sentence:

    if((ch >= 'A' and ch <= 'Z') or
       (ch >= 'a' and ch <= 'z') or
       (ch >= '0' and ch <= '9')):

        alphanumeric = alphanumeric + 1

#to count special characters
special = len(sentence) - alphanumeric

print("--------------------------------------------")

print("Number of Alphanumeric Characters :", alphanumeric)
print("Number of Special Characters :", special)

#----------------------------------------------------
'''Output :
Enter a sentence : Welcome@123 to#Python!
--------------------------------------------
Number of Alphanumeric Characters : 20
Number of Special Characters : 5
--------------------------------------------'''