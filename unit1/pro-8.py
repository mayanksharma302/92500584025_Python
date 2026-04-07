s = input("Enter a string: ")

vowels = "aeiouAEIOU"
v_count = 0
for ch in s:
    if ch in vowels:
        v_count += 1
print("Number of vowels =", v_count)

length = 0
for ch in s:
    length += 1
print("Length of string =", length)

rev = ""
for ch in s:
    rev = ch + rev
print("Reversed string =", rev)

find_str = input("Enter substring to find: ")
replace_str = input("Enter substring to replace: ")
new_s = s.replace(find_str, replace_str)
print("After replace =", new_s)

if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
