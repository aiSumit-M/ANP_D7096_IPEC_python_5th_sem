'''------- Problem Statement: Vowel Counter using Function

Write a Python program that defines a function
count_vowels(text).

The function should:
• Accept a string.
• Count the total number of vowels
  (a, e, i, o, u) irrespective of case.
• Return the total vowel count.

The main program should:
• Accept a sentence from the user.
• Call the function.
• Display the total number of vowels.
-------------------------------------------------------------'''

#------- Coding ---------------

#function to count vowels
def count_vowels(text):

    count = 0

    #to count vowels
    for ch in text:

        if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or
           ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):

            count = count + 1

    return count


#input sentence from the user
sentence = input("Enter a sentence :")

#calling function
vowels = count_vowels(sentence)

print("--------------------------------------------")

print("Total Vowels :", vowels)

#----------------------------------------------------
'''Output :
Enter a sentence : Python Programming is Fun
--------------------------------------------
Total Vowels : 6
--------------------------------------------

Output :
Enter a sentence : Welcome to Python
--------------------------------------------
Total Vowels : 5
--------------------------------------------'''