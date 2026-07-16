# Question 1: Electricity Bill Calculator

# ------Coding------

units = int(input("Enter total units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

if bill > 2000:
    final_bill = bill + (bill * 0.05)
else:
    final_bill = bill

if final_bill < 500:
    final_bill = 500

print("Total Units =", units)
print("Bill Amount = ₹", bill)
print("Final Payable Amount = ₹", final_bill)

# ------Output------

# Sample Output:
# Enter total units consumed: 250
# Total Units = 250
# Bill Amount = ₹ 1700
# Final Payable Amount = ₹ 1700