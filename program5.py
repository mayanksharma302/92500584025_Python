#Write a program to enter 10 numbers and display largest odd number from the entered number.

# Input 10 numbers
numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

largest_odd = None

# Find largest odd number
for num in numbers:
    if num % 2 != 0:
        if largest_odd is None or num > largest_odd:
            largest_odd = num

# Display result
if largest_odd is not None:
    print("Largest odd number is:", largest_odd)
else:
    print("No odd number found")
