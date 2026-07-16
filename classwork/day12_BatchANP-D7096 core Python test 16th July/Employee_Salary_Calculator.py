# Employee_Salary_Calculator.py

# ------Coding------

def calculate_hra(basic):
    return basic * 0.20

def calculate_da(basic):
    return basic * 0.10

def calculate_tax(gross_salary):
    return gross_salary * 0.08

def calculate_net_salary(basic):
    hra = calculate_hra(basic)
    da = calculate_da(basic)
    gross = basic + hra + da
    tax = calculate_tax(gross)
    net = gross - tax

    print("Basic Salary =", basic)
    print("HRA =", hra)
    print("DA =", da)
    print("Gross Salary =", gross)
    print("Tax =", tax)
    print("Net Salary =", net)

basic = float(input("Enter Basic Salary: "))
calculate_net_salary(basic)

# ------Output------

# Sample Output:
# Enter Basic Salary: 50000
# Basic Salary = 50000.0
# HRA = 10000.0
# DA = 5000.0
# Gross Salary = 65000.0
# Tax = 5200.0
# Net Salary = 59800.0