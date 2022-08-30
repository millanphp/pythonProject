# Entering a number
print("Enter a number: ")
n1= int(input())
print(f"You entered <{n1}>")

#Entering n value
print("How many fibonacci numbers you wish to print? ")

n= int(input())
print(f"Printing {n} fibonacci numbers after {n1}")

while(n-2):
    t=n1
    n1=t
    print(n1,end=" ")
    n=n-1

