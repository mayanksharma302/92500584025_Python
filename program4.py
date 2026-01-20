#Write a program to enter 10 numbers and display all armstrong numbers from those numbers.

# Input 10 numbers
numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Armstrong numbers are:")

for num in numbers:
    temp = num
    digits = len(str(num))
    sum = 0

    while temp > 0:
        d = temp % 10
        sum += d ** digits
        temp //= 10

    if sum == num:
        print(num)
