'''------- Problem Statement: Count Vowels in a Sentence

Write a Python program to accept a sentence from the user
and count the total number of vowels present in it.
Display the total number of vowels.
-------------------------------------------------------------'''

#------- Coding ---------------

#input sentence from the user
sentence = input("Enter a sentence :")

count = 0

#to count vowels
for ch in sentence:

    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or
       ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):

        count = count + 1

print("--------------------------------------------")

print("Total Number of Vowels :", count)

#----------------------------------------------------
'''Output :
Enter a sentence : Welcome to Python Programming
--------------------------------------------
Total Number of Vowels : 9
--------------------------------------------'''