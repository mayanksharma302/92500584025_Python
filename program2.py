#Write a program to input 2 numbers and one arithmetic operator. Perform operations as per arithmetic operator which is given as input


# Input two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Input arithmetic operator
op = input("Enter arithmetic operator (+, -, *, /): ")

# Perform operation
if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operator")
