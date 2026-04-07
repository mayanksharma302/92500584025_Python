add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else "Division by zero"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result =", add(a, b))
elif op == '-':
    print("Result =", sub(a, b))
elif op == '*':
    print("Result =", mul(a, b))
elif op == '/':
    print("Result =", div(a, b))
else:
    print("Invalid operator")
