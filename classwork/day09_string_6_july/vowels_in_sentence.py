'''------- Problem Statement: Count Vowels in a Sentence

Write a Python program to accept a sentence from the user
and count the total number of vowels present in it.
Display the total number of vowels.
-------------------------------------------------------------'''

#------- Coding ---------------

#input sentence from the user
sentence = input("Enter a sentence :")

vowels = 0

#to count vowels
for x in sentence:

    if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or
       x=='A' or x=='E' or x=='I' or x=='O' or x=='U'):
        #increment vowel count as
        vowels = vowels + 1

print("--------------------------------------------")

print("Total Number of Vowels :", vowels)

#----------------------------------------------------
'''Output :
Enter a sentence : Welcome to Python Programming
--------------------------------------------
Total Number of Vowels : 9
--------------------------------------------'''