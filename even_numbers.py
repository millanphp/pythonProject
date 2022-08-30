# Entering a number
print("enter a number ")
num= int(input())
print(f"The number you entered is: {num} " )

#Entering
print("How many even number do you want to print ")
n= int(input())

i=0
num1=num

#Using while loop
while i<n:
    if(num % 2) == 0:
        num=num + 2
        print(num)
    else:
        print(num+1)
        num=num+1
    i=i+1

