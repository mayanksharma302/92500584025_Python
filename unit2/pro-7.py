import os

source_file = "source.txt"
destination_file = "copy.txt"

if os.path.exists(source_file):
    src = open(source_file, "r")
    dest = open(destination_file, "w")
    for line in src:
        dest.write(line)
    print("File copied successfully.")
    src.close()
    dest.close()
else:
    print(f"Error: '{source_file}' does not exist.")
