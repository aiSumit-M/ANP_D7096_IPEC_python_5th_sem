# Question 3: Number Guessing Game

# ------Coding------

secret = 57
attempts = 0

while attempts < 7:
    num = int(input("Enter your guess: "))

    if num < 0:
        print("Negative number ignored.")
        continue

    attempts += 1

    if num == secret:
        print("Congratulations! You guessed the correct number.")
        break
    elif num < secret:
        print("Too Low!")
    else:
        print("Too High!")

else:
    print("Game Over! Secret Number was", secret)

print("Attempts Used:", attempts)

# ------Output------

# Sample Output:
# Enter your guess: 40
# Too Low!
# Enter your guess: 60
# Too High!
# Enter your guess: 57
# Congratulations! You guessed the correct number.
# Attempts Used: 3