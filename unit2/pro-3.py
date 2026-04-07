import logging

logging.basicConfig(filename="error_log.txt", level=logging.ERROR)

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)

except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")
    logging.error(e)
