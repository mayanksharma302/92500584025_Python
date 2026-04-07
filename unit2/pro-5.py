file_name = "sample.txt"

file = open(file_name, "r")
contents = file.read()
print("File Contents:\n")
print(contents)

words = contents.split()
print("\nNumber of words in file:", len(words))

file.close()
