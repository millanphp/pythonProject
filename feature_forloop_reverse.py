#Indexing values of a string
print("Entering a sting value: ")
a = input()
print(f"You entered: {a}")

str = a

#Printing the strings in the reverse characters continiously
for i in range( len(str) - 1, -1, -1) :
    print(str[i])