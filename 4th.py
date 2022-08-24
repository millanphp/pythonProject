def sub(a, b):
    sub = a - b
    return sub

# Entering a number
print("enter a ")
a= int(input())

#Entering second number
print("enter b ")
b= int(input())

# Subracting the two values
sub = (a - b)

# defining the condition
if a > b: sub = a - b
else: sub = b - a

print(sub)