# Word_Frequency_Counter.py

# ------Coding------

import string

def word_frequency(sentence):

    sentence = sentence.lower()

    for ch in string.punctuation:
        sentence = sentence.replace(ch, "")

    words = sentence.split()

    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    print("\nWord Frequencies:")

    for word in sorted(freq):
        print(word, ":", freq[word])

    most = max(freq, key=freq.get)

    print("\nMost Repeated Word:")
    print(most)

text = input("Enter a sentence: ")

word_frequency(text)

# ------Output------

# Sample Output:
# Enter a sentence: Python is easy. Python is powerful.
#
# Word Frequencies:
# easy : 1
# is : 2
# powerful : 1
# python : 2
#
# Most Repeated Word:
# python