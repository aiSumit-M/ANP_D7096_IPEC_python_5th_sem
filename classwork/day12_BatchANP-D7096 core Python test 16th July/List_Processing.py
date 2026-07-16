# List_Processing.py

# ------Coding------

numbers = []

print("Enter 20 integers:")

for i in range(20):
    num = int(input())
    numbers.append(num)

print("Largest Number =", max(numbers))

unique = list(set(numbers))
unique.sort(reverse=True)

if len(unique) >= 2:
    print("Second Largest Number =", unique[1])
else:
    print("Second Largest Number does not exist.")

print("Smallest Number =", min(numbers))

print("List Without Duplicates =", unique)

print("Even Numbers:")
for i in numbers:
    if i % 2 == 0:
        print(i, end=" ")

print()

print("Numbers Divisible by both 3 and 5:")
for i in numbers:
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")

print()

print("Reversed List:")
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i], end=" ")

# ------Output------

# Sample Output:
# Enter 20 integers:
# 10
# 20
# 15
# 30
# 45
# 20
# 18
# 12
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
#
# Largest Number = 45
# Second Largest Number = 30
# Smallest Number = 5
# List Without Duplicates = [45, 30, 20, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
# Even Numbers:
# 10 20 30 20 18 12 6 8 10 12 14 16
# Numbers Divisible by both 3 and 5:
# 15 30 45 15
# Reversed List:
# 16 15 14 13 12 11 10 9 8 7 6 5 12 18 20 45 30 15 20 10