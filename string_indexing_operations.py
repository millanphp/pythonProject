#Entering a string value
print("enter a string value: ")
a= input()
print(f"You entered: {a} " )

value = a

#Printing First character
print(f"First Character in '{a}' is ")
print(value [0])

#Printing Last character
print(f"Last Character in '{a}' is ")
print(value [-1])

#Printing the Length of the string
print(f"Length of the string {a} is" , len(value))

#Printing the middle letter
def middle_char(value):
  return value[(len(value)-1)//2:(len(value)+2)//2]

print(f"Middle index is", len(middle_char(value)))

print(f"Middle character in '{value}'is", middle_char(value))