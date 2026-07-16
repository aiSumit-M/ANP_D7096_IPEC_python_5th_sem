# Password_Strength_Checker.py

# ------Coding------

password = input("Enter Password: ")

missing = []

if len(password) < 8:
    missing.append("Minimum 8 characters")

if not any(ch.isupper() for ch in password):
    missing.append("At least one uppercase letter")

if not any(ch.islower() for ch in password):
    missing.append("At least one lowercase letter")

if not any(ch.isdigit() for ch in password):
    missing.append("At least one digit")

special = "!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/"

if not any(ch in special for ch in password):
    missing.append("At least one special character")

if len(missing) == 0:
    print("Strong Password")
else:
    print("Weak Password")
    print("Missing Conditions:")
    for i in missing:
        print("-", i)

# ------Output------

# Sample Output:
# Enter Password: Python123
# Weak Password
# Missing Conditions:
# - At least one special character