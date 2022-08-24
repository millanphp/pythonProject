# Defining all calculations
def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    return a / b

def remainder (a, b):
    return a % b

def quotient (a, b):
    return a // b

def square (a, b):
    return a ** b

# Display console
print("Choose an option from the following:\n"
      "(1) Add (+)\n"
      "(2) Subtract (-)\n"
      "(3) Multiply (*)\n"
      "(4) Divide (/)\n"
      "(5) Find Remainder (%)\n"
      "(6) Find Quotient (//)\n"
      "(7) Find Square of a number (**)")

# Establishing the choice to select  using while condition
while True:
    choice = input("Option selected(1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        #Entering the number
        print("Enter First Number: ")
        num1 = int(input())

        #Entering the number to be divided with
        print("Enter Second Number: ")
        num2 = int(input())

        #Using if condition
        if choice == '1':
           print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", remainder(num1, num2))

        elif choice == '6':
            print(num1, "//", num2, "=", quotient(num1, num2))

        elif choice == '7':
            print(num1, "**", num2, "=", square(num1, num2))
            break

    else:
        print("Invalid Input")