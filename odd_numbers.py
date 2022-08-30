# Entering a number
print("Enter a number: ")
num= int(input())
print(f"The number you entered is: {num} " )

#Entering n value
print("How many even number do you wish to print? ")

n= int(input())
print(f"Printing {n} odd number after {num}")

i=0
num1=num

#Using while loop
while i<n:
    if(num % 2) != 0:
        num=num + 2
        print(num)
    else:
        print(num+1)
        num=num+1
    i=i+1