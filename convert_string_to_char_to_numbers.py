# Entering a string
print("Enter a string: ")
s=input()
num_list = []

for c in s:
    num_list.append(ord(c) - 96)
print(f"You entered string <{s}>")
print(f"Printing characters of <{s}>")

print("Converting characters in the string to corresponding alphabet number")

print(f"String <{s}> after converting each characters to number is <{num_list}> ")