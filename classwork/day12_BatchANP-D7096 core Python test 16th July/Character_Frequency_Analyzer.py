# Question 2: Character Frequency Analyzer

# ------Coding------

text = input("Enter a string: ")

upper = 0
lower = 0
digit = 0
special = 0
freq = {}

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

most_char = max(freq, key=freq.get)

print("Uppercase :", upper)
print("Lowercase :", lower)
print("Digits :", digit)
print("Special Characters :", special)
print("Most Frequent Character :", most_char)

# ------Output------

# Sample Output:
# Enter a string: Python@2026
# Uppercase : 1
# Lowercase : 5
# Digits : 4
# Special Characters : 1
# Most Frequent Character : 2