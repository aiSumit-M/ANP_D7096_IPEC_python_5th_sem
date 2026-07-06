'''------- Problem Statement: Word Frequency Counter

Accept a sentence from the user and create a dictionary
that stores the frequency of each word.

Additionally:
1. Display the frequency of each word.
2. Display the most frequently occurring word.
3. Display all words in alphabetical order.
-------------------------------------------------------------'''

#------- Coding ---------------

#input sentence from the user
sentence = input("Enter a sentence :")

#create dictionary
words = {}
word = ""

#to extract words and count frequency
for ch in sentence + " ":

    if(ch != ' '):
        word = word + ch

    else:

        if(word != ""):

            if(word in words):
                words[word] = words[word] + 1
            else:
                words[word] = 1

        word = ""

print("--------------------------------------------")

print("Word Frequencies :")

#to display frequency of each word
for word in words:
    print(word, ":", words[word])

print("--------------------------------------------")

#to find most frequent word
max_word = list(words.keys())[0]
max_count = words[max_word]

for word in words:

    if(words[word] > max_count):

        max_count = words[word]
        max_word = word

print("Most Frequent Word :", max_word)
print("Frequency :", max_count)

print("--------------------------------------------")

print("Words in Alphabetical Order :")

#to sort words alphabetically
sorted_words = list(words.keys())
sorted_words.sort()

for word in sorted_words:
    print(word)

#----------------------------------------------------
'''Output :
Enter a sentence : python is easy and python is powerful
--------------------------------------------
Word Frequencies :
python : 2
is : 2
easy : 1
and : 1
powerful : 1
--------------------------------------------
Most Frequent Word : python
Frequency : 2
--------------------------------------------
Words in Alphabetical Order :
and
easy
is
powerful
python
--------------------------------------------'''