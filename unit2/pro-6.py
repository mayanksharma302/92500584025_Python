file_name = "number.txt"

try:
    with open(file_name, "r") as file:
        number = [int(line.strip()) for line in file]

    total = sum(number)
    maximum = max(number)
    minimum = min(number)

    print("Total of all numbers:", total)
    print("Maximum number:", maximum)
    print("Minimum number:", minimum)

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except ValueError:
    print("Error: The file contains non-numeric values.")
