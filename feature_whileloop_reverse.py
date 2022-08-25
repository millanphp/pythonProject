#Indexing values of a string

print("Entering a sting value: ")
a = input()
print(f"You entered: {a}")

string = a

#initializing the variable
i= len(string) -1

#Printing the strings in the characters continiously
#defining the while condition
while(i>=0):
    print(string[i])
    i=i-1
