class NegativeNumberError(Exception):
    pass

num = int(input("Enter a positive number: "))

try:
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    print("You entered:", num)

except NegativeNumberError as e:
    print("Error:", e)
