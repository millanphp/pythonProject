#Entering the string
print("Enter a string value: ")
a= input()
print(f"You entered: {a} " )

#Slicing of the string after removing first and last character
print(f"Slice of '{a}' after removing first and last character  {a[1:-1]}")


#Slicing of the string after removing first two character
print(f"Slice of '{a}' after removing removing first two character {a[2:]}")

#Slicing of the string after removing last two character
print(f"Slice of '{a}' after removing removing last two character {a[:-2]}")

#Printing the middle index
middle_index = int(len (a)/2)


print(f"Middle index is, {middle_index}")


print(f"First half Slice of '{a}' is {a[:middle_index]} ")
print(f"Second half Slice of '{a}' is {a[middle_index:]} ")