'''import zipfile

with zipfile.ZipFile('sample', 'w') as f:
    f.write('sample.txt')

print("Zipping complete.")'''



import zipfile

with zipfile.ZipFile('sample', 'r') as f:
    f.extractall()

print("Unzipping complete.")
