def add(a, b):
    sum = a + b
    return sum

print("enter a ")
a= int(input())

print("enter b ")
b= int(input())

sum = add(a,b)
print(sum)

sum1= add(sum, 100)
print(sum1)

sum2= add(sum1, 1000)
print(sum2)
