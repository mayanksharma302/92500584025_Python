#Write a program to input p, r, n and find out interest using simple input output statement.

# Input values
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
n = float(input("Enter time (in years): "))

# Calculate simple interest
si = (p * r * n) / 100

# Output result
print("Simple Interest is:", si)
