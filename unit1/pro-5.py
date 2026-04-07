largest = None

for i in range(10):
    num = int(input("Enter number: "))
    if num % 2 != 0:
        if largest is None or num > largest:
            largest = num

if largest is not None:
    print("Largest odd number =", largest)
else:
    print("No odd number entered")
